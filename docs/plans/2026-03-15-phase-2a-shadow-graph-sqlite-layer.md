# Phase 2A: Shadow-Graph & SQLite Layer Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Add structural memory to Threadex by shredding threadex_graph YAML pointers from JSONL records into a SQLite edge table, enabling hub scoring (PRU), graph traversal, keyword search (FTS5), and broken-edge detection -- the "Brain" layer that prevents agents from hallucinating relationships during large-scale refactoring.

**Architecture:** Extends tools/tx.py (1,586 lines) with SQLite graph.db (edges + content_index tables), edge shredder, PRU hub scorer, and tx search + tx graph commands. Files remain the source of truth (Tier 1). SQLite is a derived index (Tier 2/3) -- rebuildable from JSONL at any time via tx graph sync. Python 3.14 stdlib sqlite3 module -- no external dependencies.

**Tech Stack:** Python 3.14 stdlib only (sqlite3, hashlib, math, json, argparse, pathlib). FTS5 for keyword search (confirmed available). No vector/embedding dependencies (future seam only).

**Design Docs:**
- docs/plans/2026-03-11-threadex-memory-architecture-design.md (Three-Tier Storage, Record Schema)
- docs/plans/2026-03-14-integration-review-deployment-assessment.md (SQLite Schema, PRU Formula)
- User-provided SQLight Schema MD Plan.markdown (Phase 2A spec)

---

## Task Dependency Graph

```
Task 1 (SQLite DB init + schema)
  |
  +---> Task 2 (Edge shredder + tx record --graph + tx graph sync)
  |       |
  |       +---> Task 3 (PRU Hub Scorer + tx hubs)
  |       |
  |       +---> Task 4 (tx graph neighbors + tx graph broken)
  |
  +---> Task 5 (FTS5 content index + tx search)
          |
          +---> Task 6 (Acceptance tests + TOOL_INDEX update)
```

Parallelizable: Tasks 3+4 can run after Task 2. Task 5 can run after Task 1.
Task 6 depends on all prior tasks.

---

## Task 1: SQLite DB Initialization + Schema

**Files:**
- Modify: tools/tx.py (add DB constants, schema, init_db function, extend cmd_init)

**What to build:**

1. Add `import sqlite3`, `import hashlib`, `import math` to imports at top of file
2. Add DB path constant: `GRAPH_DB_PATH = THREADEX_DIR / "graph.db"`
3. Add SQL schema constants for edges table and content index
4. Add `init_db()` function that creates/migrates the database
5. Extend `cmd_init()` to call `init_db()` after creating folder structure
6. Add standalone `tx db init` subcommand for re-initializing DB without full tx init

**Constants to add (after GRAPH_RELATIONS):**

```python
# ============================================================
# SQLITE SCHEMA (Tier 2/3: The Edge Store)
# ============================================================

GRAPH_DB_PATH = THREADEX_DIR / "graph.db"

CREATE_EDGES_TABLE = """
CREATE TABLE IF NOT EXISTS edges (
    edge_id TEXT PRIMARY KEY,
    source_uri TEXT NOT NULL,
    target_uri TEXT NOT NULL,
    relation_type TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    utility_score REAL DEFAULT 1.0,
    last_traversed_at TEXT,
    origin_phase INTEGER DEFAULT 1,
    created_at TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    tags TEXT DEFAULT '[]'
);
"""

CREATE_EDGES_INDICES = """
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_uri);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_uri);
CREATE INDEX IF NOT EXISTS idx_edges_rel_type ON edges(relation_type);
CREATE INDEX IF NOT EXISTS idx_edges_pru ON edges(utility_score, weight);
"""

CREATE_CONTENT_INDEX = """
CREATE VIRTUAL TABLE IF NOT EXISTS content_index USING fts5(
    record_id,
    domain,
    content,
    tags,
    tokenize='porter unicode61'
);
"""

DB_SCHEMA_VERSION = 1
```

**init_db() function:**

```python
def init_db(db_path=None):
    if db_path is None:
        db_path = GRAPH_DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute(CREATE_EDGES_TABLE)
    for stmt in CREATE_EDGES_INDICES.strip().split(";"):
        stmt = stmt.strip()
        if stmt:
            conn.execute(stmt)
    try:
        conn.execute(CREATE_CONTENT_INDEX)
    except sqlite3.OperationalError as e:
        print(f"Warning: FTS5 not available ({e})", file=sys.stderr)
    conn.execute("CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)")
    conn.execute("INSERT OR REPLACE INTO meta (key, value) VALUES ('schema_version', ?)",
                 (str(DB_SCHEMA_VERSION),))
    conn.commit()
    return conn
```

**get_db() helper:**

```python
def get_db(db_path=None):
    if db_path is None:
        db_path = GRAPH_DB_PATH
    if not db_path.exists():
        return init_db(db_path)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn
```

**Extend cmd_init()** -- add after .gitattributes block:

```python
    # Initialize SQLite graph database
    conn = init_db()
    conn.close()
    print(f"  Graph DB: {GRAPH_DB_PATH}")
```

**Add db subparser + cmd_db_dispatch + cmd_db_init:**

```python
def cmd_db_dispatch(args):
    if args.db_command == "init":
        cmd_db_init(args)
    else:
        print(f"Unknown db command: {args.db_command}")
        sys.exit(1)

def cmd_db_init(args):
    if getattr(args, 'reset', False) and GRAPH_DB_PATH.exists():
        GRAPH_DB_PATH.unlink()
        print(f"Deleted existing graph.db")
    conn = init_db()
    cursor = conn.execute("SELECT COUNT(*) FROM edges")
    edge_count = cursor.fetchone()[0]
    try:
        conn.execute("SELECT COUNT(*) FROM content_index")
        fts5_status = "available"
    except sqlite3.OperationalError:
        fts5_status = "not available"
    conn.close()
    print(f"Graph DB initialized: {GRAPH_DB_PATH}")
    print(f"  Edges: {edge_count}")
    print(f"  FTS5: {fts5_status}")
    print(f"  WAL mode: enabled")
```

Add "db" to commands dict. Add subparser with --reset flag.

**Verify:**
```bash
python tools/tx.py db init
ls .threadex/graph.db
```

---

## Task 2: Edge Shredder + tx record --graph + tx graph sync

**Files:**
- Modify: tools/tx.py (add shred_to_edges, make_edge_id, extend cmd_record, add cmd_graph_sync)

**What to build:**

1. `make_edge_id(source, target, relation)` -- deterministic MD5 hash for dedup
2. `shred_to_edges(record, source_uri=None)` -- extract threadex_graph from a record into edge dicts
3. `insert_edges(conn, edges)` -- batch INSERT OR REPLACE into SQLite
4. `index_record_content(conn, record)` -- INSERT into FTS5 content_index
5. Extend cmd_record() to accept --graph flag for auto-shredding
6. cmd_graph_dispatch() + cmd_graph_sync() -- batch rebuild edges from all JSONL files

**make_edge_id():**

```python
def make_edge_id(source_uri, target_uri, relation_type):
    raw = f"{source_uri}|{target_uri}|{relation_type}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()
```

**shred_to_edges():**

```python
def shred_to_edges(record, source_uri=None):
    graph_pointers = record.get("threadex_graph", [])
    if not graph_pointers:
        return []
    if source_uri is None:
        domain = record.get("domain", "unknown")
        record_id = record.get("id", "unknown")
        source_uri = f"threadex://{domain}/{record_id}"
    edges = []
    for pointer in graph_pointers:
        if not isinstance(pointer, dict):
            continue
        target = pointer.get("target", "")
        rel = pointer.get("rel", "DEPENDS_ON")
        if not target:
            continue
        edge_id = make_edge_id(source_uri, target, rel)
        edges.append({
            "edge_id": edge_id,
            "source_uri": source_uri,
            "target_uri": target,
            "relation_type": rel,
            "weight": float(pointer.get("strength", 1.0)),
            "utility_score": float(record.get("utility_score", 0.5)),
            "origin_phase": int(pointer.get("phase", 1)),
            "tags": json.dumps(pointer.get("tags", []))
        })
    return edges
```

**insert_edges():**

```python
def insert_edges(conn, edges):
    if not edges:
        return 0
    count = 0
    for edge in edges:
        conn.execute("""
            INSERT OR REPLACE INTO edges
            (edge_id, source_uri, target_uri, relation_type, weight,
             utility_score, origin_phase, tags)
            VALUES (:edge_id, :source_uri, :target_uri, :relation_type,
                    :weight, :utility_score, :origin_phase, :tags)
        """, edge)
        count += 1
    conn.commit()
    return count
```

**index_record_content():**

```python
def index_record_content(conn, record):
    try:
        record_id = record.get("id", "")
        domain = record.get("domain", "")
        content = record.get("content", "")
        tags = ", ".join(record.get("tags", []))
        conn.execute("DELETE FROM content_index WHERE record_id = ?", (record_id,))
        conn.execute(
            "INSERT INTO content_index (record_id, domain, content, tags) VALUES (?, ?, ?, ?)",
            (record_id, domain, content, tags))
        conn.commit()
        return True
    except sqlite3.OperationalError:
        return False
```

**Extend cmd_record():** Add --graph flag to argparse. After record creation, if --graph and threadex_graph not empty, call get_db(), shred_to_edges(), insert_edges(), index_record_content().

**cmd_graph_sync():** Clear edges + content_index. Scan all JSONL files in expertise/ and production/. For each record, shred graph edges and index content. Print summary.

**Verify:**
```bash
python tools/tx.py record writer/headlines "Test graph pattern" --type pattern --graph --json
python tools/tx.py graph sync
```

---

## Task 3: PRU Hub Scorer + tx hubs Command

**Files:**
- Modify: tools/tx.py (add calculate_pru, get_all_nodes, cmd_hubs)

**What to build:**

1. `calculate_pru(conn, node_uri, alpha=0.15, lmbda=0.01)` -- PRU formula
2. `get_all_nodes(conn)` -- unique URIs from edges table
3. `cmd_hubs(args)` -- show top-N hubs by PRU score

**PRU formula from design doc:**
```
PRU(n) = alpha * Degree(n) + (1 - alpha) * Utility(n) * e^(-lambda * t)
alpha = 0.15, lambda = 0.01 (from threadex.config.yaml)
Degree = COUNT(*) incoming edges
Utility = AVG(utility_score) from incoming edges
t = hours since last traversal
```

**calculate_pru():**

```python
def calculate_pru(conn, node_uri, alpha=None, lmbda=None):
    if alpha is None:
        config = load_config()
        cfg_root = config.get("threadex", config)
        decay_cfg = cfg_root.get("decay", {})
        alpha = float(decay_cfg.get("alpha", 0.15)) if isinstance(decay_cfg, dict) else 0.15
    if lmbda is None:
        config = load_config()
        cfg_root = config.get("threadex", config)
        decay_cfg = cfg_root.get("decay", {})
        lmbda = float(decay_cfg.get("lambda_", 0.01)) if isinstance(decay_cfg, dict) else 0.01

    cursor = conn.execute("SELECT COUNT(*) FROM edges WHERE target_uri = ?", (node_uri,))
    degree = cursor.fetchone()[0]
    cursor = conn.execute("SELECT COUNT(*) FROM edges WHERE source_uri = ?", (node_uri,))
    out_degree = cursor.fetchone()[0]
    cursor = conn.execute(
        "SELECT AVG(utility_score), MAX(last_traversed_at) FROM edges WHERE target_uri = ?", (node_uri,))
    row = cursor.fetchone()
    avg_utility = row[0] if row[0] is not None else 0.5
    last_traversed = row[1]

    hours_since = 0.0
    if last_traversed:
        try:
            last_dt = datetime.fromisoformat(last_traversed.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            hours_since = (now - last_dt).total_seconds() / 3600.0
        except (ValueError, TypeError):
            hours_since = 0.0

    decay = math.exp(-lmbda * hours_since)
    pru_score = (alpha * degree) + ((1 - alpha) * avg_utility * decay)

    return {
        "uri": node_uri,
        "pru_score": round(pru_score, 4),
        "in_degree": degree,
        "out_degree": out_degree,
        "avg_utility": round(avg_utility, 4),
        "hours_since_last": round(hours_since, 1),
        "decay_factor": round(decay, 4),
    }
```

Add hubs subparser with --top N and --json flags. Add "hubs" to commands dict.

**Verify:**
```bash
python tools/tx.py hubs
python tools/tx.py hubs --json
```

---

## Task 4: tx graph neighbors + tx graph broken

**Files:**
- Modify: tools/tx.py (add cmd_graph_neighbors, cmd_graph_broken, extend graph subparser)

**What to build:**

1. `cmd_graph_neighbors(args)` -- show incoming/outgoing edges for a node URI
   - Updates last_traversed_at on query (the act of looking triggers recency)
2. `cmd_graph_broken(args)` -- detect orphan targets (edges pointing to nodes with no outgoing edges)

**cmd_graph_neighbors():** Query edges WHERE target_uri = ? for incoming, WHERE source_uri = ? for outgoing. Print formatted table. Update last_traversed_at.

**cmd_graph_broken():** LEFT JOIN edges e1 on e2 where e1.target_uri = e2.source_uri, find where e2 is NULL. Group by target, print report.

Add neighbors and broken subparsers under graph. Update cmd_graph_dispatch() dispatch dict.

**Verify:**
```bash
python tools/tx.py graph neighbors "threadex://writer/headlines/some-id"
python tools/tx.py graph broken
```

---

## Task 5: FTS5 Content Index + tx search Command

**Files:**
- Modify: tools/tx.py (add search functions, cmd_search)

**What to build:**

1. `search_fts5(conn, query, domain=None, limit=20)` -- FTS5 MATCH query
2. `search_jsonl_fallback(query, domain=None, limit=20)` -- case-insensitive substring scan of JSONL files
3. `search_graph_context(conn, record_ids)` -- enrich results with edge counts
4. `cmd_search(args)` -- combined keyword + graph search

**Search flow:**
1. Try FTS5 first (fast, ranked)
2. If FTS5 unavailable or returns None, fall back to JSONL scan
3. If --with-graph flag, enrich each result with incoming/outgoing edge counts

Add search subparser with: query (positional), --domain, --limit, --with-graph, --json.
Add "search" to commands dict.

**Verify:**
```bash
python tools/tx.py graph sync
python tools/tx.py search "headlines"
python tools/tx.py search "pattern" --with-graph
python tools/tx.py search "energy" --domain writer --json
```

---

## Task 6: Acceptance Tests + TOOL_INDEX Update

**Files:**
- Modify: tools/tx_acceptance_tests.py (add TX-12 through TX-20)
- Modify: tools/TOOL_INDEX.yaml (add 6 new entry points)

**What to build:**

9 new test methods:
- TX-12: init_db creates graph.db with edges + content_index + meta tables
- TX-13: make_edge_id is deterministic (same inputs = same hash)
- TX-14: shred_to_edges extracts edges from threadex_graph field
- TX-15: insert_edges upserts edges into SQLite
- TX-16: calculate_pru returns correct PRU scores
- TX-17: graph sync rebuilds edges from JSONL files
- TX-18: search_fts5 finds records by keyword
- TX-19: search_jsonl_fallback finds records by substring
- TX-20: graph broken detects orphan targets

Extend setUp/tearDown to patch GRAPH_DB_PATH alongside existing patches.

TOOL_INDEX.yaml: Add db_init, graph_sync, graph_neighbors, graph_broken, hubs, search entry points under threadex section.

**Verify:**
```bash
python tools/tx_acceptance_tests.py
# All TX-01 through TX-20 should pass
```

---

## Definition of Done

After all 6 tasks complete, verify:

- [ ] .threadex/graph.db exists with edges + content_index + meta tables
- [ ] tx db init creates/resets the database
- [ ] tx record --graph shreds threadex_graph pointers into SQLite edges
- [ ] tx graph sync rebuilds all edges from JSONL files
- [ ] tx graph neighbors <uri> shows incoming/outgoing edges
- [ ] tx graph broken detects orphan target nodes
- [ ] tx hubs shows top-N nodes by PRU score
- [ ] tx search "<query>" returns FTS5 keyword results
- [ ] tx search --with-graph enriches results with edge context
- [ ] PRU formula uses alpha=0.15, lambda=0.01 from config
- [ ] Edge IDs are deterministic (MD5 hash of source+target+relation)
- [ ] FTS5 failure gracefully falls back to JSONL scanning
- [ ] All TX-12 through TX-20 acceptance tests pass
- [ ] TOOL_INDEX.yaml has 6 new entry points (db, graph sync/neighbors/broken, hubs, search)

---

## Execution Notes

- **OneDrive caution:** Write tool may fail with EEXIST. Use Python patch script approach if needed.
- **Single file:** All code goes into tools/tx.py (extends from ~1,586 to ~2,100+ lines). Tests extend tools/tx_acceptance_tests.py.
- **No external deps:** Python 3.14 stdlib only. FTS5 confirmed available. Vector search deferred to future phase.
- **Files remain truth:** SQLite is a derived index. tx graph sync can rebuild from scratch at any time.
- **WAL mode:** SQLite uses WAL journal for concurrent-safe reads during writes.
- **Parallel execution:** Tasks 3+4 are independent after Task 2. Task 5 can run after Task 1 (only needs DB schema, not edge data).

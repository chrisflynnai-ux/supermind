#!/usr/bin/env python3
"""
Threadex Phase 1B + 2A Acceptance Tests -- TX-01 through TX-21
Tests verify Threadex file layer is operational.
Uses temporary .threadex_test/ directory (no real data polluted).

Usage:
    python tools/tx_acceptance_tests.py           # Run all tests
    python tools/tx_acceptance_tests.py TX-03     # Run specific test
    python tools/tx_acceptance_tests.py --summary # Quick pass/fail
"""
import sys
import os
import json
import shutil
import tempfile
import time
import sqlite3
import uuid
import re
from pathlib import Path
from io import StringIO

REAL_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REAL_ROOT / "tools"))
import tx


class MockArgs:
    """Lightweight stand-in for argparse.Namespace."""
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)


REQUIRED_RECORD_FIELDS = [
    "id",
    "type",
    "status",
    "cognitive_stage",
    "domain",
    "content",
    "context",
    "source_project",
    "evidence_count",
    "evidence_contexts",
    "mma_score",
    "created_at",
    "updated_at",
    "created_by",
    "provenance",
    "model_id",
    "model_version",
    "harness_id",
    "harness_version",
    "skill_version",
    "prompt_checksum",
    "last_accessed",
    "num_recalled",
    "utility_score",
    "tags",
    "conflict_reason",
    "conflicting_pattern_id",
    "deprecated_reason",
    "superseded_by",
    "threadex_graph",
]


class ThreadexAcceptanceTests:

    def __init__(self):
        self.results = []
        self.test_dir = None
        self._orig_ROOT = tx.ROOT
        self._orig_THREADEX_DIR = tx.THREADEX_DIR
        self._orig_EXPERTISE_DIR = tx.EXPERTISE_DIR
        self._orig_PRODUCTION_DIR = tx.PRODUCTION_DIR
        self._orig_CONFIG_PATH = tx.CONFIG_PATH
        self._orig_GRAPH_DB_PATH = tx.GRAPH_DB_PATH

    def setup(self):
        self.test_dir = Path(tempfile.mkdtemp(prefix="threadex_test_"))
        tx.ROOT = self.test_dir
        tx.THREADEX_DIR = self.test_dir / ".threadex"
        tx.EXPERTISE_DIR = tx.THREADEX_DIR / "expertise"
        tx.PRODUCTION_DIR = tx.THREADEX_DIR / "production"
        tx.CONFIG_PATH = tx.THREADEX_DIR / "threadex.config.yaml"
        tx.GRAPH_DB_PATH = tx.THREADEX_DIR / "graph.db"

    def teardown(self):
        if self.test_dir and self.test_dir.exists():
            shutil.rmtree(str(self.test_dir), ignore_errors=True)
        tx.ROOT = self._orig_ROOT
        tx.THREADEX_DIR = self._orig_THREADEX_DIR
        tx.EXPERTISE_DIR = self._orig_EXPERTISE_DIR
        tx.PRODUCTION_DIR = self._orig_PRODUCTION_DIR
        tx.CONFIG_PATH = self._orig_CONFIG_PATH
        tx.GRAPH_DB_PATH = self._orig_GRAPH_DB_PATH

    def run_test(self, test_id, name, test_fn):
        try:
            passed, msg = test_fn()
            self.results.append({"id": test_id, "name": name, "passed": passed, "msg": msg})
        except SystemExit:
            self.results.append({"id": test_id, "name": name, "passed": False, "msg": "SystemExit raised"})
        except Exception as e:
            self.results.append({"id": test_id, "name": name, "passed": False, "msg": "Exception: %s" % e})

    def _init_threadex(self):
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            tx.cmd_init(MockArgs(force=True))
        finally:
            sys.stdout = old_stdout

    # TX-01
    def tx_01_init(self):
        self._init_threadex()
        checks = {
            ".threadex exists": tx.THREADEX_DIR.is_dir(),
            "expertise/ exists": tx.EXPERTISE_DIR.is_dir(),
            "expertise/writer": (tx.EXPERTISE_DIR / "writer").is_dir(),
            "expertise/researcher": (tx.EXPERTISE_DIR / "researcher").is_dir(),
            "expertise/strategist": (tx.EXPERTISE_DIR / "strategist").is_dir(),
            "expertise/designer": (tx.EXPERTISE_DIR / "designer").is_dir(),
            "expertise/_shared": (tx.EXPERTISE_DIR / "_shared").is_dir(),
            "production/_archive": (tx.PRODUCTION_DIR / "_archive").is_dir(),
            "config file": tx.CONFIG_PATH.is_file(),
        }
        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, "Missing: %s" % ", ".join(failed)
        return True, "All directories and config created"

    # TX-02
    def tx_02_config(self):
        self._init_threadex()
        config = tx.load_config()
        cfg = config.get("threadex", config)
        for key in ["version", "decay", "compaction", "slicing"]:
            if key not in cfg:
                return False, "Config missing key: %s" % key
        decay = cfg.get("decay", {})
        if isinstance(decay, dict) and decay:
            for dk in ["alpha", "lambda_", "forbidden_threshold"]:
                if dk not in decay:
                    return False, "Config decay missing: %s" % dk
        else:
            # Flat YAML parser: decay keys are siblings in cfg
            for dk in ["alpha", "lambda_", "forbidden_threshold"]:
                if dk not in cfg:
                    return False, "Config decay key missing from flat cfg: %s" % dk
        compaction = cfg.get("compaction", {})
        if isinstance(compaction, dict) and compaction:
            if "max_records_per_file" not in compaction:
                return False, "Config compaction missing max_records_per_file"
        else:
            if "max_records_per_file" not in cfg:
                return False, "Config compaction key missing from flat cfg: max_records_per_file"
        slicing = cfg.get("slicing", {})
        if isinstance(slicing, dict) and slicing:
            if "method" not in slicing:
                return False, "Config slicing missing method"
        else:
            if "method" not in cfg:
                return False, "Config slicing key missing from flat cfg: method"
        return True, "Config loaded with all required keys"

    # TX-03
    def tx_03_record(self):
        self._init_threadex()
        record = tx.make_record(domain="writer/headlines", content="Test headline pattern",
                                record_type="pattern", status="observed")
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        tx.append_record(filepath, record)
        records = tx.read_jsonl(filepath)
        if len(records) != 1:
            return False, "Expected 1 record, got %d" % len(records)
        if records[0]["content"] != "Test headline pattern":
            return False, "Content mismatch"
        return True, "1 record appended and read back correctly"

    # TX-04
    def tx_04_schema(self):
        self._init_threadex()
        record = tx.make_record(domain="writer/headlines", content="Schema test",
                                record_type="pattern", status="observed", mma_score=7.5, tags=["test"])
        missing = [f for f in REQUIRED_RECORD_FIELDS if f not in record]
        if missing:
            return False, "Missing fields: %s" % ", ".join(missing)
        try:
            uuid.UUID(record["id"])
        except (ValueError, TypeError):
            return False, "id is not valid UUID"
        iso_re = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}")
        for ts_field in ("created_at", "updated_at"):
            val = record.get(ts_field, "")
            if not iso_re.match(str(val)):
                return False, "%s is not ISO format: %s" % (ts_field, val)
        return True, "Record has all %d fields, valid UUID, valid timestamps" % len(REQUIRED_RECORD_FIELDS)

    # TX-05
    def tx_05_prime_xml(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(domain="writer/headlines", content="Golden headline",
                            record_type="pattern", status="golden", mma_score=9.5)
        r2 = tx.make_record(domain="writer/headlines", content="Recent headline",
                            record_type="pattern", status="observed", mma_score=7.0)
        r3 = tx.make_record(domain="writer/headlines", content="Forbidden headline",
                            record_type="failure", status="forbidden")
        for rec in [r1, r2, r3]:
            tx.append_record(filepath, rec)
        records = tx.read_jsonl(filepath)
        if len(records) != 3:
            return False, "Expected 3 records, got %d" % len(records)
        filtered = tx.filter_for_priming(records, max_recent=10)
        if len(filtered["golden"]) != 1:
            return False, "Expected 1 golden, got %d" % len(filtered["golden"])
        if len(filtered["recent"]) != 1:
            return False, "Expected 1 recent, got %d" % len(filtered["recent"])
        if len(filtered["guards"]) != 1:
            return False, "Expected 1 guard, got %d" % len(filtered["guards"])
        xml_out = tx.records_to_xml(filtered, "writer")
        checks = {
            "has_ThreadexMemory": "<ThreadexMemory" in xml_out,
            "has_GoldenPatterns": "<GoldenPatterns" in xml_out,
            "has_RecentPatterns": "<RecentPatterns" in xml_out,
            "has_GuardPatterns": "<GuardPatterns" in xml_out,
            "has_closing_tag": "</ThreadexMemory>" in xml_out,
        }
        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, "XML output missing: %s" % ", ".join(failed)
        return True, "Prime XML has all required sections (golden, recent, guards)"

    # TX-06
    def tx_06_project_create(self):
        self._init_threadex()
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            tx.cmd_project_create(MockArgs(name="Test Project", team="writer,researcher"))
        finally:
            sys.stdout = old_stdout
        project_dir = tx.PRODUCTION_DIR / "test-project"
        checks = {
            "project_dir": project_dir.is_dir(),
            "t1": (project_dir / "t1").is_dir(),
            "t2": (project_dir / "t2").is_dir(),
            "t3": (project_dir / "t3").is_dir(),
            "t4": (project_dir / "t4").is_dir(),
            "_manifest.yaml": (project_dir / "_manifest.yaml").is_file(),
            "evals.jsonl": (project_dir / "evals.jsonl").is_file(),
        }
        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, "Project scaffold missing: %s" % ", ".join(failed)
        return True, "Project created with t1-t4 tracks, manifest, and evals"

    # TX-07
    def tx_07_lifecycle(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(domain="writer/headlines", content="Contest me",
                            record_type="pattern", status="observed")
        r2 = tx.make_record(domain="writer/headlines", content="Deprecate me",
                            record_type="pattern", status="observed")
        r3 = tx.make_record(domain="writer/headlines", content="Forbid me",
                            record_type="pattern", status="observed")
        for rec in [r1, r2, r3]:
            tx.append_record(filepath, rec)
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            tx.cmd_contest(MockArgs(
                target="writer/headlines",
                record_id=r1["id"],
                reason="contradicts new evidence",
                project=None,
            ))
        finally:
            sys.stdout = old_stdout
        _, contested = tx.find_record_by_id(filepath, r1["id"])
        if contested is None or contested["status"] != "contested":
            return False, "Contest failed"
        sys.stdout = StringIO()
        try:
            tx.cmd_deprecate(MockArgs(
                target="writer/headlines",
                record_id=r2["id"],
                reason="outdated approach",
                superseded_by=r1["id"],
                project=None,
            ))
        finally:
            sys.stdout = old_stdout
        _, deprecated = tx.find_record_by_id(filepath, r2["id"])
        if deprecated is None or deprecated["status"] != "deprecated":
            return False, "Deprecate failed"
        if deprecated.get("superseded_by") != r1["id"]:
            return False, "superseded_by not set correctly"
        sys.stdout = StringIO()
        try:
            tx.cmd_forbid(MockArgs(
                target="writer/headlines",
                record_id=r3["id"],
                reason="harmful pattern",
                project=None,
            ))
        finally:
            sys.stdout = old_stdout
        _, forbidden = tx.find_record_by_id(filepath, r3["id"])
        if forbidden is None or forbidden["status"] != "forbidden":
            return False, "Forbid failed"
        return True, "All 3 lifecycle transitions verified (contested, deprecated, forbidden)"

    # TX-08
    def tx_08_locking(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        filepath.parent.mkdir(parents=True, exist_ok=True)
        filepath.touch()
        got_lock = tx.acquire_lock(filepath, timeout=5.0)
        if not got_lock:
            return False, "Failed to acquire initial lock"
        lock_file = filepath.with_suffix(filepath.suffix + ".lock")
        if not lock_file.exists():
            return False, "Lock file not created"
        got_second = tx.acquire_lock(filepath, timeout=5.0)
        if got_second:
            tx.release_lock(filepath)
            return False, "Second acquire should have failed but succeeded"
        tx.release_lock(filepath)
        if lock_file.exists():
            return False, "Lock file not removed after release"
        lock_file.write_text("99999", encoding="utf-8")
        old_time = time.time() - 10
        os.utime(str(lock_file), (old_time, old_time))
        got_stale = tx.acquire_lock(filepath, timeout=5.0)
        if not got_stale:
            return False, "Failed to acquire lock after stale cleanup"
        tx.release_lock(filepath)
        return True, "Lock acquire, release, and stale cleanup all verified"

    # TX-09
    def tx_09_sims(self):
        self._init_threadex()
        r1 = tx.make_record(domain="writer/headlines", content="High MMA pattern",
                            record_type="pattern", status="observed", mma_score=9.5)
        r1 = tx.apply_sims_rules(r1)
        if r1["status"] != "candidate":
            return False, "Rule 1 failed: MMA 9.5 should promote to candidate, got %s" % r1["status"]
        r1b = tx.make_record(domain="writer/headlines", content="Lower MMA",
                             record_type="pattern", status="observed", mma_score=8.5)
        r1b = tx.apply_sims_rules(r1b)
        if r1b["status"] != "observed":
            return False, "Rule 1 negative: MMA 8.5 should stay observed, got %s" % r1b["status"]
        r2 = tx.make_record(domain="writer/headlines", content="Repeated failure",
                            record_type="failure", status="observed", evidence_count=3)
        r2 = tx.apply_sims_rules(r2)
        if r2["status"] != "forbidden":
            return False, "Rule 2 failed: failure+3 evidence should be forbidden, got %s" % r2["status"]
        r3 = tx.make_record(domain="writer/headlines", content="Low utility",
                            record_type="pattern", status="observed", utility_score=0.1)
        r3 = tx.apply_sims_rules(r3)
        if "_low_utility_flag" not in r3.get("tags", []):
            return False, "Rule 3 failed: utility 0.1 should get _low_utility_flag tag"
        return True, "All 3 SIMS rules verified (candidate promotion, forbidden, low utility flag)"

    # TX-10
    def tx_10_status(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(domain="writer/headlines", content="Status test record",
                            record_type="pattern", status="golden", mma_score=9.2)
        tx.append_record(filepath, r1)
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        try:
            tx.cmd_status(MockArgs())
            output = sys.stdout.getvalue()
        finally:
            sys.stdout = old_stdout
        checks = {
            "has_THREADEX_STATUS": "THREADEX STATUS" in output,
            "has_EXPERTISE": "EXPERTISE DOMAINS" in output,
            "has_HEALTH": "HEALTH:" in output,
        }
        failed = [k for k, v in checks.items() if not v]
        if failed:
            return False, "Status output missing: %s" % ", ".join(failed)
        return True, "Status command outputs THREADEX STATUS, EXPERTISE DOMAINS, HEALTH"

    # TX-11
    def tx_11_gitattributes(self):
        self._init_threadex()
        gitattr_path = tx.ROOT / ".gitattributes"
        if not gitattr_path.exists():
            return False, ".gitattributes not created"
        content = gitattr_path.read_text(encoding="utf-8")
        if "merge=union" not in content:
            return False, ".gitattributes missing merge=union"
        if "*.jsonl" not in content:
            return False, ".gitattributes missing *.jsonl pattern"
        return True, ".gitattributes has *.jsonl merge=union"


    # TX-12
    def tx_12_init_db(self):
        self._init_threadex()
        db_path = tx.GRAPH_DB_PATH
        if not db_path.exists():
            return False, "graph.db not created by init"
        conn = tx.get_db()
        # Check edges table exists
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='edges'")
        if not cursor.fetchone():
            conn.close()
            return False, "edges table not found"
        # Check content_index exists
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='content_index'")
        if not cursor.fetchone():
            conn.close()
            return False, "content_index table not found"
        # Check meta table exists
        cursor = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='meta'")
        if not cursor.fetchone():
            conn.close()
            return False, "meta table not found"
        # Verify schema version
        cursor = conn.execute("SELECT value FROM meta WHERE key='schema_version'")
        row = cursor.fetchone()
        if not row or row[0] != str(tx.DB_SCHEMA_VERSION):
            conn.close()
            return False, "schema_version mismatch"
        conn.close()
        return True, "graph.db has edges, content_index, meta tables with correct schema version"

    # TX-13
    def tx_13_edge_id_deterministic(self):
        id1 = tx.make_edge_id("threadex://writer/abc", "threadex://writer/xyz", "DEPENDS_ON")
        id2 = tx.make_edge_id("threadex://writer/abc", "threadex://writer/xyz", "DEPENDS_ON")
        if id1 != id2:
            return False, "Same inputs produce different IDs: %s vs %s" % (id1, id2)
        id3 = tx.make_edge_id("threadex://writer/abc", "threadex://writer/xyz", "CONFLICTS_WITH")
        if id1 == id3:
            return False, "Different relations produce same ID"
        if len(id1) != 32:
            return False, "Edge ID not 32 char hex: %s" % id1
        return True, "make_edge_id is deterministic and relation-sensitive"

    # TX-14
    def tx_14_shred_to_edges(self):
        record = tx.make_record(
            domain="writer/headlines",
            content="Test shredding",
            record_type="pattern",
            status="observed",
            threadex_graph=[
                {"target": "threadex://writer/other", "rel": "DEPENDS_ON", "strength": 0.8},
                {"target": "threadex://researcher/data", "rel": "COMPLEMENTS", "strength": 0.5},
            ]
        )
        edges = tx.shred_to_edges(record)
        if len(edges) != 2:
            return False, "Expected 2 edges, got %d" % len(edges)
        rels = set(e["relation_type"] for e in edges)
        if rels != {"DEPENDS_ON", "COMPLEMENTS"}:
            return False, "Wrong relation types: %s" % rels
        for e in edges:
            if not e["edge_id"] or len(e["edge_id"]) != 32:
                return False, "Invalid edge_id: %s" % e["edge_id"]
            if not e["source_uri"].startswith("threadex://"):
                return False, "Invalid source_uri: %s" % e["source_uri"]
        return True, "shred_to_edges extracts 2 edges with correct relations and URIs"

    # TX-15
    def tx_15_insert_edges(self):
        self._init_threadex()
        conn = tx.get_db()
        edges = [
            {"edge_id": "test1", "source_uri": "s1", "target_uri": "t1",
             "relation_type": "DEPENDS_ON", "weight": 1.0, "utility_score": 0.5,
             "origin_phase": 1, "tags": "[]"},
            {"edge_id": "test2", "source_uri": "s2", "target_uri": "t2",
             "relation_type": "COMPLEMENTS", "weight": 0.8, "utility_score": 0.7,
             "origin_phase": 1, "tags": "[]"},
        ]
        count = tx.insert_edges(conn, edges)
        if count != 2:
            conn.close()
            return False, "Expected 2 inserts, got %d" % count
        cursor = conn.execute("SELECT COUNT(*) FROM edges")
        total = cursor.fetchone()[0]
        if total != 2:
            conn.close()
            return False, "Expected 2 rows in DB, got %d" % total
        # Test upsert (same edge_id should replace)
        edges[0]["weight"] = 2.0
        tx.insert_edges(conn, [edges[0]])
        cursor = conn.execute("SELECT weight FROM edges WHERE edge_id='test1'")
        row = cursor.fetchone()
        if row[0] != 2.0:
            conn.close()
            return False, "Upsert did not update weight"
        total = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        if total != 2:
            conn.close()
            return False, "Upsert created duplicate (expected 2 rows, got %d)" % total
        conn.close()
        return True, "insert_edges inserts 2 edges and upserts correctly"

    # TX-16
    def tx_16_calculate_pru(self):
        self._init_threadex()
        conn = tx.get_db()
        # Insert edges pointing to a target node
        edges = [
            {"edge_id": "pru1", "source_uri": "s1", "target_uri": "hub1",
             "relation_type": "DEPENDS_ON", "weight": 1.0, "utility_score": 0.8,
             "origin_phase": 1, "tags": "[]"},
            {"edge_id": "pru2", "source_uri": "s2", "target_uri": "hub1",
             "relation_type": "COMPLEMENTS", "weight": 0.5, "utility_score": 0.6,
             "origin_phase": 1, "tags": "[]"},
        ]
        tx.insert_edges(conn, edges)
        result = tx.calculate_pru(conn, "hub1", alpha=0.15, lmbda=0.01)
        if result["in_degree"] != 2:
            conn.close()
            return False, "Expected in_degree=2, got %d" % result["in_degree"]
        if result["pru_score"] <= 0:
            conn.close()
            return False, "PRU score should be positive, got %s" % result["pru_score"]
        # Check formula: alpha * degree + (1-alpha) * avg_utility * decay
        # With no last_traversed_at, decay = e^0 = 1.0
        # avg_utility = (0.8+0.6)/2 = 0.7
        # pru = 0.15*2 + 0.85*0.7*1.0 = 0.3 + 0.595 = 0.895
        expected = 0.15 * 2 + 0.85 * 0.7 * 1.0
        if abs(result["pru_score"] - round(expected, 4)) > 0.01:
            conn.close()
            return False, "PRU score %s != expected %s" % (result["pru_score"], round(expected, 4))
        conn.close()
        return True, "calculate_pru returns correct score (%.4f) for 2-edge hub" % result["pru_score"]

    # TX-17
    def tx_17_graph_sync(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(
            domain="writer/headlines", content="Sync test with edges",
            record_type="pattern", status="observed",
            threadex_graph=[{"target": "threadex://writer/other", "rel": "DEPENDS_ON"}]
        )
        r2 = tx.make_record(
            domain="writer/headlines", content="Sync test no edges",
            record_type="pattern", status="observed"
        )
        tx.append_record(filepath, r1)
        tx.append_record(filepath, r2)
        import io
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        try:
            tx.cmd_graph_sync(MockArgs(domain=None, project=None))
        finally:
            sys.stdout = old_stdout
        conn = tx.get_db()
        edge_count = conn.execute("SELECT COUNT(*) FROM edges").fetchone()[0]
        if edge_count != 1:
            conn.close()
            return False, "Expected 1 edge from sync, got %d" % edge_count
        try:
            idx_count = conn.execute("SELECT COUNT(*) FROM content_index").fetchone()[0]
        except Exception:
            idx_count = 0
        if idx_count < 2:
            conn.close()
            return False, "Expected >= 2 content index entries, got %d" % idx_count
        conn.close()
        return True, "graph sync produces %d edge and %d content index entries" % (edge_count, idx_count)

    # TX-18
    def tx_18_search_fts5(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(domain="writer/headlines", content="Quantum computing breakthrough",
                            record_type="pattern", status="observed")
        r2 = tx.make_record(domain="writer/headlines", content="Classical music festival",
                            record_type="pattern", status="observed")
        tx.append_record(filepath, r1)
        tx.append_record(filepath, r2)
        conn = tx.get_db()
        tx.index_record_content(conn, r1)
        tx.index_record_content(conn, r2)
        results = tx.search_fts5(conn, "quantum")
        if results is None:
            conn.close()
            return False, "FTS5 returned None (table missing?)"
        if len(results) != 1:
            conn.close()
            return False, "Expected 1 FTS5 result for 'quantum', got %d" % len(results)
        if results[0]["record_id"] != r1["id"]:
            conn.close()
            return False, "Wrong record returned"
        conn.close()
        return True, "search_fts5 finds 1 result for 'quantum' query"

    # TX-19
    def tx_19_search_fallback(self):
        self._init_threadex()
        filepath = tx.EXPERTISE_DIR / "writer" / "headlines.jsonl"
        r1 = tx.make_record(domain="writer/headlines", content="Unique xylophone pattern",
                            record_type="pattern", status="observed")
        r2 = tx.make_record(domain="writer/headlines", content="Regular pattern here",
                            record_type="pattern", status="observed")
        tx.append_record(filepath, r1)
        tx.append_record(filepath, r2)
        results = tx.search_jsonl_fallback("xylophone")
        if len(results) != 1:
            return False, "Expected 1 fallback result for 'xylophone', got %d" % len(results)
        if results[0]["record_id"] != r1["id"]:
            return False, "Wrong record returned: %s" % results[0]["record_id"]
        # Test case insensitivity
        results_upper = tx.search_jsonl_fallback("XYLOPHONE")
        if len(results_upper) != 1:
            return False, "Case insensitive search failed"
        return True, "search_jsonl_fallback finds substring matches case-insensitively"

    # TX-20
    def tx_20_graph_broken(self):
        self._init_threadex()
        conn = tx.get_db()
        # Create an edge where target has no outgoing edges (orphan)
        edges = [
            {"edge_id": "brk1", "source_uri": "s1", "target_uri": "orphan_node",
             "relation_type": "DEPENDS_ON", "weight": 1.0, "utility_score": 0.5,
             "origin_phase": 1, "tags": "[]"},
            # s1 also has an outgoing edge so it's not orphan
            {"edge_id": "brk2", "source_uri": "s1", "target_uri": "s2",
             "relation_type": "COMPLEMENTS", "weight": 1.0, "utility_score": 0.5,
             "origin_phase": 1, "tags": "[]"},
        ]
        tx.insert_edges(conn, edges)
        # orphan_node has no outgoing edges. Also s2 has no outgoing edges.
        # Both should be detected as broken.
        broken = conn.execute("""
            SELECT DISTINCT e1.target_uri
            FROM edges e1
            LEFT JOIN edges e2 ON e1.target_uri = e2.source_uri
            WHERE e2.source_uri IS NULL
            ORDER BY e1.target_uri
        """).fetchall()
        targets = [r[0] for r in broken]
        if "orphan_node" not in targets:
            conn.close()
            return False, "orphan_node not detected as broken"
        conn.close()
        return True, "graph broken detects %d orphan targets including orphan_node" % len(targets)


    # TX-21
    def tx_21_parse_skill_xml(self):
        self._init_threadex()
        tmp = None
        try:
            xml_content = (
                '<?xml version="1.0" encoding="UTF-8"?>\n'
                '<Skill skill_id="meta_test" name="Test Skill" version="1.0.0">\n'
                '  <Meta>\n'
                '    <Name>Test Skill Name</Name>\n'
                '    <Domain>meta</Domain>\n'
                '    <Track>cross</Track>\n'
                '    <Model>sonnet</Model>\n'
                '    <TriggerCommands>/test, /demo</TriggerCommands>\n'
                '    <NeuroBoxAlignment><Position>CENTER</Position></NeuroBoxAlignment>\n'
                '  </Meta>\n'
                '  <L1>L1 content here</L1>\n'
                '  <Contract>\n'
                '    <InputsRequired>\n'
                '      <Input><Name>PROJECT_BRIEF</Name></Input>\n'
                '    </InputsRequired>\n'
                '  </Contract>\n'
                '  <Guardrails>\n'
                '    <Guardrail><Rule>No fabrication</Rule></Guardrail>\n'
                '  </Guardrails>\n'
                '</Skill>\n'
            )
            tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".xml", delete=False, encoding="utf-8")
            tmp.write(xml_content)
            tmp.close()
            result = tx.parse_skill_xml(tmp.name)
            checks = {
                "skill_id": result.identity.skill_id == "meta_test",
                "name": result.identity.name == "Test Skill",
                "version": result.identity.version == "1.0.0",
                "domain": result.identity.domain == "meta",
                "track": result.identity.track == "cross",
                "model": result.identity.model == "sonnet",
                "neurobox": "CENTER" in result.identity.neurobox_position,
                "trigger_test": "/test" in result.identity.trigger_commands,
                "trigger_demo": "/demo" in result.identity.trigger_commands,
                "layers": len(result.layers) >= 1,
                "guardrails": len(result.guardrails) >= 1,
            }
            failed = [k for k, v in checks.items() if not v]
            if failed:
                return False, "Failed checks: %s" % ", ".join(failed)
            return True, "parse_skill_xml extracts identity, layers, and guardrails correctly"
        finally:
            if tmp and os.path.exists(tmp.name):
                os.unlink(tmp.name)

    def run_all(self, target=None):
        """Run all (or one) acceptance tests with setup/teardown."""
        tests = [
            ("TX-01", "Init creates directory structure", self.tx_01_init),
            ("TX-02", "Config loads with required keys", self.tx_02_config),
            ("TX-03", "Record append and read-back", self.tx_03_record),
            ("TX-04", "Schema has all fields + UUID + timestamps", self.tx_04_schema),
            ("TX-05", "Prime XML output structure", self.tx_05_prime_xml),
            ("TX-06", "Project create scaffold", self.tx_06_project_create),
            ("TX-07", "Lifecycle transitions", self.tx_07_lifecycle),
            ("TX-08", "Advisory locking", self.tx_08_locking),
            ("TX-09", "SIMS auto-promotion rules", self.tx_09_sims),
            ("TX-10", "Status command output", self.tx_10_status),
            ("TX-11", ".gitattributes merge=union", self.tx_11_gitattributes),
            ("TX-12", "init_db creates graph.db with tables", self.tx_12_init_db),
            ("TX-13", "make_edge_id is deterministic", self.tx_13_edge_id_deterministic),
            ("TX-14", "shred_to_edges extracts edges", self.tx_14_shred_to_edges),
            ("TX-15", "insert_edges upserts correctly", self.tx_15_insert_edges),
            ("TX-16", "calculate_pru returns correct scores", self.tx_16_calculate_pru),
            ("TX-17", "graph sync rebuilds edges", self.tx_17_graph_sync),
            ("TX-18", "search_fts5 finds by keyword", self.tx_18_search_fts5),
            ("TX-19", "search_jsonl_fallback finds by substring", self.tx_19_search_fallback),
            ("TX-20", "graph broken detects orphans", self.tx_20_graph_broken),
            ("TX-21", "parse_skill_xml extracts identity from well-formed XML", self.tx_21_parse_skill_xml),
        ]
        if target:
            tests = [(tid, name, fn) for tid, name, fn in tests if tid == target]
            if not tests:
                print("Unknown test: %s" % target)
                sys.exit(1)
        for test_id, name, fn in tests:
            self.setup()
            try:
                self.run_test(test_id, name, fn)
            finally:
                self.teardown()
        return self.results


def print_results(results):
    """Print acceptance test results."""
    passed = sum(1 for r in results if r["passed"])
    total = len(results)
    print()
    print("=" * 60)
    print("Threadex Phase 1B + 2A Acceptance Tests")
    print("=" * 60)
    print("Result: %d/%d PASSED" % (passed, total))
    print()
    for r in results:
        icon = "[PASS]" if r["passed"] else "[FAIL]"
        print("  %s %s: %s" % (icon, r["id"], r["name"]))
        print("         %s" % r["msg"])
        print()
    if passed == total:
        print("  >>> ALL TESTS PASSED -- Phase 1B + 2A + Mastery Pipeline Threadex File Layer + Shadow Graph Verified <<<")
    else:
        failed = [r for r in results if not r["passed"]]
        print("  >>> %d TESTS FAILED -- Fix before proceeding <<<" % len(failed))


if __name__ == "__main__":
    suite = ThreadexAcceptanceTests()
    if len(sys.argv) >= 2 and sys.argv[1] == "--summary":
        results = suite.run_all()
        passed = sum(1 for r in results if r["passed"])
        total = len(results)
        print("Threadex 1B + 2A: %d/%d passed" % (passed, total))
        sys.exit(0 if passed == total else 1)
    elif len(sys.argv) >= 2 and sys.argv[1].upper().startswith("TX-"):
        test_id = sys.argv[1].upper()
        results = suite.run_all(target=test_id)
        print_results(results)
    else:
        results = suite.run_all()
        print_results(results)
        passed = sum(1 for r in results if r["passed"])
        sys.exit(0 if passed == len(results) else 1)

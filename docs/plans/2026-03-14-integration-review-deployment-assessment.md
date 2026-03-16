# SUPERMIND Integration Review & Deployment Assessment
# Date: 2026-03-14
# Status: COMPLETE — Feeds Phase 1B (Threadex File Layer Build)
# Sources: Antigravity Harness Deployment Manifest, Google Memory Doc II, MASFactory (GitHub)

---

## 0. Document Purpose

This working document consolidates the cross-reference assessment of three major inputs
received 2026-03-14, evaluated against the existing SUPERMIND architecture (Threadex Memory
Architecture, Harness Systems Master Knowledge Compendium, ZPWO v4.0):

1. **Antigravity Harness Deployment Manifest** (Gemini) — Action Guide / Runbook
2. **Google Memory Doc II** (Gemini) — Implementation Seed Bank (schemas, Python, framework recs)
3. **MASFactory** (GitHub: BUPT-GAMMA/MASFactory) — Graph-centric visual orchestration framework

**Outcome:** 5 conflicts found, all resolved. Zero doctrine breaks. Architecture is convergent.
The build sequence has been updated with new phases (3B Runtime Framework, 3C MASFactory Visual Layer).

---

## 1. Source Inventory

| Source | Content | Key Value |
|---|---|---|
| Antigravity Harness Deployment Manifest | Executable operating procedure: 3-tier memory, 4-phase gate, PRU scoring, boot commands, guardrails | Action Guide — turns architecture into runbook |
| Google Memory Doc II | Deep research synthesis: memory alternatives, SQLite edges schema, YAML pointer format, shredding function, PRU calculator Python, PydanticAI/SmolAgents code, MASFactory integration | Implementation Seed Bank — concrete code + schemas |
| MASFactory (GitHub) | Graph-centric multi-agent framework: Vibe Graphing (NL to executable graph), Node/Edge abstractions, Loop/Switch/Human components, VS Code visualizer | Visual Orchestration Layer — the missing dashboard |

---

## 2. Manifest vs. Existing Architecture

### 2.1 Memory Tiers

| Manifest Element | Our Existing Version | Delta |
|---|---|---|
| L1 Ephemeral (.claude.mem + DOTMACK) | Threadex Tier 1 (JSONL/YAML files) | DIFFERENT THINGS. .claude.mem is session-scoped ephemeral state. Threadex Tier 1 is persistent. .claude.mem sits ABOVE Threadex as working register before tx record commits. |
| L2 Human/Policy (Obsidian via MCP) | Threadex Tier 2 (QMD search engine) | COEXIST. Obsidian is human-facing surface. QMD is search engine indexing same files. Obsidian vault can BE Tier 1 file store that QMD indexes. |
| L3 Structural (QMD + SQLite) | Threadex Tier 3 (SQLite + DuckDB+vss) | ALIGNED. Both use SQLite for structural search. Doc II adds edges table schema. |

### 2.2 Phase-Gate vs. Track Mapping

| Manifest Phase | SUPERMIND Track | Mapping |
|---|---|---|
| Phase 1: Blueprint (Gemini+Claude) | T1 Research | Direct map |
| Phase 2: Forge (Claude+Codex) | T2 Draft + T3 Production | Phase 2 spans T2-T3 |
| Phase 3: Healing (SmolAgents+Mastra) | Fix-loops within T3 | Phase 3 is sub-loop inside T3, not separate track |
| Phase 4: Assembly (Mastra+Human) | T4 Polish | Direct map |

### 2.3 New Elements from Manifest (ADOPT)

- **context-mode --enable**: Virtualization layer for log-heavy CLI outputs (pre-compaction at I/O level)
- **tx pulse --start**: Cognitive Synch Pulsing every 5 turns (promoted to boot sequence)
- **Phase-specific model pairings**: Default assignments per phase (override-capable)
- **Adversarial pairing rule**: No agent approves its own work
- **Boot command sequence**: tx init --harness, mcp-connect --obsidian, context-mode --enable, tx pulse --start
- **Memory hygiene rule**: L1 state older than 1 session must be GC'd or promoted to L2

---

## 3. Memory Doc II — Implementation Artifacts

### 3.1 Production-Ready Code Seeds

| Artifact | Status | Target Phase |
|---|---|---|
| SQLite edges CREATE TABLE + indices | Ready to copy | Phase 2A |
| YAML threadex_graph pointer format | Ready to spec | Phase 1B (schema addition) |
| shred_to_edges() function signature | Ready to implement | Phase 2A |
| HubScorer Python class (PRU calculator) | Ready to copy | Phase 2A |
| PydanticAI GravityShiftResult tool def | Pattern to adapt | Phase 3B |
| SmolAgents RunTestSuiteTool + ApplyPatchTool | Pattern to adapt | Phase 3B |
| Omni-State Sync Protocol (YAML + watchdog) | Pattern to adapt | Phase 4A |

### 3.2 Framework Assessments

| Framework | Role | Verdict |
|---|---|---|
| PydanticAI | Type-safe tool execution (Phase 2/Forge) | INTEGRATE Phase 3B |
| SmolAgents (HF) | Code-as-actions for self-healing (Phase 3) | INTEGRATE Phase 3B |
| Context-Mode (mksglu) | Virtualization for log-heavy CLI outputs | NON-NEGOTIABLE — adopt immediately |
| CLI-Anything | Wrap Antigravity functions as agent-native commands | INTEGRATE Phase 3B |
| Mastra | Observer/Reflector architecture | MAPS TO existing Lyra/Reed personas |
| Canopy | Inherited prompting | MAPS TO existing SkillML Progressive Disclosure |
| Mulch | Corpus-scoped JSONL tables | MAPS TO existing Threadex expertise threads |
| Overstory | SQLite mailbox orchestration | ACP SUPERSEDES — use SQLite storage pattern only |
| Letta/MemGPT | Context paging (RAM/hard-drive metaphor) | EVALUATE Phase 3A vs native tx page-out |
| Cognee | Ingestion pipeline (unstructured to KG) | EVALUATE Phase 2A vs custom QMD + NetworkX |

### 3.3 SQLite Edges Table Schema (from Doc II)

```sql
CREATE TABLE edges (
    edge_id TEXT PRIMARY KEY,
    source_uri TEXT NOT NULL,
    target_uri TEXT NOT NULL,
    relation_type TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    utility_score REAL DEFAULT 1.0,
    last_traversed_at DATETIME,
    origin_phase INTEGER DEFAULT 1,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (source_uri) REFERENCES nodes(uri) ON DELETE CASCADE
);
CREATE INDEX idx_edges_source ON edges(source_uri);
CREATE INDEX idx_edges_target ON edges(target_uri);
CREATE INDEX idx_edges_rel_type ON edges(relation_type);
CREATE INDEX idx_edges_pru_calc ON edges(utility_score, weight);
```

### 3.4 YAML Pointer Format (Tier 1 Records)

```yaml
threadex_graph:
  - target: "vault/Process/Mastery.md"
    rel: "UPGRADES"
    strength: 0.85
    phase: 4
  - target: "sqlite://states/auto_research_v1"
    rel: "READ_STATE"
    strength: 1.0
    tags: ["karpathy-loop", "self-healing"]
```

### 3.5 PRU(n) Hub Scoring Formula

```
PRU(n) = alpha * Degree(n) + (1-alpha) * Utility(n) * e^(-lambda*t)

- alpha = 0.15 (default, configurable in threadex.config.yaml)
- lambda = 0.01 (decay constant)
- Degree = COUNT(*) of incoming edges
- Utility = AVG(utility_score) from edges
- t = hours since last traversal
```

---

## 4. MASFactory Integration Assessment

### 4.1 What MASFactory Is

- Graph-centric framework for multi-agent orchestration
- Vibe Graphing: NL intent to executable directed graph
- 4 layers: Graph Skeleton, Component, Protocol, Interaction
- Node types: Agent, Graph (nestable subgraphs), Loop, Switch, Human
- VS Code extension: topology preview, runtime tracing, human intervention
- Context Protocol: Memory/RAG/MCP integration
- GitHub: BUPT-GAMMA/MASFactory

### 4.2 Mapping to SUPERMIND

| MASFactory Component | SUPERMIND Equivalent | Integration Point |
|---|---|---|
| Agent Nodes | Persona invocations (Marcus, Diana, Leo, etc.) | MASFactory renders personas as typed nodes |
| Edge contracts | ACP envelope (12+ fields) | MASFactory edges carry ACP metadata |
| Vibe Graphing (NL to graph) | No equivalent (manual workflow design) | FILLS THE GAP — visual workflow authoring |
| Loop component | Fix-loops + MCTS self-healing | Maps to Phase 3 healing loop |
| Switch component | Orion task-shape routing (7 shapes) | Maps to routing decisions |
| Human component | Quality gates (GOLDEN promotion, T1-T2 approval) | Maps to human-in-the-loop gates |
| VS Code Visualizer | No equivalent | FILLS THE GAP — runtime observability |
| Context Protocol | Threadex + QMD + Dash | Already have as separate systems |

### 4.3 Integration Strategy

MASFactory is NOT a replacement. It is the VIEW LAYER:
- Sits at CONSCIENCE (Design/Front) in the Neuro Box
- Renders what SOUL (Orchestration/Center) decides
- Visualizes what BODY (Automation/Bottom) executes

Integration path:
1. Map ACP envelope to MASFactory Edge contracts
2. Map SUPERMIND personas to MASFactory Agent Nodes
3. Map Orion routing to MASFactory Switch Nodes
4. Map fix-loops to MASFactory Loop Nodes
5. Map quality gates to MASFactory Human Nodes
6. Export 4-track workflow as MASFactory graph definition
7. Use VS Code Visualizer for runtime observability

---

## 5. Conflict Resolution Log

| # | Conflict | Source A | Source B | Resolution |
|---|---|---|---|---|
| 1 | L2 = Obsidian vs L2 = QMD | Manifest | Threadex | Both coexist. Obsidian is human surface. QMD is search engine. |
| 2 | L1 = .claude.mem vs Tier 1 = JSONL | Manifest | Threadex | Different things. .claude.mem is ephemeral register above Tier 1. |
| 3 | 4-Phase vs 4-Track naming | Manifest | ZPWO/Harness | Phases are sub-structure within tracks. Phase 3 = fix-loop in T3. |
| 4 | SmolAgents/PydanticAI vs SkillML XML | Doc II | SUPERMIND | Complementary. SkillML = routing metadata. PydanticAI = runtime. |
| 5 | Overstory mailbox vs ACP envelope | Doc II | Harness Compendium | ACP supersedes. Use Overstory SQLite storage pattern only. |

---

## 6. Gemini 3.2 Deep Research (Clusters F-I) — Prior Session Assessment

### Cluster F: Memory Graph Layer (ADOPT)
- Shadow-Graph model: YAML pointers to SQLite edges (Phase 2 build anchor)
- Hub Scoring PRU(n): Additive to Threadex utility decay
- Triple indexing: Vector + FTS5 + B-Tree (refines Phase 2 plan)
- Cognee: Defer to Phase 2 evaluation

### Cluster G: Self-Healing (ADOPT)
- MCTS for Reed-Nova-Felix loop (Phase 3A design pattern)
- Utility decay alpha=0.15 (adopt as default, configurable)
- FORBIDDEN at utility < 0.3 (soft flag, not auto-demote)

### Cluster H: Cognitive Bandwidth (ADOPT/EVALUATE)
- Semantic Slicing by Action Boundaries (fills gap in pre-compaction)
- Cognitive Synch Pulsing every 5 turns (Phase 3A multi-model)
- Letta for context paging (evaluate vs native tx page-out)

### Cluster I: Business Architecture (DEFER)
- ATOMs marketplace (Phase 5)
- OpenFlow revenue sharing (Phase 5)
- RAM as competitive moat (already in motion)

---

## 7. Updated Build Sequence

```
Phase 0   [DONE]  Tooling + ZPWO v4.0

Phase 1A  [DONE]  MAA Rebuild (M1-M3)

Phase 1B  [NOW]   Threadex Phase 1 -- File Layer
                  + .claude.mem ephemeral register design
                  + threadex_graph YAML pointer block in record schema
                  + utility decay alpha=0.15 in threadex.config.yaml
                  + FORBIDDEN soft-flag at utility < 0.3
                  + Semantic Slicing by Action Boundaries in pre-compaction
                  + tx record --graph flag (design only, build Phase 2A)

Phase 1C          CLAUDE.md v4.0 upgrade

Phase 2A          Threadex Phase 2 -- Search + Graph Layer
                  + SQLite edges table (schema ready)
                  + B-Tree index for edge traversal
                  + Hub Scoring PRU(n) calculator (Python ready)
                  + shred_to_edges() ingestion function
                  + tx record --graph implementation
                  + Cognee evaluation
                  + Triple indexing: Vector + FTS5 + B-Tree

Phase 2B          Skill Evaluator tool
Phase 2C          Skill repair (Batch 1-4 + relational ops)

Phase 3A          Multi-Model Harness Build
                  + MCTS for Reed-Nova-Felix
                  + Cognitive Synch Pulsing
                  + context-mode virtualization
                  + Adversarial pairing rule
                  + Phase-specific model pairings
                  + Letta/MemGPT evaluation

Phase 3B          Runtime Framework Integration
                  + PydanticAI typed tool execution
                  + SmolAgents code-as-actions
                  + CLI-Anything wrappers
                  + context-mode --enable

Phase 3C          MASFactory Visual Layer
                  + ACP to MASFactory Edge mapping
                  + Persona to Agent Node mapping
                  + Orion to Switch Node mapping
                  + Fix-loops to Loop Node mapping
                  + Quality gates to Human Node mapping
                  + 4-track workflow export as MASFactory graph
                  + VS Code Visualizer integration

Phase 4A          Agentic OS (Antigravity + Claude Code dual-base)
                  + Omni-State Sync Protocol
                  + tx pulse --start in boot sequence

Phase 4B          Flowgrams, COSMS front-end

Phase 5           Go-to-Market (ATOMs, OpenFlow, SkillML OSS)
```

---

## 8. Schema Additions for Phase 1B (Immediate Build)

### 8.1 Record Schema Additions (to Threadex Section 5)

New optional fields in JSONL record format:
- `threadex_graph`: [] (list of graph pointers, shredded to edges in Phase 2A)
- Each pointer: {target, rel, strength, phase, tags}

### 8.2 Config File (NEW: threadex.config.yaml)

```yaml
threadex:
  version: "1.0"
  decay:
    alpha: 0.15
    lambda: 0.01
    forbidden_threshold: 0.3
    golden_review_days: 180
    episodic_archive_days: 30
  compaction:
    max_records_per_file: 10000
    soft_context_warning: 0.50
    hard_context_flush: 0.70
    emergency_flush: 0.85
  slicing:
    method: "action_boundaries"
    fallback: "token_chunks"
    max_chunk_tokens: 4000
  synch_pulse:
    interval_turns: 5
    enabled: false
```

### 8.3 Ephemeral Register (.claude.mem)

- Session-scoped working state
- DOTMACK compression for high-frequency updates
- Auto-GC: state older than 1 session must be promoted to Tier 1 or discarded
- NOT part of Threadex Tier 1 (sits above it as volatile register)
- Bridge: human or agent runs tx record to commit from .claude.mem to Threadex

---

*Assessment complete. Ready for Phase 1B build.*
*Zero-Point Context Strategy: Light Center, Heavy Edges*

# XML-to-Mastery Refactor Pipeline — Design Spec

> **Version:** 1.0.0
> **Date:** 2026-03-15
> **Status:** Draft — Awaiting Approval
> **Depends On:** Phase 2A Shadow-Graph (complete), Threadex CLI (operational)
> **Builds On:** tools/tx.py (2,317 lines), .threadex/ infrastructure

---

## 1. Problem Statement

ULTRAMIND has 78+ XML skill files (SkillML V1.4 format) across `.agents/skills/` and `.claude/skills/`. These skills contain substantial domain knowledge — frameworks, procedures, contracts, guardrails, failure modes — locked inside XML tags with no relational metadata, no searchability, and no connection to the Threadex memory graph.

The Phase 2A Shadow-Graph gave Threadex a "brain" (SQLite edges, FTS5 search, PRU hub scoring). This spec defines the pipeline that **feeds knowledge into that brain** by refactoring XML skills into Threadex-indexed, graph-connected knowledge artifacts.

---

## 2. Two-Track Architecture

The refactor operates on two distinct tracks with different levels of automation:

### Track A: Orchestration Pilot (Automated)

- **Scope:** 5 meta/orchestration skills (ZPWO, MMA, Copy Director, Meta Skill Builder, Workflow Translator)
- **Process:** Fully automated — `tx refactor <xml> --auto` runs Extraction, Synthesis, and Genesis in one call
- **Rationale:** Meta skills have standardized structure, well-defined contracts, and explicit dependency sections. Automated extraction is reliable for these.
- **Output:** Final Markdown mastery docs + JSONL records + graph edges — committed immediately

### Track B: Domain Departments (Human-Guided)

- **Scope:** 70+ domain skills across copy, design, research, product, email, ads, etc.
- **Process:** Department by department, with human revision at each stage:
  1. `tx refactor <xml> --draft` generates extraction scaffold (Markdown draft only)
  2. Human revises the draft using NotebookLM queries, knowledge enhancement, and strategic builds
  3. `tx refactor --commit <mastery_doc.md>` ingests the revised Markdown into JSONL records + graph edges
- **Rationale:** Domain skills contain nuanced knowledge that benefits from human curation, NotebookLM enrichment, and strategic revision before being committed as agent-readable records.
- **Output:** Enhanced Markdown mastery docs (human-curated) + JSONL records + graph edges — committed only after revision

### Mode Summary

| Flag | Stage 1: Extraction | Stage 2: Synthesis | Stage 3: Genesis |
|------|--------------------|--------------------|------------------|
| `--auto` | XML parse + typed validation | Final Markdown + JSONL records | Graph edges + index update |
| `--draft` | XML parse + typed validation | Draft Markdown only (no JSONL) | Skipped |
| `--commit` | Read revised Markdown frontmatter | Parse sections into records | Graph edges + index update |
| `--dry-run` | XML parse + typed validation | Print report only | Skipped |

---

## 3. Command Interface

### Primary Command

```
python tools/tx.py refactor <xml_path> [--auto] [--draft] [--domain DOMAIN] [--dry-run] [--json] [--force]
```

### Commit Command (Track B completion)

```
python tools/tx.py refactor --commit <mastery_doc.md> [--domain DOMAIN] [--json] [--force]
```

### Arguments & Flags

| Argument/Flag | Required | Default | Description |
|---------------|----------|---------|-------------|
| `xml_path` | Yes (refactor mode) | — | Path to SkillML V1.4 XML file |
| `--auto` | No | False | Full pipeline: Extraction + Synthesis + Genesis |
| `--draft` | No | True (default if no --auto) | Extraction + draft Markdown only |
| `--commit` | No | — | Ingest revised Markdown into JSONL + graph |
| `--domain` | No | Auto-detect from XML | Override target domain |
| `--dry-run` | No | False | Parse and report without writing |
| `--json` | No | False | Output extraction result as JSON |
| `--force` | No | False | Overwrite existing mastery doc |

If neither `--auto` nor `--draft` is specified, `--draft` is the default. This ensures the safe (human-reviewed) path is the default.

---

## 4. Pipeline Architecture

### Stage 1: Extraction (XML to Typed Schema)

**Input:** XML file path
**Output:** `RefactorResult` dataclass

Uses `xml.etree.ElementTree` (stdlib) to parse the XML file and extract structured data into typed dataclass contracts.

#### Typed Extraction Schema

```python
@dataclass
class SkillIdentity:
    skill_id: str           # From root skill_id attribute or <Meta>
    name: str               # Display name
    version: str            # Semantic version
    tier: str               # production | meta | experimental
    status: str             # active | draft | deprecated
    domain: str             # copy, meta, design, research, etc.
    track: str              # T1 | T2 | T3 | T4 | cross
    model: str              # sonnet | opus
    neurobox_position: str  # HEART, BODY, MIND, SPIRIT, PSYCH, CONSCIENCE, CENTER
    trigger_commands: list  # /command triggers
    source_xml: str         # Original XML file path

@dataclass
class SkillLayer:
    layer_id: str           # L1, L2, L3, L4
    name: str               # Layer display name
    token_budget: int       # Target token count
    load_priority: str      # always | when_executing | when_complexity_high | rarely
    content: str            # Raw content (CDATA stripped)
    frameworks: list        # Named frameworks extracted from this layer

@dataclass
class SkillContract:
    inputs_required: list   # [{name, format, description}]
    inputs_optional: list   # [{name, format, description}]
    outputs_primary: list   # [{name, format, description}]
    outputs_secondary: list # [{name, format, description}]
    quality_gates: dict     # {"T2": 6.0, "T3": 8.0, "T4": 9.0}
    circuit_breakers: dict  # {"max_fix_loops": 3, "on_exhausted": "HALT"}

@dataclass
class SkillEdge:
    target_id: str          # Target skill ID or SSOT reference
    relation: str           # DEPENDS_ON | COMPLEMENTS | SUPERSEDES | DERIVES_FROM | CONFLICTS_WITH
    priority: str           # critical | high | medium
    direction: str          # upstream | downstream
    strength: float         # 0.0-1.0 relationship strength

@dataclass
class RefactorResult:
    identity: SkillIdentity
    layers: list            # List of SkillLayer
    contract: SkillContract
    edges: list             # List of SkillEdge
    guardrails: list        # List of guardrail strings
    warnings: list          # Non-fatal extraction issues
    # Populated after synthesis:
    markdown_path: str
    records_created: int
    edges_created: int
```

#### Extraction Rules

- **Critical fields** (skill_id, name, version): Missing = error, abort
- **Important fields** (domain, track, tier): Missing = warning, use sensible default
- **Optional fields** (neurobox_position, trigger_commands): Missing = empty, no warning
- **Layer content:** Strip CDATA wrappers, preserve internal structure
- **Framework detection:** Scan layer content for named patterns (AwarenessFramework, BeliefLadder, ValueEquation, FailureModePlaybook, etc.)
- **Dependency extraction:** Parse `<Dependencies>`, `<UpstreamDependencies>`, `<DownstreamConsumers>` sections

### Stage 2: Synthesis (Schema to Artifacts)

**Input:** `RefactorResult` dataclass
**Output:** Markdown mastery document (+ JSONL records if `--auto`)

#### Markdown Mastery Document

Written to `.threadex/mastery/{domain}/{skill_slug}.md`

Template includes YAML frontmatter with all identity fields plus `refactored_at`, `source_xml`, `mode`, and `threadex_records` fields. Body contains sections for L1-L4 content, Contract (inputs, outputs, quality gates, circuit breakers), Dependencies (upstream/downstream), Guardrails, and Graph Edges.

#### JSONL Records (--auto mode only)

For each skill, create records via the existing `make_record()` + `append_record()` functions:

| Record # | Type | Status | Subdomain | Content Source |
|----------|------|--------|-----------|---------------|
| 1 | `reference` | `validated` | Primary subdomain | L1 quick reference + identity |
| 2-N | `pattern` | `candidate` | Thematic subdomain | Each named framework from L2-L3 |
| N+1-M | `insight` | `observed` | Thematic subdomain | Each L4 golden run example |
| M+1-P | `convention` | `golden` | `_shared/frameworks` | Critical guardrails (cross-skill) |

Each record includes `threadex_graph` pointers connecting to the mastery doc URI, other skill URIs, and SSOT references.

#### Domain Routing Table

| XML Domain | Mastery Directory | JSONL Expertise Domain | Default Subdomain |
|-----------|-------------------|----------------------|-------------------|
| `meta` | `mastery/meta/` | `strategist` | `offer_design` |
| `copy` | `mastery/copy/` | `writer` | `headlines` |
| `design` | `mastery/design/` | `designer` | `layout_patterns` |
| `research` | `mastery/research/` | `researcher` | `market_analysis` |
| `product` | `mastery/product/` | `strategist` | `offer_design` |
| `email` | `mastery/email/` | `writer` | `hooks` |
| `systems` | `mastery/systems/` | `_shared` | `frameworks` |
| `automations` | `mastery/automations/` | `_shared` | `frameworks` |
| `ads` | `mastery/ads/` | `writer` | `ctas` |
| `leadgen` | `mastery/leadgen/` | `strategist` | `funnel_architecture` |

### Stage 3: Genesis (Index + Graph)

**Input:** Created records + edges
**Output:** Updated index, shredded graph edges

1. **Shred edges into SQLite** — call existing `insert_edges()` for each edge extracted
2. **Index content in FTS5** — call existing `index_record_content()` for each JSONL record
3. **Update mastery index** — append entry to `.threadex/mastery/_index.yaml`
4. **Update Markdown frontmatter** — write record UUIDs back into mastery doc `threadex_records` field
5. **Print summary** — records created, edges shredded, warnings

---

## 5. Commit Mode (Track B Completion)

When the user finishes revising a draft mastery doc and is ready to commit it to the Threadex graph:

```
python tools/tx.py refactor --commit mastery/meta/zpwo_v4_0_0.md
```

### Commit Pipeline

1. **Parse frontmatter** — read YAML frontmatter from the Markdown file for identity metadata
2. **Parse sections** — extract L1-L4 content, contract, dependencies, guardrails from Markdown headers
3. **Create JSONL records** — same record creation as `--auto` mode
4. **Shred graph edges** — from the Dependencies section or Graph Edges section
5. **Update mastery index** — mark skill as committed in index
6. **Update frontmatter** — write record UUIDs back into the doc

### Frontmatter Requirements for Commit

The revised Markdown must retain these frontmatter fields:

```yaml
---
skill_id: (required)
name: (required)
version: (required)
domain: (required)
source_xml: (required — provenance link)
---
```

Additional fields (tier, track, model, neurobox) are optional at commit time — defaults used if missing.

---

## 6. Graph Edge Strategy

### Edge URI Convention

```
threadex://mastery/{domain}/{skill_slug}        # Mastery document node
threadex://{domain}/{subdomain}/{record_id}     # JSONL record node
ssot://{object_name}                            # SSOT reference (PROJECT_BRIEF, etc.)
```

### Edge Types Created

| Relation | When Created | Example |
|----------|-------------|---------|
| `DEPENDS_ON` | Skill requires another skill or SSOT | ZPWO DEPENDS_ON routing_table |
| `COMPLEMENTS` | Skills work together in a pipeline | ZPWO COMPLEMENTS MMA |
| `SUPERSEDES` | Newer skill replaces older version | Copy Director v3 SUPERSEDES v2 |
| `DERIVES_FROM` | Skill extracted patterns from source | Advertorial DERIVES_FROM Copy Director |
| `CONFLICTS_WITH` | Skills have incompatible approaches | (Rare — detected during extraction) |

### Edge Sources (Priority Order)

1. **XML Dependencies section** — explicit upstream/downstream declarations
2. **XML Contract section** — SSOT input references become DEPENDS_ON edges
3. **Relational operations YAML** (if available) — wake conditions, ownership chains
4. **Cross-references in content** — skill IDs mentioned in layer text (lower confidence, strength 0.5)

---

## 7. Directory Structure

### Before Refactor

```
.threadex/
+-- expertise/          # 4 domains, 15 JSONL files
+-- production/         # 1 project (sleep-energy)
+-- graph.db            # SQLite shadow graph
+-- threadex.config.yaml
```

### After Pilot (Track A)

```
.threadex/
+-- mastery/                              # NEW
|   +-- _index.yaml                       # Refactor registry
|   +-- meta/
|   |   +-- zpwo_v4_0_0.md               # 5 meta skills refactored
|   |   +-- mma_master_monitor_v1_0_0.md
|   |   +-- copy_director_v3_0_0.md
|   |   +-- meta_skill_builder_v4_0_0.md
|   |   +-- workflow_translator_v1_1_0.md
|   +-- (empty domain dirs created on demand)
+-- expertise/          # Enriched with skill pattern records
+-- production/
+-- graph.db            # Enriched with skill relationship edges
+-- threadex.config.yaml
```

### After Department Builds (Track B, progressive)

```
.threadex/
+-- mastery/
|   +-- _index.yaml
|   +-- meta/           # 5+ skills (complete)
|   +-- copy/           # 15+ skills (department build)
|   +-- design/         # 9+ skills (department build)
|   +-- research/       # 8+ skills (department build)
|   +-- email/          # 8+ skills (department build)
|   +-- ads/            # 8+ skills (department build)
|   +-- product/        # 6+ skills (department build)
|   +-- leadgen/        # 5+ skills (department build)
|   +-- systems/        # 3+ skills (department build)
|   +-- automations/    # 2+ skills (department build)
+-- expertise/          # Fully enriched
+-- production/
+-- graph.db            # Complete skill topology
+-- threadex.config.yaml
```

---

## 8. Pilot Batch (Track A: Orchestration)

### Skills Selected (5 meta/orchestration skills)

| # | Skill | XML Path | Rationale |
|---|-------|----------|-----------|
| 1 | ZPWO v4.0.0 | `.agents/skills/meta/zpwo_v4_0_0.xml` | Anchor — center node, orchestrates everything |
| 2 | MMA Master Monitor v1.0.0 | `.agents/skills/meta/mma_master_monitor_agent_v1_0_0.xml` | Quality gate — validates all production |
| 3 | Copy Director v3.0.0 | `.agents/skills/copy/skill_copy_director_v3_0_0_FINAL.xml` | Routing hub — dispatches all copy skills |
| 4 | Meta Skill Builder v4.0.0 | `.agents/skills/meta/meta_skill_builder_v4_0_0.xml` | Self-referential — builds new skills |
| 5 | Workflow Translator v1.1.0 | `.agents/skills/automations/MODULE_3_WORKFLOW_TRANSLATOR_v1_1_0.xml` | Translation patterns — cross-domain |

### Execution Order

```
1. ZPWO (anchor node — all others reference it)
   2. MMA (quality validator — ZPWO primary partner)
      3. Copy Director (routing hub — connects meta to domain)
         4. Meta Skill Builder (meta-skill — self-referential)
            5. Workflow Translator (translation — cross-domain)
```

### Success Criteria

- All 5 skills produce valid Markdown mastery docs in `.threadex/mastery/meta/`
- All JSONL records pass schema validation
- All graph edges shred into SQLite without errors
- `tx hubs` shows ZPWO as the top hub node
- `tx search "awareness"` finds patterns across refactored skills
- `tx graph neighbors threadex://mastery/meta/zpwo_v4_0_0` shows connections
- Warnings below 10% threshold (less than 3 across 5 skills)
- `tx graph broken` shows zero orphan edges within the pilot set

---

## 9. Implementation Scope

### New Code in tools/tx.py

| Component | Est. Lines | Description |
|-----------|-----------|-------------|
| Dataclass schemas | ~80 | 6 typed extraction contracts |
| XML parser functions | ~150 | parse_skill_xml, layer/contract/dependency extractors |
| Markdown generator | ~90 | generate_mastery_doc with frontmatter |
| JSONL record creator | ~70 | create_skill_records with domain routing |
| Commit mode parser | ~60 | parse_mastery_doc for --commit flag |
| Mastery index manager | ~30 | update_mastery_index |
| cmd_refactor | ~60 | CLI entry point with mode dispatch |
| Argparse extension | ~20 | Subparser with all flags |
| **Total** | **~560** | tx.py grows from ~2,317 to ~2,877 lines |

### New Acceptance Tests in tools/tx_acceptance_tests.py

| Test ID | Test Description |
|---------|-----------------|
| TX-21 | parse_skill_xml extracts identity from well-formed XML |
| TX-22 | extract_layers handles L1-L4 with missing layers gracefully |
| TX-23 | generate_mastery_doc produces valid YAML frontmatter + sections |
| TX-24 | create_skill_records creates correct record types and statuses |
| TX-25 | Full --auto pipeline: XML to Markdown + JSONL + edges (integration) |
| TX-26 | --dry-run produces report without side effects |
| TX-27 | --draft creates Markdown only, no JSONL or graph edges |
| TX-28 | --commit ingests revised Markdown into JSONL + graph |

### TOOL_INDEX.yaml Updates

Add under threadex section:

```yaml
refactor:
  command: "python tools/tx.py refactor"
  args: "<xml_path> [--auto] [--draft] [--domain DOMAIN] [--dry-run] [--json] [--force]"
  description: "Refactor XML skill into Markdown mastery doc + JSONL records"

refactor_commit:
  command: "python tools/tx.py refactor --commit"
  args: "<mastery_doc.md> [--domain DOMAIN] [--json] [--force]"
  description: "Commit revised mastery doc into JSONL records + graph edges"
```

---

## 10. What This Does NOT Include (Deferred)

| Item | Reason | When |
|------|--------|------|
| PydanticAI actual dependency | stdlib dataclasses achieve same typed validation | Future: multi-agent handoff |
| LLM-in-the-loop extraction | Automated extraction sufficient for pilot | Future: --llm-assist flag |
| Obsidian integration | User confirmed: after refactor | Next workstream |
| Batch refactor command | Pilot runs one-at-a-time for validation | Future: tx refactor --batch |
| COSM Hive Structure | Depends on refactor output to design hives | Future workstream |
| ION Classifier | Depends on mastery docs to classify | Future workstream |
| A2A Protocol integration | Seam present in dataclass contracts | Future phase |
| Temperature-based memory seams | Records use existing SIMS lifecycle | Future: HOT/WARM/COLD routing |
| Domain skill automation | Track B is human-guided by design | N/A — intentionally manual |

---

## 11. Risk & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| XML structure varies across skill versions | Extraction failures | Graceful fallback: missing fields = warnings, not errors |
| OneDrive EEXIST errors on file writes | Build interruption | Use Python patch script workaround (proven in Phase 2A) |
| Large XML files (some 90KB+) | Memory/parsing issues | ElementTree handles streaming; no full-file-in-memory needed |
| Domain routing ambiguity | Records in wrong expertise domain | --domain override flag; domain routing table configurable |
| Draft Markdown edited beyond recognition | Commit mode fails to parse | Require frontmatter fields; section headers as parse anchors |
| Graph edges create cycles | PRU scoring anomalies | Cycles are valid in skill relationships; PRU handles via decay |

---

## 12. Definition of Done

### Pilot (Track A) Complete When:

- `tx refactor --auto` works end-to-end for all 5 pilot skills
- `tx refactor --draft` produces valid Markdown drafts
- `tx refactor --commit` ingests revised Markdown
- `tx refactor --dry-run` produces report without side effects
- `.threadex/mastery/` directory created with proper structure
- `.threadex/mastery/_index.yaml` tracks all refactored skills
- All JSONL records pass schema validation
- All graph edges shred into SQLite
- `tx hubs` shows ZPWO as highest-connected node
- `tx search` finds knowledge across refactored skills
- `tx graph broken` shows zero orphans within pilot set
- TX-21 through TX-28 acceptance tests pass
- TOOL_INDEX.yaml updated with refactor entry points

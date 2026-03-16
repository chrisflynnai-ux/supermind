# Threadex Memory Architecture — Design Document

**Date:** 2026-03-11 (enhanced 2026-03-11 via NotebookLM Pass 1)
**Status:** Approved for implementation (phased) — Enhanced with 14 patches from 4 NotebookLM analyses
**System Name:** Threadex — Threaded Memory Architecture for SUPERMIND
**Philosophy:** U.L.T.R.A. — Ultimate Leverage through Relational Agentics

---

## 1. Purpose

Threadex is a three-tier, two-axis memory system that separates *what agents know* (expertise) from *what agents did* (production), stores both in human-readable files indexed by semantic search, and self-improves through a seven-stage pattern lifecycle (SIMS) with utility-based decay and auto-extraction heuristics.

**It replaces:** The 5 disconnected memory designs currently in the codebase (GOTCHA Python, Mansel Claw export, session memory.md files, SSOT-as-memory, and the unbuilt Hybrid Memory Model).

**Core principles:**
- Files are the source of truth. Databases are indexes.
- Knowledge compounds across sessions. Conversation dies with sessions.
- Every pattern has provenance. Nothing is magic.
- Local-first, zero cloud dependencies.
- Evaluators learn human judgment progressively (human-in-the-loop → Lead Evaluator skill).

**Relationship to MAA v4.0.0:** Threadex implements the memory seams that MAA declares (hot/warm/cold). MAA says *what* to remember. Threadex says *where* and *how*.

---

## 2. Two-Axis Thread Organization

### Axis 1: Expertise Threads (long-lived, agent-family-owned)

Organized by agent role family with sub-domain packs. Persistent knowledge — patterns, conventions, failures, golden frameworks.

```
.threadex/
├── expertise/
│   ├── writer/                     # Writer / Copywriter family
│   │   ├── _index.yaml             # Domain metadata, sibling links
│   │   ├── headlines.jsonl          # Sub-domain patterns
│   │   ├── hooks.jsonl
│   │   ├── ctas.jsonl
│   │   ├── voice.jsonl
│   │   └── golden/                  # Promoted golden patterns
│   │       └── headlines_golden.jsonl
│   ├── researcher/                  # Research & Discovery family
│   ├── designer/                    # Design / Producer family
│   ├── strategist/                  # Strategy / Planner family
│   ├── editor/                      # Editor / Enhancer family
│   ├── developer/                   # Developer / Builder family
│   ├── outreach/                    # Outreach / Connector family
│   ├── leads/                       # Leads / Enricher family
│   ├── ads/                         # Ads / Generator family
│   ├── publisher/                   # Publisher / Promoter family
│   ├── voice_agent/                 # Voice Agent / Supporter family
│   ├── email/                       # Email / Sequencer family
│   ├── video/                       # Video / Director family
│   ├── seo/                         # AI SEO / Ranker family
│   ├── product/                     # Product Manager family
│   ├── advisor/                     # Advisor / Strategist family
│   ├── tester/                      # Tester / Validator family
│   ├── onboarding/                  # Onboarding Mentor family
│   └── _shared/                     # Cross-domain patterns
│       ├── anti_patterns.jsonl
│       ├── frameworks.jsonl
│       └── golden/
```

**Sibling Pairs** (left-brain ↔ right-brain complements):
- Brother (left): Logical, tactical, structural (Analysis → Logic Reasoning)
- Sister (right): Strategic, creative, experiential (Synthesis → Creative Genesis)
- Defined in each `_index.yaml` with sibling links

**Progression:** Analysis → Synthesis → Genesis

### Axis 2: Production Threads (project-scoped, track-bound)

Organized by active project tracks with handoff memory. Operational layer — shorter-term, evaluated post-project for pattern extraction.

```
.threadex/
├── production/
│   ├── {project_id}/
│   │   ├── _manifest.yaml          # Project metadata, status, team
│   │   ├── t1_research/
│   │   │   ├── findings.jsonl
│   │   │   ├── handoff.yaml        # Typed contract to T2
│   │   │   └── evals.jsonl         # Post-track evaluation
│   │   ├── t2_draft/
│   │   ├── t3_production/
│   │   ├── t4_polish/
│   │   └── _postmortem.yaml        # Feeds SIMS pipeline
│   └── _archive/                    # Completed projects (cold)
```

**Bridge:** Post-project `_postmortem.yaml` → Deconstructor evaluation → SIMS promotion pipeline.

### Handoff Contract Schema (handoff.yaml)

```yaml
# Typed contract between tracks — functions as UAI TaskResult/TaskRequest bridge
from_track: t1_research
to_track: t2_draft
created_at: "2026-03-11T10:00:00Z"
created_by: researcher_agent

# State & Artifact Links
ssot_pointers:
  - file: findings.jsonl
    checksum: "sha256:abc123..."
  - file: PROJECT_BRIEF.yaml
    checksum: "sha256:def456..."
artifacts_produced:
  - "findings.jsonl (47 records)"
  - "competitor_analysis.md"

# Decisions & Rejected Alternatives
decisions_made:
  - "Cortisol-melatonin angle selected over adrenal fatigue angle"
rejected_alternatives:
  - "Adrenal fatigue framing — too clinical, low emotional resonance"
open_questions:
  - "Need clinical citation for 73% cortisol claim"

# Quality
mma_verdict:
  score: 7.8
  passed: true
  gate: "T1→T2 requires ≥7.0"

# Constraints for next track
token_budget: 50000
timeout_seconds: 3600
mma_threshold: 8.0
```

### Track-Level Eval Schema (evals.jsonl)

```yaml
# Appended per-track after completion
{
  "track": "t1_research",
  "agent_id": "researcher_agent",
  "completed_at": "2026-03-11T12:00:00Z",

  # Execution metrics
  "execution_metrics": {
    "duration_ms": 45000,
    "prompt_tokens": 12500,
    "completion_tokens": 8200,
    "total_cost_usd": 0.42
  },

  # Quality metrics
  "quality_metrics": {
    "mma_score": 7.8,
    "assertions_passed": 12,
    "assertions_failed": 1
  },

  # Friction metrics (feeds SIMS extraction heuristics)
  "friction_metrics": {
    "fix_loops_triggered": 1,
    "rework_count": 0,
    "human_interventions": 0,
    "violated_invariants": []
  }
}
```

### Abandoned Project Protocol

When a project is abandoned mid-track:
1. Mark as `abandoned` in `_manifest.yaml` with abandonment reason
2. Force **pre-compaction flush**: checkpoint decisions and summarize open loops
3. Generate `_partial_postmortem.yaml` with failure classification (e.g., `CLIENT_SCOPE_CHANGE`, `API_LIMIT_EXCEEDED`, `UNRESOLVABLE_HALLUCINATION`, `BUDGET_EXHAUSTED`)
4. Route to Reflector for **dead-end mining** (CRACKS extraction)
5. Move partial artifacts to `_archive/` (Tier 3 cold storage)
6. Do NOT let incomplete work enter Tier 2 semantic search — quarantine from active retrieval

---

## 3. Three-Tier Storage

### Tier 1 — Human Layer (Files) — BUILD PHASE 1
- JSONL records per sub-domain (append-only, merge-safe)
- YAML for indexes, manifests, handoffs, postmortems
- Markdown for human-written expertise notes
- Git-tracked with `merge=union` for JSONL
- THE SOURCE OF TRUTH

**Concurrent write protection:**
- Phase 1: Advisory file locking (like Mulch) — lock file before append, release after flush
- Phase 2+: Write-Ahead Logging (WAL) protocol — decouple disk flush from RAM updates for crash-recoverability
- Multi-agent parallel execution: agents write to isolated track directories (no cross-track file sharing during execution)

**Log rotation policy:**
- Episodic logs: daily rotation (`YYYY-MM-DD.jsonl`) to cap individual file size
- Expertise JSONL: compaction trigger when records exceed 10K per file — background thread copies live (non-tombstoned) records to new generation file
- Git diffs remain manageable through rotation + compaction

**Pre-compaction flush (GC protocol):**
- Before any context compression or archival: checkpoint open decisions, summarize active loops, archive reasoning chain
- Never discard raw context without first extracting actionable MEMORY_SEAM_NOTEs
- Flush triggers: manual `/gc`, 70% context saturation (hard), 50% context saturation (soft warning)

### Tier 2 — Search Layer (QMD) — BUILD PHASE 2
- QMD engine: BM25 keyword + local embeddings + MMR + utility-weighted scoring
- Knowledge Graph traversal for relational discovery (Phase 2 expansion — evaluate Cognee/NetworkX/custom)
- Indexes all Tier 1 files automatically
- Local, private, zero cloud dependencies
- THE RETRIEVAL ENGINE

**Future seam — Graph layer:** Pure BM25 + embeddings miss relational context. Phase 2 must evaluate adding Knowledge Graph traversal (hub nodes for cross-domain entity mapping) alongside vector search. Three-phase retrieval: Parallel Scan (BM25 + embeddings) → Deep Dive (graph traversal + metadata filtering) → Backtrack (cross-references if initial results insufficient).

### Tier 3 — Structured Layer (SQLite + DuckDB+vss) — BUILD PHASE 3
- SQLite: conversation logs, session states, outcome tracking
- DuckDB+vss: vector search on cold archived projects
- MMA scores, BENCHMARK_ARTIFACTs, pattern metadata
- THE ANALYTICS ENGINE

**Separation rule:** Factual knowledge stays in Tier 1 files. Operational data (event logs, execution metrics, high-frequency states) stays in Tier 3 databases. Never mix — routing operational data into Tier 1 causes context suffocation.

---

## 4. SIMS — Self-Improving Memory Schema

Seven-stage Hybrid Ladder with progressive evaluator learning:

```
OBSERVED → VALIDATED (3+ cross-context) → CANDIDATE (Deconstructor 8+) → GOLDEN (human-approved)
                                    ↘                        ↘
                              CONTESTED (conflicting)   DEPRECATED (retired)
                                    ↘
                              FORBIDDEN (proven anti-pattern)
```

### Positive Progression (4 stages)

**Stage 1 — Observed:** Agent logs record via `tx record`. Contains what, context, source, timestamp. Auto-extraction heuristics may fast-track (see below).

**Stage 2 — Validated:** Same insight succeeds 3+ times across *different* contexts (different agents, different projects, or different datasets). Simple same-context repetition does not count. Evidence tracked in record metadata via `evidence_count` and `evidence_contexts[]`.

**Stage 3 — Candidate:** Deconstructor skill evaluates pattern, scores via MMA. If 8.0+ → promoted to candidate. Human reviews eval report and suggests enhancements.

**Stage 4 — Golden:** Human approves. Pattern moves to `golden/` subfolder. Gets priority loading in `tx prime`. Generator → Reflector → Curator gate enforced: never auto-promote to GOLDEN.

### Negative/Lateral Stages (3 stages)

**Stage 5 — Contested:** Pattern has conflicting evidence — succeeds in some contexts, fails in others. Triggers conditional branching analysis. Curator decides: split into context-specific variants, merge with conditions, or demote.

**Stage 6 — Deprecated:** Pattern was once valid but is now superseded by a better approach, or the underlying capability has been absorbed by the foundation model. Remains searchable for historical reference but excluded from `tx prime`. Weekly consolidation passes mark deprecated patterns with `deprecated_reason` and `superseded_by`.

**Stage 7 — Forbidden:** Proven anti-pattern. Actively loaded as a "do NOT do this" guard in `tx prime --with-guards`. Prevents agents from repeatedly exploring dead ends. Extracted from max-retry failures, circuit breaker triggers, and human-flagged harmful patterns.

### Auto-Extraction Heuristics

Certain execution outcomes trigger automatic SIMS extraction:

| Signal | Auto-Action | Target Stage |
|--------|-------------|--------------|
| Zero rework + MMA ≥ 9.0 on first attempt | Extract success pattern | → CANDIDATE |
| Token usage 30%+ below baseline | Extract efficiency pattern | → CANDIDATE |
| Rework reduced 50%+ vs historical avg | Extract for A/B testing | → OBSERVED |
| `max_fix_loops` (3) circuit breaker hit | Extract anti-pattern | → FORBIDDEN |
| Unparsable/hallucinated response | Extract failure pattern | → FORBIDDEN |
| Human flags pattern as harmful | Immediate extraction | → FORBIDDEN |

### Contradiction Resolution (The Contradiction Rule)

When two GOLDEN patterns conflict:
1. **Flag** the conflict immediately — never silently overwrite
2. **Keep** the newest/most context-relevant as canonical GOLDEN
3. **Move** the older to CONTESTED with `conflict_reason` and `conflicting_pattern_id`
4. **Log** the change rationale in both records
5. **Notify** human for review
6. If both are valid in different contexts → create conditional parent with context-specific routing (e.g., "short headlines for B2B" vs "long headlines for B2C")

### Evaluator Evolution Path

1. Current: Deconstructor skills score → human reviews eval report
2. Near-term: Lead Evaluator skill absorbs human correction patterns
3. Future: Custom evaluator skills (Human Persuasion Editor, Neuro-Resonance Auditor) handle domain-specific evaluation with human-like capability
4. Human always reviews after each phase until evaluator skill is trusted
5. Progressive trust transfer: A/B shadow testing over 50+ cycles, reduce human oversight only at >95% match rate

### Utility-Based Decay (replaces static temporal decay)

Static 90/180-day decay is too rigid for domains with long project cycles. Decay is now utility-driven:

**Decay formula:** `utility = utility + alpha * (reward - utility)` where reward = outcome signal from retrieval success/failure.

**Tracking fields per record:** `last_accessed`, `num_recalled`, `utility_score`

**Decay rules by record type:**
- **Episodic traces** (operational logs): Fast exponential decay — compress or archive after 30 days of non-access
- **Procedural knowledge** (conventions, patterns): Zero temporal decay — only deprecated via explicit Curator decision or Atomic Merge
- **Golden patterns**: Flag for review if `num_recalled == 0` over 180 days, but never auto-demote

**Fallback defaults** (when utility scoring unavailable):
- Patterns with `num_recalled == 0` for 90 days: flag for review
- Golden patterns with `num_recalled == 0` for 180 days: flag for human review
- Forbidden patterns: never decay (guards must persist)

---

## 5. Record Schema (6 Types)

```yaml
# JSONL record format (one per line)
{
  "id": "uuid",
  "type": "convention | pattern | failure | decision | reference | insight",
  "status": "observed | validated | candidate | golden | contested | deprecated | forbidden",
  "cognitive_stage": "evolving | refined | wisdom",
  "domain": "writer/headlines",
  "content": "3-word power headlines convert 2.1x vs long headlines",
  "context": "Sleep Energy advertorial project, A/B test March 2026",
  "source_project": "sleep-energy-2026-03",

  # Evidence tracking
  "evidence_count": 0,
  "evidence_contexts": [],
  "mma_score": null,

  # Provenance (core)
  "created_at": "2026-03-11T10:00:00Z",
  "updated_at": "2026-03-11T10:00:00Z",
  "created_by": "writer_agent",
  "provenance": "t3_production/builds.jsonl#line42",

  # Provenance (cross-harness)
  "model_id": "claude-opus-4.6",
  "model_version": "2026-03",
  "harness_id": "claude-gemini",
  "harness_version": "1.0",
  "skill_version": "advertorial_copy_master_v2.0.0",
  "prompt_checksum": null,

  # Utility-based decay tracking
  "last_accessed": null,
  "num_recalled": 0,
  "utility_score": 0.5,

  # Metadata
  "tags": ["headlines", "health", "conversion"],

  # Lifecycle metadata (populated as needed)
  "conflict_reason": null,
  "conflicting_pattern_id": null,
  "deprecated_reason": null,
  "superseded_by": null
}
```

---

## 6. _index.yaml Schema

```yaml
# Per agent-family domain index
domain: writer
family: copywriting
description: "Writer / Copywriter agent family — headlines, hooks, CTAs, voice"
siblings:
  brother: researcher        # Left-brain complement
  sister: editor             # Right-brain complement
track: resonance             # Primary Agentic Function
progression:
  analysis: researcher       # Logic Reasoning
  synthesis: strategist      # Strategic Synthesis
  genesis: writer            # Creative Genesis

sub_domains:
  - name: headlines
    file: headlines.jsonl
    record_count: 0
    golden_count: 0
  - name: hooks
    file: hooks.jsonl
    record_count: 0
    golden_count: 0
  - name: ctas
    file: ctas.jsonl
    record_count: 0
    golden_count: 0
  - name: voice
    file: voice.jsonl
    record_count: 0
    golden_count: 0

# Governance visibility (auto-updated by tx commands)
pattern_counts:
  observed: 0
  validated: 0
  candidate: 0
  golden: 0
  contested: 0
  deprecated: 0
  forbidden: 0

created_at: "2026-03-11"
last_updated: "2026-03-11"
```

### _shared/ Governance (Private → Client → Collective Gradient)

The `_shared/` directory is NOT a dumping ground. Strict promotion rules apply:

1. **Private:** All patterns start in their agent-family domain. No pattern enters `_shared/` by default.
2. **Client:** Pattern proves effective in 2+ agent families on the same client project. Remains project-scoped.
3. **Collective:** Pattern passes through Generator → Reflector → Curator gate confirming:
   - Cross-domain transferability (validated in 2+ unrelated domains)
   - Permission-safe (no project-specific data leakage)
   - Generalized (stripped of project-specific noise)
   - HCTS-formatted (classified as Hack, Crack, Track, or Stack)
4. Only then does pattern enter `_shared/` with full attribution metadata (`origin_domain`, `promoted_by`, `promotion_reason`)

---

## 7. Threadex CLI Interface

```bash
# WRITE operations (append-only)
tx record {domain}/{subdomain} --type {type} "content"
tx record --project {id} {track}/{category} --type {type} "content"

# READ operations (context priming)
tx prime {domain}                    # Golden + recent patterns as XML
tx prime {domain} --all              # All sub-domains
tx prime --project {id}              # Production memory for project
tx prime --siblings {domain}         # Domain + its sibling patterns

# SEARCH operations (Tier 2)
tx search "query"                    # Semantic + keyword hybrid
tx search --domain {domain} "query"  # Domain-scoped
tx search --golden-only "query"      # Only golden patterns

# LIFECYCLE operations (SIMS)
tx validate {domain}/{subdomain} --record-id {id}
tx evaluate {domain}/{subdomain} --record-id {id}
tx promote {domain}/{subdomain} --record-id {id}
tx contest {domain}/{subdomain} --record-id {id} --reason "..."
tx deprecate {domain}/{subdomain} --record-id {id} --superseded-by {id}
tx forbid {domain}/{subdomain} --record-id {id} --reason "..."
tx decay --check                          # Utility-based decay scan
tx compact {domain}/{subdomain}           # Trigger log compaction

# PROJECT operations
tx project create "{name}" --team {agents}
tx handoff {project} {from_track} {to_track}
tx postmortem {project}
```

---

## 8. MAA + Harness Connections

**MAA v4.0.0:**
- MEMORY_SEAM_NOTE → `tx record`
- LEARNING_ARTIFACT → `tx record --type insight`
- Hot/warm/cold → Tier 1 (hot: active project), Tier 2 QMD (warm), Tier 3 DuckDB (cold)

**Future Harness:**
- Both harnesses read from same Threadex store
- `tx prime` output is model-agnostic (XML/Markdown)
- Production threads track which harness/model produced each artifact
- Enables cross-harness A/B comparison

---

## 9. Future Seams (Declared, Not Building Now)

These emerged from NotebookLM analysis (2026-03-11) and are acknowledged as future expansion points:

| Seam | Phase | Description |
|------|-------|-------------|
| **Third Axis (Meta/PRISM Core)** | 2 | Dedicated axis for meta-patterns (HCTS library, system intelligence). Currently housed in `_shared/`. |
| **Knowledge Graph in Tier 2** | 2 | Graph traversal alongside BM25 + embeddings for relational discovery. Evaluate Cognee/NetworkX. |
| **Semantic Lookaside Buffer (SLB)** | 2-3 | Cache recently used semantic clusters for microsecond retrieval locality. |
| **UAI TaskRequest/TaskResult schemas** | 3A | Formal JSON-schema inter-agent contracts for harness build. |
| **Cross-model GOLDEN validation** | 3A+ | Pattern must pass secondary harness execution before global GOLDEN status. |
| **Blind grading evaluator pod** | 3A+ | 4-role pod (Executor, Grader, Comparator, Analyzer) for drift detection. |
| **Cross-harness A/B experiment tracking** | 3A+ | BENCHMARK_ARTIFACT schema for model comparison. |
| **Model-aware retrieval budgets** | 2 | `tx prime` adapts output based on requesting model's context window. |
| **Context rendering pipeline** | 3A | Continuous Ingest→Evaluate→Compact→Budget→Render between API calls. |
| **Sidecar Blob Arena** | 3 | 64-byte JSONL previews + mmap-backed payload file for large records. |
| **INT8 embedding quantization** | 3 | 3.1x storage reduction, 5.6x acceleration for vector search. |
| **Shadow compaction (double-buffered GC)** | 3 | Background thread copies live records to new generation file without blocking. |
| **Cognee evaluation** | 2 | Assess Cognee as unified memory backend vs custom QMD + graph. |
| **Context quarantine** | 3A | >5000 token operations auto-routed to isolated sub-agent, returns summary + ref ID. |

---

## 10. Build Phases

**Phase 1 — File Layer (Tier 1)** — Build now
- `.threadex/` folder structure with expertise + production axes
- JSONL record schema (7 statuses, provenance fields, utility tracking) + `_index.yaml` schema (pattern counts, governance)
- Enhanced handoff.yaml, evals.jsonl, and _partial_postmortem.yaml schemas
- `tx` CLI tool (Python): record, prime, project, handoff, contest, deprecate, forbid, compact
- Advisory file locking for concurrent write protection
- Log rotation (daily episodic, compaction at 10K records)
- Pre-compaction flush protocol for GC
- _shared/ governance (Private → Client → Collective gradient)
- Auto-extraction heuristics wired into SIMS
- Seed initial expertise threads (writer, researcher, strategist, designer)
- Wire MAA MEMORY_SEAM_NOTE to `tx record`

**Phase 2 — Search Layer (Tier 2)** — After Phase 1 stable
- QMD engine integration (BM25 + local embeddings + utility-weighted scoring)
- Knowledge Graph traversal evaluation (Cognee vs NetworkX vs custom)
- `tx search` command with three-phase retrieval (Scan → Deep Dive → Backtrack)
- Model-aware retrieval budgets for `tx prime`
- Auto-index on file change (event-driven + pre-query flush)
- Evaluate: Cognee vs QMD vs custom

**Phase 3 — Structured Layer (Tier 3)** — With harness build
- SQLite for conversation logs, session states, outcomes
- DuckDB+vss for vector search on cold storage
- WAL protocol replacing advisory locking
- SIMS automated lifecycle (validate, evaluate, promote, contest, deprecate, forbid, decay)
- Evaluator Pod integration for blind A/B testing
- Shadow compaction and Sidecar Blob Arena optimizations

---

## 11. Definition of Done (Phase 1)

- [ ] `.threadex/expertise/` folder structure exists with 4+ seeded domains
- [ ] `.threadex/production/` folder structure exists with project template
- [ ] JSONL record schema defined with all 7 statuses, provenance fields, utility tracking
- [ ] `_index.yaml` schema defined with sibling pairs and pattern_counts governance
- [ ] handoff.yaml schema defined with typed contract fields
- [ ] evals.jsonl schema defined with execution/quality/friction metrics
- [ ] `tx` CLI handles: record, prime, project, handoff, contest, deprecate, forbid, compact
- [ ] Auto-extraction heuristics fire on zero-rework and max-retry signals
- [ ] Contradiction rule implemented (flag, keep, move, log, notify)
- [ ] _shared/ governance enforced (Private → Client → Collective gradient)
- [ ] Advisory file locking prevents concurrent write corruption
- [ ] Log rotation works (daily episodic, compaction at threshold)
- [ ] Pre-compaction flush checkpoints decisions before GC
- [ ] Golden promotion requires human Curator gate (never auto-promote)
- [ ] MAA MEMORY_SEAM_NOTE contract maps to tx record
- [ ] Git-tracked with merge=union for JSONL files

---

## 12. NotebookLM Enhancement History

**Pass 1 (2026-03-11):** 4 NotebookLM docs analyzed (MAA Master Build Knowledge I, IA, II, III). ~360 raw findings → 14 recurring themes → 14 patches applied, 14 future seams declared, 9 doctrine conflicts resolved. Key additions: 3 SIMS lifecycle stages (DEPRECATED/CONTESTED/FORBIDDEN), utility-based decay, cross-harness provenance fields, enhanced handoff/eval/postmortem schemas, auto-extraction heuristics, _shared/ governance, concurrent write protection, log rotation, pre-compaction flush, contradiction resolution rule, Knowledge Graph seam for Tier 2.

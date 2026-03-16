# NotebookLM Threadex Memory Architecture Query Pack V1

Date: 2026-03-11
Target: `docs/plans/2026-03-11-threadex-memory-architecture-design.md`
Stage: Pre-build enhancement — run BEFORE Phase 1 implementation begins

## Purpose

Generate enhancement inputs for the Threadex Memory Architecture design through NotebookLM analysis of memory systems, agentic patterns, and production references.

NotebookLM should help with:
- validating the two-axis (expertise + production) organization
- stress-testing the three-tier storage model
- strengthening the SIMS lifecycle stages and transitions
- identifying missing record types, fields, or edge cases
- improving the evaluator evolution path
- finding gaps in QMD/search layer design
- validating sibling pair memory threading patterns
- identifying cross-harness memory compatibility issues

NotebookLM should NOT decide:
- final search engine choice (QMD vs Cognee vs custom)
- final vector DB choice (DuckDB+vss vs alternatives)
- whether to abandon file-first for DB-first
- harness architecture (that is a separate query pack)
- which 20+ agents to build first

---

## Query Cluster A: Three-Tier Storage Validation

Prompt:
```text
Analyze the Threadex three-tier storage architecture:
- Tier 1: Human-readable files (JSONL, YAML, MD) — source of truth
- Tier 2: QMD search layer (BM25 + embeddings + MMR + temporal decay) — retrieval
- Tier 3: SQLite + DuckDB+vss — analytics and cold storage

Evaluate this against modern agentic memory patterns. Focus on:

1. Is file-first (Tier 1 as truth, databases as indexes) the right default for a multi-agent system that needs merge-safety, provenance, and human readability? What are the failure modes?

2. Where does the three-tier model break down? What memory operations require all three tiers simultaneously? Which operations only need one tier?

3. What is the optimal sync strategy between Tier 1 files and Tier 2 indexes? Event-driven (file watcher)? Batch rebuild? Lazy indexing on first query?

4. JSONL with append-only + git merge=union — what are the scaling limits? At what record count does this strategy fail? What mitigation exists (log rotation, compaction)?

5. What modern patterns exist for separating "factual knowledge" from "operational data" in memory systems? Does our Tier 1 / Tier 3 split match those patterns?

Format output as:
- Validation confirmations (what is strong)
- Failure modes identified
- Missing specifications
- Recommended additions
- Scale limits and mitigations
```

## Query Cluster B: SIMS Lifecycle & Evaluator Evolution

Prompt:
```text
Analyze the SIMS (Self-Improving Memory Schema) lifecycle:
OBSERVED → VALIDATED (3+ successes) → CANDIDATE (Deconstructor 8+) → GOLDEN (human-approved)

And the evaluator evolution path:
1. Deconstructor skills score → human reviews eval report
2. Lead Evaluator skill absorbs human correction patterns
3. Custom evaluator skills (Human Persuasion Editor, Neuro-Resonance Auditor) handle domain-specific evaluation
4. Human reviews after each phase until evaluator skill is trusted

Evaluate against modern self-improving and RLHF-lite patterns. Focus on:

1. Are 4 stages the right number? Should there be a "RETIRED" or "DEPRECATED" stage? What about "CONTESTED" (conflicting evidence)?

2. The "3+ successes" threshold for VALIDATED — what constitutes a "success"? Same agent, different agent, different project? How do you avoid confirmation bias?

3. Temporal decay (90 days demote, 180 days review for golden) — is this the right cadence? What happens to patterns in domains with long project cycles (6+ months)?

4. The evaluator evolution path moves from Deconstructor → Lead Evaluator → Custom Evaluator. What are the risks of "evaluator drift" where the automated evaluator diverges from human judgment? How to detect it?

5. What modern patterns exist for "progressive trust transfer" from human to automated evaluators? How do you measure when an evaluator is ready to reduce human oversight?

6. What happens when two golden patterns contradict each other? How should conflict resolution work in the SIMS lifecycle?

Format output as:
- Lifecycle strengths
- Missing stages or transitions
- Threshold improvements
- Evaluator evolution risks and mitigations
- Conflict resolution patterns
- Recommended additions to SIMS
```

## Query Cluster C: Two-Axis Organization & Sibling Pairs

Prompt:
```text
Analyze the Threadex two-axis memory organization:

AXIS 1 (Expertise): Long-lived, agent-family-owned knowledge organized by role (writer, researcher, designer, etc.) with sub-domain packs (headlines, hooks, CTAs, voice).

AXIS 2 (Production): Project-scoped, track-bound operational memory organized by 4 production tracks (T1 Research → T2 Draft → T3 Production → T4 Polish) with typed handoffs.

BRIDGE: Post-project postmortems → Deconstructor evaluation → SIMS promotion into Axis 1.

SIBLING PAIRS: Left-brain (logical/tactical) ↔ Right-brain (strategic/creative) complements.
Progression: Analysis → Synthesis → Genesis.

Focus on:

1. Is two-axis (knowledge vs operations) the optimal split? Should there be a third axis for "meta-patterns" — patterns about how patterns are used? Or does that belong in Axis 1 shared?

2. The bridge from Axis 2 → Axis 1 (postmortem → SIMS) — what information is typically lost in this transition? What should the postmortem schema capture that our current design doesn't?

3. Sibling pair memory threading — when a "brother" (left-brain researcher) discovers a pattern, how should that inform the "sister" (right-brain editor)? Push notification? Shared search scope? Bidirectional golden promotion?

4. 17 agent families × N sub-domains = potentially large folder structure. At what point does folder proliferation hurt navigation? What pruning or consolidation strategies work?

5. The `_shared/` cross-domain directory — what patterns should live here vs in specific agent families? How do you prevent `_shared/` from becoming a dumping ground?

6. How should the progression model (Analysis → Synthesis → Genesis) be tracked in memory? Should there be "maturity tags" on records indicating which progression stage they serve?

Format output as:
- Axis validation results
- Bridge gap analysis
- Sibling pair threading patterns
- Folder structure recommendations
- Shared memory governance
- Progression tracking patterns
```

## Query Cluster D: QMD & Search Layer Architecture

Prompt:
```text
We plan to build a QMD (Query Memory Device) as the Tier 2 search layer for Threadex:
- BM25 keyword search
- Local embeddings for semantic search
- MMR (Maximal Marginal Relevance) for diversity
- Temporal decay for recency weighting
- Zero cloud dependencies (local-first)

Reference implementations: os-eco/Mulch (BM25 + JSONL), Cognee (knowledge graphs), MemO (memory optimization).

Focus on:

1. For a multi-agent system with 17+ agent families and thousands of JSONL records — what is the right embedding model for local-first semantic search? What are the trade-offs between accuracy, speed, and resource usage?

2. BM25 + embeddings hybrid — what is the optimal fusion strategy? Score interpolation? Reciprocal rank fusion? Cascading (BM25 filter → embedding rerank)?

3. MMR for diversity — is this the right approach for agent memory retrieval? When would you want maximum relevance (no diversity) vs maximum diversity?

4. Temporal decay formula — what works for agentic memory? Linear decay? Exponential? Should decay rate vary by record type (conventions decay slowly, decisions decay fast)?

5. How should the search layer handle cross-domain queries? (e.g., "What headline patterns work for health audiences?" spans writer/headlines + researcher/audiences)

6. Index update strategy — should indexes rebuild on every `tx record` operation? On first `tx search`? On a schedule? What is the latency-freshness trade-off?

7. What modern patterns exist for "context-window-aware" retrieval — where the search layer knows how many tokens the requesting agent has available and adjusts result count?

Format output as:
- Search architecture validation
- Embedding model recommendations
- Fusion strategy recommendations
- Decay formula proposals
- Cross-domain query patterns
- Index update strategies
- Context-aware retrieval patterns
```

## Query Cluster E: Production Track Memory & Handoffs

Prompt:
```text
Analyze the Threadex production memory system:

Each project has 4 tracks: T1 Research → T2 Draft → T3 Production → T4 Polish
Each track has: findings/builds JSONL, typed handoff YAML, post-track evals JSONL
Projects end with: _postmortem.yaml → SIMS pipeline

Track handoffs are typed contracts (T1 produces research brief for T2, etc.)

Focus on:

1. What information must be in a typed handoff contract between tracks? Our current design has handoff.yaml — what fields are essential? (decisions made, rejected alternatives, open questions, quality scores, artifacts produced?)

2. Track-level evals (evals.jsonl per track) — what should the eval schema look like? MMA scores? Time spent? Error count? Rework count? How does this feed the postmortem?

3. The postmortem → SIMS bridge — what patterns should be automatically extracted vs. human-curated? Can we define extraction heuristics (e.g., "any pattern that reduced rework by 50%+ → auto-candidate")?

4. How should production memory handle parallel tracks? (e.g., T2 and T3 running simultaneously on different deliverables within the same project)

5. Project archive strategy — when a project completes and moves to `_archive/`, what should remain searchable? Full history? Only golden extracts? Postmortem + handoffs only?

6. How should production memory connect to expertise memory during execution? (e.g., T3 writer agent needs to query writer/headlines expertise while building)

7. What happens when a project is abandoned mid-track? How should partial production memory be handled?

Format output as:
- Handoff contract schema recommendations
- Eval schema proposals
- Postmortem extraction heuristics
- Parallel track patterns
- Archive strategy recommendations
- Cross-axis query patterns (production ↔ expertise)
- Abandoned project handling
```

## Query Cluster F: Cross-Harness Memory Compatibility

Prompt:
```text
Threadex must serve as the shared memory layer for a dual-harness system:
- Harness A: Claude + Gemini (primary)
- Harness B: Codex + OpenClaw (secondary/future)

Both harnesses read from and write to the same Threadex store.
Production threads track which harness/model produced each artifact.
Goal: Enable cross-harness A/B comparison.

Focus on:

1. What provenance fields are needed per record to track which model/harness generated or validated a pattern? Model name, model version, harness version, temperature, prompt version?

2. How do you prevent "model bias" in the pattern library? (e.g., if Claude generates 90% of patterns, the golden library becomes Claude-optimized and underperforms on Gemini)

3. Cross-harness A/B comparison — what is the minimal experiment tracking schema? How do you compare "Claude wrote this headline" vs "Gemini wrote this headline" fairly when contexts differ?

4. Different models have different context windows, token costs, and capabilities. How should Threadex adapt `tx prime` output based on which model is requesting memory? Model-aware context budgets?

5. What memory format is most model-agnostic? Our design uses XML/Markdown for `tx prime` output — is this optimal? Would JSON or structured YAML be more portable?

6. How should Threadex handle conflicting patterns from different harnesses? (e.g., Claude discovers "short headlines convert better" but Gemini discovers "long headlines convert better" — both may be valid in their contexts)

Format output as:
- Provenance field requirements
- Model bias mitigation strategies
- A/B experiment tracking schema
- Model-aware retrieval patterns
- Format portability analysis
- Cross-harness conflict resolution
```

---

## Normalized Output Format

Convert NotebookLM findings into a patch-ready document with these sections:

### Bucket 1: PATCH NOW (apply to design doc before build)
- Missing schema fields
- Missing lifecycle stages or transitions
- Missing specifications for Tier 1 implementation
- Improved thresholds or formulas

### Bucket 2: DECLARE AS FUTURE SEAMS (design doc addendum)
- Tier 2/Tier 3 design improvements (not building yet)
- Harness-specific adaptations
- Advanced evaluator patterns
- Scale-up strategies

### Bucket 3: DOCTRINE CONFLICTS (need resolution)
- Contradictions between Threadex design and MAA v4.0.0
- Contradictions between Threadex design and ZPWO v4.0
- Contradictions with os-eco/Mulch reference patterns

---

## Merge Rule

NotebookLM output is seed material.
Only promote findings that improve the current Threadex design.

Reject anything that:
- Abandons file-first for database-first
- Requires cloud dependencies
- Locks in a specific search engine before Phase 2 evaluation
- Adds complexity that doesn't serve Phase 1 (file layer) build
- Reintroduces flat non-relational memory patterns
- Couples memory to a specific harness implementation

---

## Recommended Notebook Loading

Load these sources into NotebookLM alongside the query pack:

**Required:**
1. `docs/plans/2026-03-11-threadex-memory-architecture-design.md` — THE design being validated
2. `.agents/skills/automations/automations_master_architect_v4_0_0.xml` — MAA v4.0.0 (memory seams + contracts)

**Highly Recommended:**
3. os-eco/Mulch README or source (BM25 + JSONL reference implementation)
4. Any Cognee / MemO documentation (search layer comparison)
5. M5 Implementation Appendix (voice agent memory patterns)
6. M6 architecture docs (conversation state + learning optimization)

**Optional Context:**
7. ZPWO v4.0 skill (orchestration doctrine)
8. Super Knowledge compendiums (agentic architecture, autonomous OS)
9. ULTRAMIND Constitution / Resonance Constitution

---
skill_id: meta_zpwo
name: Zero-Point Workflow Orchestrator
version: 4.0.0
tier: meta
status: active
domain: meta
track: cross
model: sonnet
neurobox: CENTER (7th Dimension) - THE SOUL
triggers: [/zpwo, /status, /gc, /handoff, /ship]
source_xml: .claude\skills\meta\zpwo_v4_0_0.xml
mode: auto
refactored_at: 2026-03-16T08:26:24.505203+00:00
threadex_records: []
---

# Zero-Point Workflow Orchestrator (v4.0.0)

> command Slash command or workflow trigger PROJECT_BRIEF Project goal, avatar, offer (required for T2+) MESSAGE_SPINE Promise, mechanism, proof (required for T2+) EVIDENCE_PACK Claims, citations, gaps (required for T3+) SESSION_STATE Current workflow state, fix counts, MMA scores TaskRequest Structured dispatch to specialist skill SESSION_STATE Updated workflow state 6.0 8.0 9.0 3 HALT + ESCALATION_PACKET to human Same dimension fails 2x = immediate PATCH_REQUEST

## L1: Contract

command Slash command or workflow trigger PROJECT_BRIEF Project goal, avatar, offer (required for T2+) MESSAGE_SPINE Promise, mechanism, proof (required for T2+) EVIDENCE_PACK Claims, citations, gaps (required for T3+) SESSION_STATE Current workflow state, fix counts, MMA scores TaskRequest Structured dispatch to specialist skill SESSION_STATE Updated workflow state 6.0 8.0 9.0 3 HALT + ESCALATION_PACKET to human Same dimension fails 2x = immediate PATCH_REQUEST

### Frameworks

**MMAGateContract:** 6.0 8.0 9.0

**CircuitBreaker:** 3 HALT + ESCALATION_PACKET to human Same dimension fails 2x = immediate PATCH_REQUEST

## L2: ExecutionProtocol

Never generate content directly — route to specialized skills Never allow SSOT drift — objects locked after creation, validated via checksum Never exceed 3 FIX loops per dimension — escalate to human Never bloat context — trigger GC at 70% capacity Always track state in SESSION_STATE.json Always require human gate between T1-T2 and T3-T4 transitions Always run SSOT validation before phase transitions (python tools/validate_ssot.py --pre-transition) 2000 (always-loaded L1 only) progressive_disclosure PROJECT_BRIEF (T2+), MESSAGE_SPINE (T2+), EVIDENCE_PACK (T3+) meta_mma (quality gates) orchestration/routing/routing_table.yaml orchestration/routing/aliases.yaml Identify Track Determine which track the command maps to:
          T1 Research: /intake, /scout, /deconstruct, /synthesize, /researchops
          T2 Drafts:   /draft, /advertorial, /salespage, /vsl, /shortvsl, /email, /write
          T3 Production: /produce, /offer, /infoproduct, /ads, /funnel
          T4 Polish:   /polish
          Cross-Track: /validate, /design, /zpwo, /buildskill, /workflow, /mentor Command resolves to known route in routing_table.yaml Verify Prerequisites Check SSOT state for target track:
          T1: No prerequisites (exploration)
          T2: PROJECT_BRIEF + MESSAGE_SPINE must exist and be locked
          T3: All T2 prereqs + EVIDENCE_PACK + MMA M1 score >= 6.0
          T4: All T3 prereqs + MMA M2 score >= 8.0
          Run: python tools/validate_ssot.py --pre-transition {target_track} Pre-transition check returns passed=true Compose Team Build team composition per track:
          T1: Lead (scout/intel) + 1 specialist. Brain: Left
          T2: Lead (copy_lead/director) + 1 specialist. Brain: Right
          T3: Specialist (same as T2) + MMA reviewer. Brain: Both
          T4: HPE lead + Skeptic + NRA. Brain: Right
          Max 3 agents per task. Always include reviewer for T3/T4. Team size is 3 or fewer and includes reviewer where required Dispatch TaskRequest Generate TaskRequest with:
          - task_id: auto-generated
          - instruction: skill-specific prompt
          - track: T1/T2/T3/T4
          - skill_ref: canonical skill_id from aliases.yaml
          - constraints: token_budget, timeout, min_mma_score
          - context_pointers: SSOT checksums (not full content) TaskRequest contains all required fields Process TaskResult Receive TaskResult with:
          - success: bool
          - output: generated artifact
          - tokens_used: actual consumption
          - mma_score: quality score (if applicable)
          - artifacts[]: list of produced files
          - insights[]: self-identified patterns (SIPs)

          Route based on result:
          IF success AND mma_score >= gate: advance track
          IF NOT success OR mma_score below gate: FIX loop
          IF fix_count >= 3: circuit breaker HALT SessionState updated with result 1. Read SESSION_STATE.json (python tools/scripts/session_state.py show)
          2. Check current track and pending tasks
          3. Verify SSOT lock integrity (python tools/validate_ssot.py --check-locks)
          4. Check context usage — if > 70%, trigger /gc first 1. Parse incoming command
          2. Resolve skill via alias_resolver (python tools/alias_resolver.py {command})
          3. Look up route in routing_table.yaml
          4. Check prerequisites for target track
          5. Compose team and generate TaskRequest 1. Track fix_counts per MMA dimension
          2. Enforce circuit breaker (max 3 per dimension)
          3. Update SESSION_STATE after each TaskResult
          4. Log SIPs to insights.md
          5. Trigger human gates at track transitions Read/update workflow state. Commands: show, load_skill, set, gc, reset Progressive disclosure skill loading. Commands: --list, --layer N, --manifest SSOT validation. Commands: --check-locks, --pre-transition {track} Resolve commands/names to canonical skill_ids Validate skill XML structure against SkillML V1.4 Generate SKILLS_MANIFEST.yaml from skill inventory Terminal visual dashboard. Commands: state, neurobox, track, mma Task delegation engine. Commands: status, teams, run, add Parallel dispatch. Commands: dispatch, parallel, chain ZPWO v4.0 = Zero-Point Workflow Orchestrator
ROLE: Conductor, not performer. Route, track, validate — never generate.

CORE DOCTRINE:
1. State > Chat — SESSION_STATE is truth
2. Generate Last — Tools before LLM
3. Two-Brain Teams — Left + Right paired per track
4. Locked SSOT — No drift after creation
5. Light Center — ZPWO routes, edges execute

THE 4 TRACKS:
T1: RESEARCH    — Intelligence gathering (no MMA gate)
T2: DRAFTS      — Fast angle exploration (MMA M1 >= 6.0)
T3: PRODUCTION  — Publishable assets (MMA M2 >= 8.0)
T4: POLISH      — Human Personance + AI Detox (MMA M3 >= 9.0)

HUMAN GATES:
- Between T1 and T2 (SSOT approval)
- Between T3 and T4 (production approval)
- Final ship approval

COMMANDS:
/intake    — T1: Lock SSOT objects
/scout     — T1: Market intelligence
/draft     — T2: Explore angles
/produce   — T3: Build publishable asset
/polish    — T4: Voice + UX finish
/validate  — Cross: MMA quality check
/ship      — Package deliverables
/status    — Show workflow state
/gc        — Garbage collect context
/handoff   — Session summary for handoff

CIRCUIT BREAKER:
- Max 3 FIX loops per MMA dimension
- Same failure 2x — immediate PATCH_REQUEST
- 3x — HALT + ESCALATION_PACKET to human

DECISION TREE:
IF no PROJECT_BRIEF or MESSAGE_SPINE — Run /intake first
IF command maps to T2+ and SSOT missing — Block, require /intake
IF asset_type requested — Resolve via alias_resolver, route to skill
IF MMA fails — Stay in track, trigger FIX loop (check fix_count)
IF fix_count >= 3 — Circuit breaker HALT
IF context > 70% — Auto-trigger /gc
IF track complete + MMA PASS — Human gate, then advance track

TEAM COMPOSITIONS:
T1: Market Scout (lead) + Research Ops. Brain: Left
T2: Copy Lead (lead) + Copy Director + Specialist. Brain: Right
T3: Active Specialist + MMA (reviewer). Brain: Both
T4: HPE (lead) + Skeptic Avatar + NRA. Brain: Right

### Frameworks

**ReasoningFramework:** Identify Track Determine which track the command maps to:
          T1 Research: /intake, /scout, /deconstruct, /synthesize, /researchops
          T2 Drafts:   /draft, /advertorial, /salespage, /vsl, /shortvsl, /email, /write
          T3 Production: /produce, /offer, /infoproduct, /ads, /funnel
          T4 Polish:   /polish
          Cross-Track: /validate, /design, /zpwo, /buildskill, /workflow, /mentor Command resolves to known route in routing_table.yaml Verify Prerequisites Check SSOT state for target track:
          T1: No prerequisites (exploration)
          T2: PROJECT_BRIEF + MESSAGE_SPINE must exist and be locked
          T3: All T2 prereqs + EVIDENCE_PACK + MMA M1 score >= 6.0
          T4: All T3 prereqs + MMA M2 score >= 8.0
          Run: python tools/validate_ssot.py --pre-transition {target_track} Pre-transition check returns passed=true Compose Team Build team composition per track:
          T1: Lead (scout/intel) + 1 specialist. Brain: Left
          T2: Lead (copy_lead/director) + 1 specialist. Brain: Right
          T3: Specialist (same as T2) + MMA reviewer. Brain: Both
          T4: HPE lead + Skeptic + NRA. Brain: Right
          Max 3 agents per task. Always include reviewer for T3/T4. Team size is 3 or fewer and includes reviewer where required Dispatch TaskRequest Generate TaskRequest with:
          - task_id: auto-generated
          - instruction: skill-specific prompt
          - track: T1/T2/T3/T4
          - skill_ref: canonical skill_id from aliases.yaml
          - constraints: token_budget, timeout, min_mma_score
          - context_pointers: SSOT checksums (not full content) TaskRequest contains all required fields Process TaskResult Receive TaskResult with:
          - success: bool
          - output: generated artifact
          - tokens_used: actual consumption
          - mma_score: quality score (if applicable)
          - artifacts[]: list of produced files
          - insights[]: self-identified patterns (SIPs)

          Route based on result:
          IF success AND mma_score >= gate: advance track
          IF NOT success OR mma_score below gate: FIX loop
          IF fix_count >= 3: circuit breaker HALT SessionState updated with result

## L3: (missing)

> _This layer was not present in the source XML. Add content during review._

## L4: (missing)

> _This layer was not present in the source XML. Add content during review._

## Contract

### Required Inputs

- **command** (text) — Slash command or workflow trigger

### Optional Inputs

- **PROJECT_BRIEF** (yaml) — Project goal, avatar, offer (required for T2+)
- **MESSAGE_SPINE** (yaml) — Promise, mechanism, proof (required for T2+)
- **EVIDENCE_PACK** (yaml) — Claims, citations, gaps (required for T3+)
- **SESSION_STATE** (json) — Current workflow state, fix counts, MMA scores

### Primary Outputs

- **TaskRequest** (json) — Structured dispatch to specialist skill
- **SESSION_STATE** (json) — Updated workflow state

### Quality Gates

- **T2:** 6.0
- **T3:** 8.0
- **T4:** 9.0

### Circuit Breakers

- **max_fix_loops:** 3
- **on_exhausted:** HALT + ESCALATION_PACKET to human

## Dependencies

### Upstream

(none extracted)

### Downstream

(none extracted)

## Guardrails

(none extracted)

## Graph Edges

(no edges extracted)

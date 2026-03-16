# PATCH_mma_refactor_to_meta_mma_v4_0_0

- Status: ready_for_claude
- Source: `.agents/skills/meta/mma_master_monitor_agent_v1_0_0.xml`
- Proposed replacement: `.agents/skills/meta/meta_mma_v4_0_0.xml`
- Patch type: refactor
- Apply now: no

## Intent
Refactor the legacy MMA monitor into a leaner V4 quality-gate skill with explicit contract, self-check, circuit-breaker logic, and patch-trigger output behavior.

## Required Changes
- Normalize `skill_id` to `meta_mma`
- Reduce monolithic instruction sprawl into explicit SkillML V1.4 sections
- Preserve MMA gate behavior while making failure loops and escalation rules explicit
- Align role with cross-track validation and patch emission
- Remove stale architecture assumptions not aligned to current 4-track flow

## Companion Inputs
- `.agents/skills/meta/META_FAMILY_AUDIT_V4_2026-03-07.md`
- `.agents/skills/meta/META_PATCH_PACK_V4.md`
- `.agents/skills/meta/patches/NOTEBOOKLM_META_PROMPT_FRAMEWORK_V4.md`

---

## Patch Applied Summary
- Applied: 2026-03-07
- Applied by: Claude (agent)
- Validator result: 19/19 passed
- Status: ready_for_claude → **applied**

### What Changed
1. **Normalized skill_id** to `meta_mma` (was `skill.validation.mma_master_monitor_agent.v1_0_0`)
2. **Restructured from L1-L4 layers to V1.4 sections** — legacy 4-layer progressive disclosure replaced with canonical 5-section structure (Meta, Contract, ExecutionProtocol, SelfCheck, PatchLog) + 4 layer tags
3. **Preserved 7D scoring system** — all 7 dimensions with canonical weights (D1=0.15, D2=0.20, D3=0.15, D4=0.15, D5=0.10, D6=0.15, D7=0.10) and thresholds in SevenDimensions element
4. **Preserved 6 review modes** — M1 Quick Score, M2 Deep Audit, M3 Multi-Asset, M4 Compliance Gate, M5 Comparative, plus new Migration Gate mode
5. **Added dual-mandate design** — copy quality gate (7D + 7S) AND meta-family migration gate (V1.4 compliance)
6. **Added explicit Contract** with InputsRequired (target_artifact, review_mode), InputsOptional (ssot_context, session_state, patch_pack, relational_map), OutputsPrimary (audit_scorecard, patch_trigger), OutputsSecondary (fix_plan, drift_report, compliance_result)
7. **Added MMAGateContract** with tiered track thresholds (T2>=6.0, T3>=8.0, T4>=9.0) plus meta_migration gate (19/19 + 80% lint)
8. **Added CircuitBreaker** with escalation ladder — max 3 fix loops, same issue 2x = PATCH_REQUEST to architect, 3x = HALT + human
9. **Added relational contracts** from meta_relational_operations_v4.yaml (upstream: zpwo/auditor, downstream: builder/architect, patch_owner: builder, review_owner: self)
10. **Added 7 Rules** aligned to META_PATCH_PACK_V4 heuristics (H5 Discovery Gate, FM1 Pipeline Drift, FM2 Role Bleed, FM5 Implicit Patch Ownership) plus score inflation guard and tool-first principle
11. **Added 5-step ReasoningFramework** with validation gates per step (Classify → Select Mode → Score → Evaluate Coverage → Emit Verdict)
12. **Added 3 workflow phases** (copy_review, skill_migration_gate, family_audit_review)
13. **Preserved routing decision tree** — 9 routes covering both copy routing (D1-D7 failures) and migration routing (V1.4 structural, role boundary)
14. **Preserved hard gates** — 3 gate categories (constitutional, proof, platform) for M4 compliance mode
15. **Added 5 SelfCheck elements** — verdict completeness, patch ownership, pipeline drift detection, score inflation guard, fix specificity
16. **Added 5 FailureModes** — score inflation, score deflation, routing confusion, vague fix instructions, pipeline contradiction
17. **Added 5 tool references** (skillml_validator, lint_skill, calculate_weighted_score, check_verdict, detect_ai_isms)
18. **Added QuickReference** CDATA block with copy review flow, skill migration flow, and key reference tables

### What Was Preserved
- 7D scoring dimensions with weights, thresholds, and priority levels
- 5 operating modes (M1-M5)
- 7S/7F chain coverage requirements (referenced, detailed audit logic available in legacy)
- Routing decision tree logic (copy routing by dimension failure)
- Hard gate definitions (constitutional, proof, platform)
- Verdict logic (PASS/FIX/ESCALATE)
- Core identity: "The Quality Guardian" — score accurately, decide fairly, route intelligently

### What Was Removed (Doctrine to Reference)
- Inline Python tools (code blocks) — replaced with tool references; Python code preserved in legacy file for re-implementation
- Golden runs (GR1-GR5) — preserved in legacy file for testing calibration
- Detailed 7S/7F dimension requirement breakdowns — referenced; full detail in legacy
- Self-calibration loop specifications — deferred to operational reference doc
- Output schema templates (scorecard, full report, drift report, compliance result) — moved to operational use; legacy file is reference

### Unresolved
- None. All required changes from patch file applied.

### Second Patch Needed
- No. File is V1.4 compliant (19/19) and aligned to canonical doctrine.
- **Optional enhancement**: Re-add golden runs as a companion test fixture file if calibration testing is needed.

# PATCH_skill_builder_refactor_to_meta_skill_builder_v4_0_0

- Status: ready_for_claude
- Source: `.agents/skills/meta/skill_builder_v1.2.0.xml`
- Proposed replacement: `.agents/skills/meta/meta_skill_builder_v4_0_0.xml`
- Patch type: refactor
- Apply now: no

## Intent
Convert the legacy skill builder into a canonical V4 builder role that consumes audit findings, NotebookLM patch packs, and template contracts to build or upgrade executable skills.

## Required Changes
- Normalize `skill_id` to `meta_skill_builder`
- Replace outdated pipeline references with atomic v2 doctrine
- Make inputs, outputs, and handoff expectations explicit
- Separate build logic from reference doctrine
- Attach relational ownership to architect, auditor, and template-system roles

## Companion Inputs
- `.agents/skills/meta/META_PATCH_PACK_V4.md`
- `.agents/skills/meta/meta_relational_operations_v4.yaml`
- `.agents/skills/meta/patches/NOTEBOOKLM_META_PROMPT_FRAMEWORK_V4.md`

---

## Patch Applied Summary
- Applied: 2026-03-07
- Applied by: Claude (agent)
- Validator result: 19/19 passed
- Status: ready_for_claude → **applied**

### What Changed
1. **Normalized skill_id** to `meta_skill_builder` (was `skill.meta.skill_builder.v1_2_0`)
2. **Replaced pipeline references** — all Prism-era synthesis language replaced with Atomic Pipeline v2.1 (Atoms → NotebookLM Router → Claude Synthesizer → SkillML V1.4 XML)
3. **Added atom-to-section mapping** in Step 2 of ReasoningFramework (framework→Meta, spec→Contract, heuristic→Rules, workflow→Reasoning, pattern→Impl, checklist→SelfCheck, failure→FailureModes)
4. **Added explicit Contract** with InputsRequired (skill_brief, architecture_spec), InputsOptional (patch_pack, clustered_atoms, template_bundle, legacy_asset, relational_map), OutputsPrimary (v4_skill_asset), OutputsSecondary (alias_update, validation_report, patch_applied_summary)
5. **Added MMAGateContract** with tiered track thresholds (T2>=6.0, T3>=8.0, T4>=9.0)
6. **Added CircuitBreaker** — max 3 fix loops, escalate to meta_skill_architect on exhaustion
7. **Added relational contracts** from meta_relational_operations_v4.yaml (upstream: architect/auditor/template, downstream: mma/manifest, patch_owner: self, review_owner: meta_mma)
8. **Added 7 Rules** referencing META_PATCH_PACK_V4 heuristics (H1-H5, R5 doctrine separation, R7 benchmark)
9. **Added 5-step ReasoningFramework** with validation gates per step
10. **Added 3 workflow phases** (new_build, patch_upgrade, batch_migration)
11. **Added 5 SelfCheck elements** (V1.4 compliance, relational contracts, pipeline alignment, discovery metadata, doctrine separation)
12. **Added 4 FailureModes** (legacy_copy_forward, template_mismatch, discovery_collapse, pipeline_drift)
13. **Added 4 tool references** (skillml_validator, lint_skill, alias_resolver, manifest_builder)
14. **Added QuickReference** CDATA block with single-skill and batch-migration flows

### What Was Preserved
- Build logic concepts (token budgets, dependency ordering, upstream-first processing)
- Python tool scaffolding pattern (now explicit tool references)
- Handoff artifact concepts (now formalized as OutputsSecondary)

### Unresolved
- None. All required changes from patch file applied.

### Second Patch Needed
- No. File is V1.4 compliant (19/19) and aligned to canonical doctrine.

# Claude MAA Rebuild Handoff V4

Date: 2026-03-09
Status: ready_for_execution
Primary target: build a new canonical MAA artifact from the ground up.

## Goal
Create the new `Master Automations Architect` as a present-track automation doctrine and control skill.

Do not polish the old module in place.
Do not preserve old module boundaries just because they existed.
Use modules 1-3 as seeds.
Use modules 4-5 only if needed and only as supporting pattern sources.

## Expected Primary Output
Create a new canonical working artifact in `.agents/skills/automations/`:
- `automations_master_architect_v4_0_0.xml`

## Optional Companion Outputs
Create only if needed to keep the XML skill lean:
- `AUTOMATION_CONTRACTS_V4.md`
- `FLOWGRAM_VISUAL_CONTRACT_V4.md`
- `MAA_RELATIONAL_OPS_V4.yaml`

## Required Design Shifts
- shift from flat modules to relational agentics
- make memory seams explicit without fixing the final backend
- make Flowgrams Excalidraw-first, Mermaid-terminal-second, Draw.io-secondary
- define a future insertion point for the Skill Evaluator
- keep the skill harness-agnostic enough to survive OpenClaw vs NanoClaw uncertainty
- keep execution topology explicit: deterministic scripts first, constrained tools second, autonomous browser escalation last

## Required Outputs From The New Skill
The new MAA should at minimum be able to emit or define:
- `AUTOMATION_REQUEST`
- `AUTOMATION_BLUEPRINT`
- `FLOWGRAM_SPEC`
- `HANDOFF_PACKAGE`
- `PATCH_REQUEST`
- `MEMORY_SEAM_NOTE`

## Required Relational Links
The new MAA should declare its relations to at least:
- `automations_builder`
- `automations_workflow_translator`
- future `automations_browser_orchestrator`
- future `meta_skill_evaluator`
- `meta_skill_builder`
- `meta_mma`
- future memory model layer

## Read Order
1. `AUTOMATIONS_FAMILY_TRIAGE_V4_2026-03-08.md`
2. `MASTER_AUTOMATIONS_ARCHITECT_REBUILD_BRIEF_V4.md`
3. `MAA_SOURCE_PRIORITY_V4.md`
4. `patches/PATCH_master_automations_architect_ground_up_rebuild_v2_1_0.md`
5. `STRATEGIC_UPDATE_2026-03-08.md`
6. `MODULE-ONE-MASTER-AUTOMATIONS-ARCHITECT-V1.1.0-COMPLETE (2).md`
7. `MODULE-TWO-AUTOMATION-BUILDER-V1.0.0-COMPLETE (2).md`
8. `MODULE_3_WORKFLOW_TRANSLATOR_v1_1_0.xml`
9. optional: `MODULE_4_LEAD_GEN_PLANNING.md`
10. optional: `M5_IMPLEMENTATION_APPENDIX.md`

## Constraints
- Keep current ULTRAMIND present-track decisions authoritative.
- Do not reintroduce `SKILL.md` as the primary skill artifact.
- Do not reintroduce old 3-phase orchestration language where it conflicts with the 4-track model.
- Do not make COSMS a runtime requirement inside MAA.
- Do not make the final harness decision inside the MAA skill.

## Definition Of Done
- New XML skill exists and is structurally coherent.
- Contracts are explicit.
- Relational ops are explicit.
- Visual drawing direction is explicit.
- Memory seam notes are explicit.
- Tool topology heuristics are explicit.
- The artifact is clearly better aligned to present track than the old M1-M3 set.

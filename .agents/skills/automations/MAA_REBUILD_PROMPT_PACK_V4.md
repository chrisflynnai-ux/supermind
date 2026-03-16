# MAA Rebuild Prompt Pack V4

Use this with Claude Code Desktop when starting the rebuild.

## Prompt 1: Ground-Up Rebuild
```text
Work in the ULTRAMIND workspace only.
Use `.agents/skills/automations/` as the working surface.
Do not modify `.claude/skills/`.

Task:
Build a new canonical Master Automations Architect from the ground up.
Use existing Modules 1-3 as seed references only.
If useful, pull in Module 4 and Module 5 patterns later, but do not block the rebuild on finding them.

Read in this order:
1. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\AUTOMATIONS_FAMILY_TRIAGE_V4_2026-03-08.md
2. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\MASTER_AUTOMATIONS_ARCHITECT_REBUILD_BRIEF_V4.md
3. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\MAA_SOURCE_PRIORITY_V4.md
4. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\CLAUDE_MAA_REBUILD_HANDOFF_V4.md
5. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\patches\PATCH_master_automations_architect_ground_up_rebuild_v2_1_0.md
6. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\STRATEGIC_UPDATE_2026-03-08.md
7. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\MODULE-ONE-MASTER-AUTOMATIONS-ARCHITECT-V1.1.0-COMPLETE (2).md
8. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\MODULE-TWO-AUTOMATION-BUILDER-V1.0.0-COMPLETE (2).md
9. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\MODULE_3_WORKFLOW_TRANSLATOR_v1_1_0.xml

Optional references if needed after the skeleton is defined:
- C:\Users\cfar7\OneDrive\Desktop\FULL AGENTIC SYSTMS REVIEW FILES\MMA ARCHIVES RECOVERED\MAA Module FOUR\MODULE_4_LEAD_GEN_PLANNING.md
- C:\Users\cfar7\OneDrive\Desktop\FULL AGENTIC SYSTMS REVIEW FILES\MMA ARCHIVES RECOVERED\MAA Module FIVE\M5_IMPLEMENTATION_APPENDIX.md

Required output:
Create a new canonical XML skill at:
C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\automations_master_architect_v4_0_0.xml

Required design outcomes:
- make relational agentics explicit
- define memory seams without fixing the final memory backend
- define Flowgrams as Excalidraw-first, Mermaid-terminal-second, Draw.io-secondary
- include a future Skill Evaluator insertion point
- keep the skill harness-agnostic enough to survive OpenClaw vs NanoClaw uncertainty
- preserve the best doctrine from Modules 1-3 without preserving their old packaging blindly
- use SkillML V1.4 logic, not legacy SKILL.md-first logic

Required contracts inside or beside the skill:
- AUTOMATION_REQUEST
- AUTOMATION_BLUEPRINT
- FLOWGRAM_SPEC
- HANDOFF_PACKAGE
- PATCH_REQUEST
- MEMORY_SEAM_NOTE

Required relational links:
- delegates_to: builder, workflow translator, future browser orchestrator, future interface/visual layer
- depends_on: routing rules, memory model, NotebookLM enhancements, future evaluator
- complements: meta_skill_builder, meta_mma

After building, report:
1. what was preserved from Modules 1-3
2. what was intentionally discarded
3. whether Module 4 or 5 should still be mined for a second pass
4. whether a companion relational-ops or visual-contract file is needed
```

## Prompt 2: NotebookLM Enhancement Pass
Use this after the first XML draft exists.

```text
Run a second-pass enhancement on the new MAA draft using NotebookLM-informed improvements.

Read:
1. C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND\.agents\skills\automations\NOTEBOOKLM_MAA_ENHANCEMENT_QUERY_PACK_V4.md
2. the new `automations_master_architect_v4_0_0.xml`
3. any newly available Module 4 / Module 5 references

Goal:
- identify missing heuristics
- identify missing anti-patterns
- identify weak relational operations
- identify visual workflow gaps
- identify memory seam gaps
- propose or apply a second-pass upgrade without bloating the skill unnecessarily
```

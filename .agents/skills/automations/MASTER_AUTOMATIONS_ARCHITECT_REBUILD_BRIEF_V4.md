# Master Automations Architect Rebuild Brief V4

Date: 2026-03-08
Status: ready_for_tomorrow
Primary target: reinvent `Master Automations Architect` under the updated strategic sequence.

## Why Rebuild Instead Of Patch-Light
The current Module 1 and Module 2 assets are strong seeds but were written before:
- relational agentics became explicit
- Skill Evaluator was introduced
- Flowgrams tool priority changed to Excalidraw-first
- the revised order of operations put memory model before full harness build
- COSMS front-end became a later-wave portal concern instead of an immediate runtime dependency

## Tomorrow's Build Order
1. Re-state MAA role and boundaries
2. Define memory seams and non-goals
3. Define relational ops between MAA, builder, evaluator, translator, and future harness
4. Define Flowgrams output contract
5. Define NotebookLM enhancement path for modules 2-8
6. Define patch/review loop
7. Produce the new canonical MAA artifact

## Core Role Of MAA V2
MAA is the doctrine and blueprint layer for automations.
It should:
- classify automation requests
- choose architecture patterns
- choose tools and execution tier
- detect anti-patterns early
- define handoffs to downstream modules
- emit blueprint and patch hooks
- stay aware of memory-model requirements without owning memory implementation

It should not:
- execute all automations itself
- hardcode final database choices
- become the entire harness
- collapse into a giant generic prompt

## New Required Contracts
- `AUTOMATION_REQUEST`
- `AUTOMATION_BLUEPRINT`
- `HANDOFF_PACKAGE`
- `FLOWGRAM_SPEC`
- `PATCH_REQUEST`
- `MEMORY_SEAM_NOTE`

## New Relational Graph
MAA should know its:
- dependencies
- delegates
- complements
- evaluation partners
- memory touchpoints

Minimum relation set:
- `delegates_to`: builder, workflow translator, browser automation, interface generator
- `depends_on`: memory model, routing rules, skill evaluator, NotebookLM enhancement inputs
- `complements`: meta_skill_builder, meta_mma, systems workflow skills

## Design Constraints
- Excalidraw is primary Flowgram output target
- Mermaid is acceptable for terminal-native diagrams
- Draw.io is secondary
- memory model is next-phase dependency, not solved inside MAA
- harness selection is later; MAA must remain harness-agnostic enough to survive OpenClaw/NanoClaw choice

## Immediate Deliverable For Tomorrow
A new MAA patch or replacement artifact that:
- preserves the strongest doctrine from Module 1 v1.1.0
- removes outdated module-era assumptions
- adds relational agentics
- adds future Skill Evaluator insertion point
- adds memory seam notes
- aligns to the revised build sequence from `STRATEGIC_UPDATE_2026-03-08.md`

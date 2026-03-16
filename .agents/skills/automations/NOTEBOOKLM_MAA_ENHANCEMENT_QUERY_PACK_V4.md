# NotebookLM MAA Enhancement Query Pack V4

Date: 2026-03-09
Use this after the first ground-up MAA draft exists, or earlier if you need targeted synthesis support.

## Purpose
Generate enhancement inputs for the new `Master Automations Architect` without letting NotebookLM redefine the present-track architecture.

NotebookLM should help with:
- missing heuristics
- missing anti-patterns
- better visual workflow modeling
- better translator and builder handoffs
- stronger repair loop design
- stronger evaluator insertion logic

NotebookLM should not decide:
- final harness choice
- final memory backend
- whether SkillML V1.4 is optional
- whether Excalidraw remains primary for Flowgrams

## Query Cluster A: Automation Doctrine
Prompt:
```text
Analyze the attached automation doctrine, workflow conversion, and lean-context references.
Return only the strongest additions for a modern automation doctrine skill.
Focus on:
1. tool topology heuristics
2. anti-patterns in browser-heavy or MCP-heavy automation stacks
3. when to escalate from deterministic scripts to constrained browser tools to autonomous runners
4. patterns that keep context lean while preserving observability
5. patterns for repair loops and self-improvement

Format output as:
- New heuristics
- New anti-patterns
- Missing decision rules
- Conflicts with current doctrine
```

## Query Cluster B: Relational Agentics
Prompt:
```text
Given a Master Automations Architect that must operate inside a relational skill graph, identify the strongest relation patterns.
Focus on:
1. depends_on relations
2. delegates_to relations
3. complements relations
4. review and patch ownership
5. evaluator insertion points

Output only patterns that improve a real skill network, not abstract theory.
```

## Query Cluster C: Visual Workflow System
Prompt:
```text
Analyze references related to workflow visualization, flow diagrams, Excalidraw, Mermaid, and visual-to-code systems.
We need a Flowgram standard where:
- Excalidraw is primary
- Mermaid is terminal-native
- Draw.io is secondary

Return:
1. best practices for human-friendly but machine-usable workflow diagrams
2. minimal metadata needed for a flowgram card/node model
3. how to keep visual diagrams synchronized with automation blueprints
4. anti-patterns that create visual debt
```

## Query Cluster D: Memory Seams
Prompt:
```text
We are not building the final memory backend yet.
Identify what a doctrine-level automation architect should declare now so it stays compatible with a future hybrid memory model.
Focus on:
1. what to record per automation blueprint
2. what to store as reusable pattern memory
3. what belongs in hot session state vs longer-term memory
4. what should remain backend-agnostic for now
```

## Query Cluster E: Builder / Translator / Evaluator Loop
Prompt:
```text
We need a clean handoff loop between:
- automation architect
- automation builder
- workflow translator
- future skill evaluator
- MMA / validator layer

Return the strongest patterns for:
1. build handoff contracts
2. translation handoff contracts
3. validation and repair triggers
4. evaluator-generated patch proposals
5. minimal artifacts that prevent rework
```

## Normalized Output Format
Convert NotebookLM findings into a local patch pack with these sections:
- New Heuristics
- New Anti-Patterns
- Missing Contracts
- Missing Relational Links
- Missing Visual Specifications
- Missing Memory Seams
- Proposed Patch Actions
- Confidence / Uncertainty Notes

## Merge Rule
NotebookLM output is seed material.
Only promote findings that improve the present-track architecture.
Reject anything that reintroduces:
- SKILL.md-first output standards
- flat non-relational skill libraries
- visual-first automation debt
- premature backend lock-in
- harness-specific coupling inside the doctrine layer

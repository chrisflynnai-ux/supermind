# Harness Systems Notebook A

## Scope

- `AA` Claude-Based Harness Architecture
- `CC` Lean Team Orchestration, Clock, and Named Personas
- `AA + CC` combined synthesis across the two notebook runs

## Source Note

This notebook-ready file was split from the reduced master compendium. It keeps the cleaned structure, removes the repeated variants already collapsed in the master, and preserves the intended query-cluster lineage.

### AA. Claude-Based Harness Architecture

#### Core model

- Claude is the harness or kernel layer.
- Marcus is the orchestrator or project manager layer.
- Specialists execute focused work inside strict boundaries.
- Observers and reflectors operate out-of-band so the main context stays lean.

#### Canonical decision

- The harness owns infrastructure, context enforcement, hooks, security interception, session continuity, task-board synchronization, and summary reintegration.
- Marcus owns business logic, team assembly, track progression, retry strategy, delegation intent, and quality-loop decisions.
- Specialists should be invoked statelessly or semi-statelessly through typed contracts rather than inheriting raw chat history.

#### Required execution pattern

- Use typed session boot packages, not raw transcript dumps.
- Use isolated specialist execution for heavy work.
- Return summaries and file pointers to the main loop, not raw tool noise.
- Keep phase transitions explicit and machine-readable.

#### Variant note

- Some source sections preferred `MEMORY.md` as the live surface of truth.
- Stronger recurring pattern: `MEMORY.md` is a projection layer; the durable record belongs in the deeper memory system and checkpoint artifacts.

### CC. Lean Team Orchestration, Clock, and Named Personas

#### Core model

- Default team size is `1-3 specialists + Marcus`.
- Lyra, Reed, Felix, and Orion often operate as supporting system roles rather than always-on foreground personas.
- Track movement remains the main organizational spine.

#### Canonical persona roles

- `Marcus` = orchestrator, routing, delegation, retry ownership
- `Diana` = deep research and evidence synthesis
- `Leo` = writing and generative drafting
- `Felix` = quality, MMA, gate enforcement
- `Lyra` = observer, compression, memory filtering
- `Reed` = reflection, learning, refinement
- `Orion` = model and capability router
- Dash = tool registry and CLI conversion layer
- Nova = repair, mutation, isolated correction, and patch proposal

#### Clock and transition rule

- Marcus can decide that a track is ready to advance.
- The harness performs the actual state transition and updates session records.
- Phase change should happen through a typed event or command, not through informal conversational drift.

#### Canonical team behavior

- Build the smallest viable active team for the track.
- Keep inactive personas unloaded.
- Promote sibling coordination only when the output genuinely benefits from multiple viewpoints.
- Use strict handoff packages across track boundaries.

## AA + CC Combined Run Synthesis

### Notebook 1

#### Part 1. Harness kernel and named team model

- Claude harness acts as the operating kernel.
- Marcus remains the central team router.
- Named personas are treated as bounded specialist roles, not free-form alter egos.
- Lean teams outperform bloated always-on rosters.

#### Part 2. Session boot and handoff structure

- Team sessions should start from a typed boot package.
- Handoff packages should include track, constraints, active roster, and source pointers.
- Raw previous conversation history should not be the default boot source.

#### Part 3. Clock and track transitions

- Phase transitions must be explicit and tied to quality gates.
- Marcus may declare readiness, but the harness writes the transition into system state.
- Track boundaries are part of system control, not just team convention.

#### Part 4. Delegation, reintegration, and PR-gated return

- Heavy specialists run in isolation.
- Reintegration returns summaries, pointers, and validated artifacts.
- PR-gate or equivalent review patterns prevent raw dump-backs into the shared context.

### Notebook 2

#### Part 1. Persona loading and lean team assembly

- Persona loads should be minimal by default.
- Load only the slices required for the current track.
- Large persona files belong in storage, not in the active session prefix.

#### Part 2. Progressive disclosure by track

- Research pulls deep reference.
- Drafting loads writing rules and recent evidence.
- Production uses focused execution context.
- Polish loads QA and refinement layers without reopening everything.

#### Part 3. Authority, escalation, and fix loops

- Harness stops infrastructure failures.
- Marcus handles semantic or workflow failures.
- Three failed loops trigger patch or human escalation.

#### Part 4. Failure, checkpointing, and resume

- Pre-compaction flushes are required before hard stops or dangerous boundaries.
- Resume should begin from the last clean checkpoint and condensed digest.
- Partial artifacts stay quarantined until revalidated.

## Short Canonical Summary

SUPERMIND should use a lean, typed, multi-model harness where Claude acts as the kernel, Marcus acts as the orchestrator, specialists execute inside strict contracts, ACP handles coordination, CLI handles execution, observers compress context, deeper memory stores durable traces, and routing stays rules-based until enough high-quality telemetry exists to justify learned optimization.

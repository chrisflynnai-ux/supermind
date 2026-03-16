# Harness Systems Master Knowledge Compendium (Reduced)

## Purpose

This document consolidates the NotebookLM harness and systems query outputs into one reduced master compendium. It removes repeated explanations, keeps the strongest recurring decisions, and preserves the intended source order so the material can be re-used cleanly in NotebookLM, planning docs, or future skill rebuilds.

## Source Order and Reconstruction Notes

- Primary source order from the query pack:
  - `AA` = Query Cluster A: Claude-Based Harness Architecture
  - `BB` = Query Cluster B: ACP and Internal Routing
  - `CC` = Query Cluster C: Lean Team Orchestration, Clock Mechanism, Named Personas
  - `DD` = Query Cluster D: Cognitive Bandwidth, Context Management, Memory Integration
  - `EE` = Query Cluster E: Multi-Model Routing, CLI Integration, Self-Improvement
- The original query-pack pairing emphasized `A+C`, `B+D`, then `E`.
- The actual run history later introduced overlapping combined notebook passes, especially `A+C` and `B+C`.
- This reduced compendium keeps the requested final reporting order:
  - `AA -> BB -> CC -> DD -> EE`
  - then `A+C` in four parts across two notebooks
  - then `B+C` in four parts across two notebooks
- Where `B+D` and `E` findings were repeated inside later combined runs, they were folded back into the canonical `BB`, `DD`, and `EE` sections instead of duplicated again.

## Redundancy Rules Used

- Repeated variants were merged into one canonical decision.
- Contradictions were resolved by keeping the direction that appears most operationally consistent with the current SUPERMIND track.
- Repeated tables were collapsed into compact narrative rules unless the structure itself mattered.
- Where the compendium offered two viable approaches, this document keeps:
  - one `Canonical Decision`
  - one short `Variant Note` only if the tradeoff is still important

## Canonical Master Knowledge

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

### BB. ACP and Internal Routing

#### Core model

- Inter-agent communication uses a typed Agent Communication Protocol.
- Tool and service execution uses a CLI-first pattern where possible.
- Message passing should be pointer-push and context-pull.

#### Canonical decision

- Use a typed ACP envelope for agent-to-agent coordination.
- Use CLI-first execution for external tools, integrations, and automation actions.
- Never pass raw bulk payloads inside ACP messages when a pointer and digest will do.

#### Minimum ACP envelope

- `message_id`
- `parent_message_id`
- `sender_persona`
- `receiver_persona`
- `message_type`
- `track_id`
- `disclosure_level`
- `context_budget`
- `threadex_thread_ref`
- `action_summary`
- `trajectory_semantics`
- `metadata`

#### Routing rules

- Use deterministic routing tables now.
- Route by task shape, capability requirement, context depth, and tool profile.
- Reserve learned or RL routing for later, after telemetry and gold traces exist.

#### Hybrid architecture rule

- Vertical execution: CLI-first
- Horizontal coordination: typed ACP
- Message bodies stay lean; raw artifacts stay in storage or isolated workspaces.

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

### DD. Cognitive Bandwidth, Context Management, and Memory Integration

#### Core model

- Context is treated as active RAM, not as a storage bin.
- Progressive disclosure is mandatory.
- Memory should be split by function, not duplicated everywhere.

#### Canonical disclosure levels

- `L1` = routing, identity, task classification
- `L2` = planning, structure, execution rules
- `L3` = active execution context and refined working state
- `L4` = deep reference, large corpora, full source material

#### Canonical budget principles

- Keep the orchestrator broad and shallow.
- Give specialists deep budgets only when their task truly requires it.
- Compress before injecting.
- Page out before collapse.

#### Hard rules

- Soft warning near 70 percent context saturation
- Hard flush near 85 percent saturation
- Heavy payloads trigger quarantine and summarization
- Raw tool output should be compressed before re-entry

#### Memory authority split

- Harness state: active session projection, current task status, immediate rules
- Deeper memory system: factual history, execution traces, observations, checkpoints, learned patterns
- No field duplication unless there is an explicit projection reason

#### Canonical cache decision

- Stateless fresh-load across project boundaries
- Controlled warm continuity only within the same active project or track when it improves speed without contaminating context

### EE. Multi-Model Routing, CLI Integration, and Self-Improvement

#### Core model

- Claude handles orchestration, ambiguous planning, and high-stakes synthesis.
- Codex handles execution-heavy coding, terminal work, repo surgery, and technical validation.
- Gemini handles multimodal work, long-context analysis, visual reasoning, and large research payloads.

#### Canonical model fleet responsibilities

- Claude is the default orchestration brain when the task is strategic, under-specified, or cross-domain.
- Codex is the default execution specialist when the task is implementation-heavy, test-heavy, or terminal-centric.
- Gemini is the default specialist when the task is visual, multimodal, or requires holding very large context volumes without aggressive chunking.

#### Orion task-shape taxonomy

- `ORCHESTRATION_STRATEGY` -> Claude
- `MULTI_FILE_REFACTOR` -> Codex
- `BACKEND_BUILD_OR_REPAIR` -> Codex
- `LONG_CONTEXT_SYNTHESIS` -> Gemini
- `MULTIMODAL_DESIGN_OR_VIDEO` -> Gemini
- `RESEARCH_TO_PLAN_SYNTHESIS` -> Claude or Gemini depending on context volume
- `QUALITY_REVIEW_OR_GATE_SUPPORT` -> Claude or Codex under Felix-controlled rubric

#### Canonical routing rule

- Use model specialization by task shape, not by habit.
- Lift context budgets only when the task truly needs global relational mapping.
- Route against task shape, context volume, tool profile, and deliverable type.
- Keep fallback chains quality-gated and never silent.

#### Fallback chain specification

- Retry with the same `TaskRequest`, same Definition of Done, and same score threshold.
- Preserve the same output contract even when changing models.
- Run blind evaluation after fallback so quality degradation is measurable.
- If the fallback path still fails the threshold after the allowed loops, halt and escalate rather than quietly accepting slop.

#### Dash tool doctrine

- Prefer scripts and CLIs over heavy schema-injection patterns.
- Use registry lookup and progressive disclosure for tool loading.
- Convert useful services into lean agent-native commands rather than carrying giant MCP payloads into the prompt.
- Treat `CLI-Anything` style conversion as the preferred path for wrapping useful software into agent-usable interfaces.
- Treat `MCP2CLI` style adapters as the bridge for turning bulky tool definitions into lightweight runtime commands.

#### Dash registry minimum fields

- `tool_id`
- `capability_tags`
- `auth_profile`
- `command_template`
- `output_parser`
- `safety_class`
- `fallback_behavior`

#### Self-improvement loop

- Reed identifies weak skills, routing failures, or repeated rework patterns and generates improvement hypotheses.
- Nova mutates in isolation, proposes repairs, and prepares patch candidates rather than editing the live environment directly.
- Felix grades against explicit assertions and score thresholds.
- Keep only the mutation paths that improve outcome quality.
- The loop should output a patch proposal, benchmark result, or promotion decision, not a silent production change.

#### Marketplace and external skill rule

- Community or third-party skills are untrusted by default.
- Quarantine, blind evaluation, static checks, and human promotion gates are required before production use.
- Open marketplace ingestion should be treated as a supply-chain risk, not as free capability.

## Canonical Operating Decisions Extracted from Repeated Sections

### 1. Harness vs Marcus authority boundary

- Harness owns context, memory enforcement, tool interception, infra recovery, and final state sync.
- Marcus owns delegation logic, track management, retries, and business-level decisions.

### 2. Pointer-push, context-pull

- Agents pass compact summaries plus references.
- Downstream agents retrieve only the slices they actually need.

### 3. CLI-first plus typed-bus hybrid

- CLI for execution
- ACP for coordination

### 4. Observer and reflector pattern

- Lyra compresses.
- Reed restructures and learns.
- Felix evaluates.

### 5. Track transitions are explicit system events

- No silent advancement by conversational implication.
- Handoffs and transitions should emit typed artifacts or commands.

### 6. Recovery defaults to resume, not restart

- Resume from checkpoints whenever possible.
- Full restarts are reserved for corrupted inputs, SSOT drift, or invalid upstream artifacts.

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

## BB + CC Combined Run Synthesis

### Notebook 1

#### Part 1. ACP envelope and typed coordination

- Every inter-agent message needs explicit sender, receiver, type, track, budget, and reference metadata.
- Message types should map to real seams like task assignment, result, quality check, phase transition, and patch proposal.

#### Part 2. Per-persona budget logic

- Budget is role-shaped, not equal across agents.
- Orchestrators stay broad and lean.
- Researchers and multimodal agents get larger working windows.
- Quality agents stay strict and narrow.

#### Part 3. Progressive disclosure assignment

- Default disclosure should be conservative.
- Escalation to deeper context should require either need or explicit authorization.
- Deep reference without necessity is a form of context waste.

#### Part 4. CLI vs typed message bus

- Use CLI invocation for tools and external actions.
- Use ACP for coordination and stateful collaboration.
- The two patterns solve different problems and should not be collapsed into one transport.

### Notebook 2

#### Part 1. Handoff provenance and chain control

- Multi-hop chains must preserve lineage without carrying the full prior payload.
- Track hop count, prior actors, summary, and negative-space guidance.
- Compaction becomes mandatory as handoff depth grows.

#### Part 2. Observer stream and anomaly logging

- Observers should quietly monitor routing anomalies, budget stress, failed handoffs, and disclosure abuse.
- Their outputs feed future routing and repair intelligence.

#### Part 3. Clock-to-harness synchronization and drift repair

- Team state and harness state can drift if not synchronized by deterministic events.
- Reconciliation should prefer the strongest checkpointed source of truth, then rewrite the weaker projection.

#### Part 4. Session recovery and visual oversight

- Recovery should use checkpoints, hashes, and condensed digests.
- Human-facing mission control can visualize nodes, edges, alerts, and context pressure without becoming the actual runtime memory layer.

## BB + DD Analytical Cross-Synthesis

This section is an added synthesis layer to close the main gap in the reduced notebook set. It merges ACP and context-management decisions into one operating view.

### Part 1. ACP as a context governor

- ACP is not just a transport envelope; it is the first budget-control mechanism.
- `context_budget` and `disclosure_level` should determine whether a message can enter the receiver's active window unchanged.
- Message design and context hygiene are the same problem at different layers.

### Part 2. Hook enforcement and quarantine flow

- A Pre-Message or PreTool hook should inspect both the payload size and the receiver's remaining budget.
- Oversized messages should be quarantined, compressed, and retried as summaries plus pointers.
- Hard delivery should be blocked when compression still violates the receiver's safe operating envelope.

### Part 3. Provenance plus memory authority

- ACP should carry lineage while deeper memory retains the raw artifacts.
- Harness state should hold active operational projections only.
- Durable facts, traces, and observation logs should live in deeper memory and be pulled on demand.

### Part 4. Recovery and track-safe reintegration

- Recovery should restore a clean digest, not the full noisy failure trace.
- Handoffs back into the main loop should always be compressed, typed, and checkpoint-aware.
- BB and DD together imply that context recovery is a protocol feature, not an afterthought.

## Reference Architecture Pattern Mapping

This section re-attaches the major external pattern sources that were abstracted away during reduction so the harness build can preserve design lineage.

### Context-Mode

- Maps to PreToolUse and PostToolUse interception.
- Maps to context quarantine, semantic paging, and budget-first delivery checks.
- Supplies the main anti-context-bloat operating pattern.

### Mastra Observational Memory

- Maps to Lyra as Observer and Reed as Reflector.
- Supplies the compression pipeline for raw tool outputs, observation logs, and refined knowledge write-back.
- Supplies the principle that active reasoning should not carry raw historical noise.

### CLI-Anything

- Maps to Dash as the conversion engine.
- Supplies the pattern for turning useful software or services into agent-native CLI surfaces.
- Supports the `scripts > MCPs` doctrine operationally.

### MCP2CLI

- Maps to lightweight adapters that reduce schema bloat.
- Supplies the bridge from large MCP or API definitions to lean runtime command invocation.

### PopeBot

- Maps to stateless worktrees, PR-gated execution, checkpoint-resume logic, and git-backed recovery.
- Supplies the strongest pattern for avoiding cross-session contamination while preserving reproducibility.

### KARL

- Maps to Orion's later-stage RL or policy-optimization path.
- Supplies the concept of learning routing and execution policy from accumulated high-quality traces.

### Overstory-style worker coordination

- Maps to typed mail, SQLite or WAL-backed coordination, isolated workers, and explicit escalation messages.
- Supplies practical patterns for multi-agent dispatch without collapsing into raw transcript passing.

## ACP Schema Seed

This is a first concrete schema seed for implementation. It is intentionally compact but typed enough to become YAML, JSON Schema, or a SkillML-adjacent contract later.

```yaml
acp_message:
  message_id: MSG-2026-0001
  parent_message_id: MSG-2026-0000
  sender_persona: Marcus
  receiver_persona: Diana
  message_type: TASK_REQUEST
  track_id: T1
  disclosure_level: L2
  context_budget: 8000
  threadex_thread_ref: qmd://project/research/thread_001
  action_summary: Extract pricing and positioning patterns from the source set.
  trajectory_semantics:
    - Do not repeat prior rejected angle.
    - Preserve SSOT terminology.
  metadata:
    priority: HIGH
    timestamp: 2026-03-14T12:00:00Z
    harness_version: v4.0.0
```

### Minimum contract rule

- The envelope should carry enough metadata to route, budget, and recover.
- The envelope should not carry the raw payload when a pointer is sufficient.
- The same envelope family should support `TASK_REQUEST`, `TASK_RESULT`, `QUALITY_CHECK`, `PHASE_TRANSITION`, and `PATCH_PROPOSAL`.

## Repeated Themes Removed or Collapsed

- Multiple repeated versions of the Harness vs Marcus authority boundary
- Repeated persona budget tables with small numeric variations
- Repeated warm-cache versus stateless debates
- Multiple copies of CLI-versus-message-bus tradeoff analysis
- Repeated clock-sync and reconciliation sections
- Repeated recovery architecture and hard-stop write-back patterns
- Repeated Obsidian mission-control explanations
- Repeated RL-later versus rules-now routing guidance

## Build Sequence Alignment

This compendium now maps directly to the current ULTRAMIND build sequence rather than floating as abstract theory.

### Phase 1A. Master Automations Architect

- Uses AA, CC, and the orchestration parts of EE.
- Defines the control surface, routing posture, Flowgram logic, and delegation contracts.

### Phase 1B. Memory Model

- Uses DD, BB + DD, and the authority split rules.
- Defines active state projection, deeper memory storage, checkpoints, and retrieval boundaries.

### Phase 2. Skill Repair and Evaluator Layer

- Uses the self-improvement loop in EE plus ACP schema and observation patterns.
- This is where the future Skill Evaluator should compare skills, emit patch proposals, and feed migration loops.

### Phase 3A. Claw Evaluation Track

- Uses EE, fallback-chain rules, and reference mappings to compare NanoClaw-like versus OpenClaw-like harness posture.
- Establishes the real tradeoffs before committing to one long-term harness shell.

### Phase 3B. Live Harness Assembly

- Uses AA through EE together after MAA and memory are stable.
- Binds routing, hooks, dashboards, repair loops, and specialist execution into one runtime.

## Open Decisions Still Not Fully Settled

- Final runtime choice between NanoClaw-like and OpenClaw-like harness posture
- Exact shape of the long-term memory stack beyond the current multi-tier direction
- Whether the human-facing graph layer lands first in Obsidian, Flowith-like UI, or a custom portal
- Exact data contract and storage choice for later COSMS layers

## Best Re-Use Pattern for NotebookLM

- Notebook A:
  - `AA`
  - `CC`
  - the `AA + CC` combined synthesis section
- Notebook B:
  - `BB`
  - `DD`
  - the `BB + CC` combined synthesis section
  - the `BB + DD Analytical Cross-Synthesis` section
  - the `ACP Schema Seed`
- Notebook C:
  - `EE`
  - `Reference Architecture Pattern Mapping`
  - `Build Sequence Alignment`
  - `Canonical Operating Decisions`
  - `Open Decisions Still Not Fully Settled`

## Short Canonical Summary

SUPERMIND should use a lean, typed, multi-model harness where Claude acts as the kernel, Marcus acts as the orchestrator, specialists execute inside strict contracts, ACP handles coordination, CLI handles execution, observers compress context, deeper memory stores durable traces, and routing stays rules-based until enough high-quality telemetry exists to justify learned optimization.

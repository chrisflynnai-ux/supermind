# Harness Systems Notebook C

## Scope

- `EE` Multi-Model Routing, CLI Integration, and Self-Improvement
- `Reference Architecture Pattern Mapping`
- `Build Sequence Alignment`
- Canonical operating decisions extracted from repeated sections
- Open architecture decisions still not fully settled

## Source Note

This notebook-ready file was split from the reduced master compendium. It keeps the cleaned structure, removes the repeated variants already collapsed in the master, and preserves the intended query-cluster lineage.

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

## Open Decisions Still Not Fully Settled

- Final runtime choice between NanoClaw-like and OpenClaw-like harness posture
- Exact shape of the long-term memory stack beyond the current multi-tier direction
- Whether the human-facing graph layer lands first in Obsidian, Flowith-like UI, or a custom portal
- Exact data contract and storage choice for later COSMS layers

## Short Canonical Summary

SUPERMIND should use a lean, typed, multi-model harness where Claude acts as the kernel, Marcus acts as the orchestrator, specialists execute inside strict contracts, ACP handles coordination, CLI handles execution, observers compress context, deeper memory stores durable traces, and routing stays rules-based until enough high-quality telemetry exists to justify learned optimization.

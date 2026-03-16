# Harness Systems Notebook B

## Scope

- `BB` ACP and Internal Routing
- `DD` Cognitive Bandwidth, Context Management, and Memory Integration
- `BB + CC` combined synthesis across the two notebook runs
- `BB + DD` analytical cross-synthesis added during reduction
- `ACP Schema Seed` for implementation follow-through

## Source Note

This notebook-ready file was split from the reduced master compendium. It keeps the cleaned structure, removes the repeated variants already collapsed in the master, and preserves the intended query-cluster lineage.

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

## Short Canonical Summary

SUPERMIND should use a lean, typed, multi-model harness where Claude acts as the kernel, Marcus acts as the orchestrator, specialists execute inside strict contracts, ACP handles coordination, CLI handles execution, observers compress context, deeper memory stores durable traces, and routing stays rules-based until enough high-quality telemetry exists to justify learned optimization.

# NotebookLM Harness Systems Query Pack V1

Date: 2026-03-11
Stage: Pre-design research — run BEFORE harness architecture design begins
Dependency: Threadex Memory Architecture design (completed)

## Purpose

Generate design inputs for the SUPERMIND dual-harness system through NotebookLM analysis of orchestration patterns, multi-model coordination, and agent communication references.

NotebookLM should help with:
- validating the dual-harness (Claude+Gemini / Codex+OpenClaw) strategy
- designing Agent Communication Protocol (ACP) for typed agent-to-agent messaging
- identifying cognitive bandwidth and context scheduling patterns
- designing lean team orchestration (1-3 specialists + orchestrator)
- finding patterns for cross-model routing and delegation
- identifying modern harness architectures (OpenClaw, NanoClaw, Overstory)
- designing the clock mechanism for team cycling across 4 tracks
- establishing multi-model capability mapping

NotebookLM should NOT decide:
- final memory backend (that is Threadex's domain)
- specific skill contents or copy doctrine
- whether to build Claude-first or Gemini-first
- specific API pricing or model selection
- whether SkillML V1.4 is optional

---

## Query Cluster A: Dual-Harness Architecture Patterns

Prompt:
```text
Analyze the concept of a dual-harness agentic system where:
- Harness A: Claude + Gemini (primary production harness)
  - Claude: copy, strategy, persuasion, analysis
  - Gemini: design, video, multimodal, visual production
- Harness B: Codex + OpenClaw (development/build harness)
  - Codex: code generation, testing, builds
  - OpenClaw: open-source agent orchestration

Both harnesses share the same memory layer (Threadex) and skill library.

Focus on:

1. What are the strongest patterns for dual-harness coordination? How do modern multi-model systems handle routing between different LLMs based on task type?

2. What is the right boundary between harnesses? Should they operate independently with shared memory (loose coupling) or have cross-harness delegation (tight coupling)?

3. How do you handle tasks that span both harnesses? (e.g., "build a sales page" needs Claude for copy + Gemini for design + Codex for frontend code)

4. What happens when harness capabilities overlap? (e.g., both Claude and Codex can write code) — how do you route without creating conflicts?

5. Failure modes: What happens when one harness is unavailable? How should the other harness compensate? Graceful degradation patterns?

6. Harness version management — when Claude gets a new model update, how do you validate that existing skills still work? Regression testing patterns for multi-model systems.

Format output as:
- Architecture patterns (strong, recommended)
- Architecture anti-patterns (avoid)
- Coupling recommendations (loose vs tight)
- Cross-harness routing rules
- Failure mode mitigations
- Version management strategies
```

## Query Cluster B: Agent Communication Protocol (ACP) Design

Prompt:
```text
We need to design an Agent Communication Protocol (ACP) for typed agent-to-agent messaging within the SUPERMIND system.

Current state:
- Skills communicate via typed contracts (AUTOMATION_REQUEST, HANDOFF_PACKAGE, etc.)
- Contracts are defined in SkillML V1.4 XML
- No runtime message bus exists yet
- MAA v4.0.0 declares ACP as a future seam

Requirements:
- Typed messages between agents (not free-form chat)
- Support for synchronous delegation (agent A waits for agent B)
- Support for asynchronous broadcast (agent A notifies all listeners)
- Support for handoff chains (A → B → C with provenance)
- Compatible with both harnesses
- Must work with lean teams (1-3 specialists + orchestrator)

Focus on:

1. What modern ACP / agent messaging patterns exist? Compare: A2A (Google), MCP tools (Anthropic), custom typed contracts, event bus patterns. Which fits a small-team agentic system best?

2. Message envelope design — what metadata must every ACP message carry? (sender, receiver, type, priority, context_budget, parent_message_id, harness_id?)

3. How should ACP handle "context budget negotiation"? (Agent A has 10K tokens of context to share, but Agent B only has 4K tokens available — what gets compressed/dropped?)

4. Delegation chains: Agent A delegates to Agent B, who delegates to Agent C. How do you maintain provenance without bloating context? Trace IDs? Compact handoff summaries?

5. Error handling in ACP: What happens when a delegated task fails? Retry? Escalate to orchestrator? Fall back to different agent? How many retries before circuit breaker?

6. ACP and memory: Should ACP messages be logged to Threadex? Which messages are worth persisting (decisions, handoffs) vs ephemeral (status checks, heartbeats)?

Format output as:
- Protocol comparison matrix
- Message envelope schema
- Context negotiation patterns
- Delegation chain patterns
- Error handling and circuit breaker rules
- Memory integration rules
```

## Query Cluster C: Lean Team Orchestration & Clock Mechanism

Prompt:
```text
The SUPERMIND system uses Lean Teams:
- Each team: 1-3 specialists + 1 orchestrator (max 8-10 agents total in system)
- Teams cycle across 4 production tracks: T1 Research → T2 Draft → T3 Production → T4 Polish
- A "clock mechanism" governs track transitions
- Teams are assembled dynamically based on project needs
- Sibling pairs (left-brain ↔ right-brain) work within teams

We have 20+ master agent types across 9 Agentic Functions:
- Automation, Production, Resonance, Persuasion, Development, Design, Orchestration, Learning, Repair

Focus on:

1. Clock mechanism design — what triggers a track transition? Time-based? Quality gate (MMA score threshold)? Deliverable completion? Hybrid?

2. Team assembly patterns — how does the orchestrator decide which 1-3 specialists to activate for a track? Skill-matching? Availability? Past performance on similar tasks?

3. Agent lifecycle within teams — how do specialists spin up and spin down? Pre-load context from Threadex? Warm start from previous track handoff? Cold start with `tx prime`?

4. Concurrent team patterns — can multiple lean teams run simultaneously on different projects? How do you prevent resource contention (same specialist needed by two teams)?

5. Orchestrator intelligence — should the orchestrator be a specialized agent or a meta-routing layer? What decisions does the orchestrator make vs. what is pre-configured in routing tables?

6. How do sibling pairs coordinate within a team? Do they work sequentially (analysis → synthesis → genesis) or in parallel with merge points?

7. Track-specific team compositions — are certain agent combinations "canonical" for specific tracks? (e.g., T1 always needs researcher + strategist, T3 always needs writer + editor)

Format output as:
- Clock mechanism design options
- Team assembly algorithms
- Agent lifecycle management
- Concurrent team coordination
- Orchestrator design patterns
- Sibling pair coordination models
- Canonical team compositions per track
```

## Query Cluster D: Cognitive Bandwidth & Context Management

Prompt:
```text
Multi-agent systems face "cognitive bandwidth" constraints:
- Each agent has a finite context window
- Loading memory competes with loading instructions and current work
- Different models have different context sizes (Claude 200K, Gemini 1M+, etc.)
- The SUPERMIND system uses Progressive Disclosure (L1-L4) to manage skill loading

Concepts to evaluate:
- Semantic Slicing: Breaking content into semantically coherent chunks for optimal loading
- Cognitive Bandwidth Scheduling: Allocating context space across memory, skills, and work
- Cognitive Synch Pulsing: Synchronized context refresh across team members
- Context Placement Strategy: Where in the context window information should go for best performance

Focus on:

1. Context budget allocation — what is the optimal split between skill instructions, memory retrieval, and working space? 30/20/50? 20/30/50? Does it vary by track?

2. Semantic slicing for memory retrieval — when `tx prime` returns 50 golden patterns but only 20 fit in context, how should the system slice? By relevance score? By sub-domain? By recency?

3. Cognitive Synch Pulsing — in a lean team of 3 agents, how do you keep them "synchronized" on project state without each one loading the full project context? Shared summary? Diff-based updates?

4. Context placement — modern research shows position matters in long context windows. Where should critical instructions vs. memory vs. current work be placed for optimal agent performance?

5. Progressive context escalation — how should an agent request more context when stuck? "I need more expertise on X" → orchestrator loads additional memory → agent retries?

6. Context garbage collection during execution — when should an agent dump context mid-task? What triggers a context refresh vs. a context append?

7. Model-specific context strategies — how should the system adapt when Claude (200K) vs Gemini (1M+) is the active agent? Different loading strategies?

Format output as:
- Context budget allocation formulas
- Semantic slicing algorithms
- Team synchronization patterns
- Context placement recommendations
- Escalation protocols
- Garbage collection triggers
- Model-specific adaptation strategies
```

## Query Cluster E: Multi-Model Capability Routing

Prompt:
```text
SUPERMIND must route tasks to the right model based on capability, not just availability:

Known strengths:
- Claude: Reasoning, copy, persuasion, analysis, code review, strategy
- Gemini: Multimodal, design, video, large context processing, visual understanding
- Codex: Code generation, testing, deployment, technical builds
- OpenClaw: Open-source orchestration, extensibility, custom tool chains

The system needs to:
- Route tasks to the best-fit model automatically
- Handle capability overlaps gracefully
- Support fallback when primary model is unavailable
- Track which model performed best on which task types
- Learn routing preferences over time

Focus on:

1. Capability taxonomy — what dimensions should we score models on? (reasoning, creativity, code, multimodal, speed, cost, context size, instruction following?)

2. Routing algorithm — static routing table? Dynamic scoring? ML-based router trained on outcome data? What is practical for a small system with 20 agent types?

3. Capability overlap resolution — when two models can both do a task, how do you pick? Cost optimization? Quality optimization? Round-robin for comparison data?

4. Performance tracking for routing improvement — what metrics should we capture per model-task pair? (MMA scores, time to complete, rework count, human satisfaction?)

5. How should routing handle compound tasks? (e.g., "write and design a sales page" — route copy to Claude, design to Gemini, then merge outputs)

6. Fallback chains — when Claude is rate-limited, can Gemini handle a copy task? How do you measure quality degradation and adjust routing thresholds?

7. How do existing multi-model orchestration systems (LangChain, CrewAI, AutoGen, OpenClaw) handle model routing? What patterns are proven at scale?

Format output as:
- Capability taxonomy schema
- Routing algorithm recommendations
- Overlap resolution strategies
- Performance tracking metrics
- Compound task decomposition patterns
- Fallback chain design
- Reference architecture comparison
```

---

## Normalized Output Format

Convert NotebookLM findings into a design-input document with these sections:

### Bucket 1: INCLUDE IN HARNESS DESIGN (must address)
- Architecture decisions
- Protocol schemas
- Routing rules
- Team composition patterns
- Context management strategies

### Bucket 2: DECLARE AS FUTURE SEAMS (acknowledge, defer)
- Advanced ML-based routing
- Cross-harness learning loops
- Full ACP implementation
- Scale-up strategies beyond 20 agents

### Bucket 3: ARCHITECTURE CONFLICTS (need resolution)
- Contradictions with MAA v4.0.0 contracts
- Contradictions with Threadex memory design
- Contradictions with ZPWO orchestration model
- Loose coupling vs tight coupling trade-offs

---

## Merge Rule

NotebookLM output is seed material.
Only promote findings that serve a practical dual-harness design.

Reject anything that:
- Requires a specific cloud orchestration platform
- Assumes a single-model architecture
- Ignores context window constraints
- Adds enterprise complexity to a lean-team system
- Couples harness design to specific model versions
- Contradicts the file-first memory philosophy (Threadex)
- Introduces framework lock-in (must stay harness-agnostic)

---

## Recommended Notebook Loading

Load these sources into NotebookLM alongside the query pack:

**Required:**
1. `docs/plans/2026-03-11-threadex-memory-architecture-design.md` — Memory architecture (harness must integrate)
2. `.agents/skills/automations/automations_master_architect_v4_0_0.xml` — MAA v4.0.0 (contracts, seams, ACP declaration)

**Highly Recommended:**
3. ZPWO v4.0 skill — Orchestration doctrine
4. SUB_AGENT_CONFIGS or AGENTS.md v4.0 — Current agent routing table
5. OpenClaw README / documentation — Harness B reference
6. os-eco/Overstory documentation — Orchestration reference
7. M5 Implementation Appendix — Multi-model patterns
8. M7 CONDUCTOR spec — Voice agent orchestration patterns

**Optional Research Context:**
9. LangChain / CrewAI / AutoGen documentation — Multi-model orchestration reference
10. Google A2A protocol documentation — Agent-to-agent messaging reference
11. MCP (Model Context Protocol) documentation — Tool integration reference
12. Super Knowledge compendiums (autonomous OS, super-brain)

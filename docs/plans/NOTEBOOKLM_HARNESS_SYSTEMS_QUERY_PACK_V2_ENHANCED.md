# NotebookLM Harness Systems Query Pack V2 — Enhanced

Date: 2026-03-12
Stage: Pre-design research — run BEFORE harness architecture design begins
Dependency: Threadex Memory Architecture design (completed, 14 patches applied)
Supersedes: NOTEBOOKLM_HARNESS_SYSTEMS_QUERY_PACK_V1.md

## Purpose

Generate design inputs for the SUPERMIND harness system through NotebookLM analysis of orchestration patterns, multi-model coordination, agent communication, memory integration, and modern agentic infrastructure references.

## Enhancement Patch Log

V2 enhancements over V1:
- Context-Mode plugin patterns (98% context reduction, SQLite FTS5, PreToolUse hooks)
- MCP2CLI + CLI-Anything (universal agent-native CLI interfaces, 95% token savings)
- Mastra Observational Memory (Actor/Observer/Reflector, 95% LongMemEval)
- KARL knowledge agents (Databricks RL-trained, 33% lower cost)
- PopeBot (git-as-memory, stateless Docker, PR review gates)
- OpenFang Agent OS (Rust, 137K LOC, Hands packages, Merkle audit)
- NanoClaw (500 LOC TypeScript, Claude Agent SDK, Docker sandbox)
- Claude native features (/loops, /memory, /tasks, MEMORY.md, Visualize Anything)
- Claude.mem persistent memory architecture
- Obsidian integration (graph-based 2nd brain, not abandoned)
- Auto-Research pattern (Karpathy generate-evaluate-mutate loop)
- Gemini CLI + Gemini Embedding2 (multimodal embeddings)
- Antigravity integration (Google AI production harness)
- 21 Master Agent Personas with human names
- Threadafile cross-file indexing and QMD routing
- Mission Control Dashboards concept
- OpenFlow marketplace concept
- Shifted from dual-harness (Claude+Gemini / Codex+Claw) to Claude-based harness for Gemini+Codex integration

## What Changed From V1

Key strategic shifts reflected in V2 queries:
1. **Skipping the Claws** — Claude-based harness first, not OpenClaw/NanoClaw
2. **Claude as orchestrator** — Claude native features (/loops, /memory, /tasks) replace external orchestration
3. **Obsidian retained** — Not abandoned; becomes 2nd brain front-end alongside Threadex
4. **CLI-first integration** — MCP2CLI + CLI-Anything as universal agent interface layer
5. **Context-Mode as reference architecture** — 98% context reduction patterns directly relevant to cognitive bandwidth
6. **Git-as-memory validated** — PopeBot proves stateless execution + git state works
7. **Named agent personas** — 21 master agents with human identities for persistent cross-session state
8. **Auto-Research for self-improvement** — Karpathy pattern for continuous skill/prompt optimization

---

## Query Cluster A: Claude-Based Harness Architecture

Prompt:
```text
Analyze the design of a Claude-based agentic harness system where:

- Primary Orchestrator: Claude (using native /loops, /memory, /tasks, MEMORY.md)
- Production Partner: Gemini (design, video, multimodal, visual production, Gemini CLI)
- Development Partner: Codex (code generation, testing, builds)
- Memory Layer: Threadex (file-first JSONL/YAML, QMD search, SQLite analytics)
- 2nd Brain Front-End: Obsidian (graph visualization, human archive, operations dashboard)
- CLI Layer: MCP2CLI + CLI-Anything (universal agent-native interfaces)

This is NOT a dual-harness system. Claude IS the harness. Gemini and Codex are delegated specialists.

Reference architectures to consider:
- Context-Mode plugin: 98% context reduction via SQLite FTS5 session tracking, PreToolUse hooks intercept tool calls, priority-tiered compaction to <=2KB, session recovery
- MCP2CLI: Runtime CLI generation from MCP servers, 95.2% token savings, provider-agnostic
- CLI-Anything: 7-phase pipeline converting any software to agent-native CLI
- PopeBot: Git-as-memory, stateless Docker execution, PR review gates, zero persistent state
- OpenFang: Rust Agent OS (137K LOC), Hands autonomous packages, Merkle audit trail
- NanoClaw: 500 LOC TypeScript, Claude Agent SDK, Docker sandbox isolation
- Mastra Observational Memory: Actor/Observer/Reflector trio, 95% LongMemEval, no vector DB
- Claude.mem: Claude persistent memory files across sessions
- Antigravity: Google AI production platform (Stitch, Opal)

Focus on:

1. Claude-as-harness architecture — how should Claude native features (/loops for iteration, /memory for persistence, /tasks for tracking, MEMORY.md for cross-session state) serve as the orchestration backbone? What gaps remain that need custom tooling?

2. Context-Mode patterns for harness design — the Context-Mode plugin achieves 98% context reduction via SQLite FTS5 + PreToolUse hooks + priority-tiered compaction. How should these patterns inform harness context management? Should the harness implement similar hook-based interception?

3. CLI-first integration layer — MCP2CLI generates CLIs from MCP servers at runtime (95% token savings). CLI-Anything converts any software to agent-native CLI in 7 phases. How should the harness use CLI interfaces as the universal integration pattern instead of direct API calls?

4. Delegation model — when Claude delegates to Gemini (via Gemini CLI) or Codex, what is the optimal delegation contract? Should it mirror the Threadex handoff.yaml schema? How does the harness handle async delegation vs sync delegation?

5. Stateless execution model — PopeBot proves that git-as-memory + stateless Docker execution works. Should the harness adopt stateless specialist execution (spin up, execute, commit results, spin down)? Or do long-running specialist sessions have advantages?

6. Obsidian as 2nd brain — how should Obsidian integrate as the human-facing front-end while Threadex serves as the agent-facing memory? Graph visualization for knowledge topology? Dashboard for operations? Archive for completed projects?

7. Failure modes — what happens when Gemini CLI is unavailable? When Codex is rate-limited? How should Claude compensate without degrading quality? Graceful degradation patterns for a single-orchestrator system?

8. OpenFang reference patterns — OpenFang Hands autonomous packages and Merkle audit trail represent a mature agent OS. What patterns should be adopted for the Claude harness? What is overkill for a lean system?

Format output as:
- Claude-as-harness architecture blueprint
- Context management patterns (from Context-Mode reference)
- CLI integration layer design
- Delegation contract schemas
- Execution model (stateless vs stateful trade-offs)
- Obsidian integration patterns
- Failure mode mitigations
- Reference pattern adoption matrix (what to adopt from each reference)
```

## Query Cluster B: Agent Communication Protocol (ACP) and Internal Routing

Prompt:
```text
We need to design an Agent Communication Protocol (ACP) for typed agent-to-agent messaging AND an internal routing system for scripts and agents within the SUPERMIND system.

Current state:
- Skills communicate via typed contracts (AUTOMATION_BLUEPRINT, HANDOFF_PACKAGE, etc.)
- Contracts are defined in SkillML V1.4 XML
- No runtime message bus exists yet
- MAA v4.0.0 declares ACP as a future seam
- Claude native /tasks provides task-level tracking
- Threadafile provides cross-file indexing and routing with QMD emphasis

We have 21 Master Agent Personas:
Marcus (Orchestrator), Diana (Researcher), Theo (Analyst), Maya (Strategist), Leo (Copywriter), Iris (Editor), Noel (Content Writer), Sage (Persuader), Ezra (Developer), Juno (Designer), Atlas (Automation), Petra (Producer), Felix (Quality), Vera (Optimizer), Reed (Learning), Nova (Repair), Kai (Voice Agent), Orion (Multi-Model Router), Lyra (Knowledge Manager), Dash (CLI/Tool), Ember (Dashboard/Viz)

Requirements:
- Typed messages between named agents (not free-form chat)
- Support for synchronous delegation (Marcus asks Diana to research)
- Support for asynchronous broadcast (Atlas notifies all listeners of automation event)
- Support for handoff chains (Diana -> Theo -> Maya with provenance)
- Compatible with Claude-as-harness model
- Must work with lean teams (1-3 specialists + orchestrator)
- Threadafile routing for cross-file context threading

Reference patterns to consider:
- MCP2CLI: CLI-based tool invocation eliminates token-heavy MCP payloads
- Context-Mode: PreToolUse hooks intercept and transform tool calls before execution
- Mastra OM: Actor sends messages, Observer watches for memory-worthy events, Reflector synthesizes
- KARL: RL-trained routing decisions, synthetic training data for routing optimization
- PopeBot: PR-as-review-gate for agent outputs before integration

Focus on:

1. Named agent messaging — with 21 persona-named agents, how should ACP address messages? By persona name? By role? By capability? How does naming affect routing flexibility?

2. Message envelope design — what metadata must every ACP message carry? Consider: sender_persona, receiver_persona, message_type, priority, context_budget, parent_message_id, track_id, threadex_thread_ref, timestamp, harness_version?

3. Threadafile routing — how should cross-file indexing route context between agents? When Diana (Researcher) writes findings to a JSONL file, how does Theo (Analyst) discover and load relevant context? Push vs pull? QMD search integration?

4. PreToolUse hook pattern — Context-Mode intercepts tool calls with hooks. Should ACP implement similar hooks that intercept agent-to-agent messages for: context budget enforcement, message compression, routing decisions, audit logging?

5. CLI-based agent invocation — instead of complex message buses, should agents invoke each other via CLI interfaces (MCP2CLI pattern)? What are the trade-offs vs typed message objects?

6. PR review gates — PopeBot uses PR reviews as quality gates. Should agent outputs go through review gates before being accepted? Felix (Quality) as automatic reviewer? Human review for high-stakes outputs?

7. Actor/Observer/Reflector trio — Mastra memory pattern has Actors (do work), Observers (watch for patterns), Reflectors (synthesize insights). Should ACP implement observer agents that watch message streams for memory-worthy events?

8. RL-trained routing — KARL uses reinforcement learning for routing decisions. Is RL-based routing practical for 21 agents, or is a simpler routing table (MAA v4.0.0 style) sufficient at this scale? What data would we need to train a router?

Format output as:
- Named agent addressing scheme
- Message envelope schema (with all required fields)
- Threadafile routing patterns
- Hook-based message interception design
- CLI vs message bus trade-offs
- Review gate architecture
- Observer agent patterns
- Routing algorithm recommendations (simple vs RL)
```

## Query Cluster C: Lean Team Orchestration, Clock Mechanism and Named Personas

Prompt:
```text
The SUPERMIND system uses Lean Teams with Named Agent Personas:

Team structure: 1-3 specialists + 1 orchestrator (Marcus)
Teams cycle across 4 production tracks: T1 Research -> T2 Draft -> T3 Production -> T4 Polish
A clock mechanism governs track transitions
Teams are assembled dynamically based on project needs
Sibling pairs (left-brain Brother <-> right-brain Sister) work within teams

21 Master Agent Personas across 9 Agentic Functions:
- Orchestration: Marcus (coordinator, track transitions, team assembly)
- Research: Diana (deep research), Theo (pattern analysis)
- Strategy: Maya (strategic planning, angle development)
- Copy/Resonance: Leo (copywriter), Noel (content writer)
- Editing/Persuasion: Iris (editor), Sage (persuasion specialist)
- Development: Ezra (backend, builds, integrations)
- Design: Juno (UI/UX, visual, frontend)
- Automation: Atlas (workflow automation, systems)
- Production: Petra (asset building, publishing)
- Quality: Felix (MMA scoring, quality gates)
- Optimization: Vera (performance, efficiency)
- Learning (ECR): Reed (pattern extraction, SIPs)
- Repair (ECR): Nova (patches, upgrades, fixes)
- Voice Agent: Kai (M7 CONDUCTOR, voice production)
- Multi-Model Routing: Orion (model selection, capability matching)
- Knowledge Management: Lyra (Threadex, memory curation)
- CLI/Tool Integration: Dash (MCP2CLI, CLI-Anything, tool management)
- Dashboard/Viz: Ember (Mission Control, flowgrams, monitoring)

Progression model: Analysis -> Synthesis -> Genesis
Sibling pairs: left-brain (logical/tactical) <-> right-brain (strategic/creative)

Reference patterns:
- Auto-Research (Karpathy): Generate -> Evaluate -> Mutate -> Keep/Discard loop
- PopeBot: Stateless execution per task, git-based state persistence
- Mastra OM: Actor/Observer/Reflector roles within teams
- Context-Mode: Session-aware context loading per agent persona

Focus on:

1. Clock mechanism design — what triggers track transitions for named teams? Quality gate (Felix MMA score threshold)? Deliverable completion (Petra confirms output)? Time-based? Hybrid? How does Marcus decide when to transition?

2. Team assembly with named personas — how does Marcus decide which 1-3 specialists to activate? Diana + Theo for T1 Research? Leo + Iris for T2 Draft? Petra + Felix for T3 Production? What are the canonical team compositions per track?

3. Persona persistence across sessions — each named agent should maintain consistent behavior, preferences, and expertise across sessions. How should Claude.mem / MEMORY.md store persona state? What fields define a persona beyond name and role?

4. Auto-Research integration — the Karpathy auto-research pattern can improve agent skills over time. How should Reed (Learning) + Nova (Repair) implement this loop? Which agent outputs should be auto-evaluated? What is the mutation strategy for skill prompts?

5. Sibling pair coordination — Diana (left-brain researcher) <-> Maya (right-brain strategist). Leo (left-brain copywriter) <-> Iris (right-brain editor). How do sibling pairs coordinate within a team? Sequential (analysis -> synthesis -> genesis)? Parallel with merge points? Debate/critique cycles?

6. Observer agents — should some personas (Reed, Felix) run as background observers during team execution? Watching message streams for patterns? Auto-flagging quality issues?

7. Stateless persona execution — PopeBot runs stateless per task. Should named personas load fresh each time (from Threadex persona files) or maintain warm sessions? What is the context cost of persona loading?

8. Mission Control Dashboard — Ember manages visualization. What should a Mission Control dashboard show? Active team, current track, quality scores, context usage, agent activity, Threadex memory stats, flowgram of current workflow?

Format output as:
- Clock mechanism design (triggers, thresholds, Marcus decision logic)
- Canonical team compositions per track (T1-T4)
- Persona state schema (fields for cross-session persistence)
- Auto-Research loop design (for skill self-improvement)
- Sibling pair coordination models
- Observer agent patterns (background monitoring)
- Stateless vs warm persona trade-offs
- Mission Control dashboard specification
```

## Query Cluster D: Cognitive Bandwidth, Context Management and Memory Integration

Prompt:
```text
Multi-agent systems face cognitive bandwidth constraints. The SUPERMIND system must manage context across:
- Claude (200K context window, /memory for persistence)
- Gemini (1M+ context, Gemini CLI, Embedding2 multimodal)
- Codex (specialized code context)
- Threadex memory layer (file-first, QMD search, SQLite analytics)
- Obsidian 2nd brain (graph-based knowledge topology)
- Claude.mem persistent memory files

The system uses Progressive Disclosure (L1-L4) to manage skill loading:
- L1: Classification + routing (~500 tokens)
- L2: Planning + structure (~2K tokens)
- L3: Full execution context (~5K tokens)
- L4: Deep reference + edge cases (~10K+ tokens)

Reference architectures:
- Context-Mode plugin: SQLite FTS5 session tracking, PreToolUse hooks, priority-tiered compaction (<=2KB), session recovery, 98% context reduction
- Mastra OM: 3-6x text compression via reflection, no vector DB needed, 95% LongMemEval
- KARL: Synthetic data training for context-efficient knowledge retrieval
- Threadex three-tier: Tier 1 files (truth) -> Tier 2 QMD (retrieval) -> Tier 3 SQLite (analytics)
- Claude native: /memory writes, MEMORY.md reads, /tasks tracking

Focus on:

1. Context-Mode patterns for SUPERMIND — how should 98% context reduction patterns be adapted for multi-agent context management?

2. Context budget allocation per persona — Marcus (orchestrator) needs broad shallow context. Diana (researcher) needs deep narrow context. Leo (copywriter) needs creative space. What is the optimal context split (skills/memory/workspace) per persona type?

3. Mastra compression for agent memory — how should Threadex tx prime implement 3-6x compression through reflection?

4. Claude.mem + MEMORY.md integration — how do Claude native persistent memory and Threadex file-based memory coexist?

5. Obsidian as context visualization — how should the harness surface context loading decisions to Obsidian for human review?

6. Gemini context advantages — when delegating to Gemini (1M+ context), should the harness send MORE context or maintain lean discipline?

7. Session recovery patterns — how should the harness handle mid-session crashes? What state must be persisted?

8. PreToolUse hooks for context gating — should the harness implement hooks that check context budget, compress results, strip irrelevant fields, enforce per-persona limits?

Format output as:
- Context-Mode adaptation blueprint for SUPERMIND
- Per-persona context budget allocations
- Compression pipeline design (Mastra-inspired)
- Claude.mem + Threadex coexistence model
- Obsidian visualization integration
- Model-specific context strategies
- Session recovery protocol
- PreToolUse hook specifications
```

## Query Cluster E: Multi-Model Routing, CLI Integration and Self-Improvement

Prompt:
```text
SUPERMIND must route tasks to the right model AND the right agent persona, with CLI-first integration and continuous self-improvement:

Models:
- Claude: Reasoning, copy, persuasion, analysis, code review, strategy, orchestration
- Gemini: Multimodal, design, video, large context, visual understanding, Embedding2
- Codex: Code generation, testing, deployment, technical builds

Named Router: Orion (Multi-Model Router persona)
Named Tool Manager: Dash (CLI/Tool Integration persona)
Named Learning Agent: Reed (Pattern extraction, SIPs)
Named Repair Agent: Nova (Patches, upgrades, fixes)

Integration tools:
- MCP2CLI: Runtime CLI generation from MCP servers (95.2% token savings, provider-agnostic)
- CLI-Anything: 7-phase pipeline converting any software to agent-native CLI
- Gemini CLI: Direct Gemini invocation from command line
- Antigravity: Google AI production platform (Stitch, Opal)

Self-improvement frameworks:
- Auto-Research (Karpathy): Generate batches -> Evaluate via scoring -> Mutate prompt -> Keep winners
- KARL: RL-trained knowledge agents, 33% lower cost through synthetic training data
- SIMS lifecycle: OBSERVED -> VALIDATED -> CANDIDATE -> GOLDEN with temporal decay
- MMA scoring: 7-dimension quality assessment with tiered thresholds

Focus on:

1. Orion routing algorithm — how should Orion decide between Claude, Gemini, and Codex?

2. Dash CLI integration strategy — how should Dash maintain a registry of available CLI tools?

3. Compound task decomposition — how does Orion decompose compound tasks, route sub-tasks, merge outputs?

4. Auto-Research for skill optimization — how should Reed + Felix + Nova implement the Karpathy loop?

5. KARL-style knowledge training — how could SIMS lifecycle benefit from RL-inspired training?

6. CLI-based model invocation — trade-offs of CLI-first vs API-first for multi-model systems?

7. Performance tracking — what metrics should Orion track per model-task-persona combination?

8. Fallback chains — when primary model is rate-limited, how does Orion measure quality degradation?

9. OpenFlow marketplace — how should routing handle community-contributed skills?

Format output as:
- Orion routing algorithm specification
- Dash CLI tool registry design
- Compound task decomposition patterns
- Auto-Research loop for skill optimization
- KARL-inspired knowledge training patterns
- CLI-first vs API-first trade-off analysis
- Performance tracking schema
- Fallback chain design with quality thresholds
- OpenFlow marketplace routing considerations
```

---

## Run Sequence

| Pass | Clusters | Focus | Why This Order |
|------|----------|-------|----------------|
| 1 | A + C | Claude-based harness + Lean teams | Core architecture decisions first |
| 2 | B + D | ACP/Routing + Cognitive bandwidth | Communication and context management |
| 3 | E | Multi-model routing + Self-improvement | Integration and optimization last (depends on A-D) |

**After each pass:** Copy NotebookLM outputs to a .docx file for import into Claude Code.
Name: Notebook LM Query Harness V2 [Pass Number].docx

---

## Source Loading Order

Load into NotebookLM in this order:

### Required (load first):
1. docs/plans/2026-03-11-threadex-memory-architecture-design.md
2. .agents/skills/automations/automations_master_architect_v4_0_0.xml
3. .agents/skills/automations/automations_master_architect_v4_0_0_notebooklm.md

### Highly Recommended (load second):
4. ZPWO v4.0 skill
5. AGENTS.md v4.0
6. This query pack (V2 Enhanced)

### Reference Architecture Sources (load third):
7. Context-Mode plugin documentation
8. MCP2CLI documentation
9. CLI-Anything documentation
10. Auto-Research skill
11. Mastra Observational Memory documentation
12. OpenFang README
13. NanoClaw README

### Optional Context:
14. M7 CONDUCTOR spec
15. PopeBot documentation
16. KARL research paper
17. Google A2A protocol documentation
18. Super Knowledge compendiums

---

## Normalized Output Format

### Bucket 1: INCLUDE IN HARNESS DESIGN (must address)
- Architecture decisions (Claude-as-harness model)
- Protocol schemas (ACP message envelope, delegation contracts)
- Routing rules (Orion algorithm, Dash CLI registry)
- Team composition patterns (canonical T1-T4 teams)
- Context management strategies (Context-Mode adapted patterns)
- CLI integration layer design
- Persona persistence model

### Bucket 2: DECLARE AS FUTURE SEAMS (acknowledge, defer)
- RL-trained routing (KARL-style)
- OpenFlow marketplace integration
- Advanced observer agents
- Full Obsidian integration
- Auto-Research at scale
- Cross-harness A/B comparison

### Bucket 3: ARCHITECTURE CONFLICTS (need resolution)
- Contradictions with MAA v4.0.0 contracts
- Contradictions with Threadex memory design
- Contradictions with ZPWO orchestration model
- Claude native features vs custom tooling overlap
- Obsidian vs Threadex boundary disputes

---

## Merge Rule

NotebookLM output is seed material.
Only promote findings that serve a practical Claude-based harness design.

Reject anything that:
- Requires a specific cloud orchestration platform
- Assumes a single-model architecture
- Ignores context window constraints
- Adds enterprise complexity to a lean-team system
- Couples harness design to specific model versions
- Contradicts the file-first memory philosophy (Threadex)
- Introduces framework lock-in (must stay harness-agnostic)
- Abandons Claude-as-harness for external orchestration layer
- Ignores CLI-first integration principle
- Requires infrastructure beyond local machine + API keys

---

## Key Strategic Context for NotebookLM

1. **Claude IS the harness** — Claude native features (/loops, /memory, /tasks, MEMORY.md) are the foundation.
2. **CLI-first integration** — MCP2CLI + CLI-Anything as the universal interface pattern.
3. **Named personas are persistent** — 21 master agents maintain state via Claude.mem + Threadex.
4. **Obsidian stays** — Human-facing 2nd brain alongside agent-facing Threadex.
5. **Self-improvement is built in** — Auto-Research + SIMS + MMA create continuous improvement.
6. **Context discipline is paramount** — Context-Mode 98% reduction patterns inform everything.
7. **Simplicity over complexity** — Deep roster, shallow active teams (1-3 at a time).

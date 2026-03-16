# ULTRAMIND Strategic Update
## 2026-03-08 — Vision Expansion & Next Phase Planning

> **Companion to:** `BUILD_SUMMARY_V2_2026-03-06.md`
> **Status:** Strategic planning session — capturing new directions before execution
> **Phase 0:** COMPLETE. Phase 1 prerequisites pending. New scope added below.

---

## 1. Revised Order of Operations

The following replaces the Phase 1 entry sequence from BUILD_SUMMARY_V2:

```
[TODAY]     Master Automations Architect (MAA)  ← finish tomorrow
[NEXT]      Hash out Hybrid Memory Model (3-track)
[THEN]      Skill Repair + Enhancement (batch by batch)
[THEN]      Knowledge Blocks formatting for XML review
[THEN]      Larger Agent Harness (OpenClaw/NanoClaw-type Agentic OS)
```

---

## 2. SkillML Framework Standard — Relational Agentics

### Core Concept: Relational Agentics
Skills are not isolated units. They exist in **relational graphs** — knowing what other skills they depend on, what skills they can delegate to, and what skills they complement. This is the architectural shift from a flat skill library to a connected skill network.

### Skill Evaluator (New Tool — to build)
A dedicated evaluation agent that:
- Evaluates any skill against SkillML V1.4 spec (19 checks)
- **Compares** the skill against existing skills in the same domain
- Identifies redundancy, gaps, and upgrade opportunities
- Generates **suggested repair patches** (structured patch proposals, not raw edits)
- Output: `SKILL_EVAL_REPORT.yaml` per skill

### Skill Upgrade Sequence (Per Group)
```
1. Initial Patch Pass    — fix XML errors, normalize skill_id, add V1.4 sections
2. NotebookLM Queries   — enhance capabilities via targeted query sequences
3. Relational Ops        — map skill to its network (dependencies, delegates, complements)
4. Validate 19/19        — SkillML validator + linter
5. Promote               — move to production-ready
```

### Priority Target: 7-8 Module Skills
The multi-module KB skills (ads, email, leadgen) have the highest error rates and the most complex relational structure. These get NotebookLM enhancement passes, not just XML fixes.

---

## 3. Skill Family Roadmap

### Existing Domains (to repair + enhance)
| Domain | Skills | Priority | Primary Issue |
|--------|--------|----------|---------------|
| copy | 13 | Batch 1 | XML errors, V1.4 gaps |
| research | 8 | Batch 1 | Minor errors |
| meta | 3 | Batch 1 | ZPWO done; MMA needs relational ops |
| product | 6 | Batch 2 | Mix of errors |
| design | 9 | Batch 2 | Mix of errors |
| ads | 8 | Batch 3 | 7 parse errors — KB modules |
| email | 8 | Batch 3 | 8 parse errors — KB modules |
| leadgen | 5 | Batch 3 | 5 parse errors — KB modules |
| advisor | 2 | Batch 4 | Minor |
| systems | 2 | Batch 4 | Parse errors |
| writing | 1 | Batch 4 | Parse errors |

### New Skill Families (to build out — TBD scoping)
- Personal Agentics family
- Agentic Workflow skills (connecting to COSMS hubs)
- Memory skills (aligned with hybrid memory model)
- Guardian/Regulatory Agent
- Flowgram generation skills

---

## 4. Hybrid Memory Model (3-Track — TBA)

Architecture to be defined. Working constraints:
- **Track 1:** Always-on context (CLAUDE.md / ZPWO — ≤2,000 tokens)
- **Track 2:** Session buffer (SESSION_STATE.json — hot working memory)
- **Track 3:** Semantic LTM (COSMS / SQLite — cold, searchable archive)

Second Brain component: personal knowledge modeling alongside system memory.
Human front-end for COSMS knowledge archives — expertise modeling, retrievable by agents.

---

## 5. Agentic OS — OpenClaw / NanoClaw Evaluation

### Two Candidates
| System | Repo | Profile |
|--------|------|---------|
| **OpenClaw** | (to locate) | Full-featured agentic harness |
| **NanoClaw** | https://github.com/qwibitai/nanoclaw | Lightweight alternative |

**Decision pending:** Evaluate both against harness requirements before committing.

### Harness Architecture (Multi-Model)
```
BRAIN:       Claude Code (Claude Sonnet/Opus 4.x) — reasoning, orchestration
COORDINATOR: Codex 5.4 — code generation, technical execution
PEER:        Gemini 3.1 (Flash/Pro) — parallel research, high-throughput
```

Model-agnostic at execution layer via typed I/O contracts (already spec'd in routing_table v4.0).

### Custom Dashboard
Build within Claude Code. Potential integration point with Flowgrams canvas display.

---

## 6. Flowgrams — Visual Workflow System

### Concept
A visual diagram workflow model ("Flowgrams") that represents agent pipelines, skill chains, and SSOT data flows as interactive diagrams.

### Tools Under Consideration
| Tool | Role |
|------|------|
| **Excalidraw** | Primary diagram canvas (hand-drawn aesthetic, collaborative) |
| **Draw.io** | Alternative / secondary (more formal, export-friendly) |
| **Mermaid** | In-terminal diagrams during agentic OS build phase |

### Excalidraw Skill Integration
- **Candidate repo:** https://github.com/coleam00/excalidraw-diagram-skill
- Plan: Clone → evaluate → enhance → build **custom Workflow Illustrator**
- Integration target: Master Automations Architect (MAA)
- Canvas display: potential live dashboard panel

### Mermaid Usage
Mermaid diagrams used during agentic OS build phase for:
- Agent dependency maps
- Routing flow diagrams
- Skill relationship graphs (relational agentics)

---

## 7. COSMS — Knowledge Hub Architecture

### Definition
COSMS = Connected Operational Skill Memory System
Dual-DB: DuckDB (search/vectors) + SQLite (operational memory)

### Human Front-End Layer (new addition)
COSMS nodes have human-facing interfaces for:
- Knowledge and expertise modeling
- Archive retrieval
- Contributor attribution (revenue sharing model)
- Knowledge Blocks as tradeable, sanitized training sets

### Connection Points
- Agent skills connect **to** COSMS hubs for knowledge retrieval
- Agentic Workflows route **through** COSMS for state and memory
- Human operators interact **via** front-end portals

---

## 8. Terminal Learning Track

User goal: develop terminal proficiency alongside building the system.
Approach: Claude Code as the training environment — real tasks, real commands.

Suggested progression:
1. Navigation + file operations (`ls`, `cd`, `cat`, paths)
2. Git workflow (daily push protocol, worktrees)
3. Python script execution (harness tools)
4. tmux multi-pane layout (WSL via `tmux_setup.sh`)
5. Session management + parallel agent dispatch

---

## 9. Open Items / Decisions Pending

| Item | Status | Notes |
|------|--------|-------|
| Master Automations Architect | In progress | Finishing tomorrow |
| Hybrid Memory Model spec | TBD | 3-track architecture to be defined |
| OpenClaw vs NanoClaw selection | TBD | Evaluate both repos |
| Excalidraw skill clone + eval | TBD | https://github.com/coleam00/excalidraw-diagram-skill |
| New skill families scoping | TBD | Personal Agentics, Agentic Workflows, etc. |
| COSMS human front-end design | TBD | Portal architecture needed |
| Flowgrams canvas display spec | TBD | Integration with MAA |
| Skill Evaluator tool build | Queued | After MAA + memory model |

---

## 10. Updated Build Sequence

```
Phase 0   [DONE]    Tooling + ZPWO v4.0 + Acceptance Tests
─────────────────────────────────────────────────────────
Phase 1A  [NEXT]    Master Automations Architect (MAA) — finish tomorrow
Phase 1B            Hybrid Memory Model — 3-track spec + implementation
Phase 1C            CLAUDE.md v4.0 upgrade + canvas/session_state patches
─────────────────────────────────────────────────────────
Phase 2A            Skill Evaluator tool build
Phase 2B            Skill repair + enhancement (Batch 1-4, with relational ops)
Phase 2C            Knowledge Blocks XML formatting pass
─────────────────────────────────────────────────────────
Phase 3A            OpenClaw/NanoClaw harness evaluation + selection
Phase 3B            Agentic OS build (Claude + Codex + Gemini)
Phase 3C            Custom dashboard
─────────────────────────────────────────────────────────
Phase 4A            Flowgrams / Excalidraw Workflow Illustrator
Phase 4B            COSMS human front-end
Phase 4C            New skill families (Personal Agentics, Workflows, etc.)
─────────────────────────────────────────────────────────
Phase 5             Go-to-Market: SkillML open source + marketplace
```

---

*Strategic Update — 2026-03-08*
*Session type: Vision planning + scope capture*
*Next session: Complete Master Automations Architect*

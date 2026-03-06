# SUPERMIND Architecture Briefing
## Terminal Interface & Agentic OS Design — 2026-03-04

> **Companion document to:** `BUILD_SUMMARY_2026-03-04.md`
> The build summary records *what* was created. This document explains *why* each piece exists, *how* they connect, and *what the full system is designed to become*.

---

## 1. The Problem Being Solved

### Why Terminal Instead of Chat?

Your existing workflow runs in Claude Chat/Projects. That environment excels at **single-thread cowork** — you and Claude in a conversation, one skill active at a time. But your 4-Track model requires a fundamentally different compute model:

| Chat/Projects | Terminal (Claude Code) |
|---------------|----------------------|
| One thread, sequential | Multiple parallel sessions |
| Context resets each session | State persists via SESSION_STATE.json |
| Skills pasted manually | Skills loaded programmatically |
| You are the orchestrator | Conductor script routes tasks |
| No git integration | Full branch/worktree control |
| Desktop-only | Anywhere with terminal access |

The core need: **T1 Research should run while T2 is drafting on a previous project. MMA quality checks should not block the copy agent. Skill refactoring should not interrupt active production.** Terminal + parallel sessions solves this. The harness is the coordination layer.

### The Three Accounts Problem

You currently operate across three environments:

- **Browser Chat (Desktop):** Your primary project/skills home — migrating here
- **Claude Code Desktop:** File management, visual cowork (email access issue)
- **Claude Code Terminal (this session):** New home, full harness control

The terminal harness was designed so that work done in any environment can be picked up in any other. `KANBAN.json` is the handoff object. `SESSION_STATE.json` is the working memory. `memory/` is the persistent identity.

---

## 2. The Master Architecture: Five Layers

```
┌─────────────────────────────────────────────────────────────┐
│  LAYER 5: MEMORY FRAMEWORK                                  │
│  memory.md  |  insights.md  |  agents.md                   │
│  Persistent identity, SIPs, agent registry                  │
├─────────────────────────────────────────────────────────────┤
│  LAYER 4: ORCHESTRATION                                     │
│  conductor.py  |  KANBAN.json  |  cmux.py                  │
│  Task routing, parallel dispatch, inter-agent comms         │
├─────────────────────────────────────────────────────────────┤
│  LAYER 3: WORKFLOW INTERFACE                                │
│  canvas.py  |  session_state.py  |  slash commands         │
│  Visual dashboard, state tracking, protocol shortcuts       │
├─────────────────────────────────────────────────────────────┤
│  LAYER 2: SKILL ACCESS                                      │
│  skill_loader.py  |  SKILLS_MANIFEST.yaml                  │
│  Progressive disclosure, context budget enforcement         │
├─────────────────────────────────────────────────────────────┤
│  LAYER 1: GIT INFRASTRUCTURE                               │
│  Worktrees  |  Branches  |  Daily push routine             │
│  Parallel workspaces, version control, backup              │
└─────────────────────────────────────────────────────────────┘
```

---

## 3. Layer 1: Git Infrastructure

### The Three-Tier Worktree Architecture

Git worktrees allow multiple working directories from one repository. Each worktree can have its own Claude Code terminal session open — meaning each is an independent agent workspace that shares the same git history.

```
C:/Users/cfar7/OneDrive/Desktop/

ULTRAMIND/                     [main branch]
  PURPOSE: Master integration point. All skills, all context.
  AGENT ROLE: Integration / review / release
  WORK HERE: Merging stable skill updates, daily push

ULTRAMIND-atomic/              [atomic-foundations branch]
  PURPOSE: Raw base modules — L1 descriptors, atom components
  AGENT ROLE: Skill Builder
  WORK HERE: Breaking skills into reusable atoms, building
             new skills from the ground up, base templates

ULTRAMIND-domain/              [domain-specialists branch]
  PURPOSE: Vertical expertise — copy, research, design, product
  AGENT ROLE: Domain Specialist per vertical
  WORK HERE: Full skill refinement (LFVA, SFVW, MIS, HPE, NRA)
             Adding layer tags, SelfCheck, MMAGate, normalizing

ULTRAMIND-orchestrators/       [campaign-orchestrators branch]
  PURPOSE: Workflow runners — ZPWO, MMA, Conductor, routing
  AGENT ROLE: ZPWO / MMA
  WORK HERE: 4-track routing table, orchestration patches,
             acceptance tests, SSOT validation scripts
```

**Branch naming maps directly to skill tiers** from `ARCHITECTURAL_REVIEW_SKILL_STRUCTURE_v1.md`:
- Atomic = base atoms with no cross-skill dependencies
- Domain = fully-formed specialist skills
- Orchestrators = meta-skills that coordinate other skills

**Why this matters for parallel sessions:** You can open three terminal windows simultaneously — each in a different worktree, each running a Claude Code session on a different tier — without conflicts. Merge to `main` when work is stable.

### Daily Git Push Protocol

```bash
cd "C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND"
git add .
git commit -m "Daily update: [describe changes]"
git pull origin main --rebase
git push origin main
```

The `--rebase` flag ensures your local commits always sit on top of any remote changes. This is safe: it replays your work after pulling, rather than creating a merge commit.

**Important:** The git remote URL currently contains a token (`ghp_...`) embedded in the URL. This should be rotated and replaced with a credential helper to avoid token exposure in git logs.

---

## 4. Layer 2: Skill Access — The Skill Loader

### The Core Problem: Token Budget

Your production skills are large:
- LFVA: 1,555 lines
- SFVW: 1,448 lines
- MMA: 1,066 lines

Pasting any of these in full at session start costs 8,000–12,000 tokens before you've done any work. Against your Zero-Point budget of ≤2,000 tokens for the always-loaded orchestrator, this breaks the architecture.

### Progressive Disclosure — Mechanically Enforced

`skill_loader.py` extracts XML skill layers on demand:

```bash
python tools/scripts/skill_loader.py mma --layer 1
# Output: ~600 tokens — Identity, 7D definitions, verdict logic, mode selector
# Use when: You need to know what MMA does, not run it

python tools/scripts/skill_loader.py mma --layer 2
# Output: ~4,600 tokens — Adds all 5 operating modes with full processes
# Use when: Actually running an MMA validation

python tools/scripts/skill_loader.py mma --layer 3
# Output: ~7,600 tokens — Adds edge cases, 7S/7F chain audit details
# Use when: Complex quality issues, deep audit mode

python tools/scripts/skill_loader.py mma --layer 4
# Output: ~9,600 tokens — Full atoms, examples, historical notes
# Use when: Rarely. Debugging or skill patching only.
```

**Token budget compliance:**

| Component | Budget | Enforcement |
|-----------|--------|-------------|
| ZPWO orchestrator | ≤2,000 tokens | Always-loaded rule |
| Skills manifest (L1 descriptors) | ~500 tokens | Manifest file only |
| Active skill L2 | ~1,500–3,500 tokens | Loaded per-conversation |
| SSOTs (full content) | ~2,000–4,000 tokens | Loaded per-conversation |
| **Zero-Point total** | **~1,500 tokens** | **Under 2,000 budget** |
| **Active session total** | **~5,000–9,000 tokens** | **Per-conversation only** |

### Skill Discovery

```bash
python tools/scripts/skill_loader.py --list
# Scans .claude/skills/ and SUPERMIND PROJECT/
# Reports: skill_id, name, status, parse errors

python tools/scripts/skill_loader.py --manifest
# Shows full SKILLS_MANIFEST.yaml — the routing index
```

The loader searches both ULTRAMIND (`.claude/skills/`) and SUPERMIND PROJECT directory, handling the transition period where skills exist in both locations.

---

## 5. Layer 3: Workflow Interface

### 5.1 Session State Manager

`SESSION_STATE.json` is the working memory that persists between terminal sessions. Without it, every new Claude Code session starts with zero context about what's in progress.

**What it tracks:**

```json
{
  "session_id": "session_2026_03_04_143022",
  "project_name": "Sleep for Life",
  "current_phase": "production",
  "current_track": "T3",
  "loaded_skills": ["copy_lfva"],
  "context_usage_pct": 62,
  "locked_ssots": {
    "PROJECT_BRIEF.yaml": "sha256:abc123...",
    "MESSAGE_SPINE.yaml": "sha256:def456..."
  },
  "fix_loops": {
    "D2_proof": 2
  },
  "mma_scores": {
    "last_run": "2026-03-04T14:30:22",
    "average": 7.8,
    "critical_min": 7.4
  },
  "gc_runs": 1,
  "patch_requests": [],
  "sips_logged": [],
  "human_corrected_events": []
}
```

**Practical use:**

```bash
# At session start — see where work left off
python tools/scripts/session_state.py show

# After loading a skill
python tools/scripts/session_state.py load_skill copy_lfva

# Circuit breaker check — if this returns 3, HALT
python tools/scripts/session_state.py json | grep fix_loops

# Context approaching 70% — run GC
python tools/scripts/session_state.py gc

# New project, clean slate
python tools/scripts/session_state.py reset
```

**SSOT Drift Protection:** The `locked_ssots` section stores SHA-256 checksums. Before any phase transition, compare current file checksum against stored value. If they differ, HALT — someone modified a locked SSOT without a Patch Request. This is the mechanical implementation of `SSOT_LOCKING` from ORCHESTRATOR_CORE.yaml.

### 5.2 Canvas — Terminal Visual Dashboard

Four views, all read-only (no state mutation):

**`canvas.py state` — Live Workflow Monitor**
```
Track Progress: [T1]─────────[T2]─────────[T3]─────────[T4]
Context:        [████████████████░░░░░░░░░░░░░░░░░░░░░░░░] 42%
Loaded Skills:  ▸ copy_lfva
SSOT Locks:     [LOCKED  ] PROJECT_BRIEF
                [LOCKED  ] MESSAGE_SPINE
                [unlocked] EVIDENCE_PACK
MMA:            Average: 7.8   Critical Min: 7.4
```

**`canvas.py neurobox` — 6D Architecture Diagram**
Color-coded ANSI rendering of the Neuro-Box: MIND (blue), SPIRIT (green), BODY (red), HEART (yellow), PSYCH (magenta), COSMIC (cyan), SOUL (white center). Useful at session start to orient which dimension and axis your current work targets.

**`canvas.py track T2` — Track Protocol Reference**
Commands, skill chain, outputs, gate criteria for any track. Replaces re-reading CLAUDE.md to remember what T2 requires.

**`canvas.py mma` — MMA Scorecard Template**
The full 7-dimension rubric with weights and thresholds visible while you score. Ensures you apply the correct criteria before running `/validate`.

### 5.3 Custom Slash Commands

Claude Code reads `.claude/commands/` as native slash commands. These encode your full workflow protocols as one-word triggers:

| Command | Protocol Loaded |
|---------|----------------|
| `/run-research` | T1 team: Market Scout → Research Ops → MIS. Outputs: PROJECT_BRIEF, MESSAGE_SPINE, EVIDENCE_PACK. Gate: human SSOT approval. |
| `/run-draft` | T2 team: Copy Lead → Copy Director → assigned specialist. Strategy-first, angle exploration, MMA M1 gate. |
| `/run-production` | T3 team: Active skill in production mode + MMA M2 continuous validation. Circuit breaker active. |
| `/run-polish` | T4 team: HPE → Skeptic Avatar → NRA. Human Personance + AI Detox + Neuro-Resonance audit. |
| `/score-copy` | MMA M1 Quick Score. 7D rubric, weighted average, PASS/FIX/ESCALATE verdict with routing. |

**Why this matters:** Instead of explaining your workflow architecture to Claude at the start of every session, you type `/run-draft` and the full T2 protocol — skill chain, gate criteria, SSOTs required, MMA threshold, circuit breaker rules — loads automatically. It encodes institutional knowledge that doesn't need to be re-stated.

---

## 6. Layer 4: Orchestration

### 6.1 The Conductor Pattern

The Conductor is the **master delegation engine**. It implements the "Conductor Pattern" where a lightweight orchestrator reads a task list and delegates to specialist teams — it does not execute the work itself.

```
CONDUCTOR reads KANBAN.json
         ↓
Finds next task (priority + phase order)
         ↓
Determines track (T1/T2/T3/T4)
         ↓
Generates Task tool parameters:
  - Team composition
  - SSOT references
  - Gate criteria
  - Circuit breaker rules
  - Prompt with full context
         ↓
Human pastes into Claude Code
         ↓
Sub-agent executes, writes artifacts
         ↓
Sub-agent updates KANBAN.json
         ↓
Next task / next phase
```

**Team compositions:**

```
T1: Research Team
    Lead:    Market Scout       — Intelligence gathering, competitor analysis
    Members: Research Ops       — Deep research execution
             MIS                — Market Intelligence Synthesizer
    Gate:    Human approval of PROJECT_BRIEF + MESSAGE_SPINE + EVIDENCE_PACK

T2: Draft Team
    Lead:    Copy Lead          — Strategy direction, brief creation
    Members: Copy Director      — Angle selection, specialist assignment
             Assigned Specialist — LFVA/SFVW/SPC/ACM per asset type
    Gate:    Human approval + MMA M1 >= 7.0

T3: Production Team
    Lead:    Active Specialist   — Same skill as T2, now in production mode
    Members: MMA                 — Continuous 7D validation
    Gate:    MMA M2 >= 8.0 or human override

T4: Perfecting Team
    Lead:    HPE                 — Human Persuasion Editor, voice polish
    Members: Skeptic Avatar      — Objection stress testing, red team
             NRA                 — Neuro-Resonance Auditor, 6D balance
    Gate:    MMA M4 >= 9.0 + human final publish approval
```

### 6.2 CMUX — Claude Multiplexer

CMUX generates Task tool parameters for Claude Code's native parallel execution. It doesn't run agents — it makes it trivial to construct the right prompt for each dispatch.

**Single dispatch:**
```bash
python tools/scripts/cmux.py dispatch T2 "VSL draft for Sleep for Life"
# Outputs JSON: description, prompt (with full T2 context), subagent_type, model
```

**Parallel dispatch (two tracks simultaneously):**
```bash
python tools/scripts/cmux.py parallel T2 T3 --task "Sleep for Life funnel"
# Outputs two JSON blocks
# Paste both into ONE Claude Code message
# Claude runs T2 and T3 as parallel sub-agents
```

**Full chain:**
```bash
python tools/scripts/cmux.py chain "Complete funnel for Sleep for Life"
# Outputs T1 -> T2 -> T3 -> T4 in sequence
# Each with its gate criteria noted
# Run sequentially, waiting for human gate at each transition
```

### 6.3 KANBAN.json — Inter-Agent Communication Bus

The kanban is not a project management tool in the traditional sense. It is the **shared state object between parallel Claude Code sessions**. When Session A completes T2 work, it writes:

```json
"TASK-0001": {
  "status": "T3_production",
  "current_track": "T3",
  "artifacts": ["vsl_draft_v1.md", "angle_set.yaml"],
  "mma_scores": {
    "M1": {"average": 7.4, "verdict": "PASS"}
  },
  "history": [
    {"action": "moved_to_T3_production", "timestamp": "2026-03-04T15:22:00"}
  ]
}
```

Session B (the T3 production agent) reads KANBAN at startup, sees the task is in `T3_production`, loads the artifact `vsl_draft_v1.md`, and picks up exactly where Session A left off — without Session A and Session B ever being in the same conversation.

**Column structure:**
```
backlog          → New tasks, not yet assigned
T1_research      → Active research phase
T2_drafts        → Active draft phase
T3_production    → Active production phase
T4_perfecting    → Active polish phase
done             → Shipped
blocked          → Waiting on human input or external dependency
```

---

## 7. Layer 5: Memory Framework

### 7.1 memory.md — Stable Persistent Identity

Replaces the Claude Project description. Every new terminal session should instruct Claude to read this file first. It contains:
- User context (name, accounts, working style)
- Active projects with status
- Learned behaviors (what has been confirmed to work)
- Technical context (Python version, git remote, Windows encoding constraints)

This is what prevents Claude from re-discovering the same facts in every session.

### 7.2 insights.md — ECR Learning Phase (SIPs)

The **Self-Identified Patterns** file. This is the Learning phase of your End Cycle Recursion framework made persistent. After each session, significant discoveries are logged here — architecture insights, process improvements, technical gotchas.

Example entries logged from today:
- Python cp1252 encoding on Windows — Unicode arrows fail in `canvas.py` (fixed)
- Git worktrees share `.git` but have independent working directories
- Skills inventory: 21 production-ready, ~30 with parse errors needing remediation

Future sessions that touch the same areas load this file and don't repeat the same mistakes.

### 7.3 agents.md — The Agent Registry

Master skills that can spawn sub-agents are architecturally different from leaf skills. The registry documents:
- Every master agent's canonical skill ID
- What sub-agents it can spawn
- Gate criteria for each spawn decision
- The prompt injection protocol (how Task tool parameters are structured)

**Prompt Injection Model:**

"Prompt injection" in your architecture means: a parent agent (e.g. Copy Director) constructs a Task tool call that injects:
1. The child skill's L1/L2 content
2. Relevant SSOT references
3. The specific work instruction
4. Circuit breaker parameters

The child agent (e.g. LFVA) receives a fully-loaded context and executes without needing to discover its own instructions. This is the mechanical implementation of "Heavy Edges" — the skill carries its own execution context.

---

## 8. The 4-Track Workflow — Terminal Execution Map

### How a Full Campaign Runs in Terminal

```
SESSION 1 — T1: Research Lock
├── python session_state.py reset
├── python canvas.py state
├── /run-research  (slash command)
├── [Market Scout → Research Ops → MIS]
├── Lock PROJECT_BRIEF.yaml, MESSAGE_SPINE.yaml, EVIDENCE_PACK.yaml
├── python session_state.py set current_track T2
├── [Human gate: review and approve SSOTs]
└── python conductor.py add "Sleep VSL" --type vsl --priority high

SESSION 2 — T2: Draft Development
├── python session_state.py show          (orient)
├── python canvas.py track T2            (protocol reference)
├── python skill_loader.py copy_lfva --layer 2  (load skill)
├── /run-draft  (slash command)
├── [Copy Lead → Copy Director → LFVA]
├── MMA M1 Quick Score (target: >= 7.0)
├── python conductor.py status           (update kanban)
└── [Human gate: angle approval]

SESSION 3 — T3: Production
├── python conductor.py run              (read kanban, get task)
├── python skill_loader.py copy_lfva --layer 2
├── /run-production  (slash command)
├── [LFVA production mode + MMA M2 continuous]
├── Circuit breaker: max 3 fix loops per dimension
├── MMA M2 Deep Audit (target: >= 8.0)
└── [Human override if MMA fails after 3 loops]

SESSION 4 — T4: Perfecting
├── /run-polish  (slash command)
├── [HPE → Skeptic Avatar → NRA]
├── MMA M4 Compliance Gate (target: >= 9.0)
├── python session_state.py set current_phase done
├── SHIP_PACKAGE assembled
└── [Human final publish approval]
```

---

## 9. Architectural Gaps (Phase 0 Priorities)

The harness layer is built. The following components are specified in `REFACTOR_MIGRATION_PLAN_v1.4` as Phase 0 requirements — they must exist before the skill migration begins.

| Component | Status | Location | Purpose |
|-----------|--------|----------|---------|
| `tools/lint_skill.py` | NOT BUILT | Phase 0 | SkillML validator — checks structure, layer tags, SelfCheck |
| `tools/validate_ssot.py` | NOT BUILT | Phase 0 | SSOT schema validation against 6 templates |
| `tools/alias_resolver.py` | NOT BUILT | Phase 0 | Maps old skill names to canonical IDs |
| `tools/acceptance_tests.py` | NOT BUILT | Phase 0 | AT-01 through AT-10 measurable tests |
| `tools/manifest_builder.py` | NOT BUILT | Phase 0 | Auto-generates Zero-Point manifest from L1 descriptors |
| `orchestration/routing/aliases.yaml` | NOT BUILT | Phase 0 | 50-skill backward-compat alias map |
| `schemas/ssot/` | NOT BUILT | Phase 0 | 6 SSOT schemas (including ANGLE_SET, SKILL_ACTIVATION) |
| `schemas/skillml/skillml_spec.md` | NOT BUILT | Phase 0 | SkillML dialect rules |
| `skills/_templates/master_skill_template_v1.xml` | NOT BUILT | Phase 0 | Master template for multi-module KB skills |
| ZPWO v4.0 | NOT BUILT | Phase 1 | 4-track routing table (v3 Micro still runs 3-phase) |

### Skill Inventory Status
| Category | Count | Status |
|----------|-------|--------|
| Production-ready (proper XML) | 21 | Ready for normalization |
| Parse errors (encoding/structure) | ~30 | Need remediation |
| Not built (spec exists) | 11 | Build queue |

---

## 10. Tool Split Strategy

How the three environments divide the work:

| Environment | Best Used For |
|-------------|---------------|
| **Claude Code Terminal** | Skill normalization, git operations, batch processing, harness commands, parallel agent dispatch, phase transitions |
| **Claude Code Desktop** | File management, drag-drop skill organization, visual browsing of large skill library |
| **Browser Chat / Projects** | Strategy conversations, architecture decisions, copy drafting with full project context from Chat Projects |

The `memory/` framework and `KANBAN.json` are the handoff points between environments. Any environment can read current state and resume work.

---

## 11. The SUPERMIND / ULTRAMIND Relationship

| | ULTRAMIND | SUPERMIND |
|---|-----------|-----------|
| **Role** | Master, working copy, all skills | New architecture target |
| **Git Remote** | github.com/chrisflynnai-ux/Superskills | Same repo, SUPERMIND branch |
| **Skills** | 69 total, 21 production-ready | Normalizing from ULTRAMIND |
| **CLAUDE.md** | v3.0 ZPWO (3-phase) | v4.0 target (4-track) |
| **Workflow** | 3-Phase (Draft/Production/Polish) | 4-Track (Research/Drafts/Production/Perfecting) |
| **Status** | Active, authoritative | Transition target |

**Transition path:** All skill revision happens on ULTRAMIND. Once a skill passes SkillML validation and acceptance tests, it is promoted to SUPERMIND structure. ULTRAMIND is never deleted — it remains the working master.

---

## 12. Quick Reference Card

```bash
# --- ORIENTATION ---
python tools/scripts/canvas.py state          # Workflow status
python tools/scripts/canvas.py neurobox       # 6D architecture
python tools/scripts/session_state.py show    # Session memory

# --- SKILLS ---
python tools/scripts/skill_loader.py --list            # All skills
python tools/scripts/skill_loader.py mma --layer 1     # Load MMA L1 only
python tools/scripts/skill_loader.py copy_lfva --layer 2  # Load LFVA L1+L2

# --- CONDUCTOR ---
python tools/scripts/conductor.py status      # Kanban board
python tools/scripts/conductor.py teams       # Team compositions
python tools/scripts/conductor.py run         # Process next task
python tools/scripts/conductor.py add "title" --type vsl --priority high

# --- CMUX ---
python tools/scripts/cmux.py dispatch T2 "task description"
python tools/scripts/cmux.py parallel T2 T3 --task "task"
python tools/scripts/cmux.py chain "full funnel task"

# --- STATE ---
python tools/scripts/session_state.py load_skill copy_lfva
python tools/scripts/session_state.py set context_usage_pct 65
python tools/scripts/session_state.py gc      # Garbage collect at 70%

# --- GIT ---
cd "C:\Users\cfar7\OneDrive\Desktop\ULTRAMIND"
git add . && git commit -m "Daily: [description]" && git pull origin main --rebase && git push origin main

# --- TMUX (WSL) ---
wsl bash tools/scripts/tmux_setup.sh
```

---

## 13. Design Principles Encoded in This Architecture

Every component reflects a principle from your CLAUDE.md / ZPWO doctrine:

| Principle | Encoded In |
|-----------|-----------|
| **State > Chat** | SESSION_STATE.json as working memory, KANBAN.json as bus |
| **Light Center, Heavy Edges** | ZPWO ≤2000 tokens, skills carry their own execution context |
| **Generate Last** | skill_loader reads deterministically before LLM generates |
| **Two-Brain Teams** | Team lead + member composition in conductor.py |
| **Locked SSOT** | Checksum validation in session_state.py |
| **Garbage Collection** | `gc` command in session_state.py, canvas context meter |
| **Progressive Disclosure** | skill_loader L1-L4 layer extraction |
| **Circuit Breaker** | fix_loops counter in SESSION_STATE, max=3 in conductor |
| **ECR Learning** | insights.md as SIP log, human_corrected_events in state |

---

*Architecture Briefing v1.0 — 2026-03-04*
*Companion to: BUILD_SUMMARY_2026-03-04.md*
*Next review: After Phase 0 tooling is complete*

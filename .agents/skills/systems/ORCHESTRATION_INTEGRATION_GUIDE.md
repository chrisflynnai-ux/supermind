# ORCHESTRATION INTEGRATION GUIDE
## TWE ↔ ZPWO ↔ MMA Relationship

**Version:** 1.0.0  
**Updated:** 2026-01-07

---

## THE THREE ORCHESTRATION PILLARS

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      ULTRAMIND ORCHESTRATION LAYER                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                           ┌──────────────┐                                  │
│                           │     ZPWO     │                                  │
│                           │   (Master)   │                                  │
│                           │              │                                  │
│                           │ "What phase  │                                  │
│                           │  are we in?" │                                  │
│                           └──────┬───────┘                                  │
│                                  │                                          │
│                    ┌─────────────┼─────────────┐                           │
│                    │             │             │                           │
│                    ▼             │             ▼                           │
│           ┌──────────────┐      │      ┌──────────────┐                   │
│           │     TWE      │      │      │     MMA      │                   │
│           │   (Tools)    │      │      │  (Quality)   │                   │
│           │              │      │      │              │                   │
│           │ "What tools  │      │      │ "Is it good  │                   │
│           │  do we use?" │      │      │   enough?"   │                   │
│           └──────────────┘      │      └──────────────┘                   │
│                                 │                                          │
│                                 ▼                                          │
│                          ┌──────────────┐                                  │
│                          │   ASSETS     │                                  │
│                          │  (Output)    │                                  │
│                          └──────────────┘                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## ZPWO: THE MASTER ORCHESTRATOR

**Full Name:** Zero-Point Workflow Orchestrator  
**Role:** Master controller for all production workflows  
**Question It Answers:** "What phase are we in and what should happen next?"

### Responsibilities

1. **Phase Management** — Draft → Production → Polish
2. **Pod Coordination** — Which agents work on what
3. **SSOT Locking** — Stage A creates, Stage B consumes
4. **Circuit Breakers** — Prevents infinite loops
5. **Session State** — Tracks progress across runs

### ZPWO Delegates To:

| Delegate | When | Why |
|----------|------|-----|
| **TWE** | Toolchain decisions needed | ZPWO focuses on workflow, TWE focuses on tools |
| **MMA** | Quality validation needed | ZPWO doesn't judge quality, MMA does |
| **Sub-Agents** | Actual work needed | ZPWO orchestrates, doesn't execute |

---

## TWE: THE TOOLS ORCHESTRATOR

**Full Name:** Tools & Workflow Engineer  
**Role:** Design lean, reproducible tool workflows  
**Question It Answers:** "What tools should we use and how?"

### Core Principles (From Skill)

```xml
<Principle name="ZeroPoint">
  Keep the FLOW center light (minimal context); shift execution load to scripts, CLIs,
  and narrowly-scoped tool calls invoked on-demand.
</Principle>

<Principle name="HealAndRenew">
  Every run outputs a correction log and a patch proposal pathway (system learns).
</Principle>
```

### TWE Outputs

| Output | Purpose |
|--------|---------|
| **WORKFLOW_PLAN** | What steps in what order |
| **TOOLCHAIN_PLAN** | Which tools for which steps |
| **RUNBOOK** | Reproducible instructions |
| **SCRIPT_CALL_SPECS** | Exact tool invocations |
| **CORRECTION_LOG** | What went wrong |
| **PATCH_PROPOSALS** | How to improve |

### TWE Alignment with 6D Model

| TWE Principle | 6D Mapping |
|---------------|------------|
| Zero-Point / FLOW | CENTER: SOUL/TRANSFORM |
| Heal & Renew | AXIS A: BODY-HEART |
| 3-Phase Waveforms | 7F Chain: FILTER→FORGE |
| Dual-Brain Pods | 3 Axes: Left/Right poles |
| Two-Stage SSOT | Stage A→B locking |

---

## MMA: THE QUALITY GUARDIAN

**Full Name:** Master Monitor Agent  
**Role:** 7-dimensional quality validation  
**Question It Answers:** "Is this good enough to ship?"

### The 7 Dimensions

```
D = Dimensional Balance (6D axis alignment)
I = Information Integrity (proof discipline)
M = Mechanism Clarity (does it make sense?)
E = Emotional Resonance (does it feel right?)
N = Narrative Coherence (does the story flow?)
S = Strategic Alignment (does it match strategy?)
I = Implementation Quality (is it well-crafted?)
O = Overall Resonance (the gestalt)
N = eNhancement Potential (can it be better?)

→ DIMENSION (7D scoring)

A = Architecture (Zero-Point compliance)
E = Evolution (Heal & Renew outputs)

→ TOTAL: 7D + A + E = Full Quality Assessment
```

### MMA Routing Decisions

```
IF score < 7.0 in any dimension → FAIL (send back)
IF score >= 7.0 but < 8.5 → CONDITIONAL PASS (notes)
IF score >= 8.5 all dimensions → FULL PASS (ship it)
```

---

## THE INTEGRATION FLOW

### Example: Building an Advertorial

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  1. USER REQUEST: "Create advertorial for Sleep Energy Breakthrough"        │
│                                                                              │
│  2. ZPWO ACTIVATES                                                          │
│     └── Determines: Phase 1 (Draft) needed                                  │
│     └── Checks: SSOT objects available? (PB, MS, EP, VG)                   │
│     └── Delegates to TWE: "What tools for advertorial drafting?"           │
│                                                                              │
│  3. TWE PLANS                                                               │
│     └── Returns TOOLCHAIN_PLAN:                                            │
│         - Primary: advertorial_copy_master.xml                              │
│         - Support: master_writing_partner.xml (polish)                      │
│         - Validation: python_validator.py (schema check)                   │
│     └── Returns RUNBOOK with exact steps                                    │
│                                                                              │
│  4. ZPWO EXECUTES                                                           │
│     └── Activates Draft Pod (P1)                                           │
│     └── Loads advertorial_copy_master (on-demand, not always-on)           │
│     └── Generates 3-5 angle drafts                                          │
│     └── Snapshots WORKFLOW_STATE                                           │
│                                                                              │
│  5. ZPWO TRANSITIONS TO P2 (Production)                                     │
│     └── Best angle selected                                                 │
│     └── Production loop begins                                              │
│     └── Calls MMA: "Validate this draft"                                   │
│                                                                              │
│  6. MMA VALIDATES                                                           │
│     └── Scores all 7 dimensions                                            │
│     └── Returns: "CONDITIONAL PASS - SMART dimension weak (6.8)"           │
│     └── Recommendation: "Strengthen mechanism explanation"                  │
│                                                                              │
│  7. ZPWO LOOPS (Max 3 cycles)                                               │
│     └── Sends back to production pod with MMA notes                        │
│     └── Revised draft returns                                               │
│     └── Calls MMA again                                                     │
│     └── MMA: "FULL PASS - 8.7 average"                                     │
│                                                                              │
│  8. ZPWO TRANSITIONS TO P3 (Polish)                                         │
│     └── Loads master_writing_partner                                        │
│     └── Voice consistency pass                                              │
│     └── Kitchen table test                                                  │
│     └── Final MMA validation                                                │
│                                                                              │
│  9. TWE LOGS                                                                │
│     └── CORRECTION_LOG: "First draft needed mechanism work"                │
│     └── PATCH_PROPOSAL: "Add mechanism checklist to advertorial skill"     │
│                                                                              │
│  10. ZPWO COMPLETES                                                         │
│      └── Final WORKFLOW_STATE snapshot                                      │
│      └── Asset delivered to outputs/                                        │
│      └── Returns to ZERO-POINT                                              │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## WHEN TO USE EACH

| Situation | Use | Why |
|-----------|-----|-----|
| "Start a new asset" | ZPWO | Needs phase orchestration |
| "What tools should we use?" | TWE | Toolchain expertise |
| "Is this draft good?" | MMA | Quality judgment |
| "Why did this fail?" | TWE | Has CORRECTION_LOG |
| "What's next?" | ZPWO | Tracks WORKFLOW_STATE |
| "Should we ship this?" | MMA + ZPWO | MMA validates, ZPWO decides |

---

## THE ZERO-POINT DANCE

All three maintain **Zero-Point Context Discipline**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                                                                              │
│  DEFAULT STATE (Zero-Point):                                                │
│  ├── ZPWO: Phase awareness + SSOT headers only                             │
│  ├── TWE: Tool index only (not full schemas)                               │
│  └── MMA: Dimension thresholds only                                         │
│                                                                              │
│  ACTIVATED STATE (Temporary):                                               │
│  ├── ZPWO: Full workflow state loaded                                       │
│  ├── TWE: Relevant skill + scripts loaded                                  │
│  └── MMA: Full validation rules loaded                                      │
│                                                                              │
│  AFTER ACTION:                                                              │
│  └── Return to Zero-Point, compress outputs to SSOT                        │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## RELATED HUMAN TOOLS

These orchestration skills have human-facing counterparts:

| Agent Tool | Human Tool | Relationship |
|------------|------------|--------------|
| TWE (Tools & Workflow Engineer) | Tools & Workflow Manager v2.0 | TWE executes, Manager tracks |
| ZPWO (Zero-Point Workflow Orchestrator) | — | Direct agent control |
| MMA (Master Monitor Agent) | — | Direct quality validation |

**Note:** Tools & Workflow Manager (Human Dashboard) tracks what TWE does, but doesn't replace it. The Manager is for YOU to see status; TWE is for CLAUDE to execute tool workflows.

---

## SUMMARY

```
ZPWO = "Conductor" — Orchestrates the phases
TWE  = "Stagehand" — Sets up the tools
MMA  = "Critic"    — Judges the output

All three respect Zero-Point discipline.
All three support Heal & Renew.
All three serve the 6D Agentic Super-Resonance Model.
```

---

*Orchestration Integration Guide v1.0*
*ZPWO + TWE + MMA = Production Excellence*

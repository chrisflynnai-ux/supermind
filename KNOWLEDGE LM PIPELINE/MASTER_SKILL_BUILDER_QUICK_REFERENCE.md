# MASTER SKILL BUILDER — QUICK REFERENCE CARD

## The Pipeline (3 Stages)

```
NotebookLM (Free)  →  Prism GPT-5.2 (Free)  →  Claude Opus 4.5
   EXTRACT              SYNTHESIZE              POLISH
   
   Themes               SKILL.md                XML Skill
   Patterns             implementation.py       Tests  
   Zero-Point           flowgram.mmd            Deployment
   Hierarchy            zero_point.json         Sign-off
```

---

## Quick Commands

| Command | Action |
|---------|--------|
| `New skill: [topic]` | Start creation |
| `Refine: [skill]` | Start refinement |
| `Pipeline: extraction` | NotebookLM template |
| `Pipeline: synthesis` | Prism template |
| `Pipeline: polish` | Claude template |
| `Status` | Current builds |
| `Validate: [skill]` | Production check |

---

## Complexity Tracks

| Track | Time | Sources | Flow |
|-------|------|---------|------|
| **Simple** | 1-2h | <10 | Quick extract → Direct synthesis |
| **Standard** | 4-6h | 10-30 | Full pipeline (1 notebook) |
| **Complex** | 8-12h | 30-50 | Full pipeline (2-3 notebooks) |
| **Modular** | 16h+ | 50-100+ | Per-module pipeline + orchestrator |

---

## Skill Domains

```
meta     = Orchestration (ZPWO, MMA, TWA)
copy     = Persuasion (SCD, HPE, ACM)
product  = Offers (PCG, TEA, QIPB)
research = Analysis (MIS, Framework Extractor)
design   = Visual (SDM, Image Planner)
tools    = Execution (Web Intel, Repo Ops)
```

---

## Quality Gates

### Constitution v2.1
- [ ] Zero-Point < 100 tokens
- [ ] Skills > MCPs
- [ ] Self-annealing (@retry)
- [ ] SSOT integration

### Lean Stack v2.0
- [ ] Correct domain
- [ ] Progressive disclosure (L1-L4)
- [ ] Tool index compatible

### Code Quality
- [ ] Pydantic models
- [ ] Type hints
- [ ] CLI interface
- [ ] Tests passing

---

## Version Incrementing

| Change Type | Example | Rule |
|-------------|---------|------|
| Bug fix | 1.0.0 → 1.0.1 | Patch |
| New feature | 1.0.0 → 1.1.0 | Minor |
| Breaking change | 1.0.0 → 2.0.0 | Major |

---

## Skill Bundle Structure

```
/skills/[name]/
├── SKILL.md           # Documentation
├── implementation.py  # Code
├── flowgram.mmd       # Visual
├── zero_point.json    # Index
├── tests/
│   └── test_implementation.py
└── docs/
    └── learned_constraints.md
```

---

## Architectural Rules

1. **80% Rule** — Replace MCPs with Skills
2. **10-to-1 Rule** — Cluster 10 nodes → 1 function
3. **Sandbox Filtering** — Return summaries only
4. **Package-First** — Use official SDKs
5. **Self-Annealing** — @retry with backoff

---

## Status Codes

```
discovery    → Identified, not started
extracting   → Stage 1 in progress
synthesizing → Stage 2 in progress
polishing    → Stage 3 in progress
testing      → Pre-deployment
production   → Live
deprecated   → Sunset planned
archived     → Retired
```

---

## Refinement Workflows

| Code | Type | Version |
|------|------|---------|
| R1 | Bug Fix | Patch |
| R2 | Add Feature | Minor |
| R3 | Major Upgrade | Major |
| R4 | Deprecation | N/A |

---

*Knowledge → Intelligence → Autonomy*

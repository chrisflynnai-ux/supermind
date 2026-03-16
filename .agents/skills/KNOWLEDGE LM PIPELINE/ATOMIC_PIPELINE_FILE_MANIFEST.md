# ATOMIC PIPELINE FILE MANIFEST
## What's Current vs. Deprecated

**Updated:** 2026-01-30  
**Pipeline Version:** Atomic Knowledge Synthesis v2.0

---

## ✅ CURRENT FILES (Use These)

### Core Pipeline
| File | Purpose | Location |
|------|---------|----------|
| **ATOMIC_KNOWLEDGE_SYNTHESIS_PIPELINE_v2.md** | Master pipeline architecture | `/outputs/` |
| **ATOMIC_PIPELINE_QUICK_REFERENCE.md** | One-page cheat sheet | `/outputs/` |
| **SEQUENTIAL_EXTRACTION_PROTOCOL.md** | 40+ page module extraction | `/outputs/` |

### Templates (Still Valid)
| File | Purpose | Location |
|------|---------|----------|
| **CLAUDE_POLISH_TEMPLATE.md** | Layer 3 synthesis/polish | `/outputs/templates/` |

### Project Instructions
| File | Purpose | Project |
|------|---------|---------|
| **MASTER_SKILL_BUILDER_PROJECT_INSTRUCTIONS.md** | Skill factory hub | Master Skill Builder |
| **MASTER_SKILL_BUILDER_QUICK_REFERENCE.md** | Quick reference | Master Skill Builder |
| **MAA_PIPELINE_QUICK_START.md** | MAA-specific guide | Tools & Workflow |
| **DESIGN_SKILLS_PROJECT_INSTRUCTIONS.md** | Multi-model design | Design Skills |
| **DESIGN_SKILLS_PIPELINE_QUICK_START.md** | Design quick start | Design Skills |

---

## ⚠️ DEPRECATED FILES (Don't Use)

| File | Why Deprecated | Replaced By |
|------|----------------|-------------|
| `DEPRECATED_KNOWLEDGE_REFINERY_PIPELINE_v1.md` | Incorrectly included Prism | `ATOMIC_KNOWLEDGE_SYNTHESIS_PIPELINE_v2.md` |
| `DEPRECATED_PRISM_SYNTHESIS_TEMPLATE.md` | Prism is LaTeX-centric, not for skills | `SEQUENTIAL_EXTRACTION_PROTOCOL.md` |
| `DEPRECATED_NOTEBOOKLM_EXTRACTION_TEMPLATE_v1.md` | Mega-prompt approach causes tool tax | `SEQUENTIAL_EXTRACTION_PROTOCOL.md` |

---

## THE CORRECT PIPELINE (v2.0)

```
LAYER 1: SKILL ATOMS (Sequential Extraction)
    │
    │  Use: SEQUENTIAL_EXTRACTION_PROTOCOL.md
    │  7 runs by category (heuristics, specs, failures, etc.)
    │
    ▼
LAYER 2: NOTEBOOKLM ROUTER
    │
    │  Upload atoms as sources
    │  Query, cross-link, cluster
    │
    ▼
LAYER 3: CLAUDE SYNTHESIZER
    │
    │  Use: CLAUDE_POLISH_TEMPLATE.md (still valid)
    │  Compile into Double-II bundle
    │
    ▼
OUTPUT: Production LCP Skill Bundle
```

---

## QUICK REFERENCE: What To Use When

| Task | Use This File |
|------|---------------|
| **Understanding the pipeline** | `ATOMIC_KNOWLEDGE_SYNTHESIS_PIPELINE_v2.md` |
| **Extracting from 40+ page sources** | `SEQUENTIAL_EXTRACTION_PROTOCOL.md` |
| **Quick pipeline overview** | `ATOMIC_PIPELINE_QUICK_REFERENCE.md` |
| **Final Claude polish/synthesis** | `CLAUDE_POLISH_TEMPLATE.md` |
| **MAA module builds** | `MAA_PIPELINE_QUICK_START.md` |
| **Design skill builds** | `DESIGN_SKILLS_PIPELINE_QUICK_START.md` |
| **New skill creation** | `MASTER_SKILL_BUILDER_PROJECT_INSTRUCTIONS.md` |

---

## FILE TREE (Current State)

```
/mnt/user-data/outputs/
│
├── ✅ ATOMIC_KNOWLEDGE_SYNTHESIS_PIPELINE_v2.md  (USE)
├── ✅ ATOMIC_PIPELINE_QUICK_REFERENCE.md         (USE)
├── ✅ SEQUENTIAL_EXTRACTION_PROTOCOL.md          (USE)
│
├── ✅ MASTER_SKILL_BUILDER_PROJECT_INSTRUCTIONS.md
├── ✅ MASTER_SKILL_BUILDER_QUICK_REFERENCE.md
├── ✅ MAA_PIPELINE_QUICK_START.md
├── ✅ DESIGN_SKILLS_PROJECT_INSTRUCTIONS.md
├── ✅ DESIGN_SKILLS_PIPELINE_QUICK_START.md
│
├── ⚠️ DEPRECATED_KNOWLEDGE_REFINERY_PIPELINE_v1.md
│
└── templates/
    ├── ✅ CLAUDE_POLISH_TEMPLATE.md              (USE)
    ├── ⚠️ DEPRECATED_PRISM_SYNTHESIS_TEMPLATE.md
    └── ⚠️ DEPRECATED_NOTEBOOKLM_EXTRACTION_TEMPLATE_v1.md
```

---

## WHY THE CHANGE?

### v1.0 Problems:
1. **Prism** is LaTeX-centric (for scientific papers, not skills)
2. **Mega-prompts** overload NotebookLM ("tool tax")
3. **Large extractions** degrade quality

### v2.0 Solutions:
1. **NotebookLM as Router** — not synthesizer
2. **Atomic extraction** — small, reusable units
3. **Sequential protocol** — 7 category-focused runs
4. **Claude as Synthesizer** — heavy lifting where it excels

---

*Atomic Pipeline File Manifest*  
*"Lego bricks, not monoliths"*

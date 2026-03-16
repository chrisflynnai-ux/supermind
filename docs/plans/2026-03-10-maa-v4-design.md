# Master Automations Architect v4.0.0 — Design Document

**Date:** 2026-03-10
**Status:** Approved for implementation
**Artifact:** `automations_master_architect_v4_0_0.xml`
**Location:** `.agents/skills/automations/`
**Format:** SkillML V1.4 XML

---

## 1. Purpose

The Master Automations Architect (MAA) is the doctrine hub and control surface for the SUPERMIND automation ecosystem. It classifies automation requests, selects tool/execution topologies, designs typed contracts for downstream builders, specifies visual Flowgrams, and manages self-improvement loops.

**It does NOT execute.** It architects.

**Platform Enhancer Positioning:** MAA makes Claude better at designing automation architectures by providing structured doctrine, anti-patterns, and typed contracts.

---

## 2. Architecture: Hub + Spokes

MAA is the doctrine hub. Downstream modules (M2-M8) are spoke skills that plug in via typed contracts.

```
                    ┌──────────────────────┐
                    │   MAA v4.0.0 (Hub)   │
                    │  Doctrine + Control   │
                    └──────────┬───────────┘
           ┌───────────┬──────┼──────┬───────────┐
           ▼           ▼      ▼      ▼           ▼
     ┌──────────┐ ┌────────┐ ┌────┐ ┌──────┐ ┌──────┐
     │ M2       │ │ M3     │ │ M4 │ │ M5   │ │M6-M8│
     │ Builder  │ │ Trans. │ │Brow│ │Cont. │ │ ... │
     └──────────┘ └────────┘ └────┘ └──────┘ └──────┘
```

- Spokes connect via typed contracts, not inheritance
- Each spoke can be built/upgraded independently
- MAA reviews all automation-family skills for doctrine compliance

---

## 3. Progressive Disclosure Layers

### L1: Zero-Point (~600 tokens, always loaded)
Ultra-compressed identity, tool topology tiers, anti-pattern sentinel, contract list, seam declarations. Enough for MAA to classify any request and decide what to load next.

### L2: Core Doctrine (loaded on classification + blueprint tasks)
- Request Classification Engine (complexity x domain x autonomy)
- 5-Tier Tool Topology (T0 Deterministic through T4 Multi-Agent Composition)
- 12 Core Heuristics (preserved and upgraded from M1 V1.1)
- 10 Anti-Patterns (preserved and upgraded)
- Relational Operations (delegates_to, depends_on, complements, reviews)

### L3: Advanced Patterns (loaded on complex design tasks)
- Sub-Domain Pack Architecture (internal routers, compartmentalized expertise, agent spawning)
- Lean Team Orchestration Model (1-3 specialists + orchestrator, 4-track cycling with clock)
- Blueprint Design Patterns (Pipeline, Fan-Out/Fan-In, Event-Driven, Living System, Hybrid)
- Flowgram Specification System (Excalidraw primary, Mermaid terminal, Draw.io secondary)
- 3-Phase Document Intelligence (Parallel Scan, Deep Dive, Backtrack)
- Living Systems Patterns (Generator/Reflector/Curator, Recursive Annealing)

### L4: Technical Specifications (loaded for implementation details)
- Memory Seam Declarations (hot/warm/cold, backend-agnostic)
- SkillML V1.4 XML Structure template
- Contract Schemas (inputs, outputs, validation, error handling, idempotency)
- Multi-Model Routing Seams (Claude primary, Gemini secondary, Codex tertiary)
- Skill Taxonomy Integration (Superskills, Production Skills, Light Skills)
- ACP Seam Specification (future agent communication protocol)

---

## 4. Output Contracts (6 required + 2 seams)

### Required Contracts

| Contract | Purpose | Consumer |
|----------|---------|----------|
| AUTOMATION_BLUEPRINT | Full architecture spec | Builder (M2) |
| FLOWGRAM_SPEC | Visual workflow spec (Excalidraw-first) | Human review + Builder |
| HANDOFF_PACKAGE | Typed delivery spec for spoke skills | Any spoke module |
| PATCH_REQUEST | Structured improvement request | Patch Registry |
| MEMORY_SEAM_NOTE | What to remember, at what temperature | Future memory layer |
| LEARNING_ARTIFACT | Post-execution reflection | Learning system |

### Future Contract Seams (declared, not built)

| Seam | Purpose |
|------|---------|
| ACP_MESSAGE | Agent Communication Protocol for team messaging |
| SKILL_EVAL_REQUEST | 19-check SkillML validation request |

---

## 5. Relational Operations

```yaml
delegates_to:
  - automations_builder (M2): AUTOMATION_BLUEPRINT + HANDOFF_PACKAGE
  - workflow_translator (M3): FLOWGRAM_SPEC + translation requests
  - browser_orchestrator (M4): browser-specific HANDOFF_PACKAGE
  - content_analyzer (M5): content analysis HANDOFF_PACKAGE
  - outreach_orchestrator (M6): outreach HANDOFF_PACKAGE

depends_on:
  - meta_mma: quality validation (7D scoring)
  - future_memory_layer: pattern retrieval, session state
  - future_skill_evaluator: 19-check validation

complements:
  - meta_skill_builder: MAA designs, skill_builder scaffolds
  - power_trio_router: MAA governs automation domain, PTR routes all domains

reviews:
  - all spoke skills: doctrine compliance checks
```

---

## 6. Key Design Decisions

1. **Hub + Spokes over Flat Modules** — MAA is the governance center, not one of eight equal modules
2. **5 Tiers over 3 Tiers** — added T3 (autonomous execution) and T4 (multi-agent composition) to the original tool topology
3. **Sub-Domain Packs** — skills contain compartmentalized expertise that can be loaded individually or spawned as sub-agents
4. **Lean Teams (1-3 + orchestrator)** — no agent swarms; orchestrator cycles across 4 tracks with a clock mechanism
5. **ACP as Seam** — declared but not implemented; defers to harness selection
6. **Living Systems** — automations can self-improve via Generator/Reflector/Curator but always generate PATCH_REQUEST (no auto-apply)
7. **Excalidraw-First Flowgrams** — aesthetically pleasing diagrams that are both human-readable and machine-parseable
8. **Platform Enhancement** — MAA makes Claude better at automation design, not replace it

---

## 7. What Is Preserved from Modules 1-3

- Anti-pattern logic from M1 (upgraded to 10 patterns)
- Tool-choice heuristics from M1 (upgraded to 12 heuristics)
- Builder handoff logic from M2 (formalized as HANDOFF_PACKAGE contract)
- Workflow decomposition from M3 (integrated into classification engine)
- Lean Context Protocol / Double-II Framework
- Skills + Scripts > MCPs principle
- Self-healing / recursive annealing patterns

---

## 8. What Is Discarded or Reframed

- Flat 8-module framing (replaced by Hub + Spokes)
- SKILL.md as primary artifact (replaced by SkillML V1.4 XML)
- Old 3-phase orchestration language (replaced by 4-track model)
- Overly specific model routing names (replaced by harness-agnostic seams)
- Premature memory backend commitment (replaced by memory seams)
- LCP token target as hard limit (preserved as guidance, not dogma)

---

## 9. Companion Files (optional, created if needed during build)

- `AUTOMATION_CONTRACTS_V4.md` — detailed contract schemas
- `FLOWGRAM_VISUAL_CONTRACT_V4.md` — Flowgram node model and sync rules
- `MAA_RELATIONAL_OPS_V4.yaml` — full relational graph for automation family

---

## 10. Post-Build Actions

1. Run NotebookLM Enhancement Query Pack (clusters A-E)
2. Validate against Skill Evaluator criteria (19 checks)
3. Determine whether M4/M5 archives should be mined for second pass
4. Update PATCH_REGISTRY_V4.yaml to mark automations_patch_002 as applied
5. Update memory files with new MAA status

---

## 11. Definition of Done

- [ ] XML file parses as valid SkillML V1.4
- [ ] All 6 contracts are defined with typed schemas
- [ ] All 2 future seams are declared
- [ ] Relational ops are explicit (delegates_to, depends_on, complements, reviews)
- [ ] Progressive disclosure L1-L4 is implemented
- [ ] 12 heuristics and 10 anti-patterns are embedded
- [ ] Memory seams are declared (hot/warm/cold)
- [ ] Skill Evaluator hook is present
- [ ] MMA quality gates are integrated
- [ ] Flowgram direction is specified (Excalidraw primary)
- [ ] Master prompt covers the 10-step classification-to-delivery flow
- [ ] No SKILL.md output, no old 3-phase language, no harness lock-in

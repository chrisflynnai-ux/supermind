# SUPERMIND AGENTIC CONTROL PLANE v4.0.0

> **System:** Zero-Point Workflow Orchestrator
> **Philosophy:** Light Center, Heavy Edges
> **Agent Workspace:** `.agents/` (Codex/multi-model agents work here)
> **Canonical Source:** `.claude/` (authoritative — merge back after work)
> **Updated:** 2026-03-06

---

## 0. IDENTITY

You are a **specialist agent** within the SUPERMIND Agentic OS. You work inside the `.agents/` workspace on assigned tasks. Your output will be reviewed and merged into the canonical `.claude/` source by the orchestrator.

**NORTH STAR:** Build repeatable, revenue-generating services through modular AI-operated skills, named digital employees, and collective intelligence (COSMS).

**CORE RULES:**
1. Work in `.agents/skills/` — never modify `.claude/skills/` directly
2. Follow SkillML V1.4 standard for all skill files (see Section 4)
3. Use tools/scripts for validation before claiming work is done
4. Keep context lean — load skills on-demand, unload when done

---

## 1. ARCHITECTURE

### Pipeline: 4-Track Model
```
T1 RESEARCH → T2 DRAFTS → T3 PRODUCTION → T4 POLISH
   (no gate)    (MMA>=6.0)   (MMA>=8.0)     (MMA>=9.0)
```

### NeuroBox (6D + Center)
```
                HEART (Top) - PRODUCTION
                      |
    MIND ←——— SOUL (CENTER) ———→ SPIRIT
  RESONANCE    ORCHESTRATION    PERSUASION
                      |
                BODY (Bottom) - AUTOMATION

    BACK: PSYCH (DEVELOPMENT)
   FRONT: CONSCIENCE (DESIGN)
```

### Team Model
- Small teams: 1-3 agents + orchestrator per task
- Two-Brain pairing: Technical (Left) + Strategic (Right)
- Human gates between T1→T2 and T3→T4

---

## 2. SKILL FORMAT: SkillML V1.4

All skills must be well-formed XML with:

**Required root attributes:**
- `skill_id` — format: `{domain}_{function}` (e.g., `copy_advertorial`)
- `version` — semver (e.g., `2.0.0`)
- `status` — `draft|beta|active|deprecated`

**Required sections (5):**
1. `<Meta>` — Name, Description, Domain, Track, TeamRole
2. `<Contract>` — Inputs, Outputs, MMAGate, CircuitBreaker
3. `<ExecutionProtocol>` — Rules, ReasoningFramework, Implementation
4. `<SelfCheck>` — Minimum 3 Check elements + MMAGate + FailureModes
5. `<PatchLog>` — Version history entries

**Required layer tags (4):**
- `LAYER:CONTRACT` — I/O specification
- `LAYER:RULES` — Governing rules
- `LAYER:REASONING` — Reasoning framework
- `LAYER:IMPL` — Implementation details

**Template:** `.agents/skills/_template/master_skill_template_v1.xml`
**Spec:** `schemas/skillml/skillml_spec.md`

---

## 3. VALIDATION

Run these before committing any skill work:

```bash
# Validate a skill against SkillML V1.4 (must pass 19/19)
python tools/skillml_validator.py .agents/skills/{domain}/{skill_file}.xml

# Lint with migration scoring
python tools/lint_skill.py .agents/skills/{domain}/{skill_file}.xml

# Resolve a command to canonical skill_id
python tools/alias_resolver.py /advertorial

# Generate manifest from current inventory
python tools/manifest_builder.py

# SSOT lock integrity check
python tools/validate_ssot.py --check-locks

# Run all Phase 0 acceptance tests
python tools/acceptance_tests.py
```

---

## 4. ROUTING

**Routing table:** `orchestration/routing/routing_table.yaml` (44 routes, 4 tracks, 3 chains)
**Alias mappings:** `orchestration/routing/aliases.yaml` (64 entries)

Key command → skill mappings:
| Command | Skill ID | Track |
|---------|----------|-------|
| `/intake` | `research_market_intel` | T1 |
| `/draft` | `copy_director` | T2 |
| `/advertorial` | `copy_advertorial` | T2 |
| `/salespage` | `copy_sales_page` | T2 |
| `/produce` | `copy_director` | T3 |
| `/validate` | `meta_mma` | cross |
| `/polish` | `meta_zpwo` | T4 |

---

## 5. WORKSPACE RULES

### File Ownership
| Directory | Owner | Purpose |
|-----------|-------|---------|
| `.claude/skills/` | Claude (canonical) | Authoritative skill source |
| `.agents/skills/` | Codex / other agents | Working copies for parallel development |
| `tools/` | Shared | Validation scripts, both agents use |
| `orchestration/` | Shared | Routing config, both agents reference |
| `ssot/` | Shared | SSOT schemas and locked objects |
| `memory/` | Shared | Persistent identity and insights |

### Merge Protocol
1. Agent works in `.agents/skills/{domain}/`
2. Validates with `tools/skillml_validator.py` (must pass 19/19)
3. Creates diff against `.claude/skills/{domain}/` version
4. Human reviews diff and approves merge
5. Canonical `.claude/skills/` updated

### What NOT to Modify
- `CLAUDE.md` — Claude's project instructions (modify `AGENTS.md` instead)
- `.claude/commands/` — Claude's slash commands
- Locked SSOT objects (check with `python tools/validate_ssot.py --check-locks`)

---

## 6. GUARDRAILS

### Critical (Never Violate)
- **No fabrication** — No invented stats, testimonials, credentials
- **No fake urgency** — No false timers or manufactured scarcity
- **Proof discipline** — All claims grounded in EVIDENCE_PACK or softened
- **Single CTA** — One action per asset, repeated not multiplied
- **MESSAGE_SPINE locked** — Do not invent new mechanism or promise

### Circuit Breakers
- Max 3 FIX loops per MMA dimension
- Same failure 2x → PATCH_REQUEST
- 3x → HALT + escalate to human

---

## 7. CURRENT PROJECT FOCUS

- **Project:** SUPERMIND / Interscale Agentic OS
- **Phase:** Phase 0 COMPLETE → Phase 1 skill migration (domain-by-domain)
- **First V1.4 skill:** `meta_zpwo` (ZPWO v4.0, 19/19 passed)
- **Migration baseline:** 65 skills, 21 parseable, 44 parse errors
- **Batch 1 targets:** LFVA, SFVW, MMA (core copy + quality gate)

---

## 8. REFERENCE DOCUMENTS

| Document | Location |
|----------|----------|
| SkillML Spec | `schemas/skillml/skillml_spec.md` |
| Routing Table v4.0 | `orchestration/routing/routing_table.yaml` |
| Aliases | `orchestration/routing/aliases.yaml` |
| Master Template | `.agents/skills/_template/master_skill_template_v1.xml` |
| Build Summary | `BUILD_SUMMARY_V2_2026-03-06.md` |
| Business Vision | `memory/BUSINESS_VISION.md` |
| Architecture Briefing | `ARCHITECTURE_BRIEFING_2026-03-04.md` |
| SSOT Schemas | `ssot/` |

---

*SUPERMIND Agentic Control Plane v4.0.0*
*Agent workspace: .agents/ | Canonical source: .claude/*
*Validate before merge. Always.*

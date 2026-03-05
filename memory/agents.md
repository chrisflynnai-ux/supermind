# SUPERMIND Agents Registry

> Master skills with prompt injection capability to spawn sub-agents.
> These are the orchestrators and team leads in the SUPERMIND system.

---

## Tier 1: Meta-Orchestrators

### ZPWO - Zero-Point Workflow Orchestrator
- **ID:** `skill.meta.zpwo.v3_0_0_micro`
- **Role:** Central coordinator, routes tasks to tracks
- **Spawns:** Any skill based on command routing
- **Load Cost:** High (L1: 400, L2: 1500, L3: 1000, L4: 600)
- **Status:** Production

### MMA - Master Monitor Agent
- **ID:** `skill.validation.mma_master_monitor_agent.v1_0_0`
- **Role:** Quality guardian, 7D scoring, fix routing
- **Spawns:** Specialist skills for fixes
- **Load Cost:** Medium
- **Status:** Production

---

## Tier 2: Track Leaders

### T1 - Research Team Lead
- **Agent:** Market Scout
- **ID:** `skill.market_scout.v1_2_0`
- **Spawns:** research_ops, mis
- **Gate:** Human approval of SSOTs

### T2 - Draft Team Lead
- **Agent:** Copy Lead
- **ID:** `skill.copy_lead.v1_0_0`
- **Spawns:** copy_director -> assigned_specialist
- **Gate:** Human + MMA M1 >= 7.0

### T3 - Production Team Lead
- **Agent:** Active Specialist (from T2)
- **Spawns:** MMA for validation
- **Gate:** MMA M2 >= 8.0

### T4 - Perfecting Team Lead
- **Agent:** Human Persuasion Editor (HPE)
- **Spawns:** skeptic_avatar, nra
- **Gate:** MMA M4 >= 9.0 + human final

---

## Tier 3: Domain Specialists

### Copy Domain
| Agent | ID | Specialization |
|-------|-----|----------------|
| Copy Director | `skill.copy_director.v3_0_0` | Strategic direction, angle selection |
| LFVA | `skill.copy.long_form_vsl_script_architect.v3_0_0` | 10-20min VSL scripts |
| SFVW | `skill.copy.short_form_vsl_script_writer.v3_0_0` | 2-5min VSL scripts |
| HPE | `human_persuasion_editor` | Voice polish, AI detox |
| NRA | `neuro_resonance_auditor` | 6D axis balance |

### Research Domain
| Agent | ID | Specialization |
|-------|-----|----------------|
| Market Scout | `skill.market_scout.v1_2_0` | Intelligence gathering |
| Research Ops | `skill.research_ops.v1_0_0` | Research execution |
| MIS | `skill.market_intelligence_synthesizer.v2_1_0` | Synthesis |

### Product Domain
| Agent | ID | Specialization |
|-------|-----|----------------|
| Product Creation | `skill.product_creation_genius.v2_0_0` | End-to-end products |
| Offer Architect | `skill.offer_architect.v2_0_0` | Value equation, pricing |

---

## Prompt Injection Protocol

Master agents can spawn sub-agents using Claude Code's Task tool:

```python
# Example: Copy Director spawns LFVA
{
    "description": "T2 VSL Draft",
    "prompt": "[skill context + task]",
    "subagent_type": "general-purpose",
    "model": "opus"
}
```

**Rules:**
1. Parent passes relevant SSOTs to child
2. Child returns artifacts + MMA scorecard
3. Parent updates kanban with results
4. Circuit breaker: max 3 spawns per issue

---

*Updated: 2026-03-04*

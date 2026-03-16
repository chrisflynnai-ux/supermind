# ULTRAMIND SKILL FRAMEWORK v3.0
## Unified Architecture: Agent-Centric + Skill-Centric + Pipeline Integration

**Version:** 3.0.0  
**Date:** 2026-01-30  
**Status:** Framework Patch / Upgrade  
**Merges:** SKILL_ARCHITECT_v2 + SKILL_TEMPLATE_V2.xml + Knowledge Refinery Pipeline

---

## EXECUTIVE SUMMARY

This framework unifies three architectural patterns:

| Pattern | Source | Strength |
|---------|--------|----------|
| **Agent-Centric** | SKILL_ARCHITECT_v2 | Orchestrator + specialists, voice/ICP/business profiles |
| **Skill-Centric** | SKILL_TEMPLATE_V2.xml | Progressive disclosure (L1-L4), MOD routing, MMA quality gates |
| **Pipeline-Centric** | Knowledge Refinery | 3-stage extraction → synthesis → polish |

**Result:** A complete skill manufacturing system where:
- **Profiles** provide context (WHO we serve, HOW we sound)
- **Skills** provide capability (WHAT we do)
- **Agents** provide orchestration (HOW we coordinate)
- **Pipeline** provides manufacturing (HOW we build)

---

## ARCHITECTURE DIAGRAM

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    ULTRAMIND SKILL FRAMEWORK v3.0                               │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   LAYER 1: CONTEXT PROFILES (Always Loaded)                                    │
│   ─────────────────────────────────────────                                    │
│   ┌─────────────┐ ┌─────────────┐ ┌─────────────┐ ┌─────────────┐            │
│   │ voice_dna   │ │    icp      │ │  business   │ │ zero_point  │            │
│   │   .json     │ │   .json     │ │   .json     │ │   .json     │            │
│   │             │ │             │ │             │ │             │            │
│   │ HOW we      │ │ WHO we      │ │ WHAT we     │ │ Skill       │            │
│   │ sound       │ │ serve       │ │ offer       │ │ index       │            │
│   └─────────────┘ └─────────────┘ └─────────────┘ └─────────────┘            │
│         │               │               │               │                     │
│         └───────────────┴───────────────┴───────────────┘                     │
│                                   │                                            │
│                                   ▼                                            │
│   LAYER 2: ORCHESTRATION (MOD/ZPWO)                                           │
│   ─────────────────────────────────                                           │
│   ┌─────────────────────────────────────────────────────────────┐            │
│   │                    ORCHESTRATOR AGENT                        │            │
│   │  • Routes requests to skills                                │            │
│   │  • Loads profiles into context                              │            │
│   │  • Enforces quality gates (MMA)                             │            │
│   │  • Manages context budget                                   │            │
│   └─────────────────────────────────────────────────────────────┘            │
│         │                                                                      │
│         ├──────────────┬──────────────┬──────────────┐                       │
│         ▼              ▼              ▼              ▼                       │
│   LAYER 3: SKILLS (Progressive Disclosure)                                    │
│   ────────────────────────────────────────                                    │
│   ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐                    │
│   │ Copy     │  │ Research │  │ Product  │  │ Tools    │                    │
│   │ Skills   │  │ Skills   │  │ Skills   │  │ Skills   │                    │
│   │          │  │          │  │          │  │          │                    │
│   │ L1-L4    │  │ L1-L4    │  │ L1-L4    │  │ L1-L4    │                    │
│   └──────────┘  └──────────┘  └──────────┘  └──────────┘                    │
│         │                                                                      │
│         ▼                                                                      │
│   LAYER 4: QUALITY GATES (MMA)                                                │
│   ────────────────────────────                                                │
│   ┌─────────────────────────────────────────────────────────────┐            │
│   │  7-Dimension Scoring: Strategy | Clarity | Voice | Proof   │            │
│   │                       Neuro | CTA | Ethics                  │            │
│   │  Threshold: >= 7.0 average | >= 9.0 ethics                 │            │
│   └─────────────────────────────────────────────────────────────┘            │
│         │                                                                      │
│         ▼                                                                      │
│   LAYER 5: MANUFACTURING (Knowledge Refinery Pipeline)                        │
│   ─────────────────────────────────────────────────────                       │
│   ┌──────────────┐  ┌──────────────┐  ┌──────────────┐                       │
│   │  NotebookLM  │  │    Prism     │  │   Claude     │                       │
│   │   EXTRACT    │──│  SYNTHESIZE  │──│   POLISH     │                       │
│   │              │  │              │  │              │                       │
│   │  Raw → Themes│  │ Themes →     │  │ Draft →      │                       │
│   │              │  │ Skill Draft  │  │ Production   │                       │
│   └──────────────┘  └──────────────┘  └──────────────┘                       │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## PART 1: CONTEXT PROFILES (Unified SSOT)

### Profile Architecture

The SKILL_ARCHITECT's JSON profiles map directly to ULTRAMIND's SSOT system:

| SKILL_ARCHITECT | ULTRAMIND SSOT | Purpose |
|-----------------|----------------|---------|
| `voice_dna.json` | `VOICE_GUIDE` | Tone, style, signature moves |
| `icp.json` | `PROJECT_BRIEF.audience` | Who we serve, their pains |
| `business.json` | `PROJECT_BRIEF.positioning` | What we offer, constraints |
| `evidence.json` | `EVIDENCE_PACK` | Proof, case studies, stats |
| `zero_point.json` | `SKILL_INDEX` | Always-loaded skill routing |

### Unified Profile Schema

```yaml
# /profiles/ultramind_context.yaml
# Single source of truth for all context profiles

meta:
  version: "1.0"
  project: "[project_name]"
  last_updated: "YYYY-MM-DD"
  
# ═══════════════════════════════════════════════════════════════════
# VOICE DNA (How We Sound)
# ═══════════════════════════════════════════════════════════════════
voice:
  summary:
    one_sentence: "[candid, sharp, optimistic realism with clear teaching]"
    archetype: "[builder-teacher | contrarian-analyst | empathetic-coach]"
    emotional_tone: ["grounded", "urgent", "playful"]
    reader_feeling_goal: ["seen and capable", "equipped to act"]
    
  priority_rules:
    - rule: "Clarity over cleverness"
      do: ["Short sentences", "Concrete examples", "Active voice"]
      dont: ["Jargon", "Passive constructions", "Vague abstractions"]
      
  style_mechanics:
    reading_level: "grade 6-9"
    sentence_length: "10-18 words default"
    paragraph_max_lines: 3
    whitespace_bias: "high"
    
  signature_moves:
    openers: ["contrarian premise", "vivid scene", "punch question"]
    cadence: ["triads", "hard-cut verdicts", "punchline after long"]
    
  lexicon:
    favorites: ["[phrase]", "[phrase]"]
    banned: ["[phrase]", "[phrase]"]
    
# ═══════════════════════════════════════════════════════════════════
# ICP (Who We Serve)
# ═══════════════════════════════════════════════════════════════════
audience:
  summary:
    one_sentence: "[founders of B2B SaaS doing $0-$2M ARR who need pipeline]"
    primary_segment: "[segment description]"
    
  context:
    industry: "[industry]"
    business_model: "[B2B/B2C/services]"
    typical_stage: "[pre-seed to series A]"
    constraints: ["budget", "time", "expertise"]
    
  pain:
    situation: "[where they are when pain hits — 2pm Tuesday]"
    description: "[specific pain, not abstract]"
    current_attempts: ["what they try now"]
    why_fails: ["why current solutions fail"]
    
  goals:
    primary: ["[goal]", "[goal]"]
    jobs_to_be_done:
      - job: "[job statement]"
        success: "[measurable outcome]"
        
  beliefs:
    current: ["[belief]", "[belief]"]
    misconceptions: ["[misconception]"]
    awareness_stage: "[unaware|problem|solution|product]-aware"
    desired_shift: "[what we want them to believe after]"
    
  language:
    words_they_use: ["[exact phrases]"]
    words_they_hate: ["[phrase]"]
    metaphors_that_land: ["[domain]"]
    
# ═══════════════════════════════════════════════════════════════════
# BUSINESS (What We Offer)
# ═══════════════════════════════════════════════════════════════════
positioning:
  one_liner: "[what you do + for whom + result]"
  category: "[ghostwriting | agency | coaching]"
  differentiators: ["[differentiator]"]
  anti_positioning: ["[what we are NOT]"]
  
offers:
  - name: "[offer name]"
    type: "[productized | retainer | course]"
    for_whom: "[ICP subset]"
    outcome: "[measurable outcome]"
    deliverables: ["[deliverable]"]
    
messaging:
  core_messages: ["[pillar]", "[pillar]"]
  claims_allowed: ["[substantiated claim]"]
  claims_disallowed: ["[claim to avoid]"]
  
constraints:
  compliance: ["[legal/regulatory]"]
  brand_safety: ["[topics to avoid]"]
  approval_process: "[who approves what]"
  
# ═══════════════════════════════════════════════════════════════════
# EVIDENCE (Proof We Can Use)
# ═══════════════════════════════════════════════════════════════════
proof:
  case_studies:
    - client: "[client type]"
      starting_point: "[baseline]"
      result: "[outcome]"
      timeframe: "[time]"
      
  credibility_markers: ["[credential]", "[result]"]
  
  stats:
    - stat: "[specific statistic]"
      source: "[citation]"
      use_when: "[context]"
```

---

## PART 2: SKILL STRUCTURE (Unified Format)

### The Dual-Format Skill

Skills exist in two synchronized formats:

| Format | Purpose | When to Use |
|--------|---------|-------------|
| **XML** | Machine-readable, routing, formal spec | Production deployment, MOD/MMA integration |
| **Markdown** | Human-readable, development, iteration | Building, editing, documentation |

### Unified Skill File Structure

```
/skills/[skill_name]/
├── SKILL.md                    # Human-readable (development)
├── skill.xml                   # Machine-readable (production)
├── zero_point.json             # Always-loaded index (<100 tokens)
├── implementation.py           # Code execution (if applicable)
├── flowgram.mmd                # Visual workflow
├── tests/
│   └── test_skill.py
└── docs/
    └── learned_constraints.md
```

### Markdown Skill Template (v3.0)

```markdown
# [SKILL_NAME] v[VERSION]
## [One-line description]

**Skill ID:** `[skill_id]`  
**Domain:** `[meta|copy|product|research|design|tools]`  
**Tier:** `[system|meta|production|experimental]`  
**Model:** `[sonnet|opus|haiku]`  
**Status:** `[draft|beta|active|deprecated]`

---

## ZERO-POINT SCHEMA (~100 tokens)

```json
{
  "skill": "[skill_id]",
  "desc": "[15-word description]",
  "triggers": ["[keyword]", "[phrase]"],
  "inputs": ["[required_input]"],
  "outputs": ["[primary_output]"],
  "wakes": ["[sister_skill]"],
  "budget": {"L1": 500, "L2": 1500, "L3": 3000, "L4": 6000}
}
```

---

## 1) PURPOSE

### What This Skill Does
[2-3 sentences explaining core capability]

### Use When
- [Trigger situation 1]
- [Trigger situation 2]

### Do NOT Use When
- [Anti-pattern 1]
- [Anti-pattern 2]

---

## 2) CONTRACT (I/O Specification)

### Required Inputs

| Input | Type | Source | Description |
|-------|------|--------|-------------|
| `PROJECT_BRIEF` | SSOT | upstream | Objective, audience, constraints |
| `[input_name]` | [type] | [source] | [description] |

### Optional Inputs

| Input | Type | Description |
|-------|------|-------------|
| `VOICE_GUIDE` | SSOT | Tone/style override |
| `EVIDENCE_PACK` | SSOT | Claims/proof to use |

### Primary Output

| Output | Format | Description |
|--------|--------|-------------|
| `[OUTPUT_NAME]` | [format] | [what it contains] |

### Secondary Outputs

| Output | Format | Description |
|--------|--------|-------------|
| `[secondary]` | [format] | [description] |

---

## 3) PROFILES REQUIRED

### Context Loading
```yaml
always_load:
  - profiles/ultramind_context.yaml#voice
  - profiles/ultramind_context.yaml#audience

load_if_claims:
  - profiles/ultramind_context.yaml#proof

load_if_multi_asset:
  - MESSAGE_SPINE
```

### Profile Usage
- **Voice:** Apply tone, lexicon, signature moves
- **Audience:** Match language, address pains, respect awareness level
- **Business:** Stay within claims_allowed, respect constraints

---

## 4) PROCESS STEPS

### Step 1: Prewriting Decisions
Before drafting, establish:
- [ ] Promise: [What reader gains]
- [ ] 3 Tangible Points: [Point 1] | [Point 2] | [Point 3]
- [ ] Section Formats: tips / stats / steps / lessons / examples

### Step 2: Outline
Produce:
- 5-10 headline options
- 3 subhead promises
- Bullet outline of body

### Step 3: Draft
- Write body first, hook last
- Maintain Voice DNA markers
- Use ICP language (exact phrases)

### Step 4: Variants (Recommended)
- Produce 2-3 alternate angles or openings
- Let orchestrator/user select direction

### Step 5: Polish Pass
- Compression pass (remove fluff)
- Clarity pass (simplify)
- Scannability pass (short paragraphs)
- Cliché removal
- Verb strengthening

---

## 5) QUALITY GATE (MMA Integration)

### 7-Dimension Scoring

| Dimension | Weight | Threshold | Validation |
|-----------|--------|-----------|------------|
| `strategy_alignment` | critical | 7.0 | Serves PROJECT_BRIEF objective? |
| `clarity_structure` | high | 7.0 | Clear, scannable, organized? |
| `voice_consistency` | high | 7.0 | Matches VOICE_GUIDE? |
| `proof_discipline` | critical | 8.0 | Claims backed by EVIDENCE_PACK? |
| `neuro_resonance` | high | 7.0 | Activates target axes? |
| `cta_integrity` | medium | 7.0 | Clear, singular, appropriate urgency? |
| `ethical_guardrails` | critical | 9.0 | Honest, respectful, manipulation-free? |

### Ship/No-Ship Checklist
- [ ] Promise delivered (headline/subheads)
- [ ] Voice match (DNA markers present)
- [ ] ICP fit (pains + language)
- [ ] Proof present (examples/stats/lessons)
- [ ] Scannability (short paragraphs, clear structure)
- [ ] Business constraints respected
- [ ] CTA correct tone + next step

---

## 6) COORDINATION PROTOCOLS

### Sister Skills (Always Wake)
| Skill | Why |
|-------|-----|
| `[sister_skill_id]` | [coordination reason] |

### Upstream Dependencies
| Skill | Provides |
|-------|----------|
| `[upstream_skill]` | [what it provides] |

### Downstream Consumers
| Skill | Consumes |
|-------|----------|
| `[downstream_skill]` | [what it needs] |

---

## 7) EXAMPLES

### ✅ Good Example (Voice Match)
```
[Paste short example of correct output]
```

**Why it works:**
- [Reason 1]
- [Reason 2]

### ❌ Bad Example (Generic AI Drift)
```
[Paste example of what to avoid]
```

**What went wrong:**
- [Problem 1]
- [Problem 2]

---

## 8) EDGE CASES & FAILURE MODES

### Edge Cases

| Case | Trigger | Approach |
|------|---------|----------|
| [Case name] | [When this happens] | [How to handle] |

### Common Failure Modes

| Failure | Detection | Fix |
|---------|-----------|-----|
| Too vague | No concrete examples | Add specific numbers, steps |
| Off-voice | Generic AI tone | Reapply Voice DNA rules |
| Weak proof | Unsubstantiated claims | Reference EVIDENCE_PACK |

---

## 9) CONTEXT BUDGET

| Layer | Tokens | Load Condition |
|-------|--------|----------------|
| L1 (Zero-Point) | ~100 | Always |
| L2 (Core Procedure) | ~1500 | Default execution |
| L3 (Advanced) | ~3000 | Complexity high OR edge case |
| L4 (Technical) | ~3000 | Meta-operations only |

### Unload Triggers
- Task completed
- Context pressure
- Not used within 2 turns

---

## 10) VERSION HISTORY

| Version | Date | Status | Changes |
|---------|------|--------|---------|
| 1.0.0 | YYYY-MM-DD | active | Initial release |

### Baseline MMA Scores
```yaml
strategy_alignment: 0.0
clarity_structure: 0.0
voice_consistency: 0.0
proof_discipline: 0.0
neuro_resonance: 0.0
cta_integrity: 0.0
ethical_guardrails: 0.0
average: 0.0
```
```

---

## PART 3: AGENT STRUCTURE (Unified Orchestration)

### Agent Hierarchy

```yaml
AGENT_HIERARCHY:
  
  orchestrator:
    name: "MOD (Master Orchestration Daemon)"
    role: "Routes requests, loads context, enforces quality"
    loads:
      - profiles/ultramind_context.yaml
      - skills/zero_point_index.json
    capabilities:
      - Request clarification
      - Skill selection
      - Variant generation
      - Quality gate enforcement
      - File management
    
  specialists:
    copy_agent:
      skills: ["SCD", "HPE", "ACM", "SPC", "VSL"]
      profile_focus: "voice + audience"
      
    research_agent:
      skills: ["MIS", "framework_extractor", "competitive_analysis"]
      profile_focus: "audience + business"
      
    product_agent:
      skills: ["PCG", "TEA", "offer_architect"]
      profile_focus: "business + proof"
      
    design_agent:
      skills: ["SDM", "ui_architect", "asset_pipeline"]
      profile_focus: "voice + business"
      
    tools_agent:
      skills: ["MAA", "browser_automation", "script_runner"]
      profile_focus: "business + constraints"
      
  quality:
    mma_agent:
      role: "Validates outputs against 7 dimensions"
      threshold: "7.0 average, 9.0 ethics"
      action_on_fail: "Return to specialist with critique"
```

### Orchestrator Agent Prompt (v3.0)

```markdown
# Orchestrator Agent — ULTRAMIND v3.0

## Role
You are the Master Orchestration Daemon (MOD). You coordinate specialists,
enforce process, and ensure outputs meet Quality Gates.

## On Every Request

### 1. Load Context
```yaml
always_load:
  - profiles/ultramind_context.yaml
  - skills/zero_point_index.json
```

### 2. Clarify Request
Before any work, establish:
- Deliverable type
- Target audience (ICP segment)
- Channel/format
- Length constraints
- CTA (call-to-action)
- Success criteria

### 3. Select Skill + Agent
Based on request, route to appropriate specialist:
- Copy work → copy_agent + [skill]
- Research → research_agent + [skill]
- Product → product_agent + [skill]
- Design → design_agent + [skill]
- Automation → tools_agent + [skill]

### 4. Enforce Prewriting
Before drafting, require:
- Promise (what reader gains)
- 3 tangible points
- Section formats (tips/stats/steps/lessons/examples)

### 5. Request Variants
Always generate 2-3 variants. Select best direction.

### 6. Run Quality Gate (MMA)
Check all 7 dimensions:
- strategy_alignment >= 7.0
- clarity_structure >= 7.0
- voice_consistency >= 7.0
- proof_discipline >= 8.0
- neuro_resonance >= 7.0
- cta_integrity >= 7.0
- ethical_guardrails >= 9.0

If any critical dimension fails → return to specialist with specific critique.

### 7. Save & Document
On approval:
- Save to `/deliverables/finals/YYYY-MM-DD_channel_topic_FINAL.md`
- Update `/knowledge/` with patterns learned
- Log to version history

## Operating Rules
- Never bypass Quality Gate
- Always load profiles before execution
- Prefer specialists over direct execution
- Compress to SSOT after completion
```

---

## PART 4: PIPELINE INTEGRATION

### How Knowledge Refinery Feeds the Framework

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    PIPELINE → FRAMEWORK INTEGRATION                             │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   KNOWLEDGE REFINERY PIPELINE                                                   │
│   ───────────────────────────                                                   │
│                                                                                 │
│   Stage 1: NotebookLM EXTRACT                                                   │
│   ├── Themes → Core thesis for SKILL.md                                        │
│   ├── Patterns → Process steps                                                 │
│   ├── Zero-Point candidates → zero_point.json                                  │
│   └── Contradictions → Learned constraints                                     │
│                                                                                 │
│   Stage 2: Prism SYNTHESIZE                                                    │
│   ├── SKILL.md → Human-readable format                                         │
│   ├── skill.xml → Machine-readable format                                      │
│   ├── implementation.py → Code execution                                       │
│   └── flowgram.mmd → Visual workflow                                           │
│                                                                                 │
│   Stage 3: Claude POLISH                                                        │
│   ├── Profile alignment check                                                  │
│   ├── MMA validation                                                           │
│   ├── Production hardening                                                     │
│   └── Integration testing                                                      │
│                                                                                 │
│   ↓                                                                             │
│                                                                                 │
│   ULTRAMIND FRAMEWORK v3.0                                                      │
│   ────────────────────────                                                      │
│                                                                                 │
│   Profiles ← Voice/ICP/Business context                                        │
│   Skills ← Progressive disclosure (L1-L4)                                      │
│   Agents ← Orchestration + specialists                                         │
│   Quality ← MMA 7-dimension validation                                         │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

### Pipeline Output → Framework Input Mapping

```yaml
PIPELINE_TO_FRAMEWORK_MAP:
  
  notebooklm_extraction:
    themes:
      → skill.md#purpose
      → skill.md#core_thesis
    
    hierarchy:
      → skill.xml#Layer[1-4]
      → progressive_disclosure_structure
    
    patterns:
      → skill.md#process_steps
      → skill.xml#ExecutionPattern
    
    zero_point_candidates:
      → zero_point.json
      → skill.xml#ZeroPointSchema
    
    contradictions:
      → learned_constraints.md
      → skill.xml#EdgeCases
    
  prism_synthesis:
    skill_md:
      → human_readable_format
      → development_iteration
    
    skill_xml:
      → machine_readable_format
      → mod_routing
      → mma_integration
    
    implementation_py:
      → code_execution
      → cli_interface
      → self_annealing
    
  claude_polish:
    profile_alignment:
      → voice_check
      → icp_language_check
      → business_constraints_check
    
    mma_validation:
      → 7_dimension_scoring
      → baseline_establishment
    
    production_readiness:
      → testing_specs
      → integration_protocols
```

---

## PART 5: IMPLEMENTATION CHECKLIST

### For New Skills

```yaml
NEW_SKILL_CHECKLIST:
  
  phase_1_discovery:
    - [ ] Define capability gap
    - [ ] Gather source materials
    - [ ] Estimate complexity (Simple/Standard/Complex/Modular)
    - [ ] Create SKILL_BRIEF.yaml
    
  phase_2_extraction:
    - [ ] Run NotebookLM extraction template
    - [ ] Extract themes, patterns, zero-point candidates
    - [ ] Document contradictions
    - [ ] Export structured YAML
    
  phase_3_synthesis:
    - [ ] Generate SKILL.md (human-readable)
    - [ ] Generate skill.xml (machine-readable)
    - [ ] Generate zero_point.json (<100 tokens)
    - [ ] Generate implementation.py (if applicable)
    - [ ] Generate flowgram.mmd
    
  phase_4_polish:
    - [ ] Profile alignment check (voice, ICP, business)
    - [ ] MMA validation (7 dimensions)
    - [ ] Code quality review
    - [ ] Test suite creation
    - [ ] Production readiness report
    
  phase_5_integration:
    - [ ] Update skills/zero_point_index.json
    - [ ] Add MOD routing rules
    - [ ] Configure MMA thresholds
    - [ ] Update SKILLS_MANIFEST.yaml
    - [ ] Deploy to orchestrator
```

### For Existing Skills (Upgrade Path)

```yaml
SKILL_UPGRADE_CHECKLIST:
  
  from_skill_architect_format:
    - [ ] Convert skills/*.md to unified SKILL.md format
    - [ ] Add zero_point.json
    - [ ] Add skill.xml for MOD routing
    - [ ] Add MMA quality dimensions
    - [ ] Add profile loading requirements
    
  from_xml_only_format:
    - [ ] Create human-readable SKILL.md
    - [ ] Add process steps (prewriting, outline, draft, polish)
    - [ ] Add examples (good/bad)
    - [ ] Add failure modes
    - [ ] Synchronize with XML
    
  profile_migration:
    - [ ] Merge voice_dna.json → ultramind_context.yaml#voice
    - [ ] Merge icp.json → ultramind_context.yaml#audience
    - [ ] Merge business.json → ultramind_context.yaml#positioning
    - [ ] Add proof section from evidence sources
```

---

## PART 6: FILE ORGANIZATION

### Recommended Project Structure

```
/ultramind/
├── profiles/
│   ├── ultramind_context.yaml      # Unified context (voice + ICP + business)
│   └── project_briefs/
│       └── [project_name].yaml     # Per-project overrides
│
├── skills/
│   ├── zero_point_index.json       # Always-loaded skill routing
│   │
│   ├── copy/
│   │   ├── strategic_copy_director/
│   │   │   ├── SKILL.md
│   │   │   ├── skill.xml
│   │   │   ├── zero_point.json
│   │   │   └── implementation.py
│   │   └── [other_copy_skills]/
│   │
│   ├── research/
│   │   └── [research_skills]/
│   │
│   ├── product/
│   │   └── [product_skills]/
│   │
│   ├── design/
│   │   └── [design_skills]/
│   │
│   └── tools/
│       └── master_automations_architect/
│           ├── SKILL.md
│           ├── skill.xml
│           ├── orchestrator.py
│           └── modules/
│               ├── 01_master_architect/
│               ├── 02_automation_builder/
│               └── [03-08]/
│
├── agents/
│   ├── orchestrator.md             # MOD system prompt
│   ├── copy_agent.md               # Specialist prompt
│   ├── research_agent.md           # Specialist prompt
│   └── [other_agents].md
│
├── knowledge/
│   ├── research/                   # Research outputs
│   ├── patterns/                   # Learned patterns
│   └── constraints/                # Learned constraints
│
├── deliverables/
│   ├── drafts/
│   └── finals/
│
└── templates/
    ├── SKILL_TEMPLATE_v3.md        # Unified skill template
    ├── SKILL_TEMPLATE_v3.xml       # Machine-readable template
    └── PROFILE_TEMPLATE.yaml       # Context profile template
```

---

## PART 7: MIGRATION GUIDE

### From SKILL_ARCHITECT_v2

```yaml
MIGRATION_STEPS:
  
  1_profiles:
    action: "Merge JSON profiles into YAML"
    from:
      - profiles/voice_dna.json
      - profiles/icp.json
      - profiles/business.json
    to:
      - profiles/ultramind_context.yaml
    
  2_skills:
    action: "Convert to unified format"
    from:
      - skills/[skill_name].md (simple format)
    to:
      - skills/[domain]/[skill_name]/SKILL.md (comprehensive)
      - skills/[domain]/[skill_name]/skill.xml (machine-readable)
      - skills/[domain]/[skill_name]/zero_point.json
    
  3_agents:
    action: "Upgrade orchestrator prompt"
    from:
      - agents/orchestrator-agent.md (simple)
    to:
      - agents/orchestrator.md (MOD-integrated)
    add:
      - Profile loading requirements
      - MMA quality gate enforcement
      - Skill routing logic
```

### From SKILL_TEMPLATE_V2.xml

```yaml
MIGRATION_STEPS:
  
  1_add_human_readable:
    action: "Create companion SKILL.md"
    content:
      - Process steps (prewriting → outline → draft → polish)
      - Examples (good/bad)
      - Failure modes
      - Profile requirements
    
  2_add_profiles:
    action: "Create ultramind_context.yaml"
    extract_from:
      - Existing VOICE_GUIDE references
      - Existing PROJECT_BRIEF patterns
      - Existing EVIDENCE_PACK examples
    
  3_synchronize:
    action: "Keep XML and MD in sync"
    rule: "Edit SKILL.md for development, generate skill.xml for production"
```

---

## SUMMARY: What v3.0 Unifies

| Component | SKILL_ARCHITECT | SKILL_TEMPLATE_V2 | Framework v3.0 |
|-----------|-----------------|-------------------|----------------|
| **Context** | JSON profiles | SSOT references | Unified YAML profiles |
| **Skills** | Simple MD | Complex XML | Both (synchronized) |
| **Layers** | None | L1-L4 | L1-L4 (preserved) |
| **Process** | 5 steps | Implicit | 5 steps (explicit) |
| **Quality** | QA checklist | MMA 7-dim | MMA 7-dim (enhanced) |
| **Agents** | Orchestrator + specialists | MOD routing | MOD + specialists |
| **Examples** | Good/bad | GoldenRuns | Both patterns |
| **Pipeline** | None | None | Knowledge Refinery |

**The Result:** A complete, unified system where profiles provide context, skills provide capability, agents provide orchestration, quality gates ensure standards, and the pipeline provides manufacturing.

---

*ULTRAMIND Skill Framework v3.0*  
*Agent-Centric + Skill-Centric + Pipeline-Centric = Complete System*  
*Updated: 2026-01-30*

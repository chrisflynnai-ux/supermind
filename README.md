# ULTRAMIND - Agentic Business Automation System

> **Version:** v4.1
> **Architecture:** 9D Agentic Model (6 Primary + 1 Center + 2 Meta-Cycle)
> **Philosophy:** Business automation with neuro-persuasion at its core

---

## What Is ULTRAMIND?

ULTRAMIND is a **pure agentic business automation system** built on a 6-dimensional neuro-box architecture with Zero-Point Workflow Orchestration (ZPWO). It coordinates specialized AI skills to produce revenue-generating marketing assets (advertorials, sales pages, email sequences, VSLs) using a Two-Brain Pod system (Left: Technical | Right: Strategic).

**What we build is not human healing—it's business automation with neuro-persuasion at its core.**

---

## Core Architecture

### The 9 Agentic Functions

```
                       PRODUCTION (Heart)
                    Strategic Planning & Assets
                              ▲
                              │
         DESIGN ◄────────  SOUL (Orchestration)  ────────► DEVELOP
      (Conscience)            │                           (Psych)
       Frontend              │                            Backend
                              │
       RESONANCE ◄────────────┼────────────► PERSUASION
         (Mind)               │              (Spirit)
      Viral Content           │         Compelling Copy
                              │
                              ▼
                      AUTOMATION (Body)
                  Streamlining Workflows & Systems

                META-CYCLE:
                └─► LEARNING (Review & Reflect)
                    └─► REPAIR (Rate & Repair)
                        └─► NEXT PROJECT ↺
```

### 3 Primary Axes (6 Dimensions)

**X-AXIS: RESONANCE ↔ PERSUASION**
- **MIND (Left) = RESONANCE** - Viral Writing Content & Scripts "Awareness" (Attention → Affection)
- **SPIRIT (Right) = PERSUASION** - Compelling Copy to Shift "Beliefs" + Influence Behavior "Desire" (Conversation → Convection)

**Y-AXIS: AUTOMATION ↔ PRODUCTION**
- **BODY (Bottom) = AUTOMATION** - Streamlining Workflows with "Systems"
- **HEART (Top) = PRODUCTION** - Strategic Planning & Building & Creating "Assets"

**Z-AXIS: DEVELOPMENT ↔ DESIGN**
- **PSYCH (Back) = DEVELOPMENT** - Back-End Architecture Processes / Builds "Structures"
- **CONSCIENCE (Front) = DESIGN** - Front-End Features and Functionality UI/UX "Applications"

**CENTER: ORCHESTRATION**
- **SOUL = ORCHESTRATION** - Optimize & Coordinate Teams Workflow Sequences & Transitions "FLOWS" + Runs Recursion Cycles

**META-CYCLE: LEARNING & REPAIR**
- **LEARNING** - Review & Reflect "Performance" (Self-Identified Patterns - SIPs)
- **REPAIR** - Rate & Repair - Upgrade Patches & Enhancements + New Methods & Frameworks (Human Corrected Events)

---

## Project Structure

```
ULTRAMIND/
├── .claude/
│   ├── ORCHESTRATOR_CORE.yaml          # Stateful coordination intelligence
│   ├── SESSION_STATE.json              # Runtime workflow state
│   ├── skills/                         # Specialized skill XMLs
│   │   ├── meta/                       # Orchestration & quality skills
│   │   ├── copy/                       # Copywriting skills
│   │   ├── research/                   # Intelligence & analysis skills
│   │   └── design/                     # Visual & UI/UX skills
│   └── schemas/                        # SSOT object templates
│
├── docs/
│   ├── architecture/                   # System design documents
│   │   ├── ULTRAMIND_3_AXIS_ARCHITECTURE.md
│   │   ├── ORCHESTRATION_INTEGRATION_GUIDE.md
│   │   └── ULTRAMIND_LEAN_STACK.md
│   ├── constitution/                   # Governing principles
│   │   └── ULTRAMIND_CONSTITUTION_v2_1.md
│   └── handoffs/                       # Migration & integration docs
│
├── CLAUDE.md                           # Primary control plane (Claude Code entry point)
├── ARCHITECTURE_UPGRADE_v4_SUMMARY.md  # Latest architecture changes
├── .gitignore                          # Repository exclusions
└── README.md                           # This file

```

---

## Key Concepts

### ZPWO (Zero-Point Workflow Orchestrator)

The central orchestrator that coordinates all workflow execution:

- **Informed Center:** Light enough to always load, smart enough to route well
- **Heavy Edges:** Skills loaded on-demand, unloaded after use
- **Two-Brain Pod:** Pairs Technical (Left) + Strategic (Right) for every task
- **Progressive Disclosure:** L0 (core) → L1 (index) → L2 (execution) → L3 (checksums) → L4 (heavy context)

### Two-Brain Pod System

**Left Brain (Technical):**
- Dimensions: MIND (Resonance) + PSYCH (Development)
- Functions: Analysis, structure, data, pattern recognition
- Skills: Viral analysis, hook templates, backend architecture

**Right Brain (Strategic):**
- Dimensions: SPIRIT (Persuasion) + CONSCIENCE (Design)
- Functions: Creation, persuasion, emotion, aesthetics
- Skills: Sales copy, advertorials, email sequences, visual design

**Central Coordination (Soul):**
- Dimension: SOUL (Orchestration)
- Functions: Routing, quality gates, state management, ECR cycles
- Skills: ZPWO, MMA validation, market intelligence

### SSOT (Single Source of Truth)

Foundation objects that lock workflow state:

```yaml
# Core SSOT Objects
PROJECT_BRIEF.yaml          # Goal, Avatar, Offer
MESSAGE_SPINE.yaml          # Promise, Mechanism, Proof
EVIDENCE_PACK.yaml          # Claims, Citations, Gaps
VOICE_GUIDE.yaml            # Tone, personality, style
SESSION_STATE.json          # Runtime state tracking
```

**SSOT Locking:**
- Locked after `/intake` phase
- Checksums validated before phase transitions
- Changes require PATCH_PROPOSAL approval (drift protection)

### MMA (7-Dimension Quality Standard)

Continuous quality validation across:
1. **Proof Density** - Claims grounded in evidence
2. **Mechanism Clarity** - How the solution works
3. **Voice Consistency** - Matches VOICE_GUIDE
4. **Message Clarity** - Easy to understand
5. **Engagement** - Holds attention
6. **Conversion Potential** - Drives action
7. **Compliance Safety** - Avoids risky claims

**Passing Thresholds:**
- Average score: ≥ 8.0
- Critical dimensions (Proof, Mechanism, Voice): ≥ 9.0

### ECR (End Cycle Recursion)

Self-improvement loop after each project:

```
PROJECT COMPLETE
      ↓
  LEARNING Phase
    - Extract SIPs (Self-Identified Patterns)
    - Analyze MMA failure patterns
    - Review context bloat triggers
    - Log Human-Corrected Events
      ↓
  REPAIR Phase
    - Rate issues by severity
    - Generate PATCH proposals
    - Update orchestrator rules
    - Enhance skill definitions
      ↓
  READY FOR NEXT PROJECT ↺
```

---

## Workflow Phases

### Phase 1: DRAFT (`/draft`)
- **Goal:** High-volume angle exploration (3-10 variations)
- **Tooling:** Minimal. Prioritize raw creative output.
- **Output:** Locked ANGLE_SET in SSOT
- **Gate:** User approval on selected angle

### Phase 2: PRODUCTION (`/produce`)
- **Goal:** Publishable assets with 100% proof grounding
- **Tooling:** Heavy. Activate specialized skills (advertorial, salespage, email)
- **Quality:** Continuous MMA validation (7-dimension standard)
- **Circuit Breaker:** Max 3 FIX loops per dimension
- **Output:** MMA-validated asset (avg ≥8.0, critical ≥9.0)

### Phase 3: POLISH (`/polish`)
- **Goal:** Human Personance & AI Detox
- **Tooling:** Selective. Kitchen Table Test + Cardiac Rhythm
- **Quality:** Human voice score ≥ 9.0
- **Output:** Final SHIP_PACKAGE ready for deployment

---

## Funnel Intelligence

ORCHESTRATOR_CORE routes based on funnel position:

### TOFU (Top of Funnel) - Awareness
- **Audience:** Cold traffic, problem unaware
- **Content:** Viral threads, hooks, educational posts
- **Dimensions:** MIND (Resonance) + BODY (Automation for content workflows)
- **Voice:** Conversational, curiosity-driven, non-salesy

### MOFU (Middle of Funnel) - Consideration
- **Audience:** Warm traffic, problem aware, exploring solutions
- **Content:** Advertorials, VSLs, mechanism reveals
- **Dimensions:** MIND (Resonance) + SPIRIT (Persuasion)
- **Voice:** Educational, proof-heavy, trust-building

### BOFU (Bottom of Funnel) - Conversion
- **Audience:** Hot traffic, product aware, ready to buy
- **Content:** Sales pages, order forms, urgency/scarcity
- **Dimensions:** SPIRIT (Persuasion) + HEART (Production)
- **Voice:** Direct, benefit-driven, CTA-focused

### Retention - Advocacy
- **Audience:** Customers, highest LTV potential
- **Content:** Onboarding emails, upsells, community content
- **Dimensions:** SPIRIT (Persuasion) + MIND (Resonance)
- **Voice:** Supportive, relationship-nurturing

---

## Audience Type Intelligence

### B2C (Business-to-Consumer)
- **Tone:** Personal, emotional, benefit-focused, aspirational
- **Proof:** Testimonials, before/after, social proof, guarantees
- **Message:** "Transform your life / Feel better / Solve pain"

### B2B (Business-to-Business)
- **Tone:** Professional, ROI-focused, data-driven, authority-building
- **Proof:** Case studies, metrics, industry credentials, logos
- **Message:** "Increase revenue / Save time / Reduce costs"

### Editorial (Content/Education-First)
- **Tone:** Educational, journalistic, informative, non-salesy
- **Proof:** Research citations, expert quotes, data visualization
- **Message:** "Here's what you need to know / Understanding the truth"

### Community (Existing Customers/Fans)
- **Tone:** Insider, exclusive, relationship-based, conversational
- **Proof:** Peer testimonials, community wins, insider stories
- **Message:** "You're part of something special / Here's what's next"

---

## Getting Started

### 1. Initialize a New Project

```bash
# Run intake to create and lock SSOT objects
/intake

# Verify SSOT objects were created
ls .claude/ssot/
```

### 2. Select Your Asset Type

```bash
# For cold traffic pre-sell
/advertorial

# For conversion page
/salespage

# For email nurture sequences
/email

# For video sales letter
/vsl
```

### 3. Follow the Workflow

```
INTAKE → DRAFT → PRODUCTION → POLISH → SHIP
```

Each phase has explicit gates and quality checks enforced by ZPWO.

---

## Skills Manifest

### Meta/Orchestration (7 skills)
- `zpwo_meta_orchestrator_v1.0.0.xml` - Central workflow coordinator
- `mma_master_monitor_agent_v1.0.0.xml` - Quality validation
- `market_intelligence_synthesizer_v2.1.xml` - Avatar & evidence research

### Copy/Persuasion (10 skills)
- `advertorial_copy_master_v2.0.0.xml` - Cold traffic pre-sell
- `sales_page_copywriter_lite_v2.0.0.xml` - Conversion pages
- `email_campaign_copy_genius_v2.0.0.xml` - Email sequences
- `human_persuasion_editor_v2.1.0.xml` - AI detox & polish
- `viral_resonance_analyzer_v1.0.0.xml` - Hook analysis
- `viral_thread_deconstructor_v2.1.xml` - Social proof extraction

### Design/Visual (3 skills)
- `sales_page_deconstructor_analyst_v3.0.0.xml` - Page analysis
- `image_concept_planner_v1.0.0.xml` - Visual planning
- `visual_stun_concept_architect_v1.0.xml` - Emotional imagery

### Research/Intelligence (3 skills)
- `market_intelligence_synthesizer_v2.1.xml` - Avatar research
- `competitor_analysis_specialist_v1.0.xml` - Market positioning

### Development (4 skills)
- `skill_builder_architect_v2.0.0.xml` - Build new skills
- `pydantic_schema_generator_v1.0.xml` - Backend data structures
- `api_integration_specialist_v1.0.xml` - External service connections

---

## Circuit Breakers & Guardrails

### Critical (Never Violate)
- **No fabrication** - No invented stats, testimonials, credentials
- **No fake urgency** - No false timers or manufactured scarcity
- **Proof discipline** - All claims grounded in EVIDENCE_PACK or softened
- **Single CTA** - One action per asset, repeated not multiplied
- **MESSAGE_SPINE locked** - Do not invent new mechanism or promise

### Automatic Circuit Breakers
1. **Max 3 FIX Loops** - If MMA dimension fails 3x, HALT and generate PATCH_PROPOSAL
2. **Context Bloat** - If usage >70%, run `/gc` (Garbage Collection) immediately
3. **Same Failure 3x** - Auto-generate patch, update skill definition, log SIP

---

## Core Doctrine

1. **State > Chat** — SSOT objects are memory; chat is UI
2. **Generate Last** — Use tools first (Python validation), then LLM generation
3. **Two-Brain Teams** — Every stage pairs Technical (Left) + Strategic (Right)
4. **Locked SSOT** — Stage A creates, Stage B consumes (no drift without Patch Request)
5. **Garbage Collection** — Summarize + prune context automatically at 70%
6. **Light Center, Heavy Edges** — ZPWO routes; sub-agents execute
7. **Progressive Disclosure** — Load minimum context required for current task
8. **Informed Routing** — Use funnel position + audience type to select skills

---

## Neuro-Persuasion Model

ULTRAMIND leverages neurotransmitter science to optimize persuasion:

- **GABA (Body/Safety)** - Reduce anxiety, create safety, build trust
- **Serotonin (Heart/Status)** - Elevate identity, aspirational positioning
- **Dopamine (Achievement)** - Reward anticipation, gamification, progress
- **Oxytocin (Psych/Identity)** - Belonging, community, tribal identity
- **Adrenaline (Cosmic/Action)** - Urgency, momentum, decisive action

**This is NOT human therapy** - it's understanding how persuasion works at a neurochemical level to create more effective marketing.

---

## Version History

### v4.1 (2026-01-13) - Orchestrator Intelligence Restoration
- **Added:** ORCHESTRATOR_CORE.yaml (stateful coordination intelligence)
- **Added:** SESSION_STATE.json (runtime workflow tracking)
- **Added:** Two-Brain Pod pairing rules
- **Added:** Funnel position intelligence (TOFU/MOFU/BOFU)
- **Added:** Audience type intelligence (B2C/B2B/Editorial/Community)
- **Added:** Dimensional routing logic
- **Fixed:** "Light center" context loss - now "informed center"

### v4.0 (2026-01-13) - Agentic Function Definitions
- **Added:** Explicit agentic function definitions for all 6 dimensions
- **Added:** ECR (End Cycle Recursion) framework (Learning & Repair)
- **Updated:** Y-axis from "BODY ↔ HEART" to "AUTOMATION ↔ PRODUCTION"
- **Removed:** Human healing/renewal language (scope clarification)
- **Clarified:** System is business automation, not human transformation

### v3.0 (2026-01-12) - Zero-Point Workflow Orchestration
- **Added:** ZPWO Meta-Orchestrator
- **Added:** Progressive Disclosure (Light Center, Heavy Edges)
- **Added:** Two-Brain Pod architecture
- **Added:** MMA 7-Dimension Quality Standard
- **Added:** SSOT locking and drift protection

---

## Contributing

This is a proprietary agentic business automation system. Internal use only.

---

## License

Proprietary - All Rights Reserved

---

## Contact

**Project:** ULTRAMIND Agentic Business Automation
**Architecture:** 9D Agentic Model with ZPWO
**Version:** v4.1
**Status:** Active Development

---

*"At the heart of infinitely intelligent adaptive systems is radical simplicity."*

*"What we build is not human healing—it's business automation with neuro-persuasion at its core."*

# MODULE ONE: MASTER AUTOMATIONS ARCHITECT
## The Doctrine Layer for Lean Automation Design

**Version:** 1.0.0  
**Module Type:** Doctrine (Strategy + Routing)  
**Token Budget:** ~4,100 tokens (L1: 600 | L2: 1,500 | L3: 1,200 | L4: 800)  
**Integration:** Hub connecting Modules 2-8  
**Build Date:** 2026-01-23  
**Doctrine:** Skills + Scripts > MCPs | Zero-Point Context Strategy

---

# TABLE OF CONTENTS

1. [GEO Knowledge Compendium](#section-1-geo-knowledge-compendium) (5 pages)
2. [Module Blueprint](#section-2-module-blueprint) (12-15 pages)
3. [Knowledge Blocks](#section-3-knowledge-blocks) (5-7 pages)
4. [Case Studies](#section-4-case-studies) (3-4 pages)
5. [Pattern Library](#section-5-pattern-library) (2 pages)
6. [Output Templates](#section-6-output-templates) (2 pages)
7. [README & Integration](#section-7-readme-integration) (1 page)

---

# SECTION 1: GEO KNOWLEDGE COMPENDIUM
## The Five Core Pains of Automation Architecture

*"Token discipline is accuracy discipline. Every always-loaded parameter schema competes with your offer, your copy voice, your SSOT objects, and your orchestration rules."*

---

## 1.1 THE AUTOMATION LANDSCAPE CRISIS

Before diving into solutions, we must understand why 80% of business automations fail to deliver promised value. The automation industry has created a false dichotomy: either use "no-code" visual tools (n8n, Zapier, Make) or hire developers for custom solutions. Both paths lead to the same five core pains.

### The False Promise of Visual Automation

Visual automation tools promised democratization. Instead, they created:
- **Dependency on platforms** that can change pricing, features, or shut down
- **Hidden complexity** that explodes when workflows exceed toy examples
- **Technical debt** disguised as "no-code simplicity"
- **Context bloat** when connecting these tools to AI agents

### The Hidden Cost of MCP Architecture

Model Context Protocol (MCP) promised seamless AI-tool integration. The reality:
- **Always-loaded schemas** consume 2,000-5,000 tokens per tool
- **Cognitive load** degrades model accuracy as tools accumulate
- **Vendor lock-in** to specific MCP implementations
- **Black box execution** with inconsistent error handling

---

## 1.2 THE FIVE CORE PAINS

### PAIN #1: Visual Spaghetti Syndrome

**Symptoms:**
- Workflows with 20+ nodes that nobody can follow
- "Don't touch it, it works" warnings on production automations
- Hours spent debugging a single failed node
- Inability to parallelize or optimize execution paths
- Copy-paste duplication across similar workflows

**Root Causes:**
- Visual tools encourage adding nodes instead of refactoring
- No abstraction mechanisms (functions, modules, inheritance)
- Each node is a potential failure point with its own error handling
- Connection logic embedded in visual layout, not explicit code

**Evidence from Practice:**
| Metric | Visual Workflow | PCE Equivalent |
|--------|-----------------|----------------|
| Nodes/Steps | 28 nodes | 4 scripts |
| Debug time | 2-4 hours | 15-30 minutes |
| Modification time | 45-60 minutes | 10-15 minutes |
| Error handling | Per-node (28 places) | Centralized (1 place) |
| Parallelization | Manual rewiring | Automatic |

**Strategic Implications:**
- Every hour spent debugging visual spaghetti is an hour not spent on value creation
- Accumulated technical debt makes automation migration increasingly expensive
- Team knowledge becomes concentrated in whoever built the original workflow
- Scaling requires rebuilding from scratch, not extending

**The Doctrine Response:**
> Move logic into SOP markdown + scripts (PCE), then keep only thin triggers and handoff points in any visual tool that remains.

---

### PAIN #2: Schema Bloat at Zero-Point

**Symptoms:**
- AI agent responses slow down as tools are added
- Model "forgets" earlier instructions in long conversations
- Inconsistent tool selection (uses wrong tool for task)
- Quality degradation on complex multi-step tasks
- Token costs spiral with each new MCP connection

**Root Causes:**
- MCP architecture loads full tool schemas into default context
- Each tool adds 500-2,000 tokens of parameter definitions
- No mechanism for on-demand loading/unloading
- Schemas compete with business logic for attention

**Evidence from Practice:**
| Configuration | Default Context | Accuracy (complex tasks) | Token Cost/Request |
|---------------|-----------------|--------------------------|-------------------|
| 3 MCPs | ~6,000 tokens | 94% | $0.18 |
| 8 MCPs | ~16,000 tokens | 87% | $0.48 |
| 15 MCPs | ~30,000 tokens | 71% | $0.90 |
| Zero-Point (Skills) | ~500 tokens | 96% | $0.015 |

**Strategic Implications:**
- Context is a finite resource; every token matters
- Schema bloat creates a ceiling on automation complexity
- Cost per request makes high-volume automation economically unviable
- Quality degradation compounds across multi-step workflows

**The Doctrine Response:**
> Keep only tiny skill descriptors and tool names at Zero-Point, and load heavy schemas or docs only when a specific skill is activated.

---

### PAIN #3: Tool-First Architecture

**Symptoms:**
- Automation design starts with "what tools do we have?"
- Workflow structure mirrors tool capabilities, not business logic
- New requirements require new tools instead of new scripts
- Vendor changes break entire automation suites
- "Integration specialists" become bottleneck roles

**Root Causes:**
- Tools marketed as solutions rather than components
- No workflow-first design methodology taught
- Easy to connect tools; hard to design systems
- Vendor incentives misaligned with user outcomes

**Evidence from Practice:**
| Approach | Time to First Automation | Maintenance Burden | Adaptability Score |
|----------|--------------------------|-------------------|-------------------|
| Tool-first | 2 hours | High (vendor-dependent) | 3/10 |
| Workflow-first (PCE) | 4 hours | Low (code-based) | 9/10 |

**Strategic Implications:**
- Tool-first creates vendor dependency that compounds over time
- Each vendor relationship adds communication overhead
- Switching costs increase geometrically with automation count
- Innovation bottlenecked by tool vendor roadmaps

**The Doctrine Response:**
> Start from Double-II and PCE: define the information model and scripts first, then attach tools as interchangeable backends via skills.

---

### PAIN #4: LLM-Only Execution Layer

**Symptoms:**
- Same automation produces different results on different runs
- Error messages are prompt engineering challenges, not debugging
- No test suite possible (outputs not deterministic)
- "It worked yesterday" becomes common complaint
- Production failures require prompt archaeology

**Root Causes:**
- LLMs treated as execution engines instead of orchestrators
- No separation between planning and execution
- Ad-hoc API calls without validation layers
- Error handling delegated to model's "judgment"

**Evidence from Practice:**
| Execution Style | Consistency | Debug Time | Test Coverage |
|-----------------|-------------|------------|---------------|
| LLM-only | 73% identical outputs | 45-90 min | 0% (untestable) |
| LLM + Deterministic Scripts | 99% identical outputs | 10-20 min | 85%+ |

**Strategic Implications:**
- Non-deterministic automation cannot be trusted for critical workflows
- Testing becomes impossible, so bugs reach production
- Debugging requires reproducing exact context (often impossible)
- Reliability ceiling prevents enterprise adoption

**The Doctrine Response:**
> Back every external interaction with a deterministic script (Node/Python/CLI) that the agent calls via skills, with explicit error maps and tests.

---

### PAIN #5: Static, Non-Learning Automations

**Symptoms:**
- Same errors recur weeks after being "fixed"
- No mechanism to capture and apply lessons learned
- Automations drift from business reality over time
- Manual intervention frequency increases, not decreases
- "Works but needs babysitting" is accepted state

**Root Causes:**
- Automations treated as one-time builds, not evolving systems
- No feedback loop from execution to improvement
- Error logs discarded instead of mined for patterns
- No patch/upgrade mechanism in automation design

**Evidence from Practice:**
| System Type | Error Recurrence | Improvement Rate | Maintenance Hours/Week |
|-------------|------------------|------------------|----------------------|
| Static automation | 67% recurrence | 0% (manual only) | 8-12 hours |
| Self-improving (Heal & Renew) | 12% recurrence | 15% monthly | 2-3 hours |

**Strategic Implications:**
- Static automations become liabilities, not assets
- Maintenance burden grows linearly with automation count
- Knowledge trapped in individual heads, not systems
- Competitive advantage erodes as automations age

**The Doctrine Response:**
> Attach logs, self-annealing instructions, and patch hooks so automations can propose and adopt upgrades to skills, SOPs, and routing rules.

---

## 1.3 THE COST OF INACTION

Organizations that don't address these five pains face compounding costs:

| Year | Visual Spaghetti | Schema Bloat | Tool-First | LLM-Only | Static Systems | TOTAL |
|------|------------------|--------------|------------|----------|----------------|-------|
| Y1 | $15K | $8K | $12K | $20K | $10K | $65K |
| Y2 | $35K | $22K | $28K | $45K | $25K | $155K |
| Y3 | $80K | $50K | $65K | $95K | $55K | $345K |

*Costs include: debugging time, failed automations, vendor fees, token costs, maintenance labor, and opportunity cost of unreliable systems.*

---

## 1.4 THE MASTER AUTOMATIONS ARCHITECT SOLUTION

This module addresses all five pains through a unified doctrine:

| Pain | Solution | Mechanism |
|------|----------|-----------|
| Visual Spaghetti | PCE Orchestration | SOP markdown + coordination + deterministic scripts |
| Schema Bloat | Zero-Point Context | ~500 token default, on-demand activation |
| Tool-First | Workflow-First Design | Double-II pattern (information + implementation) |
| LLM-Only Execution | Skills + Scripts | Deterministic execution layer behind LLM orchestration |
| Static Systems | Heal & Renew | Logs → patches → upgrades loop |

**The Core Thesis (5 Principles):**

1. **Skills + Scripts > MCPs** — 80% of MCPs can be replaced with on-demand scripts
2. **Zero-Point Context is Default** — Load heavy schemas only when needed
3. **IDE- and Code-First (PCE)** — SOP markdown + coordination + deterministic scripts
4. **Tool Choice is Topology** — Pick based on context cost, complexity, control, compliance
5. **Meta-Systems for Self-Improvement** — Automations that improve themselves

---

# SECTION 2: MODULE BLUEPRINT
## The Four-Phase Automation Design Workflow

*"The Automation Architect's real job is tool choice and topology: picking between skills, CLI, code execution, and MCPs based on context cost, complexity, control, and compliance—not just wiring more tools into one agent."*

---

## 2.1 WORKFLOW OVERVIEW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AUTOMATION DESIGN WORKFLOW                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PHASE 1: DISCOVER & CLASSIFY ──► PHASE 2: DESIGN TOPOLOGY                  │
│        (Day 1 AM, 2 hours)              (Day 1 PM, 3 hours)                 │
│              │                                │                              │
│              ▼                                ▼                              │
│  PHASE 3: GENERATE BLUEPRINT ──► PHASE 4: VALIDATE & SHIP                   │
│        (Day 2 AM, 2 hours)              (Day 2 PM, 2 hours)                 │
│                                                                              │
│  TOTAL: 9 hours across 2 days (or 1 intensive day)                          │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 2.2 PHASE 1: DISCOVER & CLASSIFY
### Day 1, Morning (9:00 AM - 11:00 AM) — 2 Hours

**Objective:** Understand the automation requirement and classify it for appropriate treatment.

---

#### Step 1.1: Clarify Business Requirement (30 minutes)

**Actions:**
- Ask structured discovery questions
- Document in natural language before any technical decisions
- Identify success criteria (what does "working" mean?)

**Discovery Questions Template:**
```markdown
## AUTOMATION REQUIREMENT DISCOVERY

### WHO
- Who initiates this automation? (human trigger, webhook, schedule)
- Who consumes the output? (human, system, API)
- Who maintains it? (technical level of maintainer)

### WHAT
- What is the core transformation? (input → output)
- What systems are involved? (list all)
- What data moves between systems?

### WHEN
- How often does this run? (on-demand, hourly, daily, event-driven)
- What's the latency requirement? (real-time, batch, async)
- What's the volume? (1/day, 100/day, 10,000/day)

### SUCCESS CRITERIA
- How do we know it worked? (specific measurable outcome)
- What's the acceptable failure rate? (0%, <1%, <5%)
- What happens on failure? (retry, alert, fallback)
```

**Output:** REQUIREMENT_BRIEF (structured document)

**Tools:** Structured interview template, project brief schema

**Quality Gate:** Requirement is specific enough to estimate scope

---

#### Step 1.2: Map Current State (30 minutes)

**Actions:**
- If migration: Export existing workflow (n8n JSON, Zapier config)
- If greenfield: Document current manual process
- Identify data flows, decision points, error handling

**Current State Mapping Template:**
```markdown
## CURRENT STATE MAP

### Existing Automation (if any)
- Platform: [n8n / Zapier / Make / Custom / Manual]
- Node/Step count: [number]
- Last modified: [date]
- Known issues: [list]

### Data Flow
- Sources: [list input systems]
- Transformations: [list processing steps]
- Destinations: [list output systems]

### Decision Points
- [Condition 1]: [Action A] or [Action B]
- [Condition 2]: [Action C] or [Action D]

### Error Handling
- Current approach: [describe]
- Known failure modes: [list]
- Recovery process: [describe]
```

**Output:** CURRENT_STATE_MAP

**Tools:** n8n export, process documentation, system diagrams

**Quality Gate:** All systems and data flows identified

---

#### Step 1.3: Classify Automation Type (30 minutes)

**Actions:**
- Apply classification framework
- Determine scope (one-off, reusable, production)
- Assess complexity axes

**Classification Framework:**

| Dimension | Low | Medium | High |
|-----------|-----|--------|------|
| **Context Intensity** | <1,000 tokens | 1,000-5,000 tokens | >5,000 tokens |
| **System Count** | 1-2 systems | 3-5 systems | 6+ systems |
| **Decision Complexity** | Linear flow | 2-3 branches | Complex DAG |
| **Failure Criticality** | Retry OK | Alert needed | Must not fail |
| **Volume** | <10/day | 10-1,000/day | >1,000/day |

**Scope Classification:**

| Scope | Definition | Treatment |
|-------|------------|-----------|
| **One-off** | Run once, discard | Quick script, minimal documentation |
| **Reusable** | Run multiple times, same context | Skill + script, moderate docs |
| **Production** | Business-critical, multi-context | Full PCE stack, comprehensive docs |

**Output:** AUTOMATION_CLASSIFICATION

**Tools:** Classification matrix, complexity scoring

**Quality Gate:** Classification determines Phase 2 approach

---

#### Step 1.4: Identify Constraints & Risks (30 minutes)

**Actions:**
- Document technical constraints
- Identify compliance requirements
- Assess risks and mitigation strategies

**Constraints Checklist:**
```markdown
## CONSTRAINTS & RISKS

### Technical Constraints
- [ ] API rate limits: [specify]
- [ ] Authentication complexity: [OAuth / API key / Session]
- [ ] Data format requirements: [JSON / XML / CSV / Custom]
- [ ] Platform limitations: [list]

### Compliance Requirements
- [ ] Data privacy: [GDPR / CCPA / HIPAA / None]
- [ ] Data residency: [geographic requirements]
- [ ] Audit trail: [required / not required]
- [ ] PII handling: [anonymization needed?]

### Risk Assessment
| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | [H/M/L] | [H/M/L] | [Strategy] |
| [Risk 2] | [H/M/L] | [H/M/L] | [Strategy] |

### Dependencies
- External services: [list with SLA info]
- Internal systems: [list with owners]
- Human approvals: [list decision points]
```

**Output:** CONSTRAINTS_RISKS document

**Tools:** Risk assessment template, compliance checklist

**Quality Gate:** No unknown constraints, all risks have mitigation

---

### Phase 1 Deliverables Summary

| Deliverable | Content | Token Budget |
|-------------|---------|--------------|
| REQUIREMENT_BRIEF | Who, what, when, success criteria | ~200 tokens |
| CURRENT_STATE_MAP | Systems, data flows, decision points | ~300 tokens |
| AUTOMATION_CLASSIFICATION | Scope, complexity scores | ~100 tokens |
| CONSTRAINTS_RISKS | Technical, compliance, risk matrix | ~200 tokens |

**Total Phase 1 Context:** ~800 tokens (fits in Zero-Point activation)

---

## 2.3 PHASE 2: DESIGN TOPOLOGY
### Day 1, Afternoon (1:00 PM - 4:00 PM) — 3 Hours

**Objective:** Make tool selection decisions and design the automation architecture.

---

#### Step 2.1: Apply Tool Decision Matrix (45 minutes)

**Actions:**
- For each system/operation, apply the 4-level decision framework
- Document decisions with rationale
- Identify any MCP escalations needed

**Tool Decision Matrix:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      TOOL DECISION MATRIX                                   │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  LEVEL 1: BROWSER AUTOMATION (Default for scraping/interaction)             │
│  ─────────────────────────────────────────────────────────────              │
│  When: No API exists, API expensive/limited, need human-like behavior       │
│  Tools: Playwright, Puppeteer, Browser-use patterns                         │
│  Token Cost: ~100 tokens (thin skill descriptor)                            │
│                                                                              │
│  LEVEL 2: LEAN API (Default for write operations)                           │
│  ─────────────────────────────────────────────────────────────              │
│  When: Official API available, need write access, reliability matters       │
│  Pattern: Single-file script with fetch/axios, no SDK bloat                 │
│  Token Cost: ~50 tokens (endpoint + params)                                 │
│                                                                              │
│  LEVEL 3: CUSTOM INTERFACE (When user interaction needed)                   │
│  ─────────────────────────────────────────────────────────────              │
│  When: User configuration, human-in-loop, visualization needed              │
│  Output: React artifact (Tailwind + shadcn)                                 │
│  Token Cost: ~200 tokens (component spec)                                   │
│                                                                              │
│  LEVEL 4: LEAN MCP (Only when absolutely required)                          │
│  ─────────────────────────────────────────────────────────────              │
│  When: Complex OAuth, persistent connections, multi-tenant state            │
│  Pattern: Minimal schema, load/unload on demand                             │
│  Token Cost: ~500-2,000 tokens (unavoidable)                                │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Decision Documentation Template:**
```yaml
TOOL_DECISIONS:
  
  operation_1:
    name: "Scrape LinkedIn profiles"
    decision: BROWSER_AUTOMATION
    rationale: "No official API for profile scraping, need human-like behavior"
    tool: "Playwright"
    script: "scrape_linkedin.py"
    token_cost: 100
  
  operation_2:
    name: "Send follow-up emails"
    decision: LEAN_API
    rationale: "Resend API is reliable, need delivery tracking"
    tool: "Resend API"
    script: "send_email.py"
    token_cost: 50
  
  operation_3:
    name: "Configure campaign settings"
    decision: CUSTOM_INTERFACE
    rationale: "User needs to set parameters before execution"
    tool: "React + Tailwind"
    component: "campaign_settings.jsx"
    token_cost: 200
  
  total_token_budget: 350
  mcp_count: 0
  mcp_escalation_needed: false
```

**Output:** TOOL_DECISIONS document

**Tools:** Decision matrix, tool comparison charts

**Quality Gate:** Every operation has justified tool selection

---

#### Step 2.2: Detect Anti-Patterns (30 minutes)

**Actions:**
- Review proposed design against 7 anti-patterns
- Flag any violations
- Propose corrections

**Anti-Pattern Detection Checklist:**

| # | Anti-Pattern | Detection Signal | Correction |
|---|--------------|------------------|------------|
| 1 | **Visual Spaghetti** | >15 steps/nodes | Convert to PCE (SOP + scripts) |
| 2 | **Schema Bloat** | Zero-Point >500 tokens | Wrap tools as skills, load on-demand |
| 3 | **Tool-First Architecture** | Design started with "what tools?" | Redesign from workflow, not tools |
| 4 | **Monolithic Super-Agent** | Single agent does everything | Split into specialized sub-agents |
| 5 | **LLM-Only Execution** | No deterministic scripts | Add script layer behind LLM |
| 6 | **Context Dumping** | Full logs/HTML in context | Store externally, reference by ID |
| 7 | **Static Non-Learning** | No Heal & Renew hooks | Add logging + patch proposal mechanism |

**Anti-Pattern Report Template:**
```markdown
## ANTI-PATTERN DETECTION REPORT

### Detected Violations
| Anti-Pattern | Location | Severity | Correction |
|--------------|----------|----------|------------|
| [Name] | [Where in design] | [High/Med/Low] | [Fix] |

### Design Health Score
- Violations: [count] / 7
- Severity-weighted: [score] / 10
- Recommendation: [Proceed / Revise / Redesign]

### Corrections Applied
1. [Correction 1]: [Description of change]
2. [Correction 2]: [Description of change]
```

**Output:** ANTI_PATTERN_REPORT

**Tools:** Anti-pattern checklist, severity scoring

**Quality Gate:** No high-severity violations, all medium corrected

---

#### Step 2.3: Design PCE Structure (60 minutes)

**Actions:**
- Define Planning layer (SOP markdown)
- Design Coordination layer (orchestration logic)
- Specify Execution layer (deterministic scripts)

**PCE Architecture Template:**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        PCE ORCHESTRATION STACK                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PLANNING LAYER (SOP.md)                                                    │
│  ────────────────────────                                                   │
│  - Human-readable workflow description                                      │
│  - Step sequence with decision points                                       │
│  - Success criteria per step                                                │
│  - Error handling procedures                                                │
│                                                                              │
│  COORDINATION LAYER (coordinator.py)                                        │
│  ────────────────────────────────────                                       │
│  - Step sequencing logic                                                    │
│  - Parallelization decisions                                                │
│  - Retry/fallback handling                                                  │
│  - State management                                                         │
│  - Logging and monitoring                                                   │
│                                                                              │
│  EXECUTION LAYER (scripts/*.py)                                             │
│  ─────────────────────────────                                              │
│  - One script per atomic operation                                          │
│  - Deterministic input → output                                             │
│  - Explicit error handling                                                  │
│  - Testable in isolation                                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**PCE Design Document Template:**
```yaml
PCE_DESIGN:
  
  planning:
    sop_file: "SOP.md"
    sections:
      - overview: "What this automation does"
      - prerequisites: "What must be true before running"
      - steps: "Numbered step sequence"
      - decision_points: "Branching logic"
      - error_handling: "What to do when things fail"
      - success_criteria: "How to know it worked"
  
  coordination:
    coordinator_file: "coordinator.py"
    responsibilities:
      - step_sequencing: "Execute steps in order with dependencies"
      - parallelization: "Run independent steps concurrently"
      - retry_logic: "Exponential backoff, max 3 attempts"
      - state_management: "Track progress, enable resume"
      - logging: "Structured logs for debugging and learning"
  
  execution:
    scripts:
      - name: "fetch_data.py"
        input: "config.yaml (sources, credentials)"
        output: "raw_data.json"
        error_handling: "Retry with backoff, fail after 3"
      
      - name: "transform_data.py"
        input: "raw_data.json"
        output: "processed_data.json"
        error_handling: "Log malformed records, continue"
      
      - name: "send_output.py"
        input: "processed_data.json"
        output: "delivery_report.json"
        error_handling: "Queue failed items for retry"
```

**Output:** PCE_DESIGN document

**Tools:** PCE template, script scaffolding

**Quality Gate:** All three layers defined, scripts identified

---

#### Step 2.4: Define Integration Points (45 minutes)

**Actions:**
- Map data flows between systems
- Define SSOT contracts
- Specify handoffs to other modules (2-8)

**Integration Map Template:**
```yaml
INTEGRATION_MAP:
  
  data_flows:
    - source: "LinkedIn (via Playwright)"
      destination: "LEAD_RAW_LIST"
      format: "JSON"
      frequency: "On-demand"
    
    - source: "LEAD_RAW_LIST"
      destination: "content_analyzer (Module 5)"
      format: "JSON"
      frequency: "Per lead batch"
    
    - source: "content_analyzer"
      destination: "LEAD_ENRICHED"
      format: "JSON"
      frequency: "Per analysis"
  
  ssot_contracts:
    LEAD_RAW_LIST:
      schema_ref: "schemas/lead_raw.yaml"
      owner: "lead_gen_engine"
      consumers: ["content_analyzer", "outreach_orchestrator"]
    
    LEAD_ENRICHED:
      schema_ref: "schemas/lead_enriched.yaml"
      owner: "content_analyzer"
      consumers: ["outreach_orchestrator", "onboarding_automator"]
  
  module_handoffs:
    - from: "Module 1 (this)"
      to: "Module 2 (Automation Builder)"
      artifact: "AUTOMATION_BLUEPRINT"
      trigger: "Blueprint approved"
    
    - from: "Module 1 (this)"
      to: "Module 3 (N8N Translator)"
      artifact: "MIGRATION_PLAN"
      trigger: "Legacy workflow identified"
```

**Output:** INTEGRATION_MAP

**Tools:** Data flow diagrams, SSOT schema definitions

**Quality Gate:** All handoffs defined, no orphan data flows

---

### Phase 2 Deliverables Summary

| Deliverable | Content | Token Budget |
|-------------|---------|--------------|
| TOOL_DECISIONS | Operation → tool mapping with rationale | ~400 tokens |
| ANTI_PATTERN_REPORT | Violations detected and corrected | ~200 tokens |
| PCE_DESIGN | Planning + Coordination + Execution specs | ~500 tokens |
| INTEGRATION_MAP | Data flows, SSOT contracts, module handoffs | ~300 tokens |

**Total Phase 2 Context:** ~1,400 tokens

---

## 2.4 PHASE 3: GENERATE BLUEPRINT
### Day 2, Morning (9:00 AM - 11:00 AM) — 2 Hours

**Objective:** Produce the complete AUTOMATION_BLUEPRINT for handoff to execution modules.

---

#### Step 3.1: Compile Blueprint Document (60 minutes)

**Actions:**
- Merge all Phase 1 and Phase 2 outputs
- Structure into AUTOMATION_BLUEPRINT format
- Add execution timeline and milestones

**AUTOMATION_BLUEPRINT Structure:**
```yaml
AUTOMATION_BLUEPRINT:
  
  # ═══════════════════════════════════════════════════════════════════════
  # HEADER
  # ═══════════════════════════════════════════════════════════════════════
  
  metadata:
    blueprint_id: "BP-2026-001"
    version: "1.0.0"
    created: "2026-01-23"
    author: "Master Automations Architect"
    status: "Ready for Build"
  
  # ═══════════════════════════════════════════════════════════════════════
  # REQUIREMENT SUMMARY (from Phase 1)
  # ═══════════════════════════════════════════════════════════════════════
  
  requirement:
    name: "Lead Generation Pipeline"
    description: "Discover and enrich leads from LinkedIn and Instagram"
    trigger: "Manual or scheduled (daily 9am)"
    output: "Enriched lead list with content analysis"
    success_criteria: "100 qualified leads per run"
    
    classification:
      scope: "production"
      context_intensity: "medium"
      system_count: 4
      decision_complexity: "medium"
      failure_criticality: "high"
      volume: "100/day"
  
  # ═══════════════════════════════════════════════════════════════════════
  # TOOL DECISIONS (from Phase 2)
  # ═══════════════════════════════════════════════════════════════════════
  
  tool_decisions:
    linkedin_scraping:
      level: "BROWSER_AUTOMATION"
      tool: "Playwright"
      rationale: "No API, need human-like behavior"
    
    instagram_scraping:
      level: "BROWSER_AUTOMATION"
      tool: "Playwright"
      rationale: "API limited, need profile data"
    
    content_analysis:
      level: "LLM_SKILL"
      tool: "content_analyzer (Module 5)"
      rationale: "Pattern extraction requires LLM"
    
    data_storage:
      level: "LEAN_API"
      tool: "Supabase"
      rationale: "Simple CRUD, no complex queries"
    
    dashboard:
      level: "CUSTOM_INTERFACE"
      tool: "React + Tailwind"
      rationale: "User needs to review and approve leads"
  
  # ═══════════════════════════════════════════════════════════════════════
  # PCE ARCHITECTURE (from Phase 2)
  # ═══════════════════════════════════════════════════════════════════════
  
  pce_architecture:
    planning:
      sop_file: "lead_gen_pipeline_SOP.md"
      
    coordination:
      coordinator_file: "lead_gen_coordinator.py"
      parallelization:
        - "linkedin_scrape || instagram_scrape"  # Run in parallel
        - "content_analysis (sequential per lead)"
      retry_policy:
        max_attempts: 3
        backoff: "exponential"
        
    execution:
      scripts:
        - "discover_linkedin_leads.py"
        - "discover_instagram_leads.py"
        - "merge_and_dedupe.py"
        - "analyze_content.py"
        - "score_and_rank.py"
        - "export_to_dashboard.py"
  
  # ═══════════════════════════════════════════════════════════════════════
  # EXECUTION TIMELINE
  # ═══════════════════════════════════════════════════════════════════════
  
  timeline:
    build_phase:
      duration: "3 days"
      milestones:
        day_1: "Scripts scaffolded, basic execution working"
        day_2: "Coordinator integrated, error handling complete"
        day_3: "Dashboard connected, end-to-end tested"
    
    deployment:
      target: "Production"
      rollout: "Staged (10% → 50% → 100%)"
      monitoring: "Logs to Supabase, alerts to Slack"
  
  # ═══════════════════════════════════════════════════════════════════════
  # HANDOFFS
  # ═══════════════════════════════════════════════════════════════════════
  
  handoffs:
    to_module_2:
      artifact: "This AUTOMATION_BLUEPRINT"
      action: "Generate SOP + coordinator + scripts"
    
    to_module_4:
      artifact: "BROWSER_TASKS section"
      action: "Implement Playwright scripts"
    
    to_module_5:
      artifact: "CONTENT_ANALYSIS section"
      action: "Run pattern extraction"
    
    to_module_7:
      artifact: "INTERFACE_SPEC section"
      action: "Generate React dashboard"
```

**Output:** AUTOMATION_BLUEPRINT (complete)

**Tools:** Blueprint compiler, YAML validator

**Quality Gate:** Blueprint passes schema validation

---

#### Step 3.2: Generate Interface Spec (30 minutes)

**Actions:**
- If custom interface needed, specify components
- Define user interactions
- Specify data bindings

**INTERFACE_SPEC Template:**
```yaml
INTERFACE_SPEC:
  
  type: "dashboard"
  framework: "React + Tailwind + shadcn"
  
  components:
    lead_table:
      type: "DataTable"
      columns:
        - name: "string"
        - platform: "enum[linkedin, instagram]"
        - score: "number"
        - status: "enum[new, reviewed, approved, rejected]"
      actions:
        - "approve"
        - "reject"
        - "view_details"
    
    filters:
      type: "FilterPanel"
      filters:
        - field: "platform"
          type: "multi-select"
        - field: "score"
          type: "range"
        - field: "status"
          type: "multi-select"
    
    detail_modal:
      type: "Modal"
      content:
        - "lead_profile"
        - "content_samples"
        - "analysis_results"
        - "outreach_suggestions"
  
  data_bindings:
    source: "Supabase:leads"
    refresh: "real-time"
    
  user_flows:
    review_lead:
      steps:
        1: "Click row in lead_table"
        2: "View detail_modal"
        3: "Click approve/reject"
        4: "Lead moves to next status"
```

**Output:** INTERFACE_SPEC (if needed)

**Tools:** Component library reference, UI patterns

**Quality Gate:** All user interactions defined

---

#### Step 3.3: Define Validation Plan (30 minutes)

**Actions:**
- Specify test scenarios
- Define success metrics
- Plan monitoring approach

**VALIDATION_PLAN Template:**
```yaml
VALIDATION_PLAN:
  
  test_scenarios:
    unit_tests:
      - script: "discover_linkedin_leads.py"
        test: "Returns valid lead objects"
        mock: "Sample HTML response"
      
      - script: "analyze_content.py"
        test: "Extracts patterns from samples"
        mock: "Sample content array"
    
    integration_tests:
      - flow: "LinkedIn → Analysis → Dashboard"
        test: "Leads appear in UI with scores"
        data: "10 test profiles"
      
      - flow: "Error handling"
        test: "Failed scrapes don't crash pipeline"
        trigger: "Simulate rate limit"
    
    end_to_end:
      - scenario: "Full daily run"
        test: "100 leads processed in <1 hour"
        success: "95% completion rate"
  
  success_metrics:
    - metric: "Leads discovered per run"
      target: ">= 100"
      measurement: "Count in LEAD_RAW_LIST"
    
    - metric: "Analysis completion rate"
      target: ">= 95%"
      measurement: "Analyzed / Discovered"
    
    - metric: "Execution time"
      target: "< 60 minutes"
      measurement: "Start to finish timestamp"
    
    - metric: "Error rate"
      target: "< 5%"
      measurement: "Failed operations / Total"
  
  monitoring:
    logs:
      destination: "Supabase:automation_logs"
      retention: "30 days"
      
    alerts:
      channel: "Slack #automation-alerts"
      triggers:
        - "Error rate > 10%"
        - "Execution time > 90 minutes"
        - "Zero leads discovered"
    
    dashboards:
      - "Daily run summary"
      - "Error trend analysis"
      - "Lead quality metrics"
```

**Output:** VALIDATION_PLAN

**Tools:** Test framework templates, monitoring setup guides

**Quality Gate:** All critical paths have test coverage

---

### Phase 3 Deliverables Summary

| Deliverable | Content | Token Budget |
|-------------|---------|--------------|
| AUTOMATION_BLUEPRINT | Complete build specification | ~800 tokens |
| INTERFACE_SPEC | UI component definitions (if needed) | ~300 tokens |
| VALIDATION_PLAN | Tests, metrics, monitoring | ~400 tokens |

**Total Phase 3 Context:** ~1,500 tokens

---

## 2.5 PHASE 4: VALIDATE & SHIP
### Day 2, Afternoon (1:00 PM - 3:00 PM) — 2 Hours

**Objective:** Final validation and handoff to execution modules.

---

#### Step 4.1: Blueprint Review Checklist (30 minutes)

**Actions:**
- Walk through complete blueprint
- Verify all sections complete
- Check cross-references

**Blueprint Review Checklist:**
```markdown
## BLUEPRINT REVIEW CHECKLIST

### Completeness
- [ ] Requirement clearly stated with success criteria
- [ ] All systems and operations identified
- [ ] Tool decision for each operation (with rationale)
- [ ] PCE architecture fully specified
- [ ] Integration points defined
- [ ] Timeline and milestones set
- [ ] Handoffs to other modules specified

### Consistency
- [ ] Tool decisions align with classification
- [ ] Token budget within Zero-Point limits
- [ ] No anti-patterns present (or documented exceptions)
- [ ] Data flows have matching schemas
- [ ] Error handling specified at all layers

### Feasibility
- [ ] All tools available/accessible
- [ ] Timeline realistic for scope
- [ ] Team has required skills
- [ ] Dependencies identified and manageable

### Quality
- [ ] Follows PCE pattern correctly
- [ ] Heal & Renew hooks present
- [ ] Logging sufficient for debugging
- [ ] Monitoring covers critical metrics
```

**Output:** REVIEW_CHECKLIST (completed)

**Tools:** Review checklist template

**Quality Gate:** All items checked or exceptions documented

---

#### Step 4.2: Stakeholder Approval (30 minutes)

**Actions:**
- Present blueprint summary
- Address questions/concerns
- Get explicit approval

**Approval Request Template:**
```markdown
## BLUEPRINT APPROVAL REQUEST

### Blueprint Summary
- **Name:** [Automation name]
- **Scope:** [One-off / Reusable / Production]
- **Build Time:** [Days]
- **Token Budget:** [Tokens]

### Key Decisions
1. [Decision 1]: [Choice] because [rationale]
2. [Decision 2]: [Choice] because [rationale]
3. [Decision 3]: [Choice] because [rationale]

### Resource Requirements
- Build time: [X days]
- Skills needed: [List]
- External services: [List with costs]

### Risks & Mitigations
| Risk | Mitigation |
|------|------------|
| [Risk 1] | [Mitigation] |

### Approval
- [ ] Approved to proceed
- [ ] Approved with changes: [specify]
- [ ] Rejected: [reason]

Approver: _________________ Date: _________
```

**Output:** APPROVAL_RECORD

**Tools:** Approval workflow

**Quality Gate:** Explicit approval recorded

---

#### Step 4.3: Handoff Execution (60 minutes)

**Actions:**
- Package deliverables for each receiving module
- Create handoff tickets/tasks
- Brief receiving teams

**Handoff Package Structure:**
```
handoff/
├── AUTOMATION_BLUEPRINT.yaml          # Main blueprint
├── INTERFACE_SPEC.yaml                # UI specs (if any)
├── VALIDATION_PLAN.yaml               # Test plan
├── APPROVAL_RECORD.md                 # Stakeholder sign-off
│
├── module_2_package/                  # For Automation Builder
│   ├── BLUEPRINT_SUBSET.yaml          # Relevant sections
│   └── BUILD_INSTRUCTIONS.md          # What to generate
│
├── module_4_package/                  # For Browser Automation
│   ├── BROWSER_TASKS.yaml             # Scraping requirements
│   └── PLATFORM_CONFIGS.yaml          # Platform-specific settings
│
├── module_5_package/                  # For Content Analyzer
│   ├── ANALYSIS_REQUIREMENTS.yaml     # What to extract
│   └── SAMPLE_CONTENT.json            # Test data
│
└── module_7_package/                  # For Interface Generator
    ├── INTERFACE_SPEC.yaml            # Complete spec
    └── DATA_SCHEMA.yaml               # Data to display
```

**Handoff Communication Template:**
```markdown
## HANDOFF: [Blueprint Name] → [Module Name]

### Package Location
[Path to handoff package]

### What You're Receiving
- [Artifact 1]: [Description]
- [Artifact 2]: [Description]

### What You're Producing
- [Deliverable 1]: [Description]
- [Deliverable 2]: [Description]

### Timeline
- Start: [Date]
- Due: [Date]

### Questions?
Contact: [Owner]

### Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]
```

**Output:** HANDOFF_PACKAGES (per module)

**Tools:** File packaging, task management

**Quality Gate:** All receiving modules acknowledge receipt

---

### Phase 4 Deliverables Summary

| Deliverable | Content | Token Budget |
|-------------|---------|--------------|
| REVIEW_CHECKLIST | Completed validation checklist | ~100 tokens |
| APPROVAL_RECORD | Stakeholder sign-off | ~100 tokens |
| HANDOFF_PACKAGES | Module-specific packages | ~200 tokens each |

**Total Phase 4 Context:** ~600 tokens

---

## 2.6 WORKFLOW SUMMARY

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    COMPLETE WORKFLOW SUMMARY                                │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  PHASE 1: DISCOVER & CLASSIFY (Day 1, 9am-11am, 2 hours)                    │
│  ──────────────────────────────────────────────────────                     │
│  Step 1.1: Clarify Business Requirement (30 min)                            │
│  Step 1.2: Map Current State (30 min)                                       │
│  Step 1.3: Classify Automation Type (30 min)                                │
│  Step 1.4: Identify Constraints & Risks (30 min)                            │
│  → Outputs: REQUIREMENT_BRIEF, CURRENT_STATE_MAP,                           │
│             AUTOMATION_CLASSIFICATION, CONSTRAINTS_RISKS                     │
│                                                                              │
│  PHASE 2: DESIGN TOPOLOGY (Day 1, 1pm-4pm, 3 hours)                         │
│  ──────────────────────────────────────────────────                         │
│  Step 2.1: Apply Tool Decision Matrix (45 min)                              │
│  Step 2.2: Detect Anti-Patterns (30 min)                                    │
│  Step 2.3: Design PCE Structure (60 min)                                    │
│  Step 2.4: Define Integration Points (45 min)                               │
│  → Outputs: TOOL_DECISIONS, ANTI_PATTERN_REPORT,                            │
│             PCE_DESIGN, INTEGRATION_MAP                                      │
│                                                                              │
│  PHASE 3: GENERATE BLUEPRINT (Day 2, 9am-11am, 2 hours)                     │
│  ──────────────────────────────────────────────────────                     │
│  Step 3.1: Compile Blueprint Document (60 min)                              │
│  Step 3.2: Generate Interface Spec (30 min)                                 │
│  Step 3.3: Define Validation Plan (30 min)                                  │
│  → Outputs: AUTOMATION_BLUEPRINT, INTERFACE_SPEC, VALIDATION_PLAN           │
│                                                                              │
│  PHASE 4: VALIDATE & SHIP (Day 2, 1pm-3pm, 2 hours)                         │
│  ─────────────────────────────────────────────────                          │
│  Step 4.1: Blueprint Review Checklist (30 min)                              │
│  Step 4.2: Stakeholder Approval (30 min)                                    │
│  Step 4.3: Handoff Execution (60 min)                                       │
│  → Outputs: REVIEW_CHECKLIST, APPROVAL_RECORD, HANDOFF_PACKAGES             │
│                                                                              │
│  TOTAL: 9 hours across 2 days (or 1 intensive day)                          │
│  TOKEN BUDGET: ~4,300 tokens total context                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

# SECTION 3: KNOWLEDGE BLOCKS
## Decision Frameworks and Heuristics

*"Think of Zero-Point as a calm, quiet control room: only bring heavy machinery online when it's actually needed, then shut it down and file the report."*

---

## 3.1 TOOL DECISION MATRIX (Complete)

### Level 1: Browser Automation

**When to Use:**
- No official API exists
- API is rate-limited or expensive
- Need to mimic human behavior
- Scraping public data
- Form submissions requiring JavaScript

**Tools:**
| Tool | Best For | Considerations |
|------|----------|----------------|
| Playwright | Cross-browser, complex flows | Recommended default |
| Puppeteer | Chrome-specific, simpler | Lighter weight |
| Browser-use MCP | AI-guided navigation | When paths are unpredictable |

**Token Cost:** ~100 tokens (thin skill descriptor)

**Script Template:**
```python
# scripts/browser_scrape.py
from playwright.async_api import async_playwright

async def scrape_profile(url: str) -> dict:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url)
        
        # Extract data
        data = await page.evaluate('''() => {
            return {
                name: document.querySelector('.name')?.textContent,
                bio: document.querySelector('.bio')?.textContent,
                // ... more selectors
            }
        }''')
        
        await browser.close()
        return data
```

---

### Level 2: Lean API

**When to Use:**
- Official API is available and reasonable
- Need write access (post, send, create)
- Reliability matters more than cost
- Rate limits are acceptable

**Pattern:** Single-file script with fetch/axios, no SDK bloat

**Token Cost:** ~50 tokens (endpoint + params)

**Script Template:**
```python
# scripts/lean_api.py
import httpx

async def send_email(to: str, subject: str, body: str) -> dict:
    """Send email via Resend API - no SDK, just the endpoint."""
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://api.resend.com/emails",
            headers={"Authorization": f"Bearer {API_KEY}"},
            json={
                "from": "noreply@example.com",
                "to": to,
                "subject": subject,
                "html": body
            }
        )
        return response.json()
```

**Anti-Pattern to Avoid:**
```python
# DON'T do this - SDK bloat
from resend import Resend
client = Resend(api_key=API_KEY)
# SDK adds 500+ tokens of context for simple operations
```

---

### Level 3: Custom Interface

**When to Use:**
- User needs to configure parameters
- Workflow requires human-in-the-loop
- Visualization of results needed
- Multi-step wizard flows

**Interface Types:**

| Type | Trigger Signal | Components |
|------|---------------|------------|
| Dashboard | "I need to see/monitor..." | DataTable, Charts, Filters |
| Wizard | "Walk me through..." | StepIndicator, Forms, Navigation |
| Selector | "I want to choose..." | OptionCards, Preview, Confirm |
| Form | "Configure/set up..." | InputFields, Validation, Submit |

**Token Cost:** ~200 tokens (component spec)

**Component Template:**
```jsx
// components/LeadDashboard.jsx
import { DataTable, FilterPanel, Card } from '@/components/ui';

export function LeadDashboard({ leads, onApprove, onReject }) {
  const [filters, setFilters] = useState({});
  
  const filteredLeads = useMemo(() => 
    leads.filter(lead => matchesFilters(lead, filters)),
    [leads, filters]
  );
  
  return (
    <div className="p-6 space-y-4">
      <FilterPanel filters={filters} onChange={setFilters} />
      <DataTable 
        data={filteredLeads}
        columns={columns}
        actions={[
          { label: 'Approve', onClick: onApprove },
          { label: 'Reject', onClick: onReject }
        ]}
      />
    </div>
  );
}
```

---

### Level 4: Lean MCP

**When to Use (Only These Cases):**
- Complex OAuth flow required (Google, Microsoft)
- Persistent connection needed (websockets, real-time)
- Multi-tenant with user credentials
- Heavy state management across sessions

**Build Pattern:**
- Minimal schema exposure
- Load only when invoked
- Unload after operation
- Never always-on

**Token Cost:** ~500-2,000 tokens (unavoidable overhead)

**Lean MCP Template:**
```yaml
# mcp/google_oauth.yaml
name: "google_oauth"
load_trigger: "Google API operation requested"
unload_after: "Operation complete"

schema:
  # MINIMAL - only what's needed
  authenticate:
    scopes: ["sheets.readonly", "drive.readonly"]
  
  operations:
    - read_sheet
    - list_files

# Full schema loaded only during operation
full_schema_file: "mcp/google_oauth_full.yaml"
```

---

## 3.2 ANTI-PATTERN DETECTION FRAMEWORK

### Anti-Pattern #1: Visual Spaghetti

**Detection Signals:**
- Workflow has >15 nodes/steps
- Multiple crossing connection lines
- Duplicate logic in different branches
- Comments like "don't touch this"

**Severity Score:**
| Nodes | Severity | Action |
|-------|----------|--------|
| 15-20 | Medium | Review for refactoring opportunities |
| 21-30 | High | Must convert to PCE before deployment |
| 30+ | Critical | Stop: Cannot be maintained, redesign required |

**Recovery Procedure:**
1. Export workflow to text/JSON
2. Identify atomic operations (nodes → scripts)
3. Extract decision logic (branches → coordinator)
4. Write SOP markdown (documentation)
5. Implement PCE structure
6. Validate equivalence with test cases
7. Deprecate visual workflow
8. Archive for reference

---

### Anti-Pattern #2: Schema Bloat at Zero-Point

**Detection Signals:**
- Default context >500 tokens of tool definitions
- Multiple MCPs loaded simultaneously
- Model responses slow or confused
- Token costs unexpectedly high

**Severity Score:**
| Zero-Point Tokens | Severity | Action |
|-------------------|----------|--------|
| 500-1,000 | Low | Monitor for growth |
| 1,000-2,000 | Medium | Review for skill conversion |
| 2,000-5,000 | High | Immediate MCP → Skill migration |
| 5,000+ | Critical | Urgent redesign required |

**Recovery Procedure:**
1. Audit current Zero-Point context
2. Identify bloat sources (list MCPs, schemas)
3. For each source, evaluate: Skill conversion possible?
4. Create skill wrapper with thin descriptor
5. Move full schema to on-demand loading
6. Update orchestration to activate/deactivate
7. Measure token reduction
8. Document savings for future reference

---

### Anti-Pattern #3: Tool-First Architecture

**Detection Signals:**
- Design discussions start with "what tools do we have?"
- Workflow structure mirrors tool features, not business logic
- New requirements → new tool search (not script extension)
- Heavy vendor documentation in project

**Severity Score:**
| Indicator | Severity | Action |
|-----------|----------|--------|
| Occasional tool-first thinking | Low | Training reminder |
| Design starts with tool inventory | Medium | Require workflow-first template |
| Architecture depends on specific vendor | High | Redesign with abstraction layer |
| Multiple vendor lock-ins | Critical | Strategic migration planning |

**Recovery Procedure:**
1. Document business workflow in plain language (no tools mentioned)
2. Identify each operation as input → transformation → output
3. For each operation, apply Tool Decision Matrix
4. Abstract tool-specific logic behind skill interfaces
5. Create interchangeable implementations
6. Test with different tool backends
7. Document abstraction for team
8. Add to architectural decision records

---

### Anti-Pattern #4: Monolithic Super-Agent

**Detection Signals:**
- Single agent handles >10 different task types
- Context window frequently near limit
- Agent "forgets" earlier instructions
- Debugging requires reading entire conversation

**Severity Score:**
| Task Types | Severity | Action |
|------------|----------|--------|
| 10-15 | Medium | Consider splitting |
| 15-20 | High | Split required |
| 20+ | Critical | Architecture redesign |

**Recovery Procedure:**
1. Categorize tasks by domain (research, execution, validation)
2. Design sub-agent for each domain
3. Create supervisor/router agent (lightweight)
4. Define handoff protocols between agents
5. Implement with fresh context per sub-agent
6. Test isolation and handoff
7. Monitor context usage per agent
8. Iterate on domain boundaries

---

### Anti-Pattern #5: LLM-Only Execution Layer

**Detection Signals:**
- Same automation produces different results each run
- Errors described in natural language, not codes
- No test suite exists (or tests are flaky)
- "Prompt engineering" is debugging strategy

**Severity Score:**
| Consistency Rate | Severity | Action |
|------------------|----------|--------|
| 90-95% | Low | Add validation layer |
| 80-90% | Medium | Add deterministic scripts |
| <80% | High | Redesign execution layer |

**Recovery Procedure:**
1. Identify all external interactions (API calls, DB operations)
2. For each interaction, create deterministic script
3. Define explicit input/output contracts
4. Add error handling with specific codes
5. Make LLM orchestrate scripts, not execute operations
6. Write unit tests for each script
7. Add integration tests for script sequences
8. Measure consistency improvement

---

### Anti-Pattern #6: Context Dumping

**Detection Signals:**
- Full HTML pages in conversation
- Complete log files passed to model
- PDFs/documents pasted inline
- Responses mention "based on the data you provided" for large inputs

**Severity Score:**
| Context % Used by Dumps | Severity | Action |
|-------------------------|----------|--------|
| 10-20% | Low | Consider summarization |
| 20-40% | Medium | Implement extraction pipeline |
| >40% | High | Redesign data handling |

**Recovery Procedure:**
1. Identify all large data inputs
2. For each, determine: What does the model actually need?
3. Create extraction/summarization scripts
4. Store full data externally (file, database)
5. Pass only summaries + reference IDs to model
6. Implement retrieval mechanism if full data needed
7. Measure context savings
8. Update data handling guidelines

---

### Anti-Pattern #7: Static, Non-Learning Automations

**Detection Signals:**
- Same errors recur after being "fixed"
- No changelog or version history
- "It worked last month" complaints
- Manual intervention increasing over time

**Severity Score:**
| Error Recurrence Rate | Severity | Action |
|-----------------------|----------|--------|
| 10-20% | Low | Add basic logging |
| 20-40% | Medium | Implement Heal & Renew |
| >40% | High | Fundamental redesign |

**Recovery Procedure:**
1. Implement structured logging (not just text)
2. Create error categorization taxonomy
3. Add CORRECTION_LOG to each automation run
4. Build pattern detection on logs (weekly review)
5. Create PATCH_PROPOSAL mechanism
6. Implement semi-automated upgrade path
7. Track improvement metrics over time
8. Celebrate improvements with team

---

## 3.3 HEURISTICS LIBRARY (11 Rules)

### Heuristic #1: PCE Default
```yaml
H1_PCE_DEFAULT:
  condition: "Workflow can be expressed as SOP markdown + handful of API calls"
  action: "Use PCE stack (Planning docs + coordination agent + deterministic scripts)"
  avoid: "Visual n8n flows or multi-MCP orchestration"
  rationale: "PCE provides reliability, testability, and maintainability"
```

### Heuristic #2: Token Budget Guard
```yaml
H2_TOKEN_GUARD:
  condition: "New tool would push Zero-Point context above ~500 tokens"
  action: "Wrap as skill with minimal manifest entry, load full schema only when invoked"
  avoid: "Adding tool to always-loaded context"
  rationale: "Token discipline = accuracy discipline"
```

### Heuristic #3: MCP Replacement
```yaml
H3_MCP_REPLACEMENT:
  condition: "Current MCP is thin wrapper over public APIs or CLIs"
  action: "Replace with skill-wrapped NPM/PIP/CLI scripts"
  keep_mcp_only: "For complex, multi-tenant, or strongly vendor-tuned behaviors"
  rationale: "80% of MCPs can be replaced with leaner skills"
```

### Heuristic #4: Visual Spaghetti Detection
```yaml
H4_VISUAL_SPAGHETTI:
  condition: "Workflow requires 20+ nodes in n8n"
  action: "Re-express as Double-II or PCE automation with markdown + scripts"
  avoid: "Adding more nodes"
  rationale: "Visual complexity = maintenance nightmare"
```

### Heuristic #5: Expensive Skill Demotion
```yaml
H5_SKILL_DEMOTION:
  condition: "Skill capabilities rarely used but expensive to load"
  action: "Demote to searchable tool entry, load only after explicit selection"
  trigger: "Usage <10% of sessions but >500 tokens"
  rationale: "Preserve context for frequently-used capabilities"
```

### Heuristic #6: Reusability Encoding
```yaml
H6_REUSABILITY:
  condition: "Automation will be reused across clients or projects"
  action: "Encode as information + implementation (SOP docs + scripts under version control)"
  avoid: "Ephemeral one-off prompts"
  rationale: "Reusable automations compound in value"
```

### Heuristic #7: Tool Call Batching
```yaml
H7_BATCH_TOOL_CALLS:
  condition: "Agent about to call many tools (>20) in one run"
  action: "Spawn sub-agent or helper process for batched calls and summarization"
  rationale: "Keep main agent context lean, preserve reasoning quality"
```

### Heuristic #8: New Tool Evaluation
```yaml
H8_NEW_TOOL_EVAL:
  condition: "New external tool being considered"
  first_question: "Can we express this as CLI or package wrapped by skill?"
  avoid: "Reaching for new MCP server or SaaS automation platform by default"
  rationale: "Skills provide more control and lower context cost"
```

### Heuristic #9: Browser vs API Decision
```yaml
H9_BROWSER_VS_API:
  condition: "Need to interact with external service"
  decision_tree:
    - no_api: "Use browser automation"
    - api_expensive: "Use browser automation"
    - api_limited: "Use browser automation"
    - api_available: "Use lean API (no SDK)"
  rationale: "Browser automation is often simpler than API complexity"
```

### Heuristic #10: Interface Trigger
```yaml
H10_INTERFACE_TRIGGER:
  condition: "User needs to configure, review, or interact"
  signals:
    - "I need to see...": "Dashboard"
    - "Walk me through...": "Wizard"
    - "I want to choose...": "Selector"
    - "Configure...": "Settings panel"
  action: "Generate React interface via Module 7"
  rationale: "Human-in-loop requires appropriate UI"
```

### Heuristic #11: Migration Assessment
```yaml
H11_MIGRATION_ASSESSMENT:
  condition: "Existing n8n/Zapier workflow present"
  assessment:
    - nodes_count: "<15 = consider keeping, 15-25 = migrate, >25 = must migrate"
    - error_frequency: "Weekly errors = migrate priority high"
    - modification_frequency: "Often modified = migrate for maintainability"
  action: "Apply Tool Decision Matrix to each node, migrate to PCE"
  rationale: "Migration pays off when maintenance burden exceeds conversion cost"
```

---

# SECTION 4: CASE STUDIES
## Real-World Applications with Quantified Results

*"Approach every workflow as a lab experiment: write down the hypothesis (SOP), run scripts as instruments, and let logs and expertise files tell you how to improve the next iteration."*

---

## 4.1 CASE STUDY: N8N Lead Gen Migration

### Background

**Client:** B2B SaaS company  
**Problem:** Lead generation workflow in n8n becoming unmaintainable  
**Original Setup:** 28-node n8n workflow running daily

### Before State

**N8N Workflow Analysis:**

| Metric | Value | Issue |
|--------|-------|-------|
| Total nodes | 28 | Visual spaghetti territory |
| Execution time | 45 minutes | Acceptable but slow |
| Weekly errors | 12-15 | Significant maintenance burden |
| Debug time per error | 35-60 minutes | High due to visual complexity |
| Modification time | 2-3 hours | Fear of breaking other paths |
| Test coverage | 0% | Untestable |

**Node Breakdown:**
- HTTP Request nodes: 8
- Transform/Set nodes: 7
- IF/Switch nodes: 6
- Integration nodes: 4
- Utility nodes: 3

**Pain Points Identified:**
1. Single node failure stopped entire workflow
2. No way to run partial workflow for testing
3. Error messages unhelpful ("Node X failed")
4. Changes required understanding entire flow
5. No parallelization (sequential execution only)

### Migration Process

**Phase 1: Analysis (4 hours)**
- Exported n8n JSON
- Mapped each node to operation type
- Identified parallelization opportunities
- Documented data flow

**Phase 2: Design (3 hours)**
- Applied Tool Decision Matrix to each operation
- Designed PCE structure
- Created script specifications
- Defined SSOT contracts

**Tool Decisions:**

| Operation | N8N Node | PCE Decision | Rationale |
|-----------|----------|--------------|-----------|
| Scrape LinkedIn | HTTP + Transform | Browser script | Better reliability |
| Scrape website | HTTP | Lean API script | Simple GET |
| Enrich data | Code node | Python script | Testable logic |
| Filter/dedupe | IF + Set | Python script | Complex conditions |
| Send to CRM | Integration | Lean API script | Direct control |

**Phase 3: Implementation (8 hours)**
- Created SOP.md
- Built coordinator.py
- Wrote 4 execution scripts
- Added unit tests

**PCE Structure:**
```
lead_gen_pipeline/
├── SOP.md                    # Human-readable workflow
├── coordinator.py            # Orchestration (200 lines)
├── config.yaml               # Configuration
├── scripts/
│   ├── discover_leads.py     # LinkedIn + web scraping (150 lines)
│   ├── enrich_leads.py       # Data enrichment (100 lines)
│   ├── filter_qualify.py     # Filtering logic (80 lines)
│   └── sync_to_crm.py        # CRM integration (60 lines)
└── tests/
    ├── test_discover.py
    ├── test_enrich.py
    ├── test_filter.py
    └── test_sync.py
```

### After State

**PCE Implementation Metrics:**

| Metric | Before (N8N) | After (PCE) | Improvement |
|--------|--------------|-------------|-------------|
| Components | 28 nodes | 4 scripts | 86% reduction |
| Execution time | 45 min | 18 min | 60% faster |
| Weekly errors | 12-15 | 2-3 | 80% reduction |
| Debug time per error | 35-60 min | 10-15 min | 75% faster |
| Modification time | 2-3 hours | 20-30 min | 85% faster |
| Test coverage | 0% | 87% | Full coverage |

**Additional Benefits:**
- Parallel execution of independent scraping tasks
- Automatic retry with exponential backoff
- Structured logging for pattern analysis
- Easy to extend with new data sources

### ROI Calculation

**Migration Cost:**
- Analysis: 4 hours × $150/hr = $600
- Design: 3 hours × $150/hr = $450
- Implementation: 8 hours × $150/hr = $1,200
- Testing: 3 hours × $150/hr = $450
- **Total: $2,700**

**Monthly Savings:**
- Error reduction: 10 errors/week × 45 min × $150/hr × 4 weeks = $4,500
- Faster execution: 27 min/day × 20 days × $50/hr = $450
- Faster modifications: 2 hr/week × $150/hr × 4 weeks = $1,200
- **Monthly savings: $6,150**

**Payback Period: 13 days**

### Lessons Learned

1. **Node count is vanity metric** — 28 nodes doesn't mean 28x capability
2. **Parallel execution is hidden value** — N8N sequential by default
3. **Testability changes everything** — Finding bugs before production
4. **SOP as documentation** — Reduced onboarding time for new team members

---

## 4.2 CASE STUDY: Browser vs API Decision

### Background

**Project:** Competitor price monitoring  
**Requirement:** Track pricing on 50 competitor websites, update daily  
**Initial Approach:** Use APIs where available

### Analysis Phase

**API Availability Audit:**

| Competitors | API Available | API Cost | API Limitations |
|-------------|---------------|----------|-----------------|
| 12 (24%) | Yes | $200-500/mo each | Rate limits, incomplete data |
| 18 (36%) | Yes (unofficial) | Free | Unstable, may break |
| 20 (40%) | No | N/A | Must scrape |

**Decision Point:**
- Option A: Mixed approach (APIs + scraping)
- Option B: All browser automation

### Tool Decision Matrix Application

**Option A Analysis (Mixed):**

| Factor | Score | Notes |
|--------|-------|-------|
| Context cost | High | 12 API schemas + scraping skill |
| Maintenance | High | 12 different API contracts to monitor |
| Reliability | Variable | API changes break individual integrations |
| Cost | $3,000/mo | API fees |
| Consistency | Low | Different data formats per source |

**Option B Analysis (All Browser):**

| Factor | Score | Notes |
|--------|-------|-------|
| Context cost | Low | Single scraping skill |
| Maintenance | Medium | Selector updates when sites change |
| Reliability | High | Consistent approach across all |
| Cost | $50/mo | Proxy/infrastructure only |
| Consistency | High | Same extraction logic everywhere |

### Decision

**Selected: Option B (All Browser Automation)**

**Rationale:**
1. Uniform approach reduces cognitive load
2. Selector changes are easier than API migrations
3. 98% cost reduction
4. Single skill descriptor (~100 tokens vs ~2,400 tokens for 12 MCPs)

### Implementation

**Script Structure:**
```python
# scripts/price_monitor.py
SITE_CONFIGS = {
    "competitor_a": {
        "url": "https://competitor-a.com/pricing",
        "price_selector": ".pricing-card .price",
        "plan_selector": ".plan-name"
    },
    # ... 49 more configs
}

async def scrape_pricing(site_id: str) -> dict:
    config = SITE_CONFIGS[site_id]
    # Standardized extraction logic
    ...
```

### Results

**Performance Metrics:**

| Metric | Mixed Approach (Projected) | Browser Only (Actual) |
|--------|---------------------------|----------------------|
| Monthly cost | $3,050 | $50 |
| Context tokens | 2,400 | 100 |
| Data formats | 12 different | 1 unified |
| Maintenance events/month | 8-10 | 2-3 |
| Time to add competitor | 2-4 hours | 15 minutes |

**Token Savings Impact:**
- 2,300 fewer tokens at Zero-Point
- 96% reduction in tool-related context
- Measurably better orchestration accuracy

### Lessons Learned

1. **API availability ≠ API advisability** — Just because API exists doesn't mean it's better
2. **Uniformity has hidden value** — Same approach everywhere reduces complexity
3. **Browser automation has matured** — Playwright reliability exceeds many APIs
4. **Cost savings compound** — $3K/month × 12 = $36K/year

---

# SECTION 5: PATTERN LIBRARY
## Reusable YAML Patterns

*"Frame skills as 'tiny specialists' with clear jobs, not magical black boxes—each should have a name, a capability, a script, and a place in the wider ecosystem."*

---

## 5.1 CORE PATTERNS

### Pattern 1: Zero-Point Skill Descriptor

```yaml
# PATTERN: Minimal skill descriptor for Zero-Point context
# Use: Every skill should have this thin descriptor always loaded

SKILL_DESCRIPTOR:
  id: "skill_name"
  capability: "One sentence: what this skill does"
  inputs: ["input_1", "input_2"]
  outputs: ["output_1", "output_2"]
  token_cost: 100  # Activation cost
  trigger: "When to activate this skill"
  
# Example:
lead_discovery:
  id: "lead_discovery"
  capability: "Discover leads from LinkedIn and Instagram via browser automation"
  inputs: ["search_criteria", "platform", "max_results"]
  outputs: ["LEAD_RAW_LIST"]
  token_cost: 150
  trigger: "Lead generation task requested"
```

### Pattern 2: PCE Coordinator Structure

```yaml
# PATTERN: Standard coordinator.py structure
# Use: Every automation should follow this orchestration pattern

COORDINATOR_STRUCTURE:
  imports:
    - asyncio
    - logging
    - scripts/*
  
  config:
    max_retries: 3
    backoff_base: 2
    timeout_seconds: 300
    parallel_limit: 5
  
  state:
    run_id: "uuid"
    started_at: "timestamp"
    current_step: "step_name"
    completed_steps: []
    failed_steps: []
  
  orchestration:
    - step: "step_1"
      script: "scripts/step_1.py"
      retry: true
      parallel_with: null
      on_success: "step_2"
      on_failure: "handle_error"
    
    - step: "step_2"
      script: "scripts/step_2.py"
      retry: true
      parallel_with: "step_3"  # Run 2 and 3 in parallel
      on_success: "step_4"
      on_failure: "handle_error"
  
  error_handling:
    - error_type: "RateLimitError"
      action: "exponential_backoff"
    - error_type: "NetworkError"
      action: "retry_with_timeout"
    - error_type: "DataValidationError"
      action: "log_and_skip"
```

### Pattern 3: Tool Decision Record

```yaml
# PATTERN: Document tool decisions with rationale
# Use: Every tool choice should have this record

TOOL_DECISION_RECORD:
  operation: "What operation this is"
  
  options_considered:
    - option: "Browser automation"
      pros: ["No API needed", "Full control"]
      cons: ["Slower", "Selector maintenance"]
    - option: "Official API"
      pros: ["Supported", "Documented"]
      cons: ["Rate limits", "Cost", "Schema bloat"]
  
  decision: "Selected option"
  rationale: "Why this option was chosen"
  
  implementation:
    tool: "Specific tool"
    script: "script_name.py"
    token_cost: 100
  
  review_trigger: "When to reconsider this decision"
```

### Pattern 4: Anti-Pattern Detection Result

```yaml
# PATTERN: Standard anti-pattern detection output
# Use: Every design review should produce this

ANTI_PATTERN_SCAN:
  scan_date: "2026-01-23"
  design_id: "BP-2026-001"
  
  results:
    - pattern: "visual_spaghetti"
      detected: false
      evidence: "4 scripts, no visual workflow"
    
    - pattern: "schema_bloat"
      detected: false
      evidence: "Zero-Point at 350 tokens"
    
    - pattern: "tool_first"
      detected: false
      evidence: "Design started from workflow, not tools"
    
    - pattern: "monolithic_agent"
      detected: false
      evidence: "Specialized sub-agents defined"
    
    - pattern: "llm_only_execution"
      detected: false
      evidence: "All external calls via deterministic scripts"
    
    - pattern: "context_dumping"
      detected: false
      evidence: "Data stored externally, summaries in context"
    
    - pattern: "static_non_learning"
      detected: false
      evidence: "Heal & Renew hooks implemented"
  
  health_score: 10  # 0-10, 10 = no issues
  recommendation: "Approved for build"
```

### Pattern 5: Heal & Renew Log

```yaml
# PATTERN: Standard correction log for self-improvement
# Use: Every automation run should produce this

HEAL_RENEW_LOG:
  run_id: "uuid"
  automation_id: "automation_name"
  run_date: "2026-01-23"
  
  corrections_made:
    - step: "discover_leads"
      issue: "LinkedIn rate limit hit"
      fix_applied: "Reduced request rate from 60/hr to 30/hr"
      timestamp: "2026-01-23T10:15:00Z"
    
    - step: "enrich_leads"
      issue: "3 profiles had invalid format"
      fix_applied: "Logged and skipped, added to validation patterns"
      timestamp: "2026-01-23T10:23:00Z"
  
  patch_proposals:
    - target: "scripts/discover_leads.py"
      change: "Add adaptive rate limiting based on response headers"
      priority: "medium"
      estimated_impact: "Reduce rate limit errors by 80%"
    
    - target: "config.yaml"
      change: "Update default rate to 30/hr"
      priority: "high"
      estimated_impact: "Immediate stability improvement"
  
  metrics:
    success_rate: 0.94
    execution_time_seconds: 1080
    errors_encountered: 5
    errors_recovered: 4
    errors_fatal: 1
```

---

## 5.2 INTEGRATION PATTERNS

### Pattern 6: Module Handoff Package

```yaml
# PATTERN: Standard package for module-to-module handoff
# Use: When passing work from Module 1 to Modules 2-8

HANDOFF_PACKAGE:
  source_module: "module_1_master_architect"
  target_module: "module_2_automation_builder"
  
  created: "2026-01-23T14:00:00Z"
  created_by: "Master Automations Architect"
  
  artifacts:
    - name: "AUTOMATION_BLUEPRINT"
      path: "handoff/AUTOMATION_BLUEPRINT.yaml"
      required: true
    
    - name: "TOOL_DECISIONS"
      path: "handoff/TOOL_DECISIONS.yaml"
      required: true
    
    - name: "INTERFACE_SPEC"
      path: "handoff/INTERFACE_SPEC.yaml"
      required: false  # Only if UI needed
  
  instructions: |
    Generate the following from AUTOMATION_BLUEPRINT:
    1. SOP.md - Human-readable workflow documentation
    2. coordinator.py - Orchestration logic
    3. scripts/*.py - One script per execution step
    4. tests/*.py - Unit tests for each script
  
  acceptance_criteria:
    - "All scripts execute without error on test data"
    - "Test coverage >80%"
    - "SOP.md matches blueprint exactly"
    - "coordinator.py implements all specified flows"
  
  deadline: "2026-01-25T17:00:00Z"
```

### Pattern 7: SSOT Contract

```yaml
# PATTERN: Define data contracts between components
# Use: Every data object should have this contract

SSOT_CONTRACT:
  object_id: "LEAD_RAW_LIST"
  version: "1.0.0"
  
  schema:
    type: "array"
    items:
      type: "object"
      required: ["id", "name", "platform", "discovered_at"]
      properties:
        id:
          type: "string"
          format: "uuid"
        name:
          type: "string"
        platform:
          type: "string"
          enum: ["linkedin", "instagram", "youtube"]
        profile_url:
          type: "string"
          format: "uri"
        discovered_at:
          type: "string"
          format: "date-time"
        metrics:
          type: "object"
          properties:
            followers: { type: "integer" }
            engagement_rate: { type: "number" }
  
  owner: "lead_gen_engine"
  
  producers:
    - module: "module_4_browser_automation"
      operation: "discover_leads"
  
  consumers:
    - module: "module_5_content_analyzer"
      operation: "analyze_content"
    - module: "module_6_outreach_orchestrator"
      operation: "send_campaign"
  
  validation:
    on_write: "strict"  # Reject invalid
    on_read: "permissive"  # Log warnings, don't fail
```

### Pattern 8: Interface Component Spec

```yaml
# PATTERN: Standard specification for UI components
# Use: When Module 7 needs to generate interfaces

INTERFACE_COMPONENT_SPEC:
  component_id: "lead_dashboard"
  type: "dashboard"
  
  framework: "react"
  styling: "tailwind"
  ui_library: "shadcn"
  
  layout:
    type: "split"
    regions:
      - id: "sidebar"
        width: "250px"
        components: ["filters", "stats"]
      - id: "main"
        width: "flex"
        components: ["data_table", "detail_panel"]
  
  components:
    filters:
      type: "FilterPanel"
      props:
        filters:
          - field: "platform"
            type: "multi-select"
            options: ["linkedin", "instagram", "youtube"]
          - field: "score"
            type: "range"
            min: 0
            max: 100
    
    data_table:
      type: "DataTable"
      props:
        columns:
          - field: "name"
            label: "Name"
            sortable: true
          - field: "platform"
            label: "Platform"
            sortable: true
          - field: "score"
            label: "Score"
            sortable: true
        pagination: true
        page_size: 25
    
    detail_panel:
      type: "SlideOver"
      props:
        trigger: "row_click"
        width: "400px"
        sections:
          - "profile_info"
          - "content_samples"
          - "analysis_results"
  
  data_bindings:
    source: "supabase"
    table: "leads"
    realtime: true
  
  actions:
    - id: "approve_lead"
      label: "Approve"
      type: "primary"
      handler: "updateLeadStatus('approved')"
    - id: "reject_lead"
      label: "Reject"
      type: "secondary"
      handler: "updateLeadStatus('rejected')"
```

### Pattern 9: Browser Automation Config

```yaml
# PATTERN: Platform-specific browser automation configuration
# Use: When Module 4 implements scraping

BROWSER_AUTOMATION_CONFIG:
  platform: "linkedin"
  
  settings:
    headless: true
    user_agent: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)..."
    viewport: { width: 1280, height: 720 }
    timeout_ms: 30000
  
  rate_limiting:
    requests_per_hour: 30
    delay_between_requests_ms: 5000
    backoff_on_rate_limit: true
  
  authentication:
    method: "session_cookies"
    cookie_file: "secrets/linkedin_cookies.json"
    refresh_interval_hours: 24
  
  selectors:
    profile_name: ".text-heading-xlarge"
    profile_headline: ".text-body-medium"
    profile_location: ".text-body-small.inline"
    profile_about: "#about ~ .display-flex .inline-show-more-text"
    experience_items: "#experience ~ .pvs-list__outer-container li"
  
  extraction_schema:
    name: { selector: "profile_name", type: "text" }
    headline: { selector: "profile_headline", type: "text" }
    location: { selector: "profile_location", type: "text" }
    about: { selector: "profile_about", type: "text" }
    experience: { selector: "experience_items", type: "list" }
  
  error_handling:
    - error: "ElementNotFound"
      action: "retry_with_wait"
      max_retries: 3
    - error: "LoginRequired"
      action: "refresh_cookies"
    - error: "RateLimited"
      action: "exponential_backoff"
```

### Pattern 10: Migration Plan Template

```yaml
# PATTERN: Standard n8n/Zapier to PCE migration plan
# Use: When converting legacy workflows

MIGRATION_PLAN:
  source:
    platform: "n8n"
    workflow_name: "Lead Gen v3"
    node_count: 28
    export_file: "legacy/lead_gen_v3.json"
  
  target:
    architecture: "PCE"
    estimated_scripts: 4
    estimated_total_lines: 400
  
  node_mapping:
    - n8n_node: "HTTP Request (LinkedIn)"
      n8n_type: "httpRequest"
      target: "scripts/discover_linkedin.py"
      conversion: "Replace with Playwright browser automation"
    
    - n8n_node: "Set (Transform Data)"
      n8n_type: "set"
      target: "scripts/transform.py"
      conversion: "Extract transformation logic to Python function"
    
    - n8n_node: "IF (Check Valid)"
      n8n_type: "if"
      target: "coordinator.py"
      conversion: "Move branching logic to coordinator"
  
  timeline:
    week_1:
      - "Export and analyze n8n workflow"
      - "Create node mapping"
      - "Design PCE structure"
    week_2:
      - "Implement scripts"
      - "Build coordinator"
      - "Write unit tests"
    week_3:
      - "Integration testing"
      - "Parallel run (old + new)"
      - "Validate equivalence"
    week_4:
      - "Cutover to new system"
      - "Deprecate n8n workflow"
      - "Document and close"
  
  validation:
    equivalence_test:
      method: "Run both systems with same input, compare outputs"
      success_criteria: "99% output match"
    
    performance_test:
      metrics: ["execution_time", "error_rate", "resource_usage"]
      success_criteria: "New system equal or better on all metrics"
  
  rollback_plan:
    trigger: "Error rate >10% or critical failure"
    steps:
      1: "Re-enable n8n workflow"
      2: "Disable PCE system"
      3: "Investigate and fix"
      4: "Resume migration"
```

---

# SECTION 6: OUTPUT TEMPLATES
## Ready-to-Use Deliverable Formats

*"Value token discipline as a form of respect for future reasoning: every saved token is more room for real understanding of the business problem."*

---

## 6.1 AUTOMATION_BLUEPRINT Template

```yaml
# ═══════════════════════════════════════════════════════════════════════════
# AUTOMATION_BLUEPRINT
# The complete specification for building an automation
# ═══════════════════════════════════════════════════════════════════════════

AUTOMATION_BLUEPRINT:
  
  # ─────────────────────────────────────────────────────────────────────────
  # METADATA
  # ─────────────────────────────────────────────────────────────────────────
  
  metadata:
    blueprint_id: "[BP-YYYY-NNN]"
    version: "1.0.0"
    created: "[YYYY-MM-DD]"
    author: "Master Automations Architect"
    status: "[Draft | Review | Approved | Building | Complete]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # REQUIREMENT
  # ─────────────────────────────────────────────────────────────────────────
  
  requirement:
    name: "[Automation Name]"
    description: "[What this automation does in 1-2 sentences]"
    trigger: "[Manual | Scheduled | Webhook | Event]"
    output: "[What the automation produces]"
    success_criteria: "[Measurable definition of success]"
    
    classification:
      scope: "[one-off | reusable | production]"
      context_intensity: "[low | medium | high]"
      system_count: "[number]"
      decision_complexity: "[low | medium | high]"
      failure_criticality: "[low | medium | high]"
      volume: "[N/day]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # TOOL DECISIONS
  # ─────────────────────────────────────────────────────────────────────────
  
  tool_decisions:
    "[operation_1_name]":
      level: "[BROWSER_AUTOMATION | LEAN_API | CUSTOM_INTERFACE | LEAN_MCP]"
      tool: "[Specific tool]"
      rationale: "[Why this choice]"
      script: "[script_name.py]"
      token_cost: "[number]"
    
    # ... additional operations
    
    summary:
      total_token_budget: "[sum of all token costs]"
      mcp_count: "[number of MCPs required]"
      browser_automations: "[count]"
      lean_apis: "[count]"
      interfaces: "[count]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # PCE ARCHITECTURE
  # ─────────────────────────────────────────────────────────────────────────
  
  pce_architecture:
    planning:
      sop_file: "[filename].md"
      sections:
        - overview
        - prerequisites
        - steps
        - decision_points
        - error_handling
        - success_criteria
    
    coordination:
      coordinator_file: "[filename].py"
      parallelization:
        - "[step_a] || [step_b]"  # Parallel steps
      retry_policy:
        max_attempts: 3
        backoff: "exponential"
      state_management:
        persistence: "[memory | file | database]"
        resume_capability: "[yes | no]"
    
    execution:
      scripts:
        - name: "[script_1].py"
          purpose: "[What it does]"
          input: "[Input data/format]"
          output: "[Output data/format]"
          estimated_lines: "[number]"
        
        # ... additional scripts
  
  # ─────────────────────────────────────────────────────────────────────────
  # INTEGRATION
  # ─────────────────────────────────────────────────────────────────────────
  
  integration:
    data_flows:
      - source: "[System/Script]"
        destination: "[System/Script]"
        format: "[JSON | CSV | etc]"
        frequency: "[per run | real-time | batch]"
    
    ssot_objects:
      - object_id: "[OBJECT_NAME]"
        schema_ref: "[path/to/schema.yaml]"
        owner: "[producing module/script]"
        consumers: ["[module_1]", "[module_2]"]
    
    external_systems:
      - system: "[System name]"
        integration_type: "[API | Browser | MCP]"
        credentials_location: "[secrets/...]"
        rate_limits: "[description]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # TIMELINE
  # ─────────────────────────────────────────────────────────────────────────
  
  timeline:
    build_phase:
      duration: "[N days]"
      milestones:
        "[day_1]": "[Milestone description]"
        "[day_N]": "[Milestone description]"
    
    deployment:
      target: "[Development | Staging | Production]"
      rollout_strategy: "[Big bang | Staged | Canary]"
      monitoring: "[Monitoring approach]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # HANDOFFS
  # ─────────────────────────────────────────────────────────────────────────
  
  handoffs:
    - to_module: "[Module name]"
      artifact: "[What to send]"
      action: "[What they do with it]"
      deadline: "[Date/time]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # VALIDATION
  # ─────────────────────────────────────────────────────────────────────────
  
  validation:
    test_plan:
      unit_tests: "[Coverage target]%"
      integration_tests: "[Number] scenarios"
      end_to_end: "[Description]"
    
    success_metrics:
      - metric: "[Metric name]"
        target: "[Value]"
        measurement: "[How to measure]"
    
    monitoring:
      logs: "[Destination]"
      alerts: "[Channel and triggers]"
      dashboards: "[What to build]"
```

---

## 6.2 TOOL_DECISIONS Template

```yaml
# ═══════════════════════════════════════════════════════════════════════════
# TOOL_DECISIONS
# Complete record of tool selection decisions with rationale
# ═══════════════════════════════════════════════════════════════════════════

TOOL_DECISIONS:
  
  blueprint_ref: "[BP-YYYY-NNN]"
  decision_date: "[YYYY-MM-DD]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # DECISION MATRIX APPLICATION
  # ─────────────────────────────────────────────────────────────────────────
  
  decisions:
    
    "[operation_1]":
      description: "[What this operation does]"
      
      options_evaluated:
        - option: "Browser Automation"
          score: "[1-10]"
          notes: "[Pros/cons]"
        - option: "Lean API"
          score: "[1-10]"
          notes: "[Pros/cons]"
        - option: "MCP"
          score: "[1-10]"
          notes: "[Pros/cons]"
      
      selected: "[BROWSER_AUTOMATION | LEAN_API | CUSTOM_INTERFACE | LEAN_MCP]"
      tool: "[Specific tool/library]"
      rationale: "[Why this was chosen]"
      
      implementation:
        script: "[script_name.py]"
        estimated_lines: "[number]"
        dependencies: ["[dep_1]", "[dep_2]"]
        
      token_impact:
        descriptor_tokens: "[number]"
        activation_tokens: "[number]"
        total: "[number]"
      
      review_trigger: "[When to reconsider this decision]"
    
    # ... additional operations
  
  # ─────────────────────────────────────────────────────────────────────────
  # SUMMARY
  # ─────────────────────────────────────────────────────────────────────────
  
  summary:
    total_operations: "[number]"
    
    by_level:
      browser_automation: "[count]"
      lean_api: "[count]"
      custom_interface: "[count]"
      lean_mcp: "[count]"
    
    token_budget:
      zero_point: "[tokens] (target: <500)"
      on_activation: "[tokens]"
      peak_context: "[tokens]"
    
    mcp_justifications:
      # Only if MCPs are used
      - mcp: "[MCP name]"
        justification: "[Why MCP was necessary]"
        alternatives_rejected: "[What was tried first]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # ANTI-PATTERN CHECK
  # ─────────────────────────────────────────────────────────────────────────
  
  anti_pattern_check:
    schema_bloat: "[PASS | WARN | FAIL] - [notes]"
    tool_first: "[PASS | WARN | FAIL] - [notes]"
    mcp_overuse: "[PASS | WARN | FAIL] - [notes]"
    
    health_score: "[0-10]"
    recommendations: "[Any changes needed]"
```

---

## 6.3 MIGRATION_PLAN Template

```yaml
# ═══════════════════════════════════════════════════════════════════════════
# MIGRATION_PLAN
# Convert legacy visual workflow to PCE architecture
# ═══════════════════════════════════════════════════════════════════════════

MIGRATION_PLAN:
  
  migration_id: "[MIG-YYYY-NNN]"
  created: "[YYYY-MM-DD]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # SOURCE WORKFLOW
  # ─────────────────────────────────────────────────────────────────────────
  
  source:
    platform: "[n8n | Zapier | Make | Custom]"
    workflow_name: "[Name]"
    workflow_id: "[ID if applicable]"
    export_file: "[path/to/export.json]"
    
    analysis:
      total_nodes: "[number]"
      node_breakdown:
        http_requests: "[count]"
        transformations: "[count]"
        conditionals: "[count]"
        integrations: "[count]"
        utilities: "[count]"
      
      complexity_score: "[1-10]"
      visual_spaghetti: "[yes | no]"
      
    current_metrics:
      execution_time: "[minutes]"
      weekly_errors: "[count]"
      maintenance_hours_weekly: "[hours]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # TARGET ARCHITECTURE
  # ─────────────────────────────────────────────────────────────────────────
  
  target:
    architecture: "PCE"
    
    structure:
      sop_file: "[filename].md"
      coordinator_file: "[filename].py"
      scripts:
        - name: "[script_1].py"
          replaces_nodes: ["[node_1]", "[node_2]"]
          estimated_lines: "[number]"
        # ... additional scripts
      
      total_scripts: "[count]"
      total_estimated_lines: "[number]"
    
    projected_metrics:
      execution_time: "[minutes]"
      weekly_errors: "[count] (target)"
      maintenance_hours_weekly: "[hours] (target)"
  
  # ─────────────────────────────────────────────────────────────────────────
  # NODE MAPPING
  # ─────────────────────────────────────────────────────────────────────────
  
  node_mapping:
    - source_node:
        name: "[Node name in workflow]"
        type: "[Node type]"
        purpose: "[What it does]"
      
      target:
        component: "[script | coordinator | config]"
        file: "[filename]"
        function: "[function_name if applicable]"
      
      conversion_notes: "[How to convert]"
      complexity: "[low | medium | high]"
    
    # ... additional node mappings
  
  # ─────────────────────────────────────────────────────────────────────────
  # TIMELINE
  # ─────────────────────────────────────────────────────────────────────────
  
  timeline:
    total_duration: "[N weeks]"
    
    phases:
      analysis:
        duration: "[days]"
        tasks:
          - "Export and document current workflow"
          - "Create node mapping"
          - "Identify parallelization opportunities"
          - "Design PCE structure"
      
      implementation:
        duration: "[days]"
        tasks:
          - "Scaffold script files"
          - "Implement core logic"
          - "Build coordinator"
          - "Write unit tests"
      
      validation:
        duration: "[days]"
        tasks:
          - "Integration testing"
          - "Parallel run (old + new)"
          - "Compare outputs"
          - "Performance benchmarking"
      
      cutover:
        duration: "[days]"
        tasks:
          - "Final validation"
          - "Switch to new system"
          - "Monitor closely"
          - "Deprecate old workflow"
  
  # ─────────────────────────────────────────────────────────────────────────
  # VALIDATION
  # ─────────────────────────────────────────────────────────────────────────
  
  validation:
    equivalence_testing:
      method: "[How to verify same behavior]"
      test_data: "[What data to use]"
      success_criteria: "[Acceptance threshold]"
    
    performance_testing:
      metrics:
        - name: "Execution time"
          old_baseline: "[value]"
          target: "[value]"
        - name: "Error rate"
          old_baseline: "[value]"
          target: "[value]"
    
    acceptance_criteria:
      - "[Criterion 1]"
      - "[Criterion 2]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # ROLLBACK
  # ─────────────────────────────────────────────────────────────────────────
  
  rollback:
    trigger_conditions:
      - "Error rate >10%"
      - "Critical functionality failure"
      - "Data integrity issues"
    
    procedure:
      1: "Re-enable original workflow"
      2: "Disable PCE system"
      3: "Notify stakeholders"
      4: "Investigate root cause"
      5: "Fix and re-test"
      6: "Resume migration with fixes"
    
    rollback_duration: "[estimated time]"
  
  # ─────────────────────────────────────────────────────────────────────────
  # ROI PROJECTION
  # ─────────────────────────────────────────────────────────────────────────
  
  roi_projection:
    migration_cost:
      analysis_hours: "[hours] × $[rate] = $[cost]"
      implementation_hours: "[hours] × $[rate] = $[cost]"
      testing_hours: "[hours] × $[rate] = $[cost]"
      total: "$[total]"
    
    monthly_savings:
      error_reduction: "$[amount]"
      faster_execution: "$[amount]"
      reduced_maintenance: "$[amount]"
      total: "$[total]/month"
    
    payback_period: "[days/weeks]"
    annual_roi: "[percentage]%"
```

---

# SECTION 7: README & INTEGRATION
## Quick Start and Module Connections

*"Treat automations like an operating system of small, composable programs and skills, not a giant Rube Goldberg machine of nodes and tools."*

---

## 7.1 QUICK START

### What This Module Does

**Module ONE: Master Automations Architect** is the doctrine layer that makes strategic decisions about how to build automations. It does NOT execute automations—it designs them and routes work to execution modules.

### Core Capabilities

1. **Requirement Analysis** → Classify automation type and complexity
2. **Tool Selection** → Apply Tool Decision Matrix (Browser → API → Interface → MCP)
3. **Anti-Pattern Detection** → Identify and correct design flaws
4. **Blueprint Generation** → Produce AUTOMATION_BLUEPRINT for builders
5. **Migration Planning** → Convert n8n/Zapier to PCE architecture

### When to Use This Module

- **"I need to build an automation"** → Start here
- **"Should I use API or scraping?"** → Apply Tool Decision Matrix
- **"Is this workflow design good?"** → Run anti-pattern detection
- **"How do I migrate from n8n?"** → Generate migration plan

### What This Module Produces

| Output | Description | Consumed By |
|--------|-------------|-------------|
| AUTOMATION_BLUEPRINT | Complete build specification | Module 2 (Builder) |
| TOOL_DECISIONS | Tool selection with rationale | Modules 2, 4, 6, 7 |
| INTERFACE_SPEC | UI component specifications | Module 7 (Interface) |
| MIGRATION_PLAN | n8n → PCE conversion plan | Module 3 (Translator) |
| ANTI_PATTERN_REPORT | Design health assessment | Self (iteration) |

---

## 7.2 INTEGRATION MAP

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        MODULE INTEGRATION MAP                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│                      ┌─────────────────────────┐                            │
│                      │   MODULE 1 (This)       │                            │
│                      │   Master Automations    │                            │
│                      │   Architect             │                            │
│                      └───────────┬─────────────┘                            │
│                                  │                                           │
│           ┌──────────────────────┼──────────────────────┐                   │
│           │                      │                      │                   │
│           ▼                      ▼                      ▼                   │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐            │
│  │   MODULE 2     │    │   MODULE 3     │    │   MODULE 7     │            │
│  │   Automation   │    │   N8N          │    │   Interface    │            │
│  │   Builder      │    │   Translator   │    │   Generator    │            │
│  └───────┬────────┘    └───────┬────────┘    └───────┬────────┘            │
│          │                     │                     │                      │
│          │    ┌────────────────┴─────────────────────┘                      │
│          │    │                                                             │
│          ▼    ▼                                                             │
│  ┌────────────────┐    ┌────────────────┐    ┌────────────────┐            │
│  │   MODULE 4     │    │   MODULE 5     │    │   MODULE 6     │            │
│  │   Browser      │    │   Content      │    │   Outreach     │            │
│  │   Automation   │    │   Analyzer     │    │   Orchestrator │            │
│  └───────┬────────┘    └───────┬────────┘    └───────┬────────┘            │
│          │                     │                     │                      │
│          └─────────────────────┼─────────────────────┘                      │
│                                │                                            │
│                                ▼                                            │
│                       ┌────────────────┐                                    │
│                       │   MODULE 8     │                                    │
│                       │   Onboarding   │                                    │
│                       │   Automator    │                                    │
│                       └────────────────┘                                    │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Handoff Specifications

| From Module 1 | To Module | Artifact | Purpose |
|---------------|-----------|----------|---------|
| Blueprint | Module 2 | AUTOMATION_BLUEPRINT | Generate SOP + scripts |
| Migration Plan | Module 3 | MIGRATION_PLAN | Convert n8n workflow |
| Browser Tasks | Module 4 | BROWSER_TASKS | Implement scraping |
| Analysis Spec | Module 5 | ANALYSIS_REQUIREMENTS | Extract patterns |
| Outreach Spec | Module 6 | OUTREACH_SPEC | Build campaigns |
| Interface Spec | Module 7 | INTERFACE_SPEC | Generate React UI |
| Onboarding Spec | Module 8 | ONBOARDING_SPEC | Build nurture flows |

---

## 7.3 TOKEN BUDGET

### Zero-Point Context (~500 tokens)

Always loaded:
```yaml
module_1_descriptor:
  id: "master_automations_architect"
  capability: "Design automations, select tools, detect anti-patterns, generate blueprints"
  inputs: ["requirement", "existing_workflow", "constraints"]
  outputs: ["AUTOMATION_BLUEPRINT", "TOOL_DECISIONS", "MIGRATION_PLAN"]
  token_cost: 500
  trigger: "Automation design or migration task"
```

### Activation Budget

| Layer | Content | Tokens | Load Trigger |
|-------|---------|--------|--------------|
| L1 | Quick reference + heuristics index | 600 | Always |
| L2 | Full frameworks + mechanisms | 1,500 | Design task |
| L3 | Tool matrix + anti-patterns | 1,200 | Tool decision |
| L4 | Integration + templates | 800 | Blueprint generation |
| **Total** | Complete module | **4,100** | Full activation |

---

## 7.4 VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-01-23 | Initial release: Complete doctrine layer with 4-phase workflow, 7 anti-patterns, 11 heuristics, 10 patterns, 3 output templates |

---

## 7.5 UPGRADE PATH

### Planned for v1.1.0
- Additional browser automation patterns from NotebookLM videos
- Refined heuristics based on real-world usage
- New case studies from production deployments

### Planned for v2.0.0
- LCT (Lean Context Tooling) standard integration
- Visual flow representation compiler
- Self-improving heuristics engine

---

**END OF MODULE ONE: MASTER AUTOMATIONS ARCHITECT V1**

---

*"Skills + Scripts > MCPs | Zero-Point Context Strategy | Token Discipline = Accuracy Discipline"*

*ULTRAMIND Automation Factory — Module ONE Complete*

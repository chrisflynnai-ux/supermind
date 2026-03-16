# SKILL ARCHITECT - Enhanced Skill Building Skill
**The Meta-Skill That Builds Skills**

---

**Skill Metadata:**
```yaml
skill_id: skill_architect_v2
name: Skill Architect
description: Meta-skill that generates production-grade Super-Skills with progressive disclosure, constitutional compliance, self-improvement integration, and MOD/MMA coordination. Incorporates ULTRAMIND architecture, Neuro-Box evaluation, and self-annealing patterns.
version: 2.0.0
tier: meta
status: production
model: claude-sonnet-4-20250514

inputs_required:
  - skill_concept (name, purpose, core function)
  - domain_knowledge (masterclass content, best practices, anti-patterns)
  
inputs_optional:
  - target_output_type (email, sales_page, strategy_document, etc.)
  - constitutional_constraints (specific rules for this skill)
  - upstream_dependencies (skills that feed into this one)
  - downstream_consumers (skills that use this skill's output)
  - neurobox_focus (which dimensions this skill primarily activates)

outputs_primary:
  - complete_skill_file (XML format with L1-L4 layers)
  - skill_test_suite (sample inputs/outputs for validation)
  - integration_spec (how it coordinates with MOD/MMA)
  - constitutional_alignment_report

guardrails:
  - "Every skill must have constitutional compliance section"
  - "Every skill must specify MOD awakening triggers"
  - "Every skill must define MMA quality gates"
  - "Every skill must use progressive disclosure (L1-L4)"
  - "Every skill must include self-improvement hooks"
```

---

## L1 — QUICK REFERENCE (How to Use This Skill)

### What This Skill Does
Builds complete, production-grade Super-Skills that integrate with the full ULTRAMIND ecosystem.

### Input Format
```yaml
Provide me with:
1. Skill name and core purpose
2. Domain knowledge (can be masterclass doc, best practices, or description)
3. Target output type (what the skill produces)
4. Any special constraints or constitutional rules

Optional:
- Dependencies (what it needs from other skills)
- Neuro-Box focus (which dimensions it activates)
- Example use cases
```

### Output Format
You'll receive:
1. **Complete skill file** (XML with YAML headers)
2. **Test suite** (3-5 test cases with expected outputs)
3. **Integration spec** (MOD/MMA coordination details)
4. **Deployment checklist**

### Quick Example
```
Input: "Build an Email Opener Specialist skill that creates compelling first 3 sentences of emails using MESSAGE_SPINE and VOICE_GUIDE"

Output: Complete skill with:
- L1: Quick formula for opener structure
- L2: Full procedure with Neuro-Box activation sequence
- L3: Advanced patterns, anti-patterns, edge cases
- L4: Constitutional compliance, MMA quality gates, MOD integration
```

---

## L2 — SKILL GENERATION PROCEDURE

### STEP 1: INTAKE & ANALYSIS

**Parse the concept:**
```yaml
extraction:
  skill_name: Extract clean name
  core_purpose: What problem does it solve?
  target_user: Who uses this skill? (human, MOD, another skill)
  output_artifact: What does it produce?
  domain: Which domain? (copywriting, strategy, analysis, etc.)
  complexity: simple | moderate | complex
  
validation:
  - Does this warrant a separate skill? (not duplicating existing)
  - Is scope clear and bounded? (not too broad)
  - Can it be modular? (works standalone + in teams)
```

**Analyze domain knowledge:**
```yaml
knowledge_processing:
  if masterclass_doc:
    - Extract: Frameworks, heuristics, anti-patterns
    - Identify: Key decision points
    - Categorize: L1 (core), L2 (procedure), L3 (advanced), L4 (meta)
    
  if best_practices:
    - Convert: Prose into executable logic
    - Extract: IF/THEN patterns
    - Identify: Common failure modes
    
  if examples_provided:
    - Analyze: Pattern across examples
    - Extract: Template structure
    - Note: Edge cases and variations
```

---

### STEP 2: CONSTITUTIONAL ALIGNMENT

**Before building, validate alignment:**

```yaml
constitutional_check:
  north_star:
    question: "Does this skill serve marketing transformation via Agentic Resonance?"
    action: If no → Reject or reframe
    
  resonance_principle:
    question: "Does this skill create authentic persuasion, not manipulation?"
    action: If manipulation risk → Add extra guardrails
    
  synchronous_wealth:
    question: "Does output create mutual value for both parties?"
    action: If extractive → Add balancing constraints
    
  scope_discipline:
    question: "Is this clearly within marketing/copy/business domains?"
    action: If scope drift → Narrow or split skill
```

**Document constitutional requirements:**
```xml
<ConstitutionalCompliance>
  <NorthStar>
    This skill must [specific alignment requirement]
  </NorthStar>
  
  <Guardrails>
    <Hard>
      - Never [prohibited action]
      - Always [required action]
      - Block if [violation condition]
    </Hard>
    
    <Soft>
      - Prefer [encouraged approach]
      - Avoid [discouraged pattern]
      - Consider [best practice]
    </Soft>
  </Guardrails>
  
  <ResonanceAlignment>
    This skill activates: [SAFE|SPECIAL|SMART|SIGNIFICANT|SUPPORTED|SUPERIOR]
    Primary axis: [vertical|horizontal|depth]
    Balance requirement: [specific balance rule]
  </ResonanceAlignment>
</ConstitutionalCompliance>
```

---

### STEP 3: PROGRESSIVE DISCLOSURE ARCHITECTURE

**Design the 4-layer structure:**

**Layer 1 (L1) - Quick Reference:**
```yaml
target_tokens: 300-500
purpose: "Instant orientation for fast use"
includes:
  - One-sentence purpose
  - Core formula or decision tree
  - Fast examples (2-3 quick ones)
  - When to use this skill
  - What it produces
  
writing_style: "Telegram-style, bullet points, maximum clarity"

example_structure: |
  ## L1 — QUICK REFERENCE
  
  **Purpose:** [One sentence]
  
  **Core Formula:**
  [3-5 step simple process]
  
  **Fast Example:**
  Input: [brief]
  Output: [brief]
  
  **When to Use:**
  - [Trigger condition 1]
  - [Trigger condition 2]
```

**Layer 2 (L2) - Core Procedure:**
```yaml
target_tokens: 1500-2000
purpose: "Complete executable workflow"
includes:
  - Step-by-step procedure
  - Decision points with logic
  - Neuro-Box activation sequence (if applicable)
  - Common patterns and heuristics
  - Basic error handling
  
writing_style: "Structured procedure, IF/THEN logic, clear steps"

example_structure: |
  ## L2 — CORE PROCEDURE
  
  ### STEP 1: [Action]
  [Detailed instructions]
  
  **Decision Logic:**
  - If X → Do Y
  - If A → Do B
  
  ### STEP 2: [Action]
  [Detailed instructions]
  
  **Neuro-Box Activation** (if applicable):
  - First activate SAFE: [how]
  - Then activate SMART: [how]
  - Balance SIGNIFICANT: [how]
```

**Layer 3 (L3) - Advanced Patterns:**
```yaml
target_tokens: 2000-3000
purpose: "Edge cases, nuance, mastery patterns"
includes:
  - Complex scenarios
  - Anti-patterns with fixes
  - Advanced techniques
  - Context-specific adaptations
  - Cross-skill coordination
  
writing_style: "Pattern library, case studies, comparative analysis"

example_structure: |
  ## L3 — ADVANCED USAGE
  
  ### Pattern: [Name]
  **When:** [Trigger]
  **Why:** [Reasoning]
  **How:** [Technique]
  
  ### Anti-Pattern: [Name]
  **What:** [Bad approach]
  **Why it fails:** [Explanation]
  **Instead:** [Good approach]
  
  ### Edge Case: [Scenario]
  **Problem:** [Description]
  **Solution:** [Approach]
```

**Layer 4 (L4) - Technical Spec & Integration:**
```yaml
target_tokens: 1500-2500
purpose: "MOD/MMA integration, schemas, maintenance"
includes:
  - Input/output schemas
  - MOD awakening protocol
  - MMA quality gates
  - Constitutional enforcement
  - Version history
  - Maintenance notes
  - Self-improvement hooks
  
writing_style: "Technical specification, schemas, protocols"

example_structure: |
  ## L4 — TECHNICAL SPECIFICATIONS
  
  ### Input Schema
  [JSON/YAML schema]
  
  ### Output Schema
  [JSON/YAML schema]
  
  ### MOD Integration
  <AwakeningProtocol>
    [When MOD should activate this skill]
  </AwakeningProtocol>
  
  ### MMA Quality Gates
  <QualityValidation>
    [What MMA should check]
  </QualityValidation>
  
  ### Self-Improvement Hooks
  [How this skill learns and adapts]
```

---

### STEP 4: NEURO-BOX INTEGRATION

**Map skill function to Neuro-Box dimensions:**

```yaml
neurobox_mapping:
  analysis:
    primary_dimensions: [Which 1-2 dimensions this skill primarily activates]
    secondary_dimensions: [Which dimensions it supports]
    balance_requirement: [Any specific axis balance needed]
    
  activation_sequence:
    - "Step 1 activates [DIMENSION] by [mechanism]"
    - "Step 2 activates [DIMENSION] by [mechanism]"
    - "Step 3 balances [AXIS] via [technique]"
    
  red_flag_prevention:
    - "Prevent [MANIPULATION_PATTERN] by [safeguard]"
    - Example: "Prevent SIGNIFICANT without SAFE by requiring trust-building first"
```

**Add to skill procedure:**
```xml
<NeuroBoxGuidance>
  <PrimaryActivation>
    This skill primarily activates: [DIMENSION]
    Mechanism: [How it activates this dimension]
  </PrimaryActivation>
  
  <SequenceOptimization>
    For maximum resonance, activate in this order:
    1. [DIMENSION] - [How]
    2. [DIMENSION] - [How]
    3. [DIMENSION] - [How]
  </SequenceOptimization>
  
  <BalanceChecks>
    Verify axis balance:
    - [AXIS]: Should be [balanced|weighted_toward]
    - Watch for: [Imbalance pattern to avoid]
  </BalanceChecks>
</NeuroBoxGuidance>
```

---

### STEP 5: MOD/MMA COORDINATION

**Define awakening protocol:**

```yaml
awakening_protocol:
  triggers:
    keyword_triggers: [List keywords that should awaken this skill]
    context_triggers: [Conditions that indicate this skill needed]
    upstream_triggers: [Other skills that should invoke this one]
    
  awakening_conditions:
    required_inputs: [What must be present to awaken]
    optional_inputs: [What enhances execution but not required]
    blocking_conditions: [What prevents awakening]
    
  coordination_pattern:
    typical_sequence: |
      1. MOD receives request
      2. MOD awakens [UPSTREAM_SKILL] first
      3. UPSTREAM_SKILL output ready
      4. MOD awakens THIS_SKILL with upstream output
      5. THIS_SKILL executes
      6. MMA validates output
      7. MOD delivers or routes for fixes
```

**Define MMA quality gates:**

```yaml
mma_quality_gates:
  scorecard_priorities:
    high_weight: [Which MMA dimensions most important for this skill]
    medium_weight: [Which dimensions moderately important]
    low_weight: [Which dimensions less critical]
    
  pass_criteria:
    minimum_scores:
      - "[DIMENSION]: ≥ [THRESHOLD]"
      - "[DIMENSION]: ≥ [THRESHOLD]"
    average_threshold: "[VALUE]"
    
  common_failure_modes:
    - failure_mode: "[Description]"
      mma_detection: "Low score on [dimension]"
      fix_pattern: "Route to [specialist] for [action]"
      
  routing_logic:
    - "If [condition] → Route to [specialist]"
    - "If [condition] → Route to [specialist]"
```

---

### STEP 6: SELF-IMPROVEMENT HOOKS

**Build learning capabilities into skill:**

```yaml
self_improvement:
  performance_tracking:
    - Track: Execution count
    - Track: MMA scores per execution
    - Track: Human satisfaction ratings
    - Track: Time to completion
    
  pattern_learning:
    - Detect: Recurring failure modes
    - Learn: Which fixes work best
    - Adapt: Heuristics based on outcomes
    - Store: Successful patterns in memory
    
  threshold_adaptation:
    - Monitor: Score distributions
    - Adjust: Quality thresholds based on outcomes
    - Calibrate: Against human feedback
    
  skill_evolution:
    triggers_for_update:
      - "MMA scores declining over 20 executions"
      - "New pattern detected 5+ times"
      - "Human feedback indicates gap"
      
    update_protocol:
      1. Generate patch proposal
      2. Human review
      3. Apply if approved
      4. Measure improvement
      5. Roll back if worse
```

**Add to L4:**
```xml
<SelfImprovement>
  <PerformanceTracking>
    Store: [What metrics to track]
    Frequency: [How often to measure]
  </PerformanceTracking>
  
  <LearningHooks>
    - After each execution: [What to store]
    - After 20 executions: [What to analyze]
    - Quarterly: [What to recalibrate]
  </LearningHooks>
  
  <EvolutionTriggers>
    <Trigger>
      Condition: [What indicates skill needs update]
      Action: [How to propose/apply update]
    </Trigger>
  </EvolutionTriggers>
</SelfImprovement>
```

---

### STEP 7: GENERATE COMPLETE SKILL FILE

**Assemble all components into XML:**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Skill>
  <!-- YAML Header -->
  <Meta>
    <n>[skill_name]</n>
    <Type>[foundation|capability|constraint|awakening]</Type>
    <Version>1.0.0</Version>
    <Status>draft</Status>
    <Model>claude-sonnet-4-20250514</Model>
    <TokenBudget>[500-8000]</TokenBudget>
  </Meta>
  
  <!-- Contract -->
  <Contract>
    <InputsRequired>
      [List]
    </InputsRequired>
    <InputsOptional>
      [List]
    </InputsOptional>
    <OutputsPrimary>
      [List]
    </OutputsPrimary>
  </Contract>
  
  <!-- Dependencies -->
  <Dependencies>
    <Upstream>
      [Skills that feed into this]
    </Upstream>
    <Downstream>
      [Skills that consume this output]
    </Downstream>
  </Dependencies>
  
  <!-- MOD Integration -->
  <MODIntegration>
    <AwakeningProtocol>
      [Triggers and conditions]
    </AwakeningProtocol>
    <CoordinationPattern>
      [Typical sequence]
    </CoordinationPattern>
  </MODIntegration>
  
  <!-- MMA Integration -->
  <MMAIntegration>
    <QualityGates>
      [What MMA should check]
    </QualityGates>
    <PassCriteria>
      [Thresholds for PASS verdict]
    </PassCriteria>
    <CommonFailures>
      [Failure modes and fixes]
    </CommonFailures>
  </MMAIntegration>
  
  <!-- Constitutional Compliance -->
  <ConstitutionalCompliance>
    <NorthStar>
      [Alignment statement]
    </NorthStar>
    <Guardrails>
      [Hard and soft constraints]
    </Guardrails>
    <ResonanceAlignment>
      [Neuro-Box mapping]
    </ResonanceAlignment>
  </ConstitutionalCompliance>
  
  <!-- Guardrails -->
  <Guardrails>
    <Hard>
      [Never violate these]
    </Hard>
    <Soft>
      [Prefer these approaches]
    </Soft>
  </Guardrails>
  
  <!-- Layer 1: Quick Reference -->
  <Layer1_Core>
    [L1 content - 300-500 tokens]
  </Layer1_Core>
  
  <!-- Layer 2: Core Procedure -->
  <Layer2_Context>
    [L2 content - 1500-2000 tokens]
  </Layer2_Context>
  
  <!-- Layer 3: Advanced Usage -->
  <Layer3_Examples>
    [L3 content - 2000-3000 tokens]
  </Layer3_Examples>
  
  <!-- Layer 4: Technical Spec -->
  <Layer4_Constitutional>
    [L4 content - 1500-2500 tokens]
  </Layer4_Constitutional>
  
  <!-- Neuro-Box Guidance -->
  <NeuroBoxGuidance>
    [Dimension activation instructions]
  </NeuroBoxGuidance>
  
  <!-- Self-Improvement -->
  <SelfImprovement>
    [Learning and evolution hooks]
  </SelfImprovement>
  
  <!-- Activation Triggers -->
  <ActivationTriggers>
    <Trigger type="keyword">[keyword]</Trigger>
    <Trigger type="context">[condition]</Trigger>
  </ActivationTriggers>
  
  <!-- Examples -->
  <Examples>
    <Example name="[scenario_name]">
      <Context>[Setup]</Context>
      <Input>[Sample input]</Input>
      <Output>[Expected output]</Output>
      <MMAScore>[Expected score]</MMAScore>
    </Example>
  </Examples>
  
  <!-- Version History -->
  <VersionHistory>
    <Version number="1.0.0" date="[date]">
      <Changes>
        <Change>Initial creation</Change>
      </Changes>
      <Status>draft</Status>
    </Version>
  </VersionHistory>
</Skill>
```

---

### STEP 8: GENERATE TEST SUITE

**Create validation test cases:**

```yaml
test_suite:
  test_1_basic_functionality:
    name: "Basic Happy Path"
    inputs:
      [Minimal valid inputs]
    expected_output:
      [What should be produced]
    expected_mma_score: "> 7.5"
    
  test_2_edge_case:
    name: "[Specific edge case]"
    inputs:
      [Edge case inputs]
    expected_output:
      [How skill should handle]
    expected_mma_score: "> 7.0"
    
  test_3_failure_mode:
    name: "[Known failure pattern]"
    inputs:
      [Inputs that would trigger failure]
    expected_behavior:
      - Detect issue
      - Apply safeguard
      - Generate appropriate output or ESCALATE
    
  test_4_integration:
    name: "MOD/MMA Integration"
    scenario:
      - MOD awakens skill with [inputs]
      - Skill executes
      - MMA evaluates
    expected_flow:
      - MOD → Skill → MMA → [verdict]
    
  test_5_constitutional:
    name: "Constitutional Compliance"
    inputs:
      [Inputs that test guardrails]
    expected_behavior:
      - Guardrails activated
      - Violations blocked
      - Resonance maintained
```

---

### STEP 9: GENERATE INTEGRATION SPEC

**Document coordination details:**

```markdown
# [SKILL_NAME] Integration Specification

## MOD Coordination

**When MOD should awaken this skill:**
- [Trigger condition 1]
- [Trigger condition 2]
- [Trigger condition 3]

**Typical workflow:**
```
1. User request: [example]
2. MOD routes to: [upstream_skill if needed]
3. MOD awakens: [this_skill]
4. Skill requires: [inputs]
5. Skill produces: [outputs]
6. MOD sends to: MMA for validation
7. MMA decision: [PASS|FIX|ESCALATE]
8. MOD final action: [deliver or route]
```

**Context handoff:**
- MOD provides: [list of inputs]
- Skill expects: [format details]
- Skill returns: [format details]

## MMA Validation

**Quality gates:**
- [Dimension]: must score ≥ [threshold]
- [Dimension]: must score ≥ [threshold]
- Average: must be ≥ [threshold]

**Common failure modes:**
1. [Failure]: Detected by low [dimension], route to [specialist]
2. [Failure]: Detected by low [dimension], route to [specialist]

**Constitutional checks:**
- [Constraint]: MMA must verify [condition]
- [Constraint]: MMA must block if [violation]

## Memory Integration

**This skill stores:**
- [What goes into episodic memory]
- [What goes into semantic memory]
- [What goes into procedural memory]

**This skill consults:**
- [What it queries from memory before execution]
- [How memory informs decisions]

## Self-Improvement

**Performance tracking:**
- Metric: [what to track]
- Frequency: [how often]
- Threshold: [when to trigger review]

**Evolution triggers:**
- [Condition that indicates skill needs update]
```

---

### STEP 10: DEPLOYMENT CHECKLIST

**Generate validation checklist:**

```markdown
# [SKILL_NAME] Deployment Checklist

## Pre-Deployment Validation

### Structure Validation
- [ ] All 4 layers present (L1, L2, L3, L4)
- [ ] Token budgets appropriate (L1: 300-500, L2: 1500-2000, etc.)
- [ ] XML structure valid
- [ ] YAML header complete

### Content Validation
- [ ] Purpose clearly stated
- [ ] Core procedure executable
- [ ] Examples provided (minimum 2)
- [ ] Anti-patterns documented
- [ ] Edge cases covered

### Integration Validation
- [ ] MOD awakening triggers defined
- [ ] MMA quality gates specified
- [ ] Input/output schemas documented
- [ ] Constitutional compliance section complete

### Constitutional Validation
- [ ] North Star alignment verified
- [ ] Resonance principle upheld
- [ ] Guardrails comprehensive
- [ ] No manipulation patterns

### Neuro-Box Validation
- [ ] Dimension mapping clear
- [ ] Activation sequence defined
- [ ] Balance requirements specified
- [ ] Red flag prevention in place

### Self-Improvement Validation
- [ ] Performance tracking defined
- [ ] Learning hooks present
- [ ] Evolution triggers specified
- [ ] Metrics identified

## Testing

- [ ] Test 1 (Basic) passed
- [ ] Test 2 (Edge case) passed
- [ ] Test 3 (Failure mode) handled
- [ ] Test 4 (Integration) working
- [ ] Test 5 (Constitutional) compliant

## Documentation

- [ ] Integration spec created
- [ ] Test suite documented
- [ ] Deployment checklist complete
- [ ] Version history initiated

## Approval

- [ ] Technical review complete
- [ ] Constitutional review complete
- [ ] Human approval obtained
- [ ] Ready for production deployment

## Post-Deployment

- [ ] Monitoring dashboard configured
- [ ] Performance baseline established
- [ ] Feedback mechanism active
- [ ] Scheduled for first reflection cycle (after 20 executions)
```

---

## L3 — ADVANCED USAGE

### Pattern: Multi-Skill Coordination

**When building a skill that orchestrates other skills:**

```yaml
coordination_skill:
  type: "orchestrator"
  
  layer_structure:
    L1: "High-level workflow (what skills in what order)"
    L2: "Detailed coordination logic (how to pass context)"
    L3: "Edge cases (what if skill X fails, how to adapt)"
    L4: "Technical spec for skill-to-skill communication"
    
  example_structure:
    - "Step 1: Awaken Skill A with inputs X, Y"
    - "Step 2: Pass Skill A output to Skill B"
    - "Step 3: If Skill B scores < 7, awaken Skill C for fix"
    - "Step 4: Synthesize all outputs into final deliverable"
```

### Pattern: Knowledge-Heavy Skills

**When domain knowledge is extensive (>5000 words):**

```yaml
knowledge_compression:
  L1_strategy: "Distill to absolute essence - decision tree or formula"
  L2_strategy: "Core workflow with references to knowledge sections"
  L3_strategy: "Full knowledge embedded - this is where masterclass lives"
  L4_strategy: "Schema for knowledge queries, not full knowledge"
  
  knowledge_organization:
    - Use subsections in L3
    - Create named patterns that can be referenced
    - Build decision trees that navigate knowledge
    - Provide lookup tables for quick reference
```

### Anti-Pattern: Scope Creep

**What:** Skill tries to do too many things

**Why it fails:**
- Violates progressive disclosure (L1 becomes huge)
- Confuses MOD (unclear when to awaken)
- Confuses MMA (unclear how to evaluate)
- Maintenance nightmare

**Fix:**
```
1. Identify distinct functions
2. Split into multiple skills
3. Create orchestrator skill if needed
4. Define clear handoffs between skills

Example:
❌ "Email Master Skill" (opener + body + CTA + sequence planning)
✅ Split into:
  - Email Opener Specialist
  - Email Body Builder
  - Email CTA Architect
  - Email Sequence Planner
  + Email Package Orchestrator (coordinates above)
```

### Anti-Pattern: Missing Constitutional Grounding

**What:** Skill lacks clear alignment with North Star

**Why it fails:**
- Enables drift over time
- No clear guardrails
- MMA can't enforce compliance

**Fix:**
```
ALWAYS include:

<ConstitutionalCompliance>
  <NorthStar>
    This skill exists to [specific alignment with marketing transformation]
  </NorthStar>
  
  <Guardrails>
    <Hard>
      NEVER: [specific prohibitions]
      ALWAYS: [specific requirements]
    </Hard>
  </Guardrails>
</ConstitutionalCompliance>

Test question: "Could this skill be used for something unethical?"
If yes → Add more specific guardrails
```

### Edge Case: Human-in-the-Loop Skills

**When skill requires human creativity/judgment:**

```yaml
hybrid_pattern:
  skill_role: "Prepare, structure, suggest - not decide"
  human_role: "Final decisions, creative choices, approvals"
  
  workflow:
    1. Skill generates 3-5 options
    2. Skill explains pros/cons of each
    3. Skill recommends top choice with reasoning
    4. Human makes final decision
    5. Skill executes based on human choice
    
  L2_modification:
    - Add "Human Decision Point" steps
    - Provide decision-support information
    - Make recommendations, not decisions
    - Wait for human input before proceeding
```

---

## L4 — TECHNICAL SPECIFICATIONS

### Output Schema: Skill File

```xml
<!-- This is the schema for the skill file this skill produces -->
<Skill>
  <Meta>...</Meta>
  <Contract>...</Contract>
  <Dependencies>...</Dependencies>
  <MODIntegration>...</MODIntegration>
  <MMAIntegration>...</MMAIntegration>
  <ConstitutionalCompliance>...</ConstitutionalCompliance>
  <Guardrails>...</Guardrails>
  <Layer1_Core>...</Layer1_Core>
  <Layer2_Context>...</Layer2_Context>
  <Layer3_Examples>...</Layer3_Examples>
  <Layer4_Constitutional>...</Layer4_Constitutional>
  <NeuroBoxGuidance>...</NeuroBoxGuidance>
  <SelfImprovement>...</SelfImprovement>
  <ActivationTriggers>...</ActivationTriggers>
  <Examples>...</Examples>
  <VersionHistory>...</VersionHistory>
</Skill>
```

### MOD Integration: This Skill

```yaml
awakening_protocol:
  triggers:
    - keyword: "build skill"
    - keyword: "create skill"
    - keyword: "generate skill"
    - context: User provides domain knowledge document
    - context: User requests skill for specific task
    
  required_inputs:
    - skill_concept (name + purpose)
    - domain_knowledge (some form of expertise)
    
  optional_inputs:
    - target_output_type
    - constitutional_constraints
    - dependencies
    
  coordination:
    - MOD receives: "Build me a skill for X"
    - MOD awakens: Skill Architect (this skill)
    - Skill Architect generates: Complete skill file
    - MOD sends to: MMA for validation
    - MMA checks: Completeness, constitutional alignment
    - MOD delivers: Skill file + test suite + integration spec
```

### MMA Quality Gates: For Skills Built By This Skill

```yaml
skill_quality_validation:
  structure_check:
    - All 4 layers present
    - Token budgets appropriate
    - XML validity
    
  content_check:
    - Purpose clear and bounded
    - Procedure executable
    - Examples sufficient
    - Guardrails comprehensive
    
  integration_check:
    - MOD awakening defined
    - MMA quality gates specified
    - Input/output schemas present
    
  constitutional_check:
    - North Star alignment explicit
    - Guardrails specific and enforceable
    - No manipulation patterns enabled
    
  pass_criteria:
    - All structure checks passed
    - All content checks passed
    - All integration checks passed
    - All constitutional checks passed
    
  common_failure:
    failure: "Skill scope too broad"
    detection: "L1 layer exceeds 800 tokens"
    fix: "Route back to Skill Architect to split into multiple skills"
```

### Self-Improvement: This Skill

```yaml
learning_protocol:
  after_each_skill_built:
    - Store: Skill concept, domain, output quality
    - Track: MMA score of generated skill
    - Track: Human satisfaction with skill
    
  after_20_skills_built:
    - Analyze: Which types of skills score highest
    - Analyze: Common failure patterns in generated skills
    - Analyze: Token budget accuracy
    - Adjust: Templates based on successful patterns
    
  quarterly_reflection:
    - Review: All skills built this quarter
    - Identify: Emerging patterns in skill requests
    - Update: Skill Architect procedure to handle new patterns
    - Calibrate: Quality thresholds
    
  evolution_triggers:
    - "If >30% of generated skills need major revision → update templates"
    - "If new skill type requested 5+ times → add specialized template"
    - "If constitutional violations in generated skills → strengthen guardrails"
```

---

## EXAMPLES

### Example 1: Building Simple Skill

**Input:**
```
Build a "Headline Analyzer" skill that scores headlines on clarity, emotional impact, and curiosity using a 1-10 scale.
```

**Output:**
```xml
<Skill>
  <Meta>
    <n>headline-analyzer</n>
    <Type>capability</Type>
    <Version>1.0.0</Version>
    <TokenBudget>2000</TokenBudget>
  </Meta>
  
  <Layer1_Core>
    Score headlines on 3 dimensions:
    1. Clarity (1-10): Can reader understand in 2 seconds?
    2. Emotional Impact (1-10): Does it trigger feeling?
    3. Curiosity (1-10): Does it create information gap?
    
    Fast Decision:
    - Average ≥ 8 → Strong headline
    - Average 6-7 → Good, could be stronger
    - Average < 6 → Needs work
  </Layer1_Core>
  
  <Layer2_Context>
    [Full scoring procedure with examples]
  </Layer2_Context>
  
  <Layer3_Examples>
    [Advanced patterns, common failure modes]
  </Layer3_Examples>
  
  <Layer4_Constitutional>
    [MOD/MMA integration, schemas]
  </Layer4_Constitutional>
</Skill>
```

### Example 2: Building Complex Orchestrator Skill

**Input:**
```
Build "Sales Page Builder" skill that coordinates MESSAGE_SPINE, VOICE_GUIDE, and multiple specialist skills to create complete sales pages.
```

**Output:**
```xml
<Skill>
  <Meta>
    <n>sales-page-builder</n>
    <Type>orchestrator</Type>
    <Version>1.0.0</Version>
    <TokenBudget>4000</TokenBudget>
  </Meta>
  
  <Layer1_Core>
    Orchestrates 7 specialist skills:
    1. Headline Specialist
    2. Opener Specialist
    3. Promise Builder
    4. Proof Architect
    5. Objection Handler
    6. CTA Creator
    7. Page Flow Optimizer
    
    Sequence:
    Load MESSAGE_SPINE + VOICE_GUIDE → Awaken specialists in order → Synthesize sections → MMA validates → Deliver
  </Layer1_Core>
  
  <Layer2_Context>
    [Detailed coordination logic, handoff protocols]
  </Layer2_Context>
  
  <Layer3_Examples>
    [Edge cases, failure recovery, adaptation patterns]
  </Layer3_Examples>
  
  <Layer4_Constitutional>
    [Multi-skill coordination schemas, constitutional enforcement]
  </Layer4_Constitutional>
</Skill>
```

---

## VERSION HISTORY

### v2.0.0 (2024-12-24)
- Complete rebuild integrating ULTRAMIND architecture
- Added Neuro-Box integration guidance
- Added self-improvement hooks
- Added constitutional compliance framework
- Added MOD/MMA coordination protocols
- Added memory integration patterns
- Enhanced with self-annealing concepts

### v1.0.0 (2024-12-16)
- Initial release (basic skill generation)

---

**END OF SKILL ARCHITECT SPECIFICATION**

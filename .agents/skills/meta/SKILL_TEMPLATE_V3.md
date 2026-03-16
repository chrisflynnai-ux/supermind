# [SKILL_NAME] v[VERSION]
## [One-line description of what this skill does]

<!--
  ULTRAMIND SKILL TEMPLATE v3.0
  
  Unified format merging:
  - SKILL_ARCHITECT_v2 (process steps, examples, profiles)
  - SKILL_TEMPLATE_V2.xml (L1-L4 layers, MOD routing, MMA gates)
  - Knowledge Refinery Pipeline (extraction patterns)
  
  Instructions:
  1. Replace ALL [BRACKETED_VALUES] with actual content
  2. Delete sections marked (optional) if not needed
  3. Keep XML companion file (skill.xml) synchronized
-->

**Skill ID:** `[skill_id_snake_case]`  
**Domain:** `[meta|copy|product|research|design|tools]`  
**Tier:** `[system|meta|production|experimental]`  
**Model:** `[sonnet|opus|haiku]`  
**Status:** `[draft|beta|active|deprecated]`  
**Version:** `[semver]`  
**Created:** `[YYYY-MM-DD]`  
**Last Modified:** `[YYYY-MM-DD]`

---

## ZERO-POINT SCHEMA (~100 tokens)

```json
{
  "skill": "[skill_id]",
  "desc": "[15-word max description]",
  "triggers": ["[keyword]", "[phrase]", "[task_type]"],
  "inputs": ["PROJECT_BRIEF", "[other_required]"],
  "outputs": ["[PRIMARY_OUTPUT]"],
  "wakes": ["[sister_skill_id]"],
  "budget": {
    "L1": 500,
    "L2": 1500,
    "L3": 3000,
    "L4": 6000
  }
}
```

---

## L1: CORE REFERENCE (Always Loaded ~500 tokens)

### Purpose
[2-3 sentences explaining what this skill does and why it exists]

### Primary Outcome
[What this skill produces as its main deliverable]

### Use When
- [Trigger situation 1]
- [Trigger situation 2]
- [Trigger situation 3]

### Do NOT Use When
- [Anti-pattern 1 — use [other_skill] instead]
- [Anti-pattern 2]

### Quick Start
```
INPUT: [What user provides]
↓
PROCESS: [Core transformation]
↓
OUTPUT: [What skill produces]
```

---

## L2: STANDARD EXECUTION (Default Load ~1500 tokens)

### Contract (I/O Specification)

#### Required Inputs

| Input | Type | Source | Description |
|-------|------|--------|-------------|
| `PROJECT_BRIEF` | SSOT | upstream/user | Objective, audience, constraints |
| `[input_name]` | `[ssot\|artifact\|parameter]` | `[source]` | [description] |

#### Optional Inputs

| Input | Type | Description |
|-------|------|-------------|
| `VOICE_GUIDE` | SSOT | Tone/style override (from profiles/ultramind_context.yaml#voice) |
| `EVIDENCE_PACK` | SSOT | Claims/proof to use |
| `MESSAGE_SPINE` | SSOT | Multi-asset consistency |

#### Primary Output

| Output | Format | Description |
|--------|--------|-------------|
| `[OUTPUT_NAME]` | `[markdown\|yaml\|json]` | [What it contains and structure] |

#### Secondary Outputs (optional)

| Output | Format | Description |
|--------|--------|-------------|
| `[secondary]` | `[format]` | [description] |

### Profile Requirements

```yaml
always_load:
  - profiles/ultramind_context.yaml#voice
  - profiles/ultramind_context.yaml#audience

load_if_claims:
  - profiles/ultramind_context.yaml#proof

load_if_multi_asset:
  - MESSAGE_SPINE
```

**Profile Application:**
- **Voice:** Apply tone traits, lexicon, signature moves, formatting rules
- **Audience:** Match their language, address their pains, respect awareness level
- **Business:** Stay within claims_allowed, respect constraints
- **Proof:** Back claims with case studies, stats, testimonials

### Process Steps

#### Step 1: Prewriting Decisions
Before any drafting, establish:
- [ ] **Promise:** [What reader/user gains from this output]
- [ ] **3 Tangible Points:** [Point 1] | [Point 2] | [Point 3]
- [ ] **Section Formats:** tips / stats / steps / lessons / examples / frameworks

#### Step 2: Outline
Produce structured outline:
- [ ] 5-10 headline/title options
- [ ] 3 subhead promises (what each section delivers)
- [ ] Bullet outline of body content

#### Step 3: Draft
Execution rules:
- [ ] Write body first, hook/intro last (if applicable)
- [ ] Maintain Voice DNA markers throughout
- [ ] Use ICP language (exact phrases where possible)
- [ ] Reference EVIDENCE_PACK for claims

#### Step 4: Variants (Recommended)
- [ ] Produce 2-3 alternate angles or openings
- [ ] Present options to orchestrator/user for direction selection

#### Step 5: Polish Pass
- [ ] **Compression:** Remove fluff, redundancy
- [ ] **Clarity:** Simplify complex sentences
- [ ] **Scannability:** Short paragraphs, clear structure
- [ ] **Cliché removal:** Replace with fresh language
- [ ] **Verb strengthening:** Active voice, specific verbs

### Quality Standards
- [Quality check 1: specific to this skill]
- [Quality check 2]
- [Quality check 3]
- [Quality check 4]
- [Quality check 5]

### Coordination Protocols

| Trigger | Wake Skill | Reason |
|---------|------------|--------|
| [When this happens] | `[skill_id]` | [Why coordination needed] |

---

## L3: ADVANCED USAGE (Load on complexity/edge cases ~3000 tokens)

### Quality Gate (MMA Integration)

#### 7-Dimension Scoring

| Dimension | Weight | Threshold | Validation Question |
|-----------|--------|-----------|---------------------|
| `strategy_alignment` | critical | 7.0 | Does output serve the core objective from PROJECT_BRIEF? |
| `clarity_structure` | high | 7.0 | Is output clear, scannable, well-organized? |
| `voice_consistency` | high | 7.0 | Does output match VOICE_GUIDE tone/style? |
| `proof_discipline` | critical | 8.0 | Are all claims backed by EVIDENCE_PACK or properly framed? |
| `neuro_resonance` | high | 7.0 | Does output activate target neuro-axes with proper balance? |
| `cta_integrity` | medium | 7.0 | Is call-to-action clear, singular, appropriately urgent? |
| `ethical_guardrails` | critical | 9.0 | Is output honest, respectful, manipulation-free? |

#### Ship/No-Ship Checklist
- [ ] Promise delivered (headline/subheads match content)
- [ ] Voice match (DNA markers present, no generic drift)
- [ ] ICP fit (pains addressed, language matches)
- [ ] Proof present (examples/stats/lessons where needed)
- [ ] Scannability (short paragraphs, clear structure)
- [ ] Business constraints respected (claims_allowed only)
- [ ] CTA correct (tone + next step appropriate)

### Edge Cases

| Case | Trigger | Approach | Modifications |
|------|---------|----------|---------------|
| [Edge case name] | [When this happens] | [How to handle] | [What changes from standard] |
| [Edge case 2] | [Trigger] | [Approach] | [Modifications] |

### Anti-Patterns

| Pattern | Detection | Root Cause | Recovery | Prevention |
|---------|-----------|------------|----------|------------|
| [Anti-pattern name] | [How to spot it] | [Why it happens] | [How to fix] | [How to avoid] |
| Generic AI drift | Bland, corporate tone | Voice DNA not applied | Reapply priority rules | Load voice profile first |
| Unsubstantiated claims | Claims without proof | EVIDENCE_PACK not referenced | Add citations | Require proof step |

### Failure Mode Playbook

#### FM1: [Failure Name]
- **Detection:** [Symptom description]
- **Recovery:**
  1. [Recovery step 1]
  2. [Recovery step 2]
  3. Rerun MMA validation
- **Log to:** learned_constraints.md

#### FM2: [Failure Name]
- **Detection:** [Symptom]
- **Recovery:** [Steps]

### Optimization Patterns

| Pattern | What It Optimizes | Implementation | Best For |
|---------|-------------------|----------------|----------|
| [Pattern name] | [What it improves] | [How to apply] | [When to use] |

### Extended Examples

#### Example 1: [Complete Walkthrough]

**Scenario:** [Detailed scenario description]

**Inputs:**
```yaml
PROJECT_BRIEF:
  objective: "[objective]"
  audience: "[audience]"
  constraints: "[constraints]"
```

**Process:**
1. [Step-by-step execution detail]
2. [Step]
3. [Step]

**Output:**
```
[Final result with annotations showing why it works]
```

**Why This Works:**
- [Reason 1]
- [Reason 2]

### Troubleshooting Guide

| Symptom | Diagnosis | Solution |
|---------|-----------|----------|
| [Observable problem] | [Likely cause] | [Fix steps] |

---

## L4: TECHNICAL SPECIFICATION (Meta-operations only ~3000 tokens)

### Dependencies

#### Upstream (This skill receives from)
| Skill | Priority | Provides |
|-------|----------|----------|
| `[upstream_skill_id]` | `[critical\|high\|medium]` | [What it provides] |

#### Downstream (This skill feeds into)
| Skill | Consumes |
|-------|----------|
| `[downstream_skill_id]` | [What it needs from this skill] |

#### Sister Skills (Always wake together)
| Skill | Coordination Reason |
|-------|---------------------|
| `[sister_skill_id]` | [Why they coordinate] |

### MOD Integration

#### Routing Triggers
```yaml
triggers:
  task_type: ["[task_type_value]"]
  deliverable: ["[deliverable_format]"]
  natural_language: ["[user_phrase_trigger]", "[phrase]"]
```

#### Layer Load Conditions
```yaml
default_load: "L1+L2"

load_L3_when:
  - complexity >= 4
  - edge_case_detected
  - optimization_requested
  
load_L4_when:
  - skill_building
  - debugging
  - meta_operation
```

#### Context Budget
```yaml
budget:
  estimated: [typical_token_count]
  maximum: [max_allowable_tokens]
  
unload_triggers:
  - task_completed
  - context_pressure
  - not_used_within_2_turns
```

### Input Schemas

#### PROJECT_BRIEF Schema
```yaml
required:
  project_id: string
  asset_id: string
  version: string
  owner_agent: string
  objective:
    goal: string
    constraints: list
  audience:
    segment: string
    awareness: string
    
optional:
  voice_override: object
  evidence_refs: list
```

### Output Schemas

#### [PRIMARY_OUTPUT] Schema
```yaml
format: "[markdown|yaml|json]"
structure:
  - section: "[section_name]"
    required: true
    content: "[description]"
  - section: "[section_name]"
    required: false
```

### Performance Benchmarks

| Metric | Target | Minimum |
|--------|--------|---------|
| Output quality (MMA avg) | >= 8.0 | >= 7.0 |
| Token efficiency | < 3000 tokens | < 5000 tokens |
| Execution time | < 2 minutes | < 5 minutes |

### Testing Specifications

#### Golden Run 1: [Test Case Name]
```yaml
id: "GR-[SKILL]-01"
inputs:
  PROJECT_BRIEF:
    objective: "[canonical objective]"
    audience: "[canonical audience]"
    
expected_output:
  format: "[format]"
  contains: ["[required element]", "[required element]"]
  
pass_criteria:
  - MMA scores all >= 7.0
  - "[specific quality check]"
  - "[specific quality check]"
```

### Neuro-Resonance Integration

```yaml
references_constitution: true

primary_axes:
  - "[HEAL|RENEW|RESONATE|PERSUADE|DESIGN|DEVELOP]"
  
audience_adaptation:
  cold: "[Strategy for cold audiences]"
  warm: "[Strategy for warm audiences]"
  hot: "[Strategy for hot audiences]"
```

---

## EXAMPLES

### ✅ Good Example (Voice Match)

```
[Paste short example of correct output that exemplifies:
- Correct voice/tone
- Proper structure
- Quality standards met]
```

**Why This Works:**
- [Specific reason 1]
- [Specific reason 2]
- [Specific reason 3]

### ❌ Bad Example (Generic AI Drift)

```
[Paste example of what to avoid:
- Generic tone
- Poor structure
- Quality issues]
```

**What Went Wrong:**
- [Problem 1]
- [Problem 2]
- [Problem 3]

---

## VERSION HISTORY

| Version | Date | Status | Changes |
|---------|------|--------|---------|
| [1.0.0] | [YYYY-MM-DD] | [active] | [Initial release / description] |

### Baseline MMA Scores
```yaml
# Established after first production run
strategy_alignment: 0.0
clarity_structure: 0.0
voice_consistency: 0.0
proof_discipline: 0.0
neuro_resonance: 0.0
cta_integrity: 0.0
ethical_guardrails: 0.0
average: 0.0
```

### Learned Constraints
```yaml
# Populated from failure modes and edge cases
constraints:
  - "[constraint learned from production]"
```

---

## COMPANION FILES

| File | Purpose | Sync Status |
|------|---------|-------------|
| `skill.xml` | Machine-readable MOD/MMA integration | [ ] Synchronized |
| `zero_point.json` | Always-loaded index | [ ] Synchronized |
| `implementation.py` | Code execution (if applicable) | [ ] Implemented |
| `flowgram.mmd` | Visual workflow | [ ] Created |
| `tests/test_skill.py` | Test suite | [ ] Written |

---

*ULTRAMIND Skill Template v3.0*  
*Unified: Agent-Centric + Skill-Centric + Pipeline-Centric*

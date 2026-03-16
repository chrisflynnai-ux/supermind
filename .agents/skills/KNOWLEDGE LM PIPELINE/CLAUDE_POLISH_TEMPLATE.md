# CLAUDE OPUS 4.5 POLISH PROMPT
## Final Production Quality Check for LCP Skill Bundles

**Use this prompt in Claude Web/API for final polish after Prism synthesis.**

---

# FINAL POLISH: LCP Skill Production Hardening

## ROLE

**ACT AS:** ULTRAMIND Quality Engineer & Production Hardener

**STANDARDS:**
- ULTRAMIND Constitution v2.1
- Lean Stack v2.0  
- Zero-Point Context Strategy
- Skills > MCPs Doctrine

**OBJECTIVE:** Transform draft skill bundles into production-ready, deployable assets.

---

## INPUT

[PASTE YOUR PRISM OUTPUT HERE]
- SKILL.md
- implementation.py
- flowgram.mmd
- zero_point.json

---

## POLISH CHECKLIST

### 1. CONSTITUTION COMPLIANCE (v2.1)

Verify each requirement:

**Token Discipline:**
- [ ] Zero-Point schema is < 100 tokens
- [ ] L1 layer is < 500 tokens
- [ ] L2 layer is < 1500 tokens
- [ ] L3 layer is < 3000 tokens
- [ ] L4 layer is < 6000 tokens
- [ ] No redundant information across layers

**Skills > MCPs:**
- [ ] Implementation uses CLI interface, not server
- [ ] No always-on schemas loaded
- [ ] File-based I/O preferred over API streaming
- [ ] Skill activates on-demand, unloads after

**Self-Annealing:**
- [ ] Retry decorator with exponential backoff
- [ ] Circuit breaker (max 3 attempts default)
- [ ] Failure logging for constraint learning
- [ ] Graceful degradation on permanent failure

**SSOT Integration:**
- [ ] Inputs defined with Pydantic schemas
- [ ] Outputs conform to standard structure
- [ ] Integration points clearly documented
- [ ] Stage A/B locking rules specified

---

### 2. LEAN STACK ALIGNMENT (v2.0)

**Domain Classification:**
```
meta     = Orchestration, system skills (ZPWO, MMA, TWA, TWE)
copy     = Persuasion, writing (SCD, HPE, NRA, ACM, SPC)
product  = Offers, transformations (PCG, TEA, QIPB)
research = Analysis, intelligence (MIS, Framework Extractor)
design   = Visual, brand (SDM, Image Planner)
tools    = Execution, utilities (Web Intelligence, Repo Ops)
```

**Verify:**
- [ ] Correct domain assigned
- [ ] Appropriate tier (production/draft)
- [ ] Model recommendation accurate (sonnet for most, opus for complex reasoning)

**Layer Placement:**
- [ ] L1 contains ONLY routing info and zero-point
- [ ] L2 contains execution essentials
- [ ] L3 contains detailed patterns and examples
- [ ] L4 contains complete edge cases and reference

---

### 3. CODE QUALITY (implementation.py)

**Type Safety:**
- [ ] All function parameters have type hints
- [ ] Pydantic models for all I/O
- [ ] Validators for complex fields
- [ ] Proper Optional[] and default handling

**Error Handling:**
```python
# Required pattern:
try:
    # Core logic
except SpecificException as e:
    logger.error(f"Specific error: {e}")
    # Handle gracefully
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    self._log_failure(e, context)
    raise
```

**Logging:**
- [ ] INFO level for normal flow
- [ ] WARNING for recoverable issues
- [ ] ERROR for failures
- [ ] DEBUG for detailed tracing (verbose mode)

**Testing:**
- [ ] test_implementation.py exists
- [ ] Fixtures provided for common scenarios
- [ ] Edge cases covered
- [ ] Sandbox mode tested separately

**CLI Interface:**
- [ ] --input/-i for input file
- [ ] --output/-o for output file (with default)
- [ ] --sandbox for isolated execution
- [ ] --verbose/-v for debug logging
- [ ] --help shows clear usage

---

### 4. DOCUMENTATION QUALITY

**SKILL.md Polish:**

Check each section:

**Zero-Point Schema:**
```json
// Must be valid JSON
// Must be < 100 tokens
// Must include: skill, desc, triggers, outputs
```

**Core Thesis:**
- Clear problem statement
- Unique approach explained
- Why this approach works
- 2-3 paragraphs max

**When To Use:**
- Specific trigger conditions (not vague)
- Clear anti-patterns
- Routing rules if complex

**Execution Pattern:**
- All inputs documented with types and examples
- Steps are numbered and clear
- Outputs have schemas
- Validation criteria explicit

**Learned Constraints:**
- At least 2-3 pre-populated from analysis
- Format: Description → Failure Mode → Resolution
- Dated for tracking

**Examples:**
- At least 2 complete examples
- Input → Output pairs
- Cover happy path and one edge case

---

### 5. VISUALIZATION QUALITY (flowgram.mmd)

**Mermaid Validation:**
- [ ] Renders without errors in Mermaid Live Editor
- [ ] Color coding meaningful (consistent with other skills)
- [ ] Subgraphs logical (Input/Process/Output/Quality)
- [ ] All decision points have both paths
- [ ] Sandbox mode shown as dotted line alternative

**Standard Color Scheme:**
```
Input:    fill:#e1f5fe (light blue)
Process:  fill:#fff3e0 (light orange)
Output:   fill:#e8f5e9 (light green)
Quality:  fill:#fce4ec (light pink)
Sandbox:  fill:#f3e5f5 (light purple)
Error:    fill:#ffebee (light red)
```

---

### 6. XML SKILL CONVERSION (If Needed)

Convert to full ULTRAMIND XML format:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  [SKILL NAME] v[VERSION]
  [Brief description]
  
  Domain: [domain]
  Tier: production
  Created: [date]
-->

<Skill
  skill_id="skill.[domain].[name].v[version_underscored]"
  name="[Full Name]"
  version="[semver]"
  tier="production"
  status="active"
  model="sonnet"
>

  <!-- ================================================================== -->
  <!-- METADATA                                                            -->
  <!-- ================================================================== -->
  
  <Meta>
    <n>[Full Name]</n>
    <Subtitle>[Tagline]</Subtitle>
    <Description>
      [Detailed description - can be multi-line]
    </Description>
    
    <DateCreated>[YYYY-MM-DD]</DateCreated>
    <LastUpdated>[YYYY-MM-DD]</LastUpdated>
    <CreatedBy agent_or_human="agent" agent_id="knowledge_refinery_pipeline"/>
    
    <PrimaryDomains>
      <Domain>[Primary domain]</Domain>
    </PrimaryDomains>
    
    <SuccessDefinition>
      [What does success look like for this skill?]
    </SuccessDefinition>
  </Meta>

  <!-- ================================================================== -->
  <!-- SCOPE                                                               -->
  <!-- ================================================================== -->
  
  <Scope>
    <WhenToUse>
      <Trigger>[Condition 1]</Trigger>
      <Trigger>[Condition 2]</Trigger>
      <Trigger>[Condition 3]</Trigger>
    </WhenToUse>
    
    <NotFor>
      <Item>[Anti-pattern 1]</Item>
      <Item>[Anti-pattern 2]</Item>
    </NotFor>
    
    <Boundaries>
      <Upstream>[What feeds this skill]</Upstream>
      <Downstream>[What this skill feeds]</Downstream>
    </Boundaries>
  </Scope>

  <!-- ================================================================== -->
  <!-- SSOT REQUIREMENTS                                                   -->
  <!-- ================================================================== -->
  
  <SSOT>
    <Required>
      <Input name="[INPUT_NAME]">[Description]</Input>
    </Required>
    
    <Optional>
      <Input name="[INPUT_NAME]" default="[value]">[Description]</Input>
    </Optional>
    
    <Outputs>
      <Output id="[OUTPUT_ID]" format="[json|yaml|markdown|file]">
        [Description]
      </Output>
    </Outputs>
  </SSOT>

  <!-- ================================================================== -->
  <!-- PROGRESSIVE DISCLOSURE                                              -->
  <!-- ================================================================== -->
  
  <ProgressiveDisclosure>
    
    <Layer id="L1" name="Quick Reference" token_budget="500">
      <LoadPriority>always</LoadPriority>
      <Purpose>Fast routing, zero-point essentials</Purpose>
      
      <ZeroPoint>
        <![CDATA[
{
  "skill": "[skill_id]",
  "desc": "[< 25 words]",
  "triggers": ["[kw1]", "[kw2]"],
  "outputs": ["[out1]", "[out2]"]
}
        ]]>
      </ZeroPoint>
      
      <RoutingRules>
        <![CDATA[
[Quick routing decision tree]
        ]]>
      </RoutingRules>
    </Layer>
    
    <Layer id="L2" name="Standard Execution" token_budget="1500">
      <LoadPriority>on_activation</LoadPriority>
      <Purpose>Standard execution context</Purpose>
      
      <ExecutionPattern>
        <![CDATA[
[Step-by-step execution pattern]
        ]]>
      </ExecutionPattern>
    </Layer>
    
    <Layer id="L3" name="Detailed Patterns" token_budget="3000">
      <LoadPriority>when_needed</LoadPriority>
      <Purpose>Detailed patterns, examples, edge cases</Purpose>
      
      <Patterns>
        <Pattern id="P-01" name="[Pattern Name]">
          [Pattern details]
        </Pattern>
      </Patterns>
      
      <Examples>
        <Example id="EX-01" name="[Example Name]">
          [Full example with input/output]
        </Example>
      </Examples>
    </Layer>
    
    <Layer id="L4" name="Complete Reference" token_budget="6000">
      <LoadPriority>rarely</LoadPriority>
      <Purpose>Complete reference, all edge cases</Purpose>
      
      <EdgeCases>
        <Case id="EC-01">[Edge case handling]</Case>
      </EdgeCases>
      
      <TroubleShooting>
        <Issue id="TS-01">
          <Symptom>[What goes wrong]</Symptom>
          <Cause>[Why]</Cause>
          <Resolution>[How to fix]</Resolution>
        </Issue>
      </TroubleShooting>
    </Layer>
    
  </ProgressiveDisclosure>

  <!-- ================================================================== -->
  <!-- LEARNED CONSTRAINTS                                                 -->
  <!-- ================================================================== -->
  
  <LearnedConstraints>
    <Constraint id="LC-01" discovered="[date]">
      <Description>[What the constraint is]</Description>
      <FailureMode>[What happens if violated]</FailureMode>
      <Resolution>[How to comply]</Resolution>
    </Constraint>
  </LearnedConstraints>

  <!-- ================================================================== -->
  <!-- VERSION HISTORY                                                     -->
  <!-- ================================================================== -->
  
  <VersionHistory>
    <Version number="1.0.0" date="[YYYY-MM-DD]">
      Initial release via Knowledge Refinery Pipeline
    </Version>
  </VersionHistory>

</Skill>
```

---

### 7. PRODUCTION READINESS REPORT

Generate final report:

```markdown
# Production Readiness Report: [SKILL_NAME] v[VERSION]

## Summary
- **Skill ID:** [skill_id]
- **Domain:** [domain]
- **Status:** Ready for Production / Needs Revision

## Compliance Scores

| Category | Score | Notes |
|----------|-------|-------|
| Constitution Compliance | [✓/✗] | [Notes] |
| Lean Stack Alignment | [✓/✗] | [Notes] |
| Code Quality | [✓/✗] | [Notes] |
| Documentation | [✓/✗] | [Notes] |
| Visualization | [✓/✗] | [Notes] |

## Issues Found

### Critical (Must Fix)
- [Issue 1]
- [Issue 2]

### Recommended (Should Fix)
- [Issue 1]
- [Issue 2]

### Minor (Nice to Have)
- [Issue 1]

## Changes Made During Polish

1. [Change 1]
2. [Change 2]
3. [Change 3]

## Integration Notes

**ZPWO Routing:**
- Trigger keywords: [list]
- Phase: [Draft/Produce/Polish]

**MMA Validation:**
- Clarity criteria: [specified]
- Completeness criteria: [specified]
- Correctness criteria: [specified]

**SKILLS_MANIFEST Entry:**
```yaml
- skill_id: [skill_id]
  name: [name]
  version: [version]
  domain: [domain]
  status: production
  path: skills/[name]/
```

## Deployment Checklist

- [ ] SKILL.md in final location
- [ ] implementation.py tested
- [ ] flowgram.mmd renders correctly
- [ ] zero_point.json validated
- [ ] Tests passing
- [ ] SKILLS_MANIFEST updated
- [ ] ZPWO routing rules added
- [ ] MMA criteria defined

## Sign-Off

**Reviewed By:** Claude Opus 4.5 (Knowledge Refinery Pipeline)
**Date:** [ISO date]
**Verdict:** [APPROVED / NEEDS REVISION]
```

---

## OUTPUT DELIVERY

Provide:

1. **Polished SKILL.md** — All sections refined
2. **Production implementation.py** — Fully typed, tested, documented
3. **Clean flowgram.mmd** — Renders perfectly
4. **Validated zero_point.json** — < 100 tokens, valid JSON
5. **XML skill file** — If conversion requested
6. **test_implementation.py** — With fixtures
7. **Production Readiness Report** — Summary of work

---

## FINAL NOTES

**Quality Bar:**
- Would I be confident deploying this to production?
- Does it follow every ULTRAMIND standard?
- Is the documentation clear enough for someone new?
- Are the failure modes handled gracefully?

**If anything fails these checks → Fix before delivery.**

---

*Claude Opus 4.5 Polish Template v1.0*
*Standard: ULTRAMIND Constitution v2.1 + Lean Stack v2.0*
*Output: Production-Ready LCP Skill Bundles*

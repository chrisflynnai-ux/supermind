---
name: skill-slug
description: >
  [1-2 sentence description of what this skill does and when to invoke it.
  Include trigger terms. Max 1024 chars. Third person.]
disable-model-invocation: true
argument-hint: "[optional-args]"
metadata:
  domain: meta
  skill_id: meta_skill_slug
  version: "1.0.0"
  track: T3
  team_role: specialist
  input_schema: "TaskRequest"
  output_schema: "TaskResult"
  min_mma_score: 8.0
  atoms: []
---

# Skill Name

## Purpose
[What this skill does and why it exists]

## When to Use
- [Trigger condition 1]
- [Trigger condition 2]

## Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Input Contract
```yaml
TaskRequest:
  task_id: string
  instruction: string
  track: T1|T2|T3|T4
  context_pointers: []
  constraints:
    token_budget: 8000
    timeout: 300
    min_mma_score: 8.0
```

## Output Contract
```yaml
TaskResult:
  task_id: string
  success: boolean
  output: string
  tokens_used: number
  mma_score: number
  artifacts: []
  insights: []
```

## Deep Knowledge
For full skill knowledge, see: `references/skill_slug_v1.0.0.xml`

## SelfCheck
Before submitting output, verify:
- [ ] Check 1
- [ ] Check 2
- [ ] Check 3

## Validation
Run: `python scripts/validate.py`

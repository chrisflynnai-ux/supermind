# SEQUENTIAL EXTRACTION PROTOCOL
## Handling 40+ Page Module Extractions in Atomic Pipeline v2.0

**Problem:** A single module requires 40+ pages of extracted knowledge  
**Solution:** Sequential chunked extraction by category, then recombination  
**Principle:** "Many small queries > One mega-prompt"

---

## THE SEQUENTIAL EXTRACTION ARCHITECTURE

```
┌─────────────────────────────────────────────────────────────────────────────────┐
│                    SEQUENTIAL EXTRACTION FOR LARGE MODULES                      │
├─────────────────────────────────────────────────────────────────────────────────┤
│                                                                                 │
│   40+ PAGE MODULE                                                               │
│   ───────────────                                                               │
│   ┌─────────────────────────────────────────────────────────────────────┐      │
│   │  Module 3: Workflow Translator                                      │      │
│   │  • 50 video sources                                                 │      │
│   │  • ~40 pages of extractable knowledge                               │      │
│   │  • Multiple knowledge categories                                    │      │
│   └─────────────────────────────────────────────────────────────────────┘      │
│                              │                                                  │
│                              ▼                                                  │
│   ════════════════════════════════════════════════════════════════════════     │
│                                                                                 │
│   PHASE 1: CHUNKED EXTRACTION (7 Sequential Runs)                              │
│   ───────────────────────────────────────────────                              │
│                                                                                 │
│   Run 1        Run 2        Run 3        Run 4                                 │
│   ──────       ──────       ──────       ──────                                │
│   HEURISTICS   SPECS        FAILURES     FRAMEWORKS                            │
│   (~6 pages)   (~8 pages)   (~5 pages)   (~4 pages)                            │
│       │            │            │            │                                  │
│       ▼            ▼            ▼            ▼                                  │
│   5-8 atoms    6-10 atoms   4-6 atoms    3-5 atoms                             │
│                                                                                 │
│   Run 5        Run 6        Run 7                                              │
│   ──────       ──────       ──────                                             │
│   PATTERNS     CHECKLISTS   WORKFLOWS                                          │
│   (~7 pages)   (~4 pages)   (~6 pages)                                         │
│       │            │            │                                               │
│       ▼            ▼            ▼                                               │
│   5-8 atoms    3-5 atoms    4-6 atoms                                          │
│                                                                                 │
│   ════════════════════════════════════════════════════════════════════════     │
│                                                                                 │
│   PHASE 2: ATOM LIBRARY (30-50 atoms total)                                    │
│   ─────────────────────────────────────────                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐      │
│   │  /library/atoms/module_3/                                           │      │
│   │  ├── heuristics/  (5-8 files)                                       │      │
│   │  ├── specs/       (6-10 files)                                      │      │
│   │  ├── failures/    (4-6 files)                                       │      │
│   │  ├── frameworks/  (3-5 files)                                       │      │
│   │  ├── patterns/    (5-8 files)                                       │      │
│   │  ├── checklists/  (3-5 files)                                       │      │
│   │  └── workflows/   (4-6 files)                                       │      │
│   └─────────────────────────────────────────────────────────────────────┘      │
│                              │                                                  │
│                              ▼                                                  │
│   ════════════════════════════════════════════════════════════════════════     │
│                                                                                 │
│   PHASE 3: NOTEBOOKLM RECOMBINATION                                            │
│   ─────────────────────────────────────                                        │
│   ┌─────────────────────────────────────────────────────────────────────┐      │
│   │  Upload all 30-50 atoms as sources                                  │      │
│   │  Query: "Cluster all atoms for Workflow Translator"                 │      │
│   │  Cross-link: "Find dependencies between atoms"                      │      │
│   │  Gap analysis: "What's missing?"                                    │      │
│   └─────────────────────────────────────────────────────────────────────┘      │
│                              │                                                  │
│                              ▼                                                  │
│   ════════════════════════════════════════════════════════════════════════     │
│                                                                                 │
│   PHASE 4: CLAUDE SYNTHESIS                                                    │
│   ─────────────────────────                                                    │
│   ┌─────────────────────────────────────────────────────────────────────┐      │
│   │  Input: Clustered atoms (now organized, cross-linked)               │      │
│   │  Output: Complete Double-II skill bundle                            │      │
│   └─────────────────────────────────────────────────────────────────────┘      │
│                                                                                 │
└─────────────────────────────────────────────────────────────────────────────────┘
```

---

## PHASE 1: SEQUENTIAL EXTRACTION RUNS

### The 7-Run Protocol

Each run focuses on **ONE category** to prevent NotebookLM overload:

| Run | Category | Focus Question | Expected Output |
|-----|----------|----------------|-----------------|
| 1 | **Heuristics** | "What rules of thumb guide decisions?" | 5-8 atoms |
| 2 | **Specs** | "What technical patterns/code exist?" | 6-10 atoms |
| 3 | **Failures** | "What breaks and how to prevent?" | 4-6 atoms |
| 4 | **Frameworks** | "What conceptual architectures?" | 3-5 atoms |
| 5 | **Patterns** | "What reusable code snippets?" | 5-8 atoms |
| 6 | **Checklists** | "What validation criteria?" | 3-5 atoms |
| 7 | **Workflows** | "What process sequences?" | 4-6 atoms |

**Total: 30-50 atoms across 7 runs**

---

### Run 1: HEURISTICS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — HEURISTICS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on HEURISTICS (rules of thumb).

## SOURCE BASE
[Your sources about workflow translation, n8n, automation]

## EXTRACTION TASK

**Extract ONLY heuristics** — rules of thumb that guide translation decisions.

For each heuristic, generate an atom using this exact format:

---

# ATOM: heuristic.[name].v1
# Source Ref: [Video/Doc name + timestamp/page]

## 1. CORE LOGIC
- **Constraint:** [One-sentence rule]
- **Rationale:** [Why this rule exists]

## 2. TECHNICAL PATTERN
- **Application:** [How to apply this rule]
- **Example:** [Concrete example if available]

## 3. FAILURE MODES
- **Warning:** [What happens if violated]
- **Fix:** [How to recover]

## 4. USAGE TRIGGER
- **Trigger:** [When to apply]
- **Anti-Trigger:** [When NOT to apply]

---

## HEURISTICS TO LOOK FOR
- Clustering rules (e.g., 10-to-1)
- Naming conventions
- Complexity thresholds
- Decision boundaries
- Simplification rules
- Priority ordering

## OUTPUT CONSTRAINTS
- Each atom: 1-2 pages MAX
- Naming: heuristic.[descriptive_name].v1
- Include source citations
- If you find 8+ heuristics, list the top 8 most important
```

---

### Run 2: SPECS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — SPECS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on TECHNICAL SPECIFICATIONS.

## EXTRACTION TASK

**Extract ONLY specs** — technical patterns, CLI commands, SDK usage.

For each spec, generate an atom:

---

# ATOM: spec.[name].v1
# Source Ref: [Citation]

## 1. CORE LOGIC
- **Specification:** [What this defines]
- **Rationale:** [Why this approach]

## 2. TECHNICAL PATTERN
- **Language/SDK:** [e.g., Python / n8n API]
- **Code Snippet:**
```python
# Exact pattern from source
```

## 3. FAILURE MODES
- **Warning:** [Edge cases, limitations]
- **Fix:** [Workarounds]

## 4. USAGE TRIGGER
- **Trigger:** [When to use this spec]
- **Anti-Trigger:** [When to use alternative]

---

## SPECS TO LOOK FOR
- CLI commands (uv run, npm, etc.)
- API endpoints and patterns
- Data structures and schemas
- Configuration formats
- SDK method signatures
- Protocol specifications

## OUTPUT CONSTRAINTS
- Each atom: 1-3 pages MAX
- Naming: spec.[descriptive_name].v1
- Include actual code where available
```

---

### Run 3: FAILURES Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — FAILURES ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on FAILURE MODES (learned constraints).

## EXTRACTION TASK

**Extract ONLY failures** — what breaks, why, and how to prevent.

For each failure, generate an atom:

---

# ATOM: failure.[name].v1
# Source Ref: [Citation]

## 1. THE FAILURE
- **What Breaks:** [Specific failure mode]
- **Symptoms:** [How you know it's happening]
- **Root Cause:** [Why it breaks]

## 2. THE IMPACT
- **Severity:** [Critical / High / Medium / Low]
- **Blast Radius:** [What else is affected]

## 3. PREVENTION
- **Pattern:** [How to avoid]
- **Code Example:**
```python
# Prevention pattern
```

## 4. RECOVERY
- **Detection:** [How to catch it]
- **Fix:** [How to recover]

---

## FAILURES TO LOOK FOR
- Context rot scenarios
- Scaling failures
- Integration breaks
- Data loss risks
- Performance degradation
- Security vulnerabilities

## OUTPUT CONSTRAINTS
- Each atom: 1-2 pages MAX
- Naming: failure.[descriptive_name].v1
- Be specific about conditions that trigger failure
```

---

### Run 4: FRAMEWORKS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — FRAMEWORKS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on CONCEPTUAL FRAMEWORKS.

## EXTRACTION TASK

**Extract ONLY frameworks** — mental models, architectures, conceptual structures.

For each framework, generate an atom:

---

# ATOM: framework.[name].v1
# Source Ref: [Citation]

## 1. THE MODEL
- **Name:** [Framework name]
- **Core Concept:** [One-paragraph summary]
- **Components:** [Key parts]

## 2. VISUAL REPRESENTATION
```
[ASCII diagram or description of structure]
```

## 3. APPLICATION
- **Use Case:** [When to apply this framework]
- **Decision Flow:** [How it guides decisions]

## 4. LIMITATIONS
- **Boundaries:** [Where this framework doesn't apply]
- **Alternatives:** [Other frameworks for edge cases]

---

## FRAMEWORKS TO LOOK FOR
- Architecture patterns (LCP, Double-II, etc.)
- Decision frameworks
- Classification systems
- Mental models for translation
- Layered approaches

## OUTPUT CONSTRAINTS
- Each atom: 1-3 pages MAX
- Naming: framework.[descriptive_name].v1
- Include diagrams where possible
```

---

### Run 5: PATTERNS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — PATTERNS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on REUSABLE CODE PATTERNS.

## EXTRACTION TASK

**Extract ONLY patterns** — reusable code snippets, templates, boilerplate.

For each pattern, generate an atom:

---

# ATOM: pattern.[name].v1
# Source Ref: [Citation]

## 1. PATTERN PURPOSE
- **What It Does:** [One-line description]
- **Problem It Solves:** [The pain point]

## 2. THE CODE
```python
# Complete, copy-paste ready pattern

def pattern_name():
    """Docstring explaining usage"""
    pass
```

## 3. USAGE EXAMPLE
```python
# How to use this pattern in practice
```

## 4. VARIATIONS
- **Variant A:** [Alternative for scenario X]
- **Variant B:** [Alternative for scenario Y]

---

## PATTERNS TO LOOK FOR
- Retry patterns
- Wrapper patterns
- Transformation patterns
- Validation patterns
- Error handling patterns
- Logging patterns

## OUTPUT CONSTRAINTS
- Each atom: 1-3 pages MAX
- Naming: pattern.[descriptive_name].v1
- Code must be copy-paste ready
```

---

### Run 6: CHECKLISTS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — CHECKLISTS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on VALIDATION CHECKLISTS.

## EXTRACTION TASK

**Extract ONLY checklists** — validation criteria, quality gates, review items.

For each checklist, generate an atom:

---

# ATOM: checklist.[name].v1
# Source Ref: [Citation]

## 1. PURPOSE
- **What It Validates:** [The thing being checked]
- **When To Use:** [At what stage]

## 2. THE CHECKLIST

### Required (Must Pass)
- [ ] [Item 1]
- [ ] [Item 2]
- [ ] [Item 3]

### Recommended (Should Pass)
- [ ] [Item 4]
- [ ] [Item 5]

### Optional (Nice to Have)
- [ ] [Item 6]

## 3. FAILURE ACTIONS
- **If Required Fails:** [What to do]
- **If Recommended Fails:** [What to do]

---

## CHECKLISTS TO LOOK FOR
- Pre-translation validation
- Post-translation validation
- Code quality checks
- Security checks
- Performance checks
- Integration readiness

## OUTPUT CONSTRAINTS
- Each atom: 1-2 pages MAX
- Naming: checklist.[descriptive_name].v1
- Use checkbox format
```

---

### Run 7: WORKFLOWS Extraction Prompt

```markdown
# NOTEBOOKLM EXTRACTION: Module 3 — WORKFLOWS ONLY

## CONTEXT
I am extracting Skill Atoms for Module 3: Workflow Translator.
This run focuses ONLY on PROCESS WORKFLOWS.

## EXTRACTION TASK

**Extract ONLY workflows** — step-by-step processes, sequences, procedures.

For each workflow, generate an atom:

---

# ATOM: workflow.[name].v1
# Source Ref: [Citation]

## 1. WORKFLOW PURPOSE
- **Goal:** [What this workflow achieves]
- **Input:** [What it starts with]
- **Output:** [What it produces]

## 2. THE STEPS

### Step 1: [Name]
- Action: [What to do]
- Tool: [What tool to use]
- Output: [What this step produces]

### Step 2: [Name]
- Action: [What to do]
- Tool: [What tool to use]
- Output: [What this step produces]

[Continue for all steps...]

## 3. DECISION POINTS
- **At Step N:** If [condition], then [branch A], else [branch B]

## 4. ERROR HANDLING
- **If Step X Fails:** [Recovery procedure]

---

## WORKFLOWS TO LOOK FOR
- Translation workflow (n8n → Python)
- Validation workflow
- Testing workflow
- Deployment workflow
- Rollback workflow

## OUTPUT CONSTRAINTS
- Each atom: 2-3 pages MAX
- Naming: workflow.[descriptive_name].v1
- Include decision points
```

---

## PHASE 2: ATOM LIBRARY ORGANIZATION

After all 7 runs, organize into folder structure:

```
/library/atoms/module_3_workflow_translator/
│
├── heuristics/
│   ├── heuristic.10_to_1_rule.v1.md
│   ├── heuristic.node_naming.v1.md
│   ├── heuristic.complexity_threshold.v1.md
│   ├── heuristic.credential_extraction.v1.md
│   └── heuristic.loop_translation.v1.md
│
├── specs/
│   ├── spec.n8n_json_schema.v1.md
│   ├── spec.python_output_format.v1.md
│   ├── spec.cli_interface.v1.md
│   ├── spec.pydantic_models.v1.md
│   └── spec.error_codes.v1.md
│
├── failures/
│   ├── failure.context_rot.v1.md
│   ├── failure.credential_exposure.v1.md
│   ├── failure.infinite_loop.v1.md
│   └── failure.type_mismatch.v1.md
│
├── frameworks/
│   ├── framework.lcp_translation.v1.md
│   ├── framework.node_to_function_mapping.v1.md
│   └── framework.intent_extraction.v1.md
│
├── patterns/
│   ├── pattern.retry_wrapper.v1.md
│   ├── pattern.json_parser.v1.md
│   ├── pattern.http_to_requests.v1.md
│   ├── pattern.switch_to_match.v1.md
│   └── pattern.webhook_handler.v1.md
│
├── checklists/
│   ├── checklist.pre_translation.v1.md
│   ├── checklist.post_translation.v1.md
│   └── checklist.deployment_ready.v1.md
│
└── workflows/
    ├── workflow.full_translation.v1.md
    ├── workflow.single_node_translation.v1.md
    ├── workflow.validation_sequence.v1.md
    └── workflow.rollback_procedure.v1.md
```

---

## PHASE 3: NOTEBOOKLM RECOMBINATION

### Upload All Atoms

Create a NEW NotebookLM notebook and upload all 30-50 atoms as individual sources.

### Recombination Queries

**Query 1: Dependency Mapping**
```
"Map the dependencies between all atoms. 
Which atoms reference other atoms? 
Create a dependency graph."
```

**Query 2: Gap Analysis**
```
"Based on the complete atom library for Module 3: Workflow Translator,
what knowledge gaps exist? What atoms are missing?"
```

**Query 3: Priority Ranking**
```
"Rank all atoms by importance for the core translation capability.
Which are essential vs. nice-to-have?"
```

**Query 4: Contradiction Check**
```
"Do any atoms contradict each other? 
Where do heuristics conflict with specs?
Flag any inconsistencies."
```

**Query 5: Synthesis Clusters**
```
"Group atoms into logical clusters for the final skill bundle:
- Core Translation Cluster
- Validation Cluster
- Error Handling Cluster
- Integration Cluster"
```

---

## PHASE 4: CLAUDE SYNTHESIS

### Final Compilation Prompt

```markdown
# CLAUDE SYNTHESIS: Module 3 — Workflow Translator

## INPUT
I have extracted 35 Skill Atoms across 7 categories for Module 3.
NotebookLM has clustered them into 4 logical groups.

[Paste the clustered atoms here - organized by cluster]

## CLUSTER 1: Core Translation
- heuristic.10_to_1_rule.v1
- framework.node_to_function_mapping.v1
- pattern.http_to_requests.v1
- workflow.single_node_translation.v1
...

## CLUSTER 2: Validation
- checklist.pre_translation.v1
- checklist.post_translation.v1
- failure.type_mismatch.v1
...

## CLUSTER 3: Error Handling
- failure.context_rot.v1
- pattern.retry_wrapper.v1
...

## CLUSTER 4: Integration
- spec.cli_interface.v1
- workflow.deployment_ready.v1
...

## TASK
Synthesize these atoms into a complete Double-II skill bundle:
1. SKILL.md — Information layer
2. implementation.py — Code layer
3. flowgram.mmd — Visual bridge
4. zero_point.json — Index

Apply all ULTRAMIND standards:
- Constitution v2.1 compliance
- Self-annealing patterns
- Pydantic type safety
- Progressive disclosure (L1-L4)
```

---

## TIME ESTIMATES

| Phase | Activities | Time |
|-------|------------|------|
| **Phase 1** | 7 extraction runs | 3-4 hours |
| **Phase 2** | Organize atoms | 30 min |
| **Phase 3** | Recombination queries | 1 hour |
| **Phase 4** | Claude synthesis | 1-2 hours |
| **Total** | | **5-7 hours** |

---

## TIPS FOR 40+ PAGE EXTRACTIONS

### 1. Batch by Theme, Not Size
Don't try to extract "pages 1-10, then 11-20."
Extract by category — all heuristics, then all specs, etc.

### 2. Run Fresh Notebooks
For each extraction run, you can use the SAME NotebookLM notebook.
Just change the prompt focus.

### 3. Track Coverage
Create a simple tracker:

```markdown
## Module 3 Extraction Tracker

| Category | Run Date | Atoms Generated | Coverage |
|----------|----------|-----------------|----------|
| Heuristics | 2026-01-30 | 6 | ✅ Complete |
| Specs | 2026-01-30 | 8 | ✅ Complete |
| Failures | | | ⏳ Pending |
| Frameworks | | | ⏳ Pending |
| Patterns | | | ⏳ Pending |
| Checklists | | | ⏳ Pending |
| Workflows | | | ⏳ Pending |
```

### 4. Iterate If Needed
If a run produces too many atoms, split further:
- `heuristics_translation.run1`
- `heuristics_validation.run2`

### 5. Quality Over Quantity
Better to have 30 high-quality atoms than 60 mediocre ones.
Each atom should be a **complete, standalone unit**.

---

## QUICK REFERENCE: SEQUENTIAL PROTOCOL

```
RUN 1: Extract HEURISTICS → 5-8 atoms
RUN 2: Extract SPECS → 6-10 atoms
RUN 3: Extract FAILURES → 4-6 atoms
RUN 4: Extract FRAMEWORKS → 3-5 atoms
RUN 5: Extract PATTERNS → 5-8 atoms
RUN 6: Extract CHECKLISTS → 3-5 atoms
RUN 7: Extract WORKFLOWS → 4-6 atoms
         ↓
ORGANIZE: Create folder structure
         ↓
RECOMBINE: Upload all atoms to fresh NotebookLM
         ↓
QUERY: Map dependencies, find gaps, cluster
         ↓
SYNTHESIZE: Feed clusters to Claude
         ↓
OUTPUT: Complete Double-II skill bundle
```

---

*Sequential Extraction Protocol v1.0*  
*For modules requiring 40+ pages of extraction*  
*"Many small queries > One mega-prompt"*

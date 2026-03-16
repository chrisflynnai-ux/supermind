# NOTEBOOKLM EXTRACTION PROMPT TEMPLATE
## For LCP Skill Bundle Development

**Copy this entire prompt into NotebookLM when starting a new extraction.**

---

# EXTRACTION: [MODULE NAME] Knowledge Synthesis

## CONTEXT
I am building an LCP (Lean Context Protocol) skill bundle for the ULTRAMIND ecosystem.
This notebook contains [N] sources about [TOPIC].

**Architecture Doctrine:** Skills + Scripts > MCPs  
**Target Output:** Production-ready skill documentation

---

## EXTRACTION OBJECTIVES

### 1. CORE THEMES (Priority: Critical)
Identify the 5-10 most important themes across all sources:

**Questions to Answer:**
- What concepts appear repeatedly across multiple sources?
- What frameworks, models, or methodologies are referenced?
- What core principles or beliefs underpin the content?
- What transformation or outcome is being promised?

**Output Format:**
```yaml
themes:
  - name: "[Theme Name]"
    importance: [1-10 scale]
    frequency: "[appears in X of Y sources]"
    summary: "[1-2 sentence synthesis]"
    key_quotes: ["[Direct quote with source]"]
    related_themes: ["[Theme A]", "[Theme B]"]
```

---

### 2. KNOWLEDGE HIERARCHY (Priority: High)
Extract the information architecture showing learning dependencies:

**Foundational (Must understand first):**
- Core definitions and terminology
- Fundamental principles
- Basic building blocks

**Intermediate (Build on foundations):**
- Applied techniques
- Patterns and frameworks
- Decision-making models

**Advanced (Require full context):**
- Complex integrations
- Edge cases and exceptions
- Advanced optimizations

**Output Format:**
```yaml
hierarchy:
  foundational:
    - concept: "[Name]"
      definition: "[Brief definition]"
      sources: ["[Source IDs]"]
      
  intermediate:
    - concept: "[Name]"
      definition: "[Brief definition]"
      requires: ["[Foundational concept names]"]
      
  advanced:
    - concept: "[Name]"
      definition: "[Brief definition]"
      requires: ["[Intermediate concept names]"]
```

---

### 3. CONTRADICTIONS & TENSIONS (Priority: High)
Where do sources disagree or present alternative approaches?

**Questions to Answer:**
- Do any sources directly contradict each other?
- Are there different schools of thought or approaches?
- What assumptions differ between sources?
- How might these tensions be resolved?

**Output Format:**
```yaml
contradictions:
  - tension: "[Description of the disagreement]"
    position_a:
      source: "[Source ID]"
      claim: "[What they say]"
    position_b:
      source: "[Source ID]"  
      claim: "[What they say]"
    resolution: "[How to synthesize or when each applies]"
```

---

### 4. ACTIONABLE PATTERNS (Priority: Critical)
What specific, repeatable patterns can be extracted for implementation?

**Pattern Types to Extract:**

**A) Frameworks** (Sequential processes)
```yaml
frameworks:
  - name: "[Framework Name]"
    steps:
      - "[Step 1]"
      - "[Step 2]"
      - "[Step 3]"
    when_to_use: "[Context/trigger]"
    expected_outcome: "[What it produces]"
```

**B) Decision Trees** (Conditional logic)
```yaml
decision_trees:
  - name: "[Decision Name]"
    trigger: "[When to use this decision tree]"
    branches:
      - condition: "[If X]"
        action: "[Then Y]"
      - condition: "[If A]"
        action: "[Then B]"
```

**C) Checklists** (Validation criteria)
```yaml
checklists:
  - name: "[Checklist Name]"
    purpose: "[What it validates]"
    items:
      - "[Check 1]"
      - "[Check 2]"
      - "[Check 3]"
```

---

### 5. ZERO-POINT CANDIDATES (Priority: Critical)
What information is so foundational it must ALWAYS be loaded?

**Constraints:**
- Total Zero-Point context should be < 200 tokens
- Only include what's absolutely essential for ANY task
- Think "if I forget everything else, what must I remember?"

**Output Format:**
```yaml
zero_point:
  definitions:
    - term: "[Key Term]"
      definition: "[< 20 words]"
      
  relationships:
    - "[A] → [B]": "[Nature of relationship, < 10 words]"
    
  constraints:
    - "[Must always...]"
    - "[Must never...]"
    
  triggers:
    - keyword: "[Trigger word]"
      activates: "[What skill/module]"
```

---

### 6. IMPLEMENTATION HINTS (Priority: Medium)
What clues exist for turning this knowledge into executable code?

**Extract:**
- APIs, tools, or services mentioned
- Code patterns or pseudocode suggested
- Data structures implied
- Integration points referenced
- Error handling approaches mentioned

**Output Format:**
```yaml
implementation_hints:
  tools_mentioned:
    - name: "[Tool/API]"
      purpose: "[What it's used for]"
      source: "[Where mentioned]"
      
  code_patterns:
    - pattern: "[Pattern name/description]"
      example: "[Brief code or pseudocode]"
      
  data_structures:
    - name: "[Structure type]"
      fields: ["[field1]", "[field2]"]
      
  error_handling:
    - scenario: "[What could go wrong]"
      approach: "[How to handle]"
```

---

### 7. QUOTES & CITATIONS (Priority: Medium)
Extract the most powerful quotes that capture core insights:

**Selection Criteria:**
- Captures a key principle in memorable language
- Would work as a "pull quote" in documentation
- Represents the source's core contribution

**Output Format:**
```yaml
key_quotes:
  - quote: "[Exact quote]"
    source: "[Source name/ID]"
    context: "[Brief context]"
    use_for: "[Where this quote would be valuable]"
```

---

## FINAL SYNTHESIS REQUEST

After extracting all the above, provide:

### 1. EXECUTIVE SUMMARY (3-5 sentences)
What is the core synthesis across all sources? What's the "one big idea"?

### 2. SKILL CAPABILITY STATEMENT
"This skill enables [WHO] to [DO WHAT] by [HOW] resulting in [OUTCOME]."

### 3. RECOMMENDED MODULE STRUCTURE
If this knowledge should be split into sub-modules, what would they be?

### 4. KNOWLEDGE GAPS
What important questions do these sources NOT answer? What's missing?

### 5. NEXT SOURCES NEEDED
What additional sources would strengthen this knowledge base?

---

## AUDIO/VIDEO OVERVIEW REQUESTS (Optional)

**For Audio Overview:**
"Create a 10-minute podcast-style discussion that explains the core thesis in the first 2 minutes, walks through the main themes conversationally, highlights the most surprising insights or contradictions, and ends with a clear 'if you remember one thing' takeaway."

**For FAQ Format:**
"Based on all sources, what are the 10 most important questions someone learning this topic would ask, and what are the synthesized answers?"

---

*Template Version: 1.0*
*Compatible with: ULTRAMIND Lean Stack v2.0*
*Target Output: LCP Skill Bundle inputs*

# Sales Page Deconstructor v2.0.0 — Quick Start Guide

**Purpose:** Extract patterns from high-performing sales pages to improve the entire ULTRAMIND system.

---

## 🚀 QUICK START (3 Steps)

### 1. Provide Sales Page
```
Options:
- Paste markdown content directly
- Provide URL (will fetch and analyze)
- Reference file path (e.g., "outputs/sleep_page_v3.md")
```

### 2. Add Context (Optional but Recommended)
```yaml
Performance data: "4.2% conversion rate"
Traffic source: "Cold traffic from Facebook ads"
Avatar: "Hormonal women 40+"
Comparison: "Compare to version 2 (outputs/sleep_page_v2.md)"
```

### 3. Receive Deconstruction Report
```
Output includes:
✅ Structure blueprint (flow, sections, CTAs)
✅ Mechanism framework (promise, proof, belief shifts)
✅ Offer architecture (value equation, pricing psychology)
✅ Voice signature (tone, rhythm, word patterns)
✅ 7S coverage scores (all 7 dimensions)
✅ Pattern library updates (new patterns discovered)
✅ Patch proposals (specific skill improvements)
✅ insights.md entry (session memory)
```

---

## 📋 SAMPLE COMMANDS

### Analyze Your Own Page
```
"Analyze the sales page at outputs/sleep_energy_v3.md and extract
what made it perform well (4.2% conversion). I want to codify the
patterns into our copy skills."
```

### Competitive Analysis
```
"I've saved a competitor's sales page to research/competitor_sleep_page.md.
Deconstruct their mechanism framework and offer architecture so we can
create differentiated angles."
```

### A/B Test Winner Analysis
```
"Compare outputs/variant_A.md (2.8% conversion) vs outputs/variant_B.md
(4.1% conversion). What made B win? Generate patches to improve our skills."
```

### Pre-Production Research (P0 Phase)
```
"Before I start drafting, analyze these 3 reference pages:
- research/ref_1.md
- research/ref_2.md
- research/ref_3.md

Extract universal patterns I should use in the Sleep Energy offer."
```

---

## 🎯 USE CASES

### 1️⃣ Learn from Your Best Work
**When:** You created pages that performed well
**Goal:** Extract what worked, codify into skills
**Output:** Patterns become templates for future pages

### 2️⃣ Competitive Intelligence
**When:** Competitor has high-converting page
**Goal:** Learn market-tested patterns (without copying)
**Output:** Alternative angles + mechanism insights

### 3️⃣ A/B Test Learning
**When:** One version outperformed another
**Goal:** Understand why, improve system
**Output:** Validated patterns + skill patches

### 4️⃣ Multi-Market Extraction
**When:** Successful pages across different niches
**Goal:** Build cross-market intelligence
**Output:** Universal + conditional patterns

### 5️⃣ Performance Diagnosis
**When:** Page underperformed
**Goal:** Identify gaps and fixes
**Output:** Specific improvements + rebuild strategy

---

## 📊 WHAT GETS ANALYZED (5 Dimensions)

### 1. STRUCTURE
- Section types (headline, lead, mechanism, proof, offer, CTA)
- Flow sequence (Hook → Problem → Mechanism → Proof → Offer → CTA)
- Transitions between sections
- Word counts, CTA positions

**Python Tool:** `extract_structure(page_content)`

### 2. MECHANISM
- Promise (primary outcome, emotional, tangible, timeframe)
- Mechanism name and explanation
- Unique element (what makes it different)
- Failed alternatives (why they don't work)
- Belief shifts (from → to)
- Proof pillars

**Manual Analysis:** Strategic interpretation required

### 3. OFFER ARCHITECTURE
- Core offer (name, price, perceived value)
- Value Equation (Dream Outcome, Likelihood, Time, Effort)
- Bonus stack
- Pricing psychology (anchoring, scarcity, guarantee)
- CTA structure

**Manual Analysis:** Strategic interpretation required

### 4. VOICE SIGNATURE
- Tone markers (formality, warmth, authority, urgency)
- Sentence rhythm (avg length, short/long/medium ratios)
- Word choice (second-person ratio, active voice, sensory words)
- Forbidden words check
- Power phrases

**Python Tool:** `analyze_voice(text)`

### 5. 7S/7F COVERAGE
- SAFE (Security) — Guarantees, credentials
- SPECIAL (Status) — Unique positioning
- SMART (Clarity) — Clear explanation
- SIGNIFICANT (Social Proof) — Testimonials
- SUPPORTED (Ease) — Simple CTA
- SUPERIOR (Belonging) — Community language
- STEAL (Value) — Bonus stack, pricing

**Manual Scoring:** Evidence-based assessment (1-10 scale)

---

## 🔧 PYTHON VALIDATION TOOLS

Located in: `.claude/skills/research/spdc_validation_tools.py`

### Available Functions

```python
# Structure extraction
extract_structure(page_content: str) -> Dict

# Voice analysis
analyze_voice(text: str) -> Dict

# Pattern matching
match_patterns(text: str, pattern_library: List[Dict]) -> List[Dict]

# 7S evidence extraction
extract_7s_evidence(text: str) -> Dict

# Comparative analysis
compare_structures(structure1: Dict, structure2: Dict) -> Dict
compare_voices(voice1: Dict, voice2: Dict) -> Dict
```

### Run Tools Directly
```bash
cd .claude/skills/research
python spdc_validation_tools.py
```

---

## 📦 OUTPUT FILES

### DECONSTRUCTION_REPORT
```yaml
deconstruction_report:
  metadata: {...}
  structure_blueprint: {...}
  mechanism_framework: {...}
  offer_architecture: {...}
  voice_signature: {...}
  seven_s_coverage: {...}
  pattern_library_additions: {...}
  patch_proposals: {...}
  executive_summary: {...}
```

**Location:** `outputs/deconstruction_reports/[page_name]_[date].yaml`

### PATTERN_LIBRARY_UPDATE
```yaml
pattern_library_update:
  new_patterns_discovered: [...]
  existing_patterns_confirmed: [...]
  anti_patterns_flagged: [...]
```

**Location:** `outputs/pattern_library/updates_[date].yaml`

### PATCH_PROPOSALS
```yaml
patch_proposals:
  - patch_id: "patch_027"
    priority: "HIGH"
    skill_target: "sales_page_copywriter_lite"
    implementation_estimate: "15 min"
    ...
```

**Location:** `outputs/patches/proposals_[date].yaml`

### insights.md Entry
```markdown
## Deconstruction: [Page Name] — [Date]

**Performance:** [Conversion rate]
**Overall Score:** [X.X/10]

### Top Patterns Discovered
- **[Pattern Name]** (p_XXX): [Description]

### Recommended Patches
- **[Skill]** (patch_XXX): [What to add]
```

**Location:** `insights.md` (session memory)

---

## 🔄 ECR INTEGRATION (Self-Healing Loop)

The Sales Page Deconstructor operates in the **End Cycle Recursion** framework:

### LEARNING Phase (Agentic LEARNING)
```
Input: High-performing page
  ↓
Extract 5-dimension analysis
  ↓
Identify new patterns (SIPs - Self-Identified Patterns)
  ↓
Confirm existing patterns (confidence++)
  ↓
Flag anti-patterns (what to avoid)
  ↓
Output: PATTERN_LIBRARY_UPDATE
```

### REPAIR Phase (Agentic REPAIR)
```
Input: Pattern library + current skills
  ↓
Identify gaps in skills
  ↓
Generate patch proposals (prioritized)
  ↓
Human reviews patches
  ↓
Approved patches → Skill updates
  ↓
Output: Updated skills (v[X+1])
```

### COMPOUND Effect
```
Each deconstruction → More patterns → Better skills → Better output → Repeat
```

---

## ⚡ PERFORMANCE TIPS

### Fast Analysis (5-10 min)
- Single page
- Focus on structure + 7S coverage
- Skip comparative analysis

### Deep Analysis (15-20 min)
- Multiple pages
- Full 5-dimension extraction
- Comparative analysis
- Patch proposal generation

### Batch Analysis (30-60 min)
- 5+ pages across markets
- Meta-pattern synthesis
- Universal pattern extraction
- Framework upgrades

---

## 🎓 PATTERN LIBRARY STRUCTURE

### Pattern Template
```yaml
pattern_id: "p_XXX"
name: "Descriptive Name"
category: "mechanism_intro|objection_handling|offer_reveal|proof_stacking"
description: "What this pattern does"
example: "Concrete example from page"
effectiveness: "High|Medium|Low for [context]"
when_to_use: "Specific scenarios"
mma_impact: "Which 7S dimensions this strengthens"
```

### Example Patterns

**p_087: Reversed Rhythm Hook**
- Category: mechanism_intro
- Example: "Your cortisol rhythm isn't broken—it's just backwards"
- When to use: Biological/hormonal mechanisms
- MMA impact: SMART +1.5, SAFE +0.5

**p_088: Failed Alternative Validation**
- Category: objection_handling
- Example: "Melatonin can't work when cortisol is blocking it"
- When to use: Sophisticated audiences who tried solutions
- MMA impact: SMART +1.0, SPECIAL +0.8

---

## 🚨 CIRCUIT BREAKERS

### Unstructured Content
**Detection:** Structure extraction returns empty/broken sections
**Recovery:** Request cleaned markdown, manually identify major sections

### Pattern Overload
**Detection:** >20 patterns flagged
**Recovery:** Filter to top 5 highest-confidence, focus HIGH priority only

### No Comparable Patterns
**Detection:** Page too unique, no existing matches
**Recovery:** Tag as new category, create foundational pattern

### Missing Performance Data
**Detection:** Comparative analysis without metrics
**Recovery:** Analyze structure/voice only, caveat validation needed

---

## 📈 SUCCESS METRICS

### Deconstruction Quality
- ✅ All 5 dimensions analyzed
- ✅ At least 1 pattern identified (new/confirmed/anti)
- ✅ Executive summary with top 3 strengths + gaps
- ✅ Evidence-based 7S scoring
- ✅ Actionable patch proposals

### Pattern Library Growth
- Target: +10 validated patterns/month
- Acceptance rate: ≥60% of proposed patches approved
- Improvement delta: +0.5 MMA score after patch application

### False Positive Rate
- Target: ≤10% incorrect pattern flagging
- Validation: Human review confirms pattern effectiveness

---

## 🎬 GOLDEN RUN EXAMPLE

### Input
```
Page: "Sleep Energy Breakthrough Sales Page v3.md"
Performance: 4.2% conversion (above 3% target)
Avatar: Hormonal women 40+
```

### Output Highlights
```yaml
overall_score: 8.1/10

top_strengths:
  - SMART dimension (9.5/10) - Mechanism clarity
  - Value stack (8.8/10) - 5.1x value ratio
  - Proof integration (8.5/10) - Testimonials + science

top_gaps:
  - SUPERIOR dimension (7.0/10) - Weak community language
  - Could add more sensory words
  - Mobile scannability could improve

patterns_discovered:
  - p_087: "Reversed Rhythm Hook" (NEW)
  - p_088: "Failed Alternative Validation" (NEW)
  - p_042: "Kitchen Table Language" (CONFIRMED)

patches_proposed:
  - patch_027: Add "Reversed System Framework" to sales_page_copywriter_lite
    Priority: HIGH, Est: 15 min, Impact: SMART +1.0
```

---

## 🔗 INTEGRATION WITH ZPWO

### P0 Phase (Pre-Draft Research)
```
P0: LEARN
├── Input: Reference pages, competitor analysis
├── Skill: sales_page_deconstructor_v2.0.0
├── Output: DECONSTRUCTION_REPORT + patterns
└── Next: Use learnings in P1 (Draft) for angle exploration
```

### P4 Phase (Post-Production Analysis)
```
P3: POLISH → Complete
  ↓
P4: ANALYZE
├── Deconstruct what was created
├── Compare to original brief
├── Extract what worked
├── Generate patches
└── Output: IMPROVEMENT_CYCLE_REPORT
```

---

## 📚 REFERENCES

- **Skill XML:** `.claude/skills/research/sales_page_deconstructor_v2.0.0.xml`
- **Python Tools:** `.claude/skills/research/spdc_validation_tools.py`
- **Spec Doc:** `specs/SALES_PAGE_DECONSTRUCTOR_ANALYST_SPEC.md`
- **Lean Skills Guide:** `specs/Lean Skills Development Guide MD.txt`

---

**Status:** ✅ Production Ready
**Version:** 2.0.0
**Last Updated:** 2026-01-15

*This skill closes the feedback loop: Generate → Analyze → Learn → Improve → Generate Better*

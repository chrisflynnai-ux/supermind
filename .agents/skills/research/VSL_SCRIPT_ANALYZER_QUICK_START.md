# VSL SCRIPT ANALYZER v1.0.0 — QUICK START GUIDE

> **Built from:** 5 high-performing high-ticket VSLs (Charlie Morgan, Sabri Suby, Daniel Fazio, Mason, Jon Benson)
> **Patterns:** 17+ proven VSL patterns (p_097-p_113)
> **Structure:** Universal VSL Flow (10-part framework)

---

## 🎯 WHAT THIS SKILL DOES

Deconstructs VSL scripts to extract:
- **Structure** — 10-part Universal Flow validation with timing analysis
- **Patterns** — Matches against 17+ proven patterns from top performers
- **Voice** — Classifies voice signature (Sabri-style irreverent, Charlie Morgan authority, etc.)
- **Timing** — Validates proof front-loading, pitch percentage, section pacing
- **Recommendations** — Specific, actionable improvements based on structural violations

---

## 🚀 3-STEP QUICK START

### **Step 1: Provide VSL Script**
```
Option A: Paste script text directly
Option B: Provide video URL (analyzer will extract transcript)
Option C: Upload .txt or .docx file
```

### **Step 2: Run Analysis**
```
/vsl-analyze [script or URL]
```

The analyzer will:
- Extract 10-part Universal Flow structure
- Match patterns (p_097-p_113+)
- Calculate timing percentages
- Classify voice signature
- Score against MMA 7S framework
- Generate improvement recommendations

### **Step 3: Review Report**
```
Output: VSL_ANALYSIS_REPORT_[date].md
```

Report includes:
- Executive summary (word count, duration, overall score)
- Structure breakdown with timing
- Pattern matches with examples
- Voice analysis
- MMA 7S scoring
- Critical fixes + high-priority improvements

---

## 📋 COMMON USE CASES

### **Use Case 1: Competitor Analysis**
**Goal:** Extract patterns from high-performing competitor VSLs

**Workflow:**
1. Find competitor VSL (transcribe if needed)
2. Run VSL Analyzer
3. Review pattern matches (what patterns do they use?)
4. Note timing (when do they pitch? proof placement?)
5. Extract patterns for your own VSL

**Output:** Pattern library additions, timing benchmarks

---

### **Use Case 2: Pre-Production Validation**
**Goal:** Validate VSL script BEFORE video production

**Workflow:**
1. Write VSL script draft
2. Run VSL Analyzer
3. Check for structural violations (proof after mechanism = CRITICAL)
4. Validate timing (pitch at 60-70%?)
5. Fix violations before filming

**Output:** Production-ready script with validated structure

---

### **Use Case 3: Performance Diagnosis**
**Goal:** Understand why existing VSL underperforms

**Workflow:**
1. Provide underperforming VSL script
2. Run VSL Analyzer
3. Review violations and missing patterns
4. Compare to high-performer benchmarks
5. Implement recommendations

**Output:** Specific fixes to improve conversion

---

### **Use Case 4: Pattern Library Expansion (ECR LEARNING)**
**Goal:** Extract new patterns from successful VSLs

**Workflow:**
1. Analyze multiple high-performing VSLs
2. Analyzer identifies patterns NOT in current library
3. Review pattern_extraction_log.yaml
4. Validate new patterns across multiple VSLs
5. Add to pattern library (p_114, p_115, etc.)

**Output:** Expanded pattern library, skill patches

---

## 🔍 UNDERSTANDING THE OUTPUT

### **Executive Summary**
```yaml
Overall Score: 8.7/10
Word Count: 5,234 (~26 min)
Offer Tier: High-ticket ($15k+)
Voice: Charlie Morgan - Authority Professional (confidence: 0.85)
Structure Adherence: 95%
Critical Issues: 0
```

### **Structure Breakdown**
```
HOOK              | 0:00-1:30 min | 12.5% | 654 words
QUALIFIER         | 1:30-2:30 min |  8.2% | 429 words  [High-ticket confirmation]
PROBLEM AGITATION | 2:30-4:30 min | 16.1% | 843 words
AUTHORITY STACK   | 4:30-6:00 min | 12.3% | 644 words
PROOF FRONT-LOAD  | 6:00-9:00 min | 24.6% | 1,288 words ✓ BEFORE mechanism
MECHANISM REVEAL  | 9:00-13:00 min | 26.9% | 1,408 words
...
```

### **Pattern Matches**
```yaml
p_098: Qualifier Fence (confidence: 0.92)
  Example: "This is for agencies already at $5k-$20k/month. If you're brand new..."
  Timing: 1:45 (8.5%) ✓ Optimal
  Impact: SIGNIFICANT +2.0, SPECIAL +1.5

p_102: Proof Front-Loading (confidence: 0.88)
  Example: "Let me share 5 client stories. John went from $5k to $50k in 90 days..."
  Timing: 6:30 (25%) ✓ BEFORE mechanism (9:00)
  Impact: SMART +2.0, SIGNIFICANT +1.0

[... 12 more patterns matched ...]
```

### **Missing Patterns**
```yaml
p_111: "Why Can't That Be You?" Identity Shift
  Recommendation: Add after social proof section (80-90% mark)
  Example: "John did it. Sarah did it. Why can't that be you?"
  Impact: SIGNIFICANT +2.0, SAFE +1.0
```

### **MMA 7S Scoring**
```yaml
SMART:       9.5/10 ✓ (Massive proof, authority stack, revenue screenshots)
SPECIAL:     9.0/10 ✓ (Qualifier fence, unique mechanism, premium positioning)
SAFE:        8.5/10 ✓ (Ethical guarantee, no manipulation, trust signals)
SIGNIFICANT: 8.2/10 ✓ (Problem agitation, identity shift)
SUPPORTED:   9.2/10 ✓ (Client stories throughout, not stacked)
SUPERIOR:    8.8/10 ✓ (Mechanism framing, belief shift declarations)
STEAL:       7.5/10 ⚠ (Moderate - application CTA less urgent than buy-now)

Overall: 8.7/10 ✓ PASS
```

### **Recommendations**

**CRITICAL FIXES (Must Address):**
```
None detected ✓
```

**HIGH PRIORITY IMPROVEMENTS:**
```
1. Add "Why Can't That Be You?" identity shift (p_111)
   - Placement: 80-90% mark (after social proof)
   - Impact: SIGNIFICANT +2.0, SAFE +1.0
   - Example: "John did it in 90 days. Sarah did it in 60. Why can't that be you?"

2. Enhance guarantee with Ethical Contrast (p_112)
   - Current: Simple promise
   - Upgrade: "I'm NOT guaranteeing you'll hit $100k overnight. I AM guaranteeing..."
   - Impact: SAFE +2.0, SMART +1.0, reduces FTC risk
```

**MEDIUM PRIORITY ENHANCEMENTS:**
```
1. Voice consistency: Excellent (authority professional maintained throughout)
2. Pattern density: 4.8 per 1000 words (target: 4-6) ✓
3. CTA frequency: 6 mentions (optimal: 5-7) ✓
```

---

## 🛠️ PYTHON TOOLS REFERENCE

### **vsl_timing_analyzer.py**

**calculate_timing_percentages(script_text)**
```python
from vsl_timing_analyzer import calculate_timing_percentages

timing = calculate_timing_percentages(script_text)
print(f"Duration: {timing.estimated_duration_minutes:.1f} min")
print(f"Pitch at: {timing.pitch_percentage:.1f}%")
print(f"Proof before mechanism: {timing.proof_before_mechanism}")
```

**validate_proof_timing(timing)**
```python
from vsl_timing_analyzer import validate_proof_timing

is_valid, message = validate_proof_timing(timing)
if not is_valid:
    print(f"VIOLATION: {message}")
```

**analyze_sentence_metrics(script_text)**
```python
from vsl_timing_analyzer import analyze_sentence_metrics

metrics = analyze_sentence_metrics(script_text)
print(f"Avg sentence length: {metrics['avg_sentence_length']:.1f} words")
# Sabri-style: 8-12 words
# Professional: 15-20 words
```

**classify_voice_signature()**
```python
from vsl_timing_analyzer import *

sentence_metrics = analyze_sentence_metrics(script_text)
second_person = calculate_second_person_ratio(script_text)
humor = detect_humor_markers(script_text)
voice, confidence = classify_voice_signature(sentence_metrics, second_person, humor)

print(f"Voice: {voice} (confidence: {confidence:.2f})")
```

---

## 📊 UNIVERSAL VSL FLOW (10-Part Structure)

```
1. HOOK (10-15% | 0:00-1:30)
   Pattern interrupt + curiosity gap + target audience callout

2. QUALIFIER (5-10% | 1:30-2:30) [HIGH-TICKET ONLY]
   "This is for X already at $Y. If you're brand new, this isn't for you."

3. EMPATHY/PROBLEM AGITATION (10-20% | 2:30-4:30)
   "Let me guess..." accumulation OR absurdist frustration painting

4. AUTHORITY STACK (10-15% | 4:30-6:00)
   Revenue + clients served + aggregate client results

5. PROOF FRONT-LOAD (15-25% | 6:00-9:00) ⚠️ CRITICAL
   Show results BEFORE mechanism reveal
   3-5 named client stories with specific numbers + timeframes

6. MECHANISM REVEAL (20-30% | 9:00-13:00)
   Named system/framework with 3-7 components
   Belief shift declaration

7. OFFER REVEAL (5-10% | 13:00-15:00)
   Application/call CTA (NOT "buy now")
   What happens on call + value even if rejected

8. GUARANTEE (2-5% | 15:00-16:00)
   "I'm NOT guaranteeing X... I AM guaranteeing Y"

9. SCARCITY (2-5% | 16:00-17:00)
   Honest capacity limits OR no scarcity (confidence play)

10. FINAL CTA (2-5% | 17:00-18:00)
    Repeat application instructions + negative contrast OR confident close
```

---

## 🎭 VOICE SIGNATURES

### **Sabri Suby - Irreverent Anti-Guru**
- Absurdist humor ("crazier than your ex")
- Self-aware fourth wall breaks
- Profanity (strategic)
- Short sentences (8-12 words avg)
- High second-person (3-5x "you" per paragraph)

**When to use:** Sophisticated, burnt-out entrepreneurs (30-50 male)
**When NOT:** Conservative industries, first-time visitors, 50+ demographics

---

### **Charlie Morgan - Authority Professional**
- Direct, no-nonsense
- Revenue-focused
- "I'm going to show you exactly..."
- Structured, logical
- Minimal humor, maximum credibility

**When to use:** B2B services, agency growth, business scaling

---

### **Mason - Transformation Empathy**
- Deep empathy for suffering
- Personal vulnerability
- Hope + possibility language
- "Imagine feeling..."
- Partnership framing ("together")

**When to use:** Health transformation, personal growth, coaching

---

### **Jon Benson - Origin Story Authority**
- Hero's journey structure
- Visceral crisis moment
- Transformation narrative
- Ongoing evolution
- Vulnerability → Credibility → Aspiration

**When to use:** Founder stories, About pages, personal brand authority

---

## ⚠️ CRITICAL RULES

### **1. Proof MUST appear BEFORE Mechanism**
```
✗ WRONG: Problem → Mechanism → Proof → Offer
✓ RIGHT: Problem → Proof → Mechanism → Offer
```

**Why:** Skeptical buyers need to believe results are possible BEFORE they care how

---

### **2. Pitch at 60-70% (NOT at end)**
```
Too early (<50%): Belief not built yet
Too late (>75%): Viewer already dropped off
Optimal: 60-70% (belief built, attention still high)
```

---

### **3. High-Ticket = Application CTA (NOT "Buy Now")**
```
✗ WRONG: "Click here to purchase for $15,000"
✓ RIGHT: "Fill out application to see if you qualify"
```

**Why:** High-ticket requires call qualification, builds exclusivity

---

### **4. Qualifier Fence for High-Ticket ($5k+)**
```
Required for: Offers $5k+
Optional for: Offers <$5k
Pattern: "This is for [X already at $Y]. If you're [beginner], this isn't for you."
```

**Impact:** Pre-qualifies audience, increases perceived value (SIGNIFICANT +2.0)

---

## 🔄 ECR INTEGRATION

### **LEARNING Phase**
VSL Analyzer extracts Self-Identified Patterns (SIPs) from successful VSLs

**Output:** `pattern_extraction_log.yaml`
```yaml
new_patterns:
  - id: p_114
    name: "Fear-Based Future Projection"
    source: "Competitor VSL analysis"
    occurrences: 3
    effectiveness: "High"
    recommendation: "Add to pattern library"
```

### **REPAIR Phase**
Generates patch proposals for skill improvements

**Output:** `patch_proposals.yaml`
```yaml
patches:
  - skill: vsl_script_analyzer_v1.0.0
    version_target: v1.1.0
    type: pattern_library_expansion
    additions:
      - pattern_id: p_114
        name: "Fear-Based Future Projection"
    benefit: "Increased pattern recognition accuracy"
```

---

## 📚 PATTERN LIBRARY REFERENCE

**Full pattern documentation:** See `insights.md` or `HIGH_TICKET_VSL_PATTERN_ANALYSIS_2026-01-15.md`

**Quick Reference:**
- **p_097:** VSL Absurdist Hook
- **p_098:** Qualifier Fence ⭐ (high-ticket essential)
- **p_099:** Three-Question Self-Identification
- **p_100:** Authority Stack
- **p_101:** Before/After Case Study Grid
- **p_102:** Proof Front-Loading ⭐ (critical rule)
- **p_103:** Student Revenue Screenshots
- **p_104:** Systemized Module Naming
- **p_105:** Application CTA ⭐ (high-ticket essential)
- **p_106:** Origin Story Arc
- **p_107:** Absurdist Bio Closer
- **p_108:** Sabri-Style Pattern Interrupt
- **p_109:** Reverse Objection Pre-Handle
- **p_110:** Negative Contrast CTA
- **p_111:** "Why Can't That Be You?" Identity Shift
- **p_112:** Ethical Guarantee Contrast ⭐ (reduces FTC risk)
- **p_113:** Named Framework Components

---

## 🎓 GOLDEN RUN EXAMPLE

**Input:** Charlie Morgan EasyGrow VSL (~5000 words, 25 min)

**Expected Output:**
```yaml
structure_adherence: 95%
patterns_matched: 12 (p_098, p_100, p_102, p_104, p_105, p_112, etc.)
voice: "Charlie Morgan - Authority Professional" (confidence: 0.92)
mma_overall: 9.0/10
critical_violations: 0
recommendations:
  - high_priority: "Add p_111 identity shift at 80% mark"
  - medium_priority: "Voice consistency excellent"
```

---

## 💡 PRO TIPS

1. **Run BEFORE video production** — Cheaper to fix script than re-film
2. **Analyze top 3 competitors** — Extract pattern suite for your niche
3. **Track pattern density** — High-performers: 4-6 patterns per 1000 words
4. **Voice consistency matters** — Sabri-style hook + formal body = mismatch
5. **Proof front-loading is NON-NEGOTIABLE** — #1 structural violation to fix

---

## 🔗 RELATED SKILLS

**Pairs well with:**
- High-Ticket VSL Script Writer v1.0.0 (generate new VSLs using extracted patterns)
- Sales Page Deconstructor v2.0.0 (for traditional sales pages vs VSLs)
- MMA Master Monitor Agent (for 7S scoring validation)

---

**Status:** ✅ Production-ready
**Version:** 1.0.0
**Last Updated:** 2026-01-15
**Built from:** 5 VSL analyses, 17+ patterns, Universal VSL Flow framework

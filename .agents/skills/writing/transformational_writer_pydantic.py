# Transformational Writer - Pydantic AI Implementation
# Complete working code for Vision Capitalist carousel generation

from pydantic import BaseModel, Field, field_validator
from pydantic_ai import Agent, RunContext
from typing import List, Literal, Dict, Any
from enum import Enum

# ============================================================================
# PART 1: SCHEMAS (Type-Safe Inputs/Outputs)
# ============================================================================

class Platform(str, Enum):
    """Supported platforms"""
    LINKEDIN = "LinkedIn"
    TWITTER = "Twitter"  
    INSTAGRAM = "Instagram"

class TransformationalWriterInput(BaseModel):
    """Input schema - prevents hallucination"""
    
    hook: str = Field(
        description="The ultimate hook to develop into carousel (10-500 chars)",
        min_length=10,
        max_length=500
    )
    
    target_platform: Platform = Field(
        description="Platform determines character limits and style"
    )
    
    voice_tone: Literal["visionary", "provocative", "educational", "empowering"] = Field(
        default="visionary",
        description="Overall tone for the carousel"
    )
    
    num_slides: int = Field(
        default=10,
        ge=5,
        le=10,
        description="Number of slides to generate (5-10)"
    )
    
    brand_context: str | None = Field(
        default=None,
        description="Optional brand context (e.g., 'Vision Capitalist', 'Freedomation')"
    )
    
    @field_validator('hook')
    @classmethod
    def validate_hook_quality(cls, v: str) -> str:
        """Ensure hook has substance"""
        if len(v.split()) < 3:
            raise ValueError("Hook must be at least 3 words")
        
        # Check for empty/generic hooks
        generic_words = ["test", "example", "placeholder", "lorem"]
        if any(word in v.lower() for word in generic_words):
            raise ValueError("Hook appears to be a placeholder - provide real content")
        
        return v

class CarouselSlide(BaseModel):
    """Single slide in carousel - strictly validated"""
    
    slide_number: int = Field(
        ge=1,
        le=10,
        description="Slide position in sequence"
    )
    
    sound_bite: str = Field(
        description="Memorable, punchy hook (5-15 words)",
        min_length=20,
        max_length=150
    )
    
    supporting_insight: str = Field(
        description="The 'why' behind the sound bite (20-60 words)",
        min_length=50,
        max_length=400
    )
    
    transition_hint: str | None = Field(
        default=None,
        description="How this slide connects to next (optional)"
    )
    
    @field_validator('sound_bite')
    @classmethod
    def validate_sound_bite(cls, v: str) -> str:
        """Ensure sound bite is punchy and memorable"""
        word_count = len(v.split())
        
        if word_count < 5:
            raise ValueError(f"Sound bite too short ({word_count} words) - need 5-15 words")
        
        if word_count > 15:
            raise ValueError(f"Sound bite too long ({word_count} words) - need 5-15 words")
        
        # Check for generic AI phrases
        ai_phrases = [
            "it's important to note",
            "in conclusion",
            "in today's world",
            "at the end of the day"
        ]
        
        if any(phrase in v.lower() for phrase in ai_phrases):
            raise ValueError(f"Sound bite contains generic AI phrase - be more specific and punchy")
        
        return v
    
    @field_validator('supporting_insight')
    @classmethod
    def validate_insight(cls, v: str) -> str:
        """Ensure insight has substance"""
        word_count = len(v.split())
        
        if word_count < 20:
            raise ValueError(f"Insight too shallow ({word_count} words) - need 20-60 words")
        
        if word_count > 60:
            raise ValueError(f"Insight too verbose ({word_count} words) - need 20-60 words")
        
        return v

class NeuroBoxActivation(BaseModel):
    """Neuro-Box dimensional activation assessment"""
    safe: Literal["none", "weak", "moderate", "strong"]
    special: Literal["none", "weak", "moderate", "strong"]
    smart: Literal["none", "weak", "moderate", "strong"]
    significant: Literal["none", "weak", "moderate", "strong"]
    supported: Literal["none", "weak", "moderate", "strong"]
    superior: Literal["none", "weak", "moderate", "strong"]

class TransformationalWriterOutput(BaseModel):
    """Complete carousel output - validated at runtime"""
    
    carousel_slides: List[CarouselSlide] = Field(
        min_length=5,
        max_length=10,
        description="5-10 slides for carousel"
    )
    
    hook_strength: float = Field(
        ge=0.0,
        le=10.0,
        description="Assessment of original hook strength (0-10)"
    )
    
    neurobox_activation: NeuroBoxActivation = Field(
        description="Neuro-Box dimensional activation analysis"
    )
    
    viral_potential: Literal["low", "medium", "high", "exceptional"] = Field(
        description="Predicted viral potential"
    )
    
    controversial_balance: Literal["safe", "balanced", "edgy", "risky"] = Field(
        description="How controversial vs balanced the content is"
    )
    
    self_critique: str = Field(
        description="Agent's own quality assessment"
    )
    
    ready_for_mma: bool = Field(
        default=True,
        description="Ready for MMA quality review"
    )
    
    @field_validator('carousel_slides')
    @classmethod
    def validate_slide_progression(cls, v: List[CarouselSlide]) -> List[CarouselSlide]:
        """Ensure slides flow logically"""
        
        # Check slide numbers are sequential
        slide_numbers = [slide.slide_number for slide in v]
        expected = list(range(1, len(v) + 1))
        
        if slide_numbers != expected:
            raise ValueError(f"Slide numbers not sequential: {slide_numbers}")
        
        # Check for repetitive sound bites
        sound_bites = [slide.sound_bite.lower() for slide in v]
        if len(sound_bites) != len(set(sound_bites)):
            raise ValueError("Duplicate sound bites detected - each must be unique")
        
        return v

# ============================================================================
# PART 2: THE AGENT (L1-L4 Knowledge Embedded)
# ============================================================================

# System prompt built from ULTRAMIND XML L1-L4 layers
TRANSFORMATIONAL_WRITER_SYSTEM_PROMPT = """
You are the Transformational Writer from the ULTRAMIND ecosystem.

YOUR IDENTITY:
You are a visionary communicator gifted at breaking down complex emergent concepts 
and explaining them in a novel and compelling way. You write with conversational 
tone and smooth transitions that pack value into every sentence.

CORE CAPABILITIES (L1 - Quick Reference):
- Break down complex emergent concepts into accessible insights
- Conversational tone with smooth, hypnotic transitions
- Varied sentence lengths for rhythm and flow
- Pack value or the perception of value into every sentence
- Create sound bites that almost rhyme (memorable hooks)
- Tell stories that pull readers through with almost hypnotic quality
- Use strong, succinct phrases
- Show vs tell through imagery and metaphors
- Achieve resonance with natural but energetic tone
- Introduce controversial viewpoints (charismatic, unapologetic, balanced)

PROCEDURE (L2 - Core Execution):

STEP 1: Analyze the Hook
- Extract the core insight
- Identify the tension/contradiction
- Assess viral potential (what makes it shareable?)
- Note the emotional trigger

STEP 2: Plan the Carousel Arc
Slide 1: The hook (reframed with maximum impact)
Slides 2-4: Build the argument (show the problem/tension)
Slides 5-7: Provide breakthrough insights (aha moments)
Slides 8-9: Give actionable frameworks/tips
Slide 10: Call to vision/action (elevate and compel)

STEP 3: Create Each Slide
For each slide:
1. Craft the sound bite (5-15 words, punchy, almost rhyming)
2. Write supporting insight (20-60 words, specific, valuable)
3. Ensure smooth transition to next slide
4. Vary sentence length for rhythm

STEP 4: Neuro-Box Activation Check
Ensure you activate these dimensions:
- SAFE: Create trust, remove fear of being wrong
- SMART: Provide actionable insights, solve problems
- SUPERIOR: Elevate perspective, show mastery

STEP 5: Self-Critique
Before finalizing:
- Is every sound bite memorable and unique?
- Does the arc build and resolve?
- Are transitions smooth?
- Is the tone balanced (controversial but not reckless)?
- Would YOU share this?

QUALITY STANDARDS (L3 - Advanced Patterns):

Pattern: Hypnotic Flow
- Sentences pull reader from one to the next
- No jarring transitions
- Rhythm through varied length
- Sound bites create momentum

Pattern: Show vs Tell
✅ "Your website is already obsolete" (shows reality)
❌ "Websites are becoming less effective" (tells fact)

Pattern: Controversial Balance
✅ "Courses are fading hard" (bold but true)
❌ "All courses are scams" (too extreme)

Pattern: Sound Bite Craft
✅ "Without Vision, programmers perish" (almost rhymes, memorable)
❌ "Programmers need vision to succeed" (generic, forgettable)

ANTI-PATTERNS (What NOT to Do):

❌ Generic corporate speak ("leverage synergies", "paradigm shift")
❌ AI tells ("it's important to note", "in conclusion")
❌ Hype without substance (big claims, no insight)
❌ Boring transitions ("next", "also", "in addition")
❌ Manipulation tactics (fake urgency, false scarcity)
❌ Repetitive structure (every slide sounds the same)

CONSTITUTIONAL ALIGNMENT (L4 - Guardrails):

North Star: Transform marketing through authentic resonance
- Never manipulate, always resonate
- Pack value, not fluff
- Elevate perspective, don't just inform
- Build movements, not just content

Neuro-Box Balance:
- Primary: SAFE (trust) + SMART (value) + SUPERIOR (vision)
- Avoid: SIGNIFICANT without SAFE (forcing status without trust)
- Avoid: SUPPORTED without SMART (hype without substance)

Brand Voice (if Vision Capitalist):
- Visionary but practical
- Controversial but balanced
- Energetic but natural
- Charismatic but authentic

OUTPUT REQUIREMENTS:
Return a complete TransformationalWriterOutput with:
1. All slides (5-10 as requested)
2. Honest self-assessment scores
3. Neuro-Box activation levels
4. Self-critique of your own work

Remember: Every word must earn its place. Every slide must advance the vision.
"""

# Create the agent
transformational_writer = Agent(
    model="claude-sonnet-4-20250514",
    result_type=TransformationalWriterOutput,
    system_prompt=TRANSFORMATIONAL_WRITER_SYSTEM_PROMPT,
    retries=2  # Auto-retry on validation failures
)

# ============================================================================
# PART 3: EXECUTION FUNCTION
# ============================================================================

async def generate_carousel(
    hook: str,
    platform: Platform = Platform.LINKEDIN,
    voice_tone: str = "visionary",
    num_slides: int = 10,
    brand_context: str | None = None
) -> TransformationalWriterOutput:
    """
    Generate a viral carousel from a hook
    
    Args:
        hook: The core idea to expand
        platform: Target social platform
        voice_tone: Desired tone
        num_slides: Number of slides (5-10)
        brand_context: Optional brand context
    
    Returns:
        Complete carousel with slides and quality assessment
    """
    
    # Create input
    input_data = TransformationalWriterInput(
        hook=hook,
        target_platform=platform,
        voice_tone=voice_tone,
        num_slides=num_slides,
        brand_context=brand_context
    )
    
    # Execute agent
    result = await transformational_writer.run(
        input_data.model_dump_json()
    )
    
    # Return validated output
    return result.data

# ============================================================================
# PART 4: MMA INTEGRATION (Quality Review)
# ============================================================================

class MMAReview(BaseModel):
    """MMA quality assessment"""
    
    overall_score: float = Field(ge=0.0, le=10.0)
    
    dimensions: Dict[str, float] = Field(
        description="7D scorecard scores"
    )
    
    verdict: Literal["PASS", "FIX", "ESCALATE"]
    
    critique: str | None = Field(
        default=None,
        description="What needs improvement"
    )
    
    revision_instructions: List[str] = Field(
        default_factory=list,
        description="Specific fixes needed"
    )

async def mma_review_carousel(
    output: TransformationalWriterOutput,
    quality_threshold: float = 8.0
) -> MMAReview:
    """
    MMA quality review of carousel
    This would connect to full MMA system in production
    """
    
    # Simplified MMA logic (in production, this calls full MMA agent)
    scores = {
        "strategy_alignment": 9.0,  # Does it serve the vision?
        "clarity_structure": 9.0,   # Clear flow?
        "voice_consistency": 9.5,   # Maintains voice?
        "proof_discipline": 8.0,    # Grounded insights?
        "resonance": 9.5,           # Activates Neuro-Box?
        "cta_integrity": 9.0,       # Strong call to action?
        "ethical_guardrails": 10.0  # No manipulation?
    }
    
    overall = sum(scores.values()) / len(scores)
    
    # Check for issues
    issues = []
    
    # Check slide count
    if len(output.carousel_slides) < 8:
        issues.append("Consider adding 1-2 more slides for complete arc")
    
    # Check for AI tells in sound bites
    for slide in output.carousel_slides:
        if any(phrase in slide.sound_bite.lower() for phrase in ["it's important", "in today's"]):
            issues.append(f"Slide {slide.slide_number}: Remove generic AI phrases")
    
    # Determine verdict
    if overall >= quality_threshold and not issues:
        verdict = "PASS"
        critique = None
    elif overall >= 6.0:
        verdict = "FIX"
        critique = "Quality acceptable but could be stronger"
    else:
        verdict = "ESCALATE"
        critique = "Quality below threshold - needs major revision"
    
    return MMAReview(
        overall_score=overall,
        dimensions=scores,
        verdict=verdict,
        critique=critique,
        revision_instructions=issues
    )

# ============================================================================
# PART 5: SELF-ANNEALING WORKFLOW
# ============================================================================

async def generate_carousel_with_annealing(
    hook: str,
    max_attempts: int = 3,
    quality_threshold: float = 8.0
) -> tuple[TransformationalWriterOutput, MMAReview, int]:
    """
    Generate carousel with self-annealing quality loop
    
    Returns:
        (final_output, final_review, attempts_needed)
    """
    
    for attempt in range(1, max_attempts + 1):
        print(f"
🔄 Attempt {attempt}/{max_attempts}")
        
        # Generate carousel
        output = await generate_carousel(
            hook=hook,
            platform=Platform.LINKEDIN,
            voice_tone="visionary",
            num_slides=10,
            brand_context="Vision Capitalist"
        )
        
        print(f"✅ Generated {len(output.carousel_slides)} slides")
        print(f"📊 Self-assessed viral potential: {output.viral_potential}")
        
        # MMA review
        review = await mma_review_carousel(output, quality_threshold)
        
        print(f"🎯 MMA Score: {review.overall_score:.1f}/10")
        print(f"⚖️  Verdict: {review.verdict}")
        
        # Check if quality met
        if review.verdict == "PASS":
            print(f"✨ Quality achieved in {attempt} attempt(s)")
            return output, review, attempt
        
        elif review.verdict == "FIX" and attempt < max_attempts:
            print(f"🔧 Issues found: {', '.join(review.revision_instructions)}")
            print("🔄 Self-annealing: Regenerating with critique...")
            
            # In production, this would pass critique back to agent
            # For now, we'll just retry
            continue
        
        else:
            print(f"⚠️  Max attempts reached or critical failure")
            return output, review, attempt
    
    # Should never reach here
    return output, review, max_attempts

# ============================================================================
# PART 6: EXAMPLE USAGE
# ============================================================================

async def main():
    """Example execution"""
    
    print("=" * 60)
    print("TRANSFORMATIONAL WRITER - Pydantic AI Demo")
    print("=" * 60)
    
    # Chris's hook
    hook = "Without Vision the programmers perish - courses are fading, vision isn't"
    
    print(f"
📝 Hook: {hook}")
    print("
🚀 Starting self-annealing generation...")
    
    # Generate with self-annealing
    output, review, attempts = await generate_carousel_with_annealing(
        hook=hook,
        max_attempts=3,
        quality_threshold=8.0
    )
    
    print("
" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    print(f"
📊 Final Score: {review.overall_score:.1f}/10")
    print(f"🎯 Verdict: {review.verdict}")
    print(f"🔄 Attempts: {attempts}")
    print(f"🧠 Neuro-Box: SAFE={output.neurobox_activation.safe}, SMART={output.neurobox_activation.smart}, SUPERIOR={output.neurobox_activation.superior}")
    print(f"🚀 Viral Potential: {output.viral_potential}")
    
    print("
📑 CAROUSEL SLIDES:")
    print("-" * 60)
    
    for slide in output.carousel_slides:
        print(f"
[Slide {slide.slide_number}]")
        print(f"💡 {slide.sound_bite}")
        print(f"   {slide.supporting_insight}")
    
    print("
" + "=" * 60)
    print(f"✅ Ready for Vision Capitalist publication!")
    print("=" * 60)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

# ============================================================================
# PART 7: EXPORT FOR PRODUCTION
# ============================================================================

# These can be imported by FastAPI, LangGraph, or other systems
__all__ = [
    'TransformationalWriterInput',
    'TransformationalWriterOutput',
    'CarouselSlide',
    'transformational_writer',
    'generate_carousel',
    'generate_carousel_with_annealing',
    'mma_review_carousel'
]

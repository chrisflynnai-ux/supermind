"""
VSL TIMING ANALYZER v1.0.0
Python validation tools for VSL Script Analyzer

PURPOSE:
Deterministic timing calculations, structure validation, and pattern matching
for Video Sales Letter analysis. Provides objective metrics to complement
strategic VSL pattern interpretation.

FUNCTIONS:
- calculate_timing_percentages(): Estimate VSL timing based on word count
- validate_proof_timing(): Check if proof appears BEFORE mechanism (critical rule)
- calculate_pitch_percentage(): Determine where offer first mentioned
- extract_section_boundaries(): Identify 10-part Universal Flow sections
- calculate_pattern_density(): Patterns per 1000 words metric
- analyze_sentence_metrics(): Voice signature quantitative analysis

USAGE:
from vsl_timing_analyzer import *

script_text = "Your VSL script here..."
timing = calculate_timing_percentages(script_text)
proof_valid = validate_proof_timing(timing)
pitch_pct = calculate_pitch_percentage(timing)
"""

import re
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


# CONSTANTS
WORDS_PER_MINUTE = 200  # Average speaking rate for VSLs
TARGET_PITCH_PERCENTAGE_MIN = 60
TARGET_PITCH_PERCENTAGE_MAX = 70


@dataclass
class VSLSection:
    """Represents a section of the VSL"""
    name: str
    start_word: int
    end_word: int
    start_time: float  # minutes
    end_time: float    # minutes
    percentage: float  # of total VSL
    word_count: int


@dataclass
class TimingAnalysis:
    """Complete timing breakdown of VSL"""
    total_words: int
    estimated_duration_minutes: float
    sections: List[VSLSection]
    proof_before_mechanism: bool
    pitch_percentage: float
    violations: List[str]


def count_words(text: str) -> int:
    """
    Count words in script text

    Args:
        text: VSL script content

    Returns:
        Word count
    """
    # Remove extra whitespace and count
    words = re.findall(r'\b\w+\b', text)
    return len(words)


def calculate_estimated_duration(word_count: int) -> float:
    """
    Calculate estimated VSL duration in minutes

    Args:
        word_count: Total words in script

    Returns:
        Duration in minutes (float)
    """
    return word_count / WORDS_PER_MINUTE


def words_to_time(word_position: int, total_words: int, total_duration: float) -> float:
    """
    Convert word position to estimated time

    Args:
        word_position: Position in script (word count from start)
        total_words: Total words in script
        total_duration: Total duration in minutes

    Returns:
        Time in minutes (float)
    """
    return (word_position / total_words) * total_duration


def extract_section_boundaries(text: str, section_markers: Dict[str, List[str]]) -> Dict[str, Tuple[int, int]]:
    """
    Extract approximate section boundaries using keyword markers

    Args:
        text: VSL script content
        section_markers: Dict mapping section names to keyword lists

    Returns:
        Dict mapping section names to (start_word, end_word) tuples
    """
    words = text.split()
    boundaries = {}

    for section_name, keywords in section_markers.items():
        # Find first occurrence of any keyword for this section
        for i, word in enumerate(words):
            if any(keyword.lower() in word.lower() for keyword in keywords):
                boundaries[section_name] = i
                break

    return boundaries


def calculate_timing_percentages(
    script_text: str,
    custom_markers: Optional[Dict[str, List[str]]] = None
) -> TimingAnalysis:
    """
    Calculate timing percentages for VSL sections

    Args:
        script_text: Full VSL transcript
        custom_markers: Optional custom section markers (uses defaults if None)

    Returns:
        TimingAnalysis object with complete breakdown
    """
    # Default section markers based on Universal VSL Flow
    default_markers = {
        "hook": ["hey", "what if", "imagine", "let me ask", "are you"],
        "qualifier": ["this is for", "if you're brand new", "already at", "established"],
        "problem": ["tired of", "frustrated", "struggling", "let me guess"],
        "authority": ["before i show", "who am i", "i've helped", "worked with"],
        "proof": ["client", "case study", "went from", "revenue", "results"],
        "mechanism": ["system", "framework", "formula", "method", "process"],
        "offer": ["here's what", "application", "call", "book", "schedule"],
        "guarantee": ["guarantee", "promise", "risk", "refund"],
        "scarcity": ["limited", "spots", "only", "deadline"],
        "cta": ["click", "apply", "book", "schedule", "get started"]
    }

    markers = custom_markers or default_markers

    # Calculate basic metrics
    total_words = count_words(script_text)
    duration = calculate_estimated_duration(total_words)

    # Extract section boundaries
    boundaries = extract_section_boundaries(script_text, markers)

    # Build sections list
    sections = []
    violations = []

    # For each section, calculate timing
    section_order = ["hook", "qualifier", "problem", "authority", "proof", "mechanism",
                     "offer", "guarantee", "scarcity", "cta"]

    for i, section_name in enumerate(section_order):
        if section_name not in boundaries:
            continue

        start_word = boundaries[section_name]
        # End word is start of next section (or end of script)
        end_word = boundaries.get(section_order[i+1], total_words) if i < len(section_order)-1 else total_words

        start_time = words_to_time(start_word, total_words, duration)
        end_time = words_to_time(end_word, total_words, duration)
        percentage = (end_word - start_word) / total_words * 100

        section = VSLSection(
            name=section_name,
            start_word=start_word,
            end_word=end_word,
            start_time=start_time,
            end_time=end_time,
            percentage=percentage,
            word_count=end_word - start_word
        )
        sections.append(section)

    # Validate proof before mechanism
    proof_section = next((s for s in sections if s.name == "proof"), None)
    mechanism_section = next((s for s in sections if s.name == "mechanism"), None)

    proof_before_mechanism = True
    if proof_section and mechanism_section:
        if proof_section.start_word > mechanism_section.start_word:
            proof_before_mechanism = False
            violations.append(
                f"CRITICAL: Proof appears AFTER mechanism (proof at {proof_section.start_time:.1f}min, "
                f"mechanism at {mechanism_section.start_time:.1f}min). Should be BEFORE."
            )

    # Calculate pitch percentage
    offer_section = next((s for s in sections if s.name == "offer"), None)
    pitch_percentage = 0.0
    if offer_section:
        pitch_percentage = (offer_section.start_word / total_words) * 100

        if pitch_percentage < TARGET_PITCH_PERCENTAGE_MIN:
            violations.append(
                f"Pitch too early: {pitch_percentage:.1f}% (target {TARGET_PITCH_PERCENTAGE_MIN}-{TARGET_PITCH_PERCENTAGE_MAX}%)"
            )
        elif pitch_percentage > TARGET_PITCH_PERCENTAGE_MAX:
            violations.append(
                f"Pitch too late: {pitch_percentage:.1f}% (target {TARGET_PITCH_PERCENTAGE_MIN}-{TARGET_PITCH_PERCENTAGE_MAX}%)"
            )

    return TimingAnalysis(
        total_words=total_words,
        estimated_duration_minutes=duration,
        sections=sections,
        proof_before_mechanism=proof_before_mechanism,
        pitch_percentage=pitch_percentage,
        violations=violations
    )


def validate_proof_timing(timing: TimingAnalysis) -> Tuple[bool, str]:
    """
    Validate that proof appears BEFORE mechanism (critical rule)

    Args:
        timing: TimingAnalysis object from calculate_timing_percentages()

    Returns:
        Tuple of (is_valid: bool, message: str)
    """
    if timing.proof_before_mechanism:
        return True, "✓ Proof correctly appears BEFORE mechanism"
    else:
        proof_section = next((s for s in timing.sections if s.name == "proof"), None)
        mechanism_section = next((s for s in timing.sections if s.name == "mechanism"), None)

        return False, (
            f"✗ CRITICAL VIOLATION: Proof appears AFTER mechanism\n"
            f"  Proof at: {proof_section.start_time:.1f} min ({proof_section.percentage:.1f}%)\n"
            f"  Mechanism at: {mechanism_section.start_time:.1f} min ({mechanism_section.percentage:.1f}%)\n"
            f"  FIX: Move client stories to 6-9 min mark (BEFORE mechanism)"
        )


def calculate_pitch_percentage(timing: TimingAnalysis) -> Tuple[float, str]:
    """
    Calculate where pitch occurs and validate against target

    Args:
        timing: TimingAnalysis object

    Returns:
        Tuple of (percentage: float, assessment: str)
    """
    pitch_pct = timing.pitch_percentage

    if TARGET_PITCH_PERCENTAGE_MIN <= pitch_pct <= TARGET_PITCH_PERCENTAGE_MAX:
        return pitch_pct, f"✓ Pitch at {pitch_pct:.1f}% (optimal: {TARGET_PITCH_PERCENTAGE_MIN}-{TARGET_PITCH_PERCENTAGE_MAX}%)"
    elif pitch_pct < TARGET_PITCH_PERCENTAGE_MIN:
        return pitch_pct, f"⚠ Pitch too early at {pitch_pct:.1f}% (belief not yet built, target {TARGET_PITCH_PERCENTAGE_MIN}%+)"
    else:
        return pitch_pct, f"⚠ Pitch too late at {pitch_pct:.1f}% (viewer already dropped off, target <{TARGET_PITCH_PERCENTAGE_MAX}%)"


def calculate_pattern_density(pattern_matches: List[Dict], word_count: int) -> float:
    """
    Calculate patterns per 1000 words

    Args:
        pattern_matches: List of matched patterns
        word_count: Total words in script

    Returns:
        Pattern density (patterns per 1000 words)
    """
    if word_count == 0:
        return 0.0

    return (len(pattern_matches) / word_count) * 1000


def analyze_sentence_metrics(text: str) -> Dict[str, float]:
    """
    Analyze sentence-level metrics for voice signature analysis

    Args:
        text: VSL script content

    Returns:
        Dict with sentence metrics
    """
    # Split into sentences (simple approach - look for .!?)
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return {
            "avg_sentence_length": 0,
            "sentence_length_variance": 0,
            "total_sentences": 0
        }

    # Calculate sentence lengths
    sentence_lengths = [len(s.split()) for s in sentences]
    avg_length = sum(sentence_lengths) / len(sentence_lengths)

    # Calculate variance
    variance = sum((l - avg_length) ** 2 for l in sentence_lengths) / len(sentence_lengths)

    return {
        "avg_sentence_length": avg_length,
        "sentence_length_variance": variance,
        "total_sentences": len(sentences),
        "min_sentence_length": min(sentence_lengths),
        "max_sentence_length": max(sentence_lengths)
    }


def calculate_second_person_ratio(text: str) -> float:
    """
    Calculate second-person pronoun usage ratio

    Args:
        text: VSL script content

    Returns:
        Ratio of "you" occurrences per sentence
    """
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return 0.0

    # Count "you" (case-insensitive)
    you_count = len(re.findall(r'\byou\b', text, re.IGNORECASE))

    return you_count / len(sentences)


def detect_humor_markers(text: str) -> Dict[str, any]:
    """
    Detect humor markers for voice signature classification

    Args:
        text: VSL script content

    Returns:
        Dict with humor metrics
    """
    # Sabri-style absurdist humor markers
    absurdist_phrases = [
        "crazier than", "throw.*out.*window", "habanero", "eyeballs",
        "lost count", "tamed.*sharks", "grey pit of pity", "weird flavored"
    ]

    # Self-aware markers
    self_aware = [
        "yep, this", "pay attention to", "ask yourself", "obviously great from",
        "fourth wall", "this funnel"
    ]

    # Sarcasm markers
    sarcasm = [
        "common f\\*cking sense", "use some", "stupid idea", "behind the barn"
    ]

    # Count occurrences
    absurdist_count = sum(len(re.findall(phrase, text, re.IGNORECASE)) for phrase in absurdist_phrases)
    self_aware_count = sum(len(re.findall(phrase, text, re.IGNORECASE)) for phrase in self_aware)
    sarcasm_count = sum(len(re.findall(phrase, text, re.IGNORECASE)) for phrase in sarcasm)

    total_humor = absurdist_count + self_aware_count + sarcasm_count

    # Humor index (normalized by word count)
    word_count = count_words(text)
    humor_index = (total_humor / word_count) * 1000 if word_count > 0 else 0

    return {
        "absurdist_count": absurdist_count,
        "self_aware_count": self_aware_count,
        "sarcasm_count": sarcasm_count,
        "total_humor_markers": total_humor,
        "humor_index": humor_index  # per 1000 words
    }


def classify_voice_signature(
    sentence_metrics: Dict,
    second_person_ratio: float,
    humor_metrics: Dict
) -> Tuple[str, float]:
    """
    Classify voice signature based on metrics

    Args:
        sentence_metrics: From analyze_sentence_metrics()
        second_person_ratio: From calculate_second_person_ratio()
        humor_metrics: From detect_humor_markers()

    Returns:
        Tuple of (signature_name: str, confidence: float)
    """
    avg_sentence_length = sentence_metrics["avg_sentence_length"]
    humor_index = humor_metrics["humor_index"]

    # Decision tree classification

    # Sabri-style: Short sentences + high humor + high second-person
    if (avg_sentence_length < 14 and
        humor_index > 3 and
        second_person_ratio > 2.5):
        return "Sabri Suby - Irreverent Anti-Guru", 0.9

    # Charlie Morgan: Medium sentences + low humor + professional
    if (15 <= avg_sentence_length <= 18 and
        humor_index < 1 and
        second_person_ratio > 1.5):
        return "Charlie Morgan - Authority Professional", 0.85

    # Mason: Longer sentences + moderate second-person + empathy
    if (avg_sentence_length > 16 and
        humor_index < 2 and
        second_person_ratio > 2.0):
        return "Mason - Transformation Empathy", 0.75

    # Jon Benson: Story-driven, varied sentence length
    if sentence_metrics["sentence_length_variance"] > 40:
        return "Jon Benson - Origin Story Authority", 0.7

    # Default: Unknown (confidence low)
    return "Unknown/Mixed Voice", 0.5


def generate_timing_report(timing: TimingAnalysis) -> str:
    """
    Generate human-readable timing report

    Args:
        timing: TimingAnalysis object

    Returns:
        Formatted string report
    """
    report = []
    report.append(f"=== VSL TIMING ANALYSIS ===")
    report.append(f"Total Words: {timing.total_words:,}")
    report.append(f"Estimated Duration: {timing.estimated_duration_minutes:.1f} minutes")
    report.append(f"Pitch Percentage: {timing.pitch_percentage:.1f}%")
    report.append(f"Proof Before Mechanism: {'✓ YES' if timing.proof_before_mechanism else '✗ NO (VIOLATION)'}")
    report.append("")

    report.append("SECTION BREAKDOWN:")
    for section in timing.sections:
        report.append(
            f"  {section.name.upper():15} | "
            f"{section.start_time:5.1f}-{section.end_time:5.1f} min | "
            f"{section.percentage:5.1f}% | "
            f"{section.word_count:,} words"
        )

    if timing.violations:
        report.append("")
        report.append("⚠ VIOLATIONS DETECTED:")
        for violation in timing.violations:
            report.append(f"  • {violation}")

    return "\n".join(report)


# Example usage
if __name__ == "__main__":
    # Example VSL script snippet
    sample_script = """
    Hey, are you tired of struggling to get clients online? Let me guess - you've tried
    Facebook ads, you've tried cold email, you've tried LinkedIn outreach. Nothing seems
    to work consistently.

    Before I show you exactly how to fix this, let me tell you who I am. I've helped over
    500 businesses generate $100M+ in revenue through our systems.

    Let me share a quick case study. John came to us making $5k/month. Within 90 days,
    he was at $50k/month using our exact framework.

    So here's the system we use. It's called the Acquisition OS. There are 4 main components:
    System #1 is Acquisition Genesis, System #2 is Demand Machine...

    So here's what this means for you. If you want to scale your agency, book a call below
    and we'll see if you qualify for our program.

    I'm not guaranteeing you'll hit six figures overnight. I AM guaranteeing you'll get
    the exact framework that's worked for 500+ businesses.

    So click the link now and book your strategy call. Or don't, and stay stuck at $5k/month
    watching your competitors scale past you.
    """

    # Run analysis
    timing = calculate_timing_percentages(sample_script)
    print(generate_timing_report(timing))

    print("\n" + "="*60 + "\n")

    # Voice analysis
    sentence_metrics = analyze_sentence_metrics(sample_script)
    second_person = calculate_second_person_ratio(sample_script)
    humor = detect_humor_markers(sample_script)
    voice, confidence = classify_voice_signature(sentence_metrics, second_person, humor)

    print("VOICE SIGNATURE ANALYSIS:")
    print(f"  Avg Sentence Length: {sentence_metrics['avg_sentence_length']:.1f} words")
    print(f"  Second-Person Ratio: {second_person:.2f} per sentence")
    print(f"  Humor Index: {humor['humor_index']:.2f} per 1000 words")
    print(f"  Classification: {voice} (confidence: {confidence:.2f})")

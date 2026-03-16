"""
SALES PAGE DECONSTRUCTOR - PYTHON VALIDATION TOOLS
Version: 2.0.0
Purpose: Deterministic pattern extraction and analysis tools

These tools provide quantitative analysis to complement strategic interpretation.
Used by sales_page_deconstructor_v2.0.0.xml for structure and voice analysis.
"""

import re
from typing import Dict, List, Tuple
from collections import Counter


# ==============================================================================
# STRUCTURE EXTRACTION
# ==============================================================================

def extract_structure(page_content: str) -> Dict:
    """
    Parse page content to extract structure blueprint.

    Args:
        page_content: Markdown or plain text content of sales page

    Returns:
        Dictionary with sections, flow_sequence, transitions, and metrics
    """
    sections = []

    # Identify headings (markdown ## or HTML h2-h6)
    heading_pattern = r'^#{2,6}\s+(.+)$'
    headings = re.findall(heading_pattern, page_content, re.MULTILINE)

    # Split content by headings
    content_blocks = re.split(heading_pattern, page_content, flags=re.MULTILINE)

    for i, heading in enumerate(headings):
        # Get content block for this section
        content_index = i * 2 + 2
        content = content_blocks[content_index] if content_index < len(content_blocks) else ""

        word_count = len(content.split())

        section = {
            "section_id": f"sec_{i+1:03d}",
            "type": classify_section_type(heading, content),
            "heading": heading,
            "content_sample": content.strip()[:80] + "..." if len(content.strip()) > 80 else content.strip(),
            "function": infer_section_function(heading, content),
            "length_words": word_count,
            "position_percent": round((i / len(headings)) * 100, 1) if headings else 0
        }
        sections.append(section)

    # Calculate metrics
    total_words = sum(s["length_words"] for s in sections)
    avg_section_length = total_words / len(sections) if sections else 0

    # Count CTAs
    cta_pattern = r'\b(get|start|join|buy|claim|download|access|enroll)\s+(now|today|instant|free|your|started)\b'
    cta_matches = re.findall(cta_pattern, page_content, re.IGNORECASE)
    cta_count = len(cta_matches)

    # Find CTA positions
    cta_positions = []
    for i, section in enumerate(sections):
        if 'cta' in section['type'].lower() or re.search(cta_pattern, section['content_sample'], re.IGNORECASE):
            position = f"After section {i+1}: {section['heading']}"
            cta_positions.append(position)

    # Infer flow sequence
    flow_sequence = infer_flow_sequence([s['type'] for s in sections])

    return {
        "sections": sections,
        "flow_sequence": flow_sequence,
        "metrics": {
            "total_word_count": total_words,
            "avg_section_length": round(avg_section_length, 1),
            "section_count": len(sections),
            "cta_count": cta_count,
            "cta_positions": cta_positions
        }
    }


def classify_section_type(heading: str, content: str) -> str:
    """Classify section type based on heading and content."""
    heading_lower = heading.lower()
    content_lower = content.lower()

    # Mechanism indicators
    if any(word in heading_lower for word in ["how it works", "the mechanism", "the method", "the system", "the secret"]):
        return "mechanism_intro"

    # Proof indicators
    if any(word in heading_lower for word in ["proof", "results", "testimonial", "success", "case study"]):
        return "proof"

    # Offer indicators
    if any(word in heading_lower for word in ["offer", "package", "price", "bonus", "get access", "what you get"]):
        return "offer"

    # Problem/agitation indicators
    if any(word in heading_lower for word in ["problem", "struggle", "why you", "frustrated", "failed"]):
        return "problem_agitation"

    # CTA indicators
    if re.search(r'\b(get|claim|start|join|enroll)\b', content_lower[:100]):
        return "cta"

    # Lead indicators (first section after headline)
    if any(word in heading_lower for word in ["imagine", "what if", "are you", "do you"]):
        return "lead"

    return "content"


def infer_section_function(heading: str, content: str) -> str:
    """Infer the functional purpose of a section."""
    section_type = classify_section_type(heading, content)

    function_map = {
        "mechanism_intro": "Solution framework reveal",
        "proof": "Build credibility and trust",
        "offer": "Present value and CTA",
        "problem_agitation": "Problem awareness and agitation",
        "cta": "Drive conversion action",
        "lead": "Hook and engagement",
        "content": "Supporting information"
    }

    return function_map.get(section_type, "Information delivery")


def infer_flow_sequence(section_types: List[str]) -> List[str]:
    """Infer the persuasion flow from section types."""
    flow_map = {
        "lead": "Hook",
        "problem_agitation": "Problem",
        "mechanism_intro": "Mechanism",
        "proof": "Proof",
        "offer": "Offer",
        "cta": "CTA"
    }

    flow = [flow_map.get(t, "Content") for t in section_types]
    # Remove consecutive duplicates
    return [flow[i] for i in range(len(flow)) if i == 0 or flow[i] != flow[i-1]]


# ==============================================================================
# VOICE ANALYSIS
# ==============================================================================

def analyze_voice(text: str) -> Dict:
    """
    Analyze voice signature: rhythm, word choice, tone markers.

    Args:
        text: Full page content

    Returns:
        Dictionary with tone_markers, sentence_rhythm, word_choice_patterns
    """
    # Clean text and split into sentences
    sentences = re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]

    # Sentence rhythm analysis
    sentence_lengths = [len(s.split()) for s in sentences]
    avg_length = sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0

    short_count = sum(1 for l in sentence_lengths if l < 10)
    long_count = sum(1 for l in sentence_lengths if l > 25)
    medium_count = len(sentence_lengths) - short_count - long_count

    total_sentences = len(sentence_lengths)

    # Paragraph analysis
    paragraphs = [p.strip() for p in text.split('\n\n') if p.strip()]
    avg_paragraph_sentences = sum(len(re.split(r'[.!?]+', p)) for p in paragraphs) / len(paragraphs) if paragraphs else 0
    one_sentence_paras = sum(1 for p in paragraphs if len(re.split(r'[.!?]+', p)) <= 2)

    # Word choice analysis
    words = text.lower().split()
    word_count = len(words)

    you_words = ['you', 'your', "you're", "you've", "you'll", 'yours']
    you_count = sum(words.count(w) for w in you_words)
    second_person_ratio = you_count / word_count if word_count else 0

    # Active voice detection (simplified - looks for active verbs)
    active_verbs = ['do', 'make', 'create', 'build', 'start', 'get', 'take', 'feel', 'see', 'discover']
    active_count = sum(words.count(v) for v in active_verbs)
    active_voice_ratio = active_count / (word_count / 100) if word_count else 0  # Normalize to percentage

    # Sensory words detection
    sensory_words = extract_sensory_words(text)

    # Metaphors detection (simplified)
    metaphors = extract_metaphors(text)

    # Forbidden words check
    forbidden = {
        'game-changer': 'AI-ism',
        'revolutionary': 'hype',
        'secret': 'false intrigue',
        'miracle': 'overclaim',
        'breakthrough': 'overused',
        'amazing': 'vague',
        'incredible': 'vague'
    }

    found_forbidden = []
    for word, reason in forbidden.items():
        if word in text.lower():
            count = text.lower().count(word)
            found_forbidden.append({"word": word, "reason": reason, "count": count})

    # Power phrases detection
    power_phrases = extract_power_phrases(text)

    return {
        "sentence_rhythm": {
            "avg_sentence_length": round(avg_length, 1),
            "short_sentence_ratio": round(short_count / total_sentences, 2) if total_sentences else 0,
            "long_sentence_ratio": round(long_count / total_sentences, 2) if total_sentences else 0,
            "medium_sentence_ratio": round(medium_count / total_sentences, 2) if total_sentences else 0,
            "total_sentences": total_sentences
        },
        "paragraph_structure": {
            "avg_paragraph_length": round(avg_paragraph_sentences, 1),
            "one_sentence_paragraphs": round(one_sentence_paras / len(paragraphs), 2) if paragraphs else 0,
            "total_paragraphs": len(paragraphs),
            "mobile_friendly": avg_paragraph_sentences <= 4  # 4 sentences or less is mobile-friendly
        },
        "word_choice_patterns": {
            "second_person_ratio": round(second_person_ratio, 2),
            "active_voice_ratio": round(active_voice_ratio, 2),
            "sensory_words": sensory_words[:10],  # Top 10
            "metaphors": metaphors[:5]  # Top 5
        },
        "forbidden_words_found": found_forbidden,
        "power_phrases_used": power_phrases[:10]  # Top 10
    }


def extract_sensory_words(text: str) -> List[str]:
    """Extract sensory and emotional words."""
    sensory_patterns = [
        r'\b(wired|exhausted|foggy|vibrant|drained|energized|alive|heavy|light)\b',
        r'\b(racing|pounding|tense|relaxed|smooth|sharp|dull|bright)\b',
        r'\b(struggle|frustrated|overwhelmed|relieved|confident|anxious)\b'
    ]

    sensory_words = []
    for pattern in sensory_patterns:
        matches = re.findall(pattern, text.lower())
        sensory_words.extend(matches)

    # Return unique words with counts
    word_counts = Counter(sensory_words)
    return [word for word, count in word_counts.most_common()]


def extract_metaphors(text: str) -> List[str]:
    """Extract common metaphor patterns."""
    metaphor_patterns = [
        r'(running|going|moving|spinning|flying) (backwards|forward|in circles)',
        r'(battery|tank|reservoir|well) (drained|empty|full|depleted)',
        r'(stuck|trapped|caught) (in|on|between)',
        r'rhythm (is|running|going)',
        r'switch (flipped|turned|activated)'
    ]

    metaphors = []
    for pattern in metaphor_patterns:
        matches = re.findall(pattern, text.lower(), re.IGNORECASE)
        if matches:
            metaphors.extend([' '.join(m) if isinstance(m, tuple) else m for m in matches])

    return list(set(metaphors))[:5]


def extract_power_phrases(text: str) -> List[str]:
    """Extract common power phrases and pattern interrupts."""
    power_patterns = [
        r"here's what (nobody|no one|most|few) (tells you|knows|realizes)",
        r"the real (reason|truth|problem|solution) (is|lies)",
        r"not because you're (broken|wrong|failing)",
        r"but (because|here's the thing|what if)",
        r"what if (you could|I told you|there was)"
    ]

    phrases = []
    for pattern in power_patterns:
        matches = re.findall(pattern, text, re.IGNORECASE)
        if matches:
            phrases.extend([' '.join(m) if isinstance(m, tuple) else m for m in matches])

    return list(set(phrases))


# ==============================================================================
# PATTERN MATCHING
# ==============================================================================

def match_patterns(text: str, pattern_library: List[Dict]) -> List[Dict]:
    """
    Match text against known pattern library.

    Args:
        text: Page content to analyze
        pattern_library: List of pattern dictionaries with id, name, example, category

    Returns:
        List of matches with pattern_id, confidence, location
    """
    matches = []

    for pattern in pattern_library:
        # Extract keywords from pattern example
        pattern_keywords = extract_keywords(pattern.get('example', ''))
        text_lower = text.lower()

        # Count keyword matches
        keyword_matches = sum(1 for kw in pattern_keywords if kw in text_lower)
        confidence = keyword_matches / len(pattern_keywords) if pattern_keywords else 0

        if confidence > 0.5:  # Threshold for match
            # Find approximate location
            location = find_pattern_location(text, pattern_keywords)

            matches.append({
                "pattern_id": pattern.get('pattern_id', 'unknown'),
                "pattern_name": pattern.get('name', 'Unknown'),
                "confidence": round(confidence, 2),
                "category": pattern.get('category', 'uncategorized'),
                "location": location
            })

    return sorted(matches, key=lambda x: x['confidence'], reverse=True)


def extract_keywords(example: str) -> List[str]:
    """Extract meaningful keywords from pattern example."""
    # Remove common words
    stopwords = {
        'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were',
        'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'from', 'as',
        'this', 'that', 'these', 'those', 'it', 'they', 'you', 'your'
    }

    words = re.findall(r'\b\w+\b', example.lower())
    return [w for w in words if w not in stopwords and len(w) > 3]


def find_pattern_location(text: str, keywords: List[str]) -> str:
    """Find approximate location of pattern in text."""
    # Find sentences containing most keywords
    sentences = re.split(r'[.!?]+', text)

    best_sentence = ""
    best_match_count = 0

    for sentence in sentences:
        sentence_lower = sentence.lower()
        match_count = sum(1 for kw in keywords if kw in sentence_lower)

        if match_count > best_match_count:
            best_match_count = match_count
            best_sentence = sentence.strip()

    if best_sentence:
        return best_sentence[:100] + "..." if len(best_sentence) > 100 else best_sentence
    else:
        return "Location not found"


# ==============================================================================
# 7S SCORING HELPERS
# ==============================================================================

def extract_7s_evidence(text: str) -> Dict:
    """
    Extract textual evidence for 7S dimensions.
    Returns: Dictionary with evidence snippets for each dimension
    """
    evidence = {
        "SAFE": [],
        "SPECIAL": [],
        "SMART": [],
        "SIGNIFICANT": [],
        "SUPPORTED": [],
        "SUPERIOR": [],
        "STEAL": []
    }

    # SAFE indicators
    safe_patterns = [
        r'guarantee',
        r'risk.free',
        r'money.back',
        r'science.backed',
        r'research',
        r'study',
        r'proven',
        r'no credit card'
    ]
    evidence["SAFE"] = find_evidence(text, safe_patterns)

    # SPECIAL indicators
    special_patterns = [
        r'unique',
        r'exclusive',
        r'not for everyone',
        r'only (if|when)',
        r'unlike',
        r'different from'
    ]
    evidence["SPECIAL"] = find_evidence(text, special_patterns)

    # SMART indicators
    smart_patterns = [
        r'how (it|this) works',
        r'step.by.step',
        r'clear',
        r'simple',
        r'understand',
        r'makes sense'
    ]
    evidence["SMART"] = find_evidence(text, smart_patterns)

    # SIGNIFICANT indicators
    significant_patterns = [
        r'testimonial',
        r'\\d+ (women|people|clients)',
        r'success',
        r'results',
        r'transformed',
        r'helped thousands'
    ]
    evidence["SIGNIFICANT"] = find_evidence(text, significant_patterns)

    # SUPPORTED indicators
    supported_patterns = [
        r'(get|claim|start)',
        r'easy',
        r'simple',
        r'we.ll (help|guide|support)',
        r'just (\\d+|click)'
    ]
    evidence["SUPPORTED"] = find_evidence(text, supported_patterns)

    # SUPERIOR indicators
    superior_patterns = [
        r'join (others|thousands)',
        r'community',
        r'you.re not alone',
        r'together',
        r'group',
        r'(like|just like) you'
    ]
    evidence["SUPERIOR"] = find_evidence(text, superior_patterns)

    # STEAL indicators
    steal_patterns = [
        r'\\$\\d+',
        r'value',
        r'bonus',
        r'free',
        r'included',
        r'normally \\$',
        r'\\d+x (value|more)'
    ]
    evidence["STEAL"] = find_evidence(text, steal_patterns)

    return evidence


def find_evidence(text: str, patterns: List[str]) -> List[str]:
    """Find sentences containing evidence patterns."""
    sentences = re.split(r'[.!?]+', text)
    evidence = []

    for pattern in patterns:
        for sentence in sentences:
            if re.search(pattern, sentence, re.IGNORECASE) and sentence.strip():
                snippet = sentence.strip()[:120]
                if snippet and snippet not in evidence:
                    evidence.append(snippet)
                    if len(evidence) >= 3:  # Max 3 pieces of evidence per dimension
                        return evidence

    return evidence


# ==============================================================================
# COMPARATIVE ANALYSIS
# ==============================================================================

def compare_structures(structure1: Dict, structure2: Dict) -> Dict:
    """Compare two structure blueprints."""
    return {
        "word_count_diff": structure1['metrics']['total_word_count'] - structure2['metrics']['total_word_count'],
        "section_count_diff": structure1['metrics']['section_count'] - structure2['metrics']['section_count'],
        "cta_count_diff": structure1['metrics']['cta_count'] - structure2['metrics']['cta_count'],
        "flow_comparison": {
            "page1_flow": structure1['flow_sequence'],
            "page2_flow": structure2['flow_sequence'],
            "same_flow": structure1['flow_sequence'] == structure2['flow_sequence']
        }
    }


def compare_voices(voice1: Dict, voice2: Dict) -> Dict:
    """Compare two voice signatures."""
    rhythm1 = voice1['sentence_rhythm']
    rhythm2 = voice2['sentence_rhythm']

    return {
        "sentence_length_diff": rhythm1['avg_sentence_length'] - rhythm2['avg_sentence_length'],
        "second_person_diff": voice1['word_choice_patterns']['second_person_ratio'] -
                              voice2['word_choice_patterns']['second_person_ratio'],
        "rhythm_similarity": calculate_rhythm_similarity(rhythm1, rhythm2),
        "voice_analysis": {
            "page1_style": classify_voice_style(voice1),
            "page2_style": classify_voice_style(voice2)
        }
    }


def calculate_rhythm_similarity(rhythm1: Dict, rhythm2: Dict) -> float:
    """Calculate similarity score between two rhythm profiles."""
    diffs = [
        abs(rhythm1['short_sentence_ratio'] - rhythm2['short_sentence_ratio']),
        abs(rhythm1['medium_sentence_ratio'] - rhythm2['medium_sentence_ratio']),
        abs(rhythm1['long_sentence_ratio'] - rhythm2['long_sentence_ratio'])
    ]
    avg_diff = sum(diffs) / len(diffs)
    similarity = 1 - avg_diff  # Convert difference to similarity
    return round(similarity, 2)


def classify_voice_style(voice: Dict) -> str:
    """Classify voice style based on metrics."""
    rhythm = voice['sentence_rhythm']

    if rhythm['short_sentence_ratio'] > 0.4:
        return "Punchy/Direct"
    elif rhythm['long_sentence_ratio'] > 0.3:
        return "Flowing/Narrative"
    else:
        return "Balanced/Conversational"


# ==============================================================================
# UTILITY FUNCTIONS
# ==============================================================================

def generate_report_summary(deconstruction_data: Dict) -> str:
    """Generate executive summary text from deconstruction data."""
    summary_lines = []

    # Overall metrics
    if 'structure' in deconstruction_data:
        wc = deconstruction_data['structure']['metrics']['total_word_count']
        summary_lines.append(f"Total word count: {wc}")

    # Top insights
    summary_lines.append("\nKey Findings:")
    # This would be populated based on the full analysis

    return "\n".join(summary_lines)


if __name__ == "__main__":
    # Example usage
    sample_page = """
    ## Stop Fighting Sleep—Start Fixing Your Rhythm

    Your cortisol rhythm isn't broken—it's just running backwards.

    If you're wired at night and exhausted all day, it's not because you're broken.
    It's because your body's natural rhythm got flipped.

    ## Here's What Nobody Tells You

    Melatonin can't work when cortisol is blocking it. That's why supplements fail.

    ## Get Instant Access

    Join thousands of women who've already reset their rhythm.
    """

    print("=== STRUCTURE EXTRACTION ===")
    structure = extract_structure(sample_page)
    print(f"Sections found: {structure['metrics']['section_count']}")
    print(f"Total words: {structure['metrics']['total_word_count']}")
    print(f"CTAs: {structure['metrics']['cta_count']}")

    print("\n=== VOICE ANALYSIS ===")
    voice = analyze_voice(sample_page)
    print(f"Avg sentence length: {voice['sentence_rhythm']['avg_sentence_length']}")
    print(f"Second-person ratio: {voice['word_choice_patterns']['second_person_ratio']}")
    print(f"Mobile friendly: {voice['paragraph_structure']['mobile_friendly']}")

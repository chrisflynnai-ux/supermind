#!/usr/bin/env python3
"""
Skill Validation Script — skill_slug
Deterministic quality checks on skill outputs.
Runs BEFORE MMA scoring to catch structural issues.
"""
import sys
import json
from pathlib import Path


def validate_output(output_path: str) -> dict:
    """
    Validate skill output against structural requirements.
    Returns: {passed: bool, score: float, checks: [...]}
    """
    checks = []

    # Check 1: Output exists and is non-empty
    path = Path(output_path)
    if not path.exists():
        checks.append({"name": "file_exists", "passed": False, "msg": "Output file not found"})
        return {"passed": False, "score": 0.0, "checks": checks}

    content = path.read_text(encoding="utf-8")
    checks.append({"name": "file_exists", "passed": True, "msg": "Output file found"})

    # Check 2: Minimum content length
    min_length = 500  # Customize per skill
    passed = len(content) >= min_length
    checks.append({
        "name": "min_length",
        "passed": passed,
        "msg": f"Content length: {len(content)} chars (min: {min_length})"
    })

    # Check 3: Required sections present
    required_sections = []  # Customize: ["## Headline", "## Body", "## CTA"]
    for section in required_sections:
        found = section.lower() in content.lower()
        checks.append({
            "name": f"section_{section}",
            "passed": found,
            "msg": f"Section '{section}': {'found' if found else 'MISSING'}"
        })

    # Calculate score
    passed_count = sum(1 for c in checks if c["passed"])
    score = passed_count / len(checks) if checks else 0.0
    all_passed = all(c["passed"] for c in checks)

    return {"passed": all_passed, "score": round(score, 2), "checks": checks}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python validate.py <output_file>")
        sys.exit(1)

    result = validate_output(sys.argv[1])
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["passed"] else 1)

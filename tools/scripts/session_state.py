#!/usr/bin/env python3
"""
SUPERMIND Session State Manager v1.0.0
Manages SESSION_STATE.json for workflow tracking

Usage:
    python session_state.py show
    python session_state.py set phase production
    python session_state.py set context_usage 65
    python session_state.py load_skill copy_lfva
    python session_state.py unload_skill copy_lfva
    python session_state.py gc
    python session_state.py reset
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

ULTRAMIND_ROOT = Path(__file__).parent.parent.parent
STATE_PATH = ULTRAMIND_ROOT / ".claude" / "SESSION_STATE.json"

DEFAULT_STATE = {
    "session_id": None,
    "project_name": None,
    "current_phase": "intake",
    "current_track": "T1",
    "workflow_step": None,
    "locked_ssots": {
        "PROJECT_BRIEF.yaml": None,
        "MESSAGE_SPINE.yaml": None,
        "EVIDENCE_PACK.yaml": None,
        "VOICE_GUIDE.yaml": None
    },
    "loaded_skills": [],
    "fix_loops": {},
    "context_usage_pct": 0,
    "last_action": None,
    "awaiting": None,
    "funnel_position": None,
    "audience_type": None,
    "active_brain": None,
    "mma_scores": {
        "last_run": None,
        "average": None,
        "critical_min": None
    },
    "gc_runs": 0,
    "patch_requests": [],
    "sips_logged": [],
    "human_corrected_events": [],
    "notes": None
}


def load_state() -> dict:
    """Load current session state."""
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return DEFAULT_STATE.copy()


def save_state(state: dict):
    """Save session state."""
    STATE_PATH.write_text(json.dumps(state, indent=2))


def show_state(state: dict):
    """Display session state in formatted output."""
    print("=" * 60)
    print("SUPERMIND SESSION STATE")
    print("=" * 60)
    print(f"Session:    {state.get('session_id', 'N/A')}")
    print(f"Project:    {state.get('project_name', 'N/A')}")
    print(f"Phase:      {state.get('current_phase', 'N/A')}")
    print(f"Track:      {state.get('current_track', 'N/A')}")
    print(f"Context:    {state.get('context_usage_pct', 0)}%")
    print("-" * 60)

    print("LOADED SKILLS:")
    for skill in state.get("loaded_skills", []):
        print(f"  - {skill}")
    if not state.get("loaded_skills"):
        print("  (none)")

    print("-" * 60)
    print("LOCKED SSOTs:")
    for ssot, checksum in state.get("locked_ssots", {}).items():
        status = "LOCKED" if checksum else "unlocked"
        print(f"  [{status:8}] {ssot}")

    print("-" * 60)
    print("MMA SCORES:")
    mma = state.get("mma_scores", {})
    print(f"  Last Run:     {mma.get('last_run', 'N/A')}")
    print(f"  Average:      {mma.get('average', 'N/A')}")
    print(f"  Critical Min: {mma.get('critical_min', 'N/A')}")

    print("-" * 60)
    print(f"GC Runs:    {state.get('gc_runs', 0)}")
    print(f"Fix Loops:  {state.get('fix_loops', {})}")
    print(f"Awaiting:   {state.get('awaiting', 'N/A')}")
    print("=" * 60)


def set_value(state: dict, key: str, value: str) -> dict:
    """Set a state value."""
    # Handle nested keys like mma_scores.average
    if "." in key:
        parts = key.split(".")
        target = state
        for part in parts[:-1]:
            target = target.setdefault(part, {})
        target[parts[-1]] = value
    else:
        # Type conversion for known fields
        if key in ["context_usage_pct", "gc_runs"]:
            value = int(value)
        state[key] = value

    return state


def load_skill(state: dict, skill_id: str) -> dict:
    """Add skill to loaded_skills list."""
    if skill_id not in state.get("loaded_skills", []):
        state.setdefault("loaded_skills", []).append(skill_id)
        state["last_action"] = f"load_skill:{skill_id}"
    return state


def unload_skill(state: dict, skill_id: str) -> dict:
    """Remove skill from loaded_skills list."""
    skills = state.get("loaded_skills", [])
    if skill_id in skills:
        skills.remove(skill_id)
        state["last_action"] = f"unload_skill:{skill_id}"
    return state


def garbage_collect(state: dict) -> dict:
    """Run garbage collection - clear loaded skills, increment counter."""
    state["loaded_skills"] = []
    state["gc_runs"] = state.get("gc_runs", 0) + 1
    state["context_usage_pct"] = 15  # Reset to baseline
    state["last_action"] = "garbage_collect"
    return state


def reset_state() -> dict:
    """Reset to default state with new session ID."""
    state = DEFAULT_STATE.copy()
    state["session_id"] = f"session_{datetime.now().strftime('%Y_%m_%d_%H%M%S')}"
    state["last_action"] = "session_reset"
    return state


def main():
    parser = argparse.ArgumentParser(description="SUPERMIND Session State Manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # show
    subparsers.add_parser("show", help="Show current state")

    # set
    set_parser = subparsers.add_parser("set", help="Set a state value")
    set_parser.add_argument("key", help="State key (e.g., phase, context_usage)")
    set_parser.add_argument("value", help="Value to set")

    # load_skill
    load_parser = subparsers.add_parser("load_skill", help="Mark skill as loaded")
    load_parser.add_argument("skill_id", help="Skill ID to load")

    # unload_skill
    unload_parser = subparsers.add_parser("unload_skill", help="Mark skill as unloaded")
    unload_parser.add_argument("skill_id", help="Skill ID to unload")

    # gc
    subparsers.add_parser("gc", help="Run garbage collection")

    # reset
    subparsers.add_parser("reset", help="Reset to fresh state")

    # json (raw output)
    subparsers.add_parser("json", help="Output raw JSON")

    args = parser.parse_args()
    state = load_state()

    if args.command == "show":
        show_state(state)
    elif args.command == "set":
        state = set_value(state, args.key, args.value)
        save_state(state)
        print(f"Set {args.key} = {args.value}")
    elif args.command == "load_skill":
        state = load_skill(state, args.skill_id)
        save_state(state)
        print(f"Loaded skill: {args.skill_id}")
    elif args.command == "unload_skill":
        state = unload_skill(state, args.skill_id)
        save_state(state)
        print(f"Unloaded skill: {args.skill_id}")
    elif args.command == "gc":
        state = garbage_collect(state)
        save_state(state)
        print("Garbage collection complete")
        show_state(state)
    elif args.command == "reset":
        state = reset_state()
        save_state(state)
        print("Session reset")
        show_state(state)
    elif args.command == "json":
        print(json.dumps(state, indent=2))


if __name__ == "__main__":
    main()

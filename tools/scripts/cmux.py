#!/usr/bin/env python3
"""
CMUX - Claude Multiplexer v1.0.0
Parallel sub-agent dispatch for SUPERMIND 4-Track workflow

This script generates Task tool invocations for Claude Code
to run parallel agents. Output is meant to be copied into Claude Code.

Usage:
    python cmux.py dispatch T2 "Write VSL draft for Sleep product"
    python cmux.py parallel T2 T3 "Draft and produce simultaneously"
    python cmux.py chain "Full funnel: research -> draft -> produce -> polish"
    python cmux.py status
"""

import argparse
import json
from pathlib import Path

ULTRAMIND_ROOT = Path(__file__).parent.parent.parent
STATE_PATH = ULTRAMIND_ROOT / ".claude" / "SESSION_STATE.json"

# Track definitions from REFACTOR_MIGRATION_PLAN_v1.4
TRACKS = {
    "T1": {
        "name": "Research & Plan",
        "commands": ["/intake", "/research", "/synthesize"],
        "skills": ["market_scout", "research_ops", "mis"],
        "brain": "sonnet",
        "gate": "human_approval",
        "mma": None,
        "subagent_type": "Explore"
    },
    "T2": {
        "name": "Drafts & Development",
        "commands": ["/draft", "/strategy", "/vsl-long", "/vsl-short", "/salespage"],
        "skills": ["copy_lead", "copy_director", "{assigned_skill}"],
        "brain": "opus",
        "gate": "human_approval",
        "mma": {"mode": "M1", "threshold": 7.0},
        "subagent_type": "general-purpose"
    },
    "T3": {
        "name": "Production & Refine",
        "commands": ["/produce", "/build", "/validate"],
        "skills": ["{active_skill}_production", "mma"],
        "brain": "opus",
        "gate": "mma_pass_or_human",
        "mma": {"mode": "M2", "threshold": 8.0},
        "subagent_type": "general-purpose"
    },
    "T4": {
        "name": "Polish & Perfect",
        "commands": ["/polish", "/skeptic", "/resonance", "/publish"],
        "skills": ["skeptic_avatar", "hpe", "nra"],
        "brain": "opus",
        "gate": "human_final",
        "mma": {"mode": "M4", "threshold": 9.0},
        "subagent_type": "general-purpose"
    }
}


def load_state() -> dict:
    """Load current session state."""
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


def generate_task_prompt(track: str, user_task: str) -> str:
    """Generate a Task tool prompt for Claude Code."""
    track_config = TRACKS.get(track, TRACKS["T2"])

    return f"""SUPERMIND {track} - {track_config['name']}

TASK: {user_task}

TRACK CONFIG:
- Skills chain: {', '.join(track_config['skills'])}
- Quality gate: {track_config['gate']}
- MMA: {track_config['mma']}

CONSTRAINTS:
- Follow progressive disclosure (L1 always, L2 when executing)
- Run MMA validation before completing
- Update SESSION_STATE.json with progress
- Circuit breaker: max 3 fix loops

DELIVER:
- Primary output artifact
- MMA scorecard (if applicable)
- Patch proposals (if issues found)
"""


def generate_task_json(track: str, user_task: str) -> dict:
    """Generate Task tool parameters as JSON."""
    track_config = TRACKS.get(track, TRACKS["T2"])

    return {
        "description": f"{track} {track_config['name'][:20]}",
        "prompt": generate_task_prompt(track, user_task),
        "subagent_type": track_config["subagent_type"],
        "model": track_config["brain"]
    }


def dispatch_single(track: str, task: str):
    """Generate single track dispatch."""
    params = generate_task_json(track, task)
    print("=" * 60)
    print(f"CMUX DISPATCH: {track} - {TRACKS[track]['name']}")
    print("=" * 60)
    print("\nCopy this Task tool invocation into Claude Code:\n")
    print(json.dumps(params, indent=2))
    print("\n" + "=" * 60)


def dispatch_parallel(tracks: list, task: str):
    """Generate parallel track dispatch."""
    print("=" * 60)
    print(f"CMUX PARALLEL DISPATCH: {' + '.join(tracks)}")
    print("=" * 60)
    print("\nUse multiple Task tools in a single Claude Code message:\n")

    for track in tracks:
        params = generate_task_json(track, task)
        print(f"\n--- {track} ---")
        print(json.dumps(params, indent=2))

    print("\n" + "=" * 60)


def dispatch_chain(task: str):
    """Generate full 4-track chain."""
    print("=" * 60)
    print("CMUX CHAIN: T1 -> T2 -> T3 -> T4")
    print("=" * 60)
    print("\nSequential execution - run each after previous completes:\n")

    for track in ["T1", "T2", "T3", "T4"]:
        params = generate_task_json(track, task)
        print(f"\n--- {track}: {TRACKS[track]['name']} ---")
        print(f"Gate: {TRACKS[track]['gate']}")
        print(json.dumps(params, indent=2))

    print("\n" + "=" * 60)


def show_status():
    """Show current CMUX status."""
    state = load_state()
    print("=" * 60)
    print("CMUX STATUS")
    print("=" * 60)
    print(f"Current Track:  {state.get('current_track', 'N/A')}")
    print(f"Current Phase:  {state.get('current_phase', 'N/A')}")
    print(f"Context Usage:  {state.get('context_usage_pct', 0)}%")
    print(f"Loaded Skills:  {state.get('loaded_skills', [])}")
    print(f"Fix Loops:      {state.get('fix_loops', {})}")
    print("-" * 60)
    print("\nAVAILABLE TRACKS:")
    for track, config in TRACKS.items():
        print(f"  {track}: {config['name']}")
        print(f"      Commands: {', '.join(config['commands'])}")
        print(f"      Agent: {config['subagent_type']} ({config['brain']})")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="CMUX - Claude Multiplexer for SUPERMIND",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
    python cmux.py dispatch T2 "Write VSL draft for Sleep product"
    python cmux.py parallel T2 T3 "Draft and validate in parallel"
    python cmux.py chain "Complete funnel for Sleep for Life"
    python cmux.py status
        """
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    # dispatch
    dispatch_parser = subparsers.add_parser("dispatch", help="Single track dispatch")
    dispatch_parser.add_argument("track", choices=["T1", "T2", "T3", "T4"])
    dispatch_parser.add_argument("task", help="Task description")

    # parallel
    parallel_parser = subparsers.add_parser("parallel", help="Parallel track dispatch")
    parallel_parser.add_argument("tracks", nargs="+",
                                  help="Tracks to run (e.g., T2 T3)")
    parallel_parser.add_argument("--task", "-t", required=True, help="Task description")

    # chain
    chain_parser = subparsers.add_parser("chain", help="Full 4-track chain")
    chain_parser.add_argument("task", help="Task description")

    # status
    subparsers.add_parser("status", help="Show CMUX status")

    args = parser.parse_args()

    if args.command == "dispatch":
        dispatch_single(args.track, args.task)
    elif args.command == "parallel":
        dispatch_parallel(args.tracks, args.task)
    elif args.command == "chain":
        dispatch_chain(args.task)
    elif args.command == "status":
        show_status()


if __name__ == "__main__":
    main()

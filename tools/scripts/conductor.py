#!/usr/bin/env python3
"""
SUPERMIND Conductor v1.0.0
Master agent that reads task board and delegates to sub-agents through 4-phase execution

The Conductor Pattern:
1. Reads KANBAN.json for pending tasks
2. Routes to appropriate track (T1-T4)
3. Delegates to sub-agent teams via Claude Code Task tool
4. Updates task status as work progresses
5. Runs MMA validation at gates

Usage:
    python conductor.py run                    # Process next pending task
    python conductor.py run --all              # Process all pending tasks
    python conductor.py delegate T2 "task"    # Direct delegation
    python conductor.py status                 # Show conductor status
    python conductor.py teams                  # Show team compositions
"""

import argparse
import json
from datetime import datetime
from pathlib import Path

ULTRAMIND_ROOT = Path(__file__).parent.parent.parent
KANBAN_PATH = ULTRAMIND_ROOT / "KANBAN.json"
STATE_PATH = ULTRAMIND_ROOT / ".claude" / "SESSION_STATE.json"

# Team compositions for each track
TEAMS = {
    "T1": {
        "name": "Research Team",
        "lead": "market_scout",
        "members": ["research_ops", "mis"],
        "description": "Gathers intelligence, synthesizes research, builds SSOTs",
        "gate": "Human approval of PROJECT_BRIEF + MESSAGE_SPINE + EVIDENCE_PACK"
    },
    "T2": {
        "name": "Draft Team",
        "lead": "copy_lead",
        "members": ["copy_director", "assigned_specialist"],
        "description": "Strategic copy direction, angle exploration, draft generation",
        "gate": "Human approval + MMA M1 >= 7.0"
    },
    "T3": {
        "name": "Production Team",
        "lead": "active_skill",
        "members": ["mma"],
        "description": "Full asset production with continuous quality validation",
        "gate": "MMA M2 >= 8.0 or human override"
    },
    "T4": {
        "name": "Perfecting Team",
        "lead": "hpe",
        "members": ["skeptic_avatar", "nra"],
        "description": "Polish, humanize, stress-test, final resonance check",
        "gate": "MMA M4 >= 9.0 + human final approval"
    }
}

# Phase flow
PHASE_ORDER = ["T1", "T2", "T3", "T4"]
PHASE_NAMES = {
    "T1": "Research",
    "T2": "Drafts",
    "T3": "Production",
    "T4": "Perfecting"
}


def load_kanban() -> dict:
    """Load kanban board."""
    if KANBAN_PATH.exists():
        return json.loads(KANBAN_PATH.read_text())
    return create_default_kanban()


def save_kanban(kanban: dict):
    """Save kanban board."""
    kanban["updated"] = datetime.now().isoformat()
    KANBAN_PATH.write_text(json.dumps(kanban, indent=2))


def create_default_kanban() -> dict:
    """Create default kanban structure."""
    return {
        "version": "1.0.0",
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "columns": {
            "backlog": [],
            "T1_research": [],
            "T2_drafts": [],
            "T3_production": [],
            "T4_perfecting": [],
            "done": [],
            "blocked": []
        },
        "tasks": {}
    }


def create_task(kanban: dict, title: str, description: str = "",
                asset_type: str = None, priority: str = "normal") -> str:
    """Create a new task in backlog."""
    task_id = f"TASK-{len(kanban['tasks']) + 1:04d}"
    task = {
        "id": task_id,
        "title": title,
        "description": description,
        "asset_type": asset_type,
        "priority": priority,
        "status": "backlog",
        "current_track": None,
        "created": datetime.now().isoformat(),
        "updated": datetime.now().isoformat(),
        "history": [{"action": "created", "timestamp": datetime.now().isoformat()}],
        "mma_scores": {},
        "artifacts": [],
        "notes": []
    }
    kanban["tasks"][task_id] = task
    kanban["columns"]["backlog"].append(task_id)
    save_kanban(kanban)
    return task_id


def move_task(kanban: dict, task_id: str, to_column: str):
    """Move task to a different column."""
    task = kanban["tasks"].get(task_id)
    if not task:
        return False

    # Remove from current column
    for col_name, col_tasks in kanban["columns"].items():
        if task_id in col_tasks:
            col_tasks.remove(task_id)
            break

    # Add to new column
    kanban["columns"][to_column].append(task_id)
    task["status"] = to_column
    task["updated"] = datetime.now().isoformat()
    task["history"].append({
        "action": f"moved_to_{to_column}",
        "timestamp": datetime.now().isoformat()
    })

    # Update current track
    if to_column.startswith("T"):
        task["current_track"] = to_column.split("_")[0]

    save_kanban(kanban)
    return True


def get_next_task(kanban: dict) -> dict | None:
    """Get the next task to process based on priority and phase."""
    # Check each phase in order for pending work
    for phase in PHASE_ORDER:
        col_name = f"{phase}_{PHASE_NAMES[phase].lower()}"
        if kanban["columns"].get(col_name):
            task_id = kanban["columns"][col_name][0]
            return kanban["tasks"].get(task_id)

    # Fall back to backlog
    if kanban["columns"]["backlog"]:
        task_id = kanban["columns"]["backlog"][0]
        return kanban["tasks"].get(task_id)

    return None


def generate_delegation(task: dict, track: str) -> dict:
    """Generate Claude Code Task tool parameters for delegation."""
    team = TEAMS[track]

    prompt = f"""SUPERMIND CONDUCTOR DELEGATION
==============================

TASK: {task['title']}
DESCRIPTION: {task.get('description', 'N/A')}
ASSET TYPE: {task.get('asset_type', 'N/A')}
TASK ID: {task['id']}

TRACK: {track} - {team['name']}
TEAM LEAD: {team['lead']}
TEAM MEMBERS: {', '.join(team['members'])}

MISSION: {team['description']}

GATE CRITERIA: {team['gate']}

EXECUTION PROTOCOL:
1. Load required skills via progressive disclosure (L1 always, L2 when executing)
2. Execute team workflow
3. Run MMA validation before gate
4. Update KANBAN.json with progress
5. Generate artifacts list

CIRCUIT BREAKERS:
- Max 3 fix loops per dimension
- GC at 70% context
- Escalate to human if gate fails 2x

DELIVER:
- Primary output artifact
- MMA scorecard
- Updated task status
- Next action recommendation
"""

    return {
        "description": f"{track} {team['name'][:15]}",
        "prompt": prompt,
        "subagent_type": "general-purpose",
        "model": "opus"
    }


def run_conductor(all_tasks: bool = False):
    """Run the conductor to process tasks."""
    kanban = load_kanban()

    print("=" * 60)
    print("SUPERMIND CONDUCTOR")
    print("=" * 60)

    processed = 0
    while True:
        task = get_next_task(kanban)
        if not task:
            print("\nNo pending tasks.")
            break

        # Determine track
        if task["current_track"]:
            track = task["current_track"]
        else:
            track = "T1"  # Start at Research
            move_task(kanban, task["id"], "T1_research")

        print(f"\nProcessing: {task['id']} - {task['title']}")
        print(f"Track: {track} - {TEAMS[track]['name']}")
        print("-" * 40)

        delegation = generate_delegation(task, track)
        print("\nDELEGATION PARAMETERS:")
        print(json.dumps(delegation, indent=2))

        processed += 1
        if not all_tasks:
            break

    print(f"\n{'=' * 60}")
    print(f"Processed {processed} task(s)")


def show_status():
    """Show conductor status."""
    kanban = load_kanban()

    print("=" * 60)
    print("CONDUCTOR STATUS")
    print("=" * 60)

    print("\nKANBAN BOARD:")
    for col_name, col_tasks in kanban["columns"].items():
        count = len(col_tasks)
        print(f"  [{count:2d}] {col_name}")

    print("\nACTIVE TASKS:")
    for phase in PHASE_ORDER:
        col_name = f"{phase}_{PHASE_NAMES[phase].lower()}"
        for task_id in kanban["columns"].get(col_name, []):
            task = kanban["tasks"][task_id]
            print(f"  {phase}: {task_id} - {task['title']}")

    print("\nTEAMS:")
    for track, team in TEAMS.items():
        print(f"  {track}: {team['name']} (Lead: {team['lead']})")

    print("=" * 60)


def show_teams():
    """Show detailed team compositions."""
    print("=" * 60)
    print("SUPERMIND AGENT TEAMS")
    print("=" * 60)

    for track, team in TEAMS.items():
        print(f"\n{track}: {team['name']}")
        print("-" * 40)
        print(f"  Lead:        {team['lead']}")
        print(f"  Members:     {', '.join(team['members'])}")
        print(f"  Mission:     {team['description']}")
        print(f"  Gate:        {team['gate']}")

    print("\n" + "=" * 60)
    print("PHASE FLOW: T1 -> T2 -> T3 -> T4")
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(description="SUPERMIND Conductor")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # run
    run_parser = subparsers.add_parser("run", help="Process tasks")
    run_parser.add_argument("--all", action="store_true", help="Process all pending")

    # delegate
    delegate_parser = subparsers.add_parser("delegate", help="Direct delegation")
    delegate_parser.add_argument("track", choices=["T1", "T2", "T3", "T4"])
    delegate_parser.add_argument("task", help="Task description")

    # add
    add_parser = subparsers.add_parser("add", help="Add task to backlog")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("--desc", "-d", help="Description")
    add_parser.add_argument("--type", "-t", help="Asset type")
    add_parser.add_argument("--priority", "-p", default="normal",
                            choices=["low", "normal", "high", "critical"])

    # status
    subparsers.add_parser("status", help="Show status")

    # teams
    subparsers.add_parser("teams", help="Show team compositions")

    # init
    subparsers.add_parser("init", help="Initialize kanban board")

    args = parser.parse_args()

    if args.command == "run":
        run_conductor(args.all)
    elif args.command == "delegate":
        task = {
            "id": "DIRECT",
            "title": args.task,
            "description": args.task,
            "asset_type": None
        }
        delegation = generate_delegation(task, args.track)
        print(json.dumps(delegation, indent=2))
    elif args.command == "add":
        kanban = load_kanban()
        task_id = create_task(kanban, args.title, args.desc or "",
                              args.type, args.priority)
        print(f"Created: {task_id}")
    elif args.command == "status":
        show_status()
    elif args.command == "teams":
        show_teams()
    elif args.command == "init":
        kanban = create_default_kanban()
        save_kanban(kanban)
        print("Kanban board initialized.")


if __name__ == "__main__":
    main()

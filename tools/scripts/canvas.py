#!/usr/bin/env python3
"""
SUPERMIND Canvas v1.0.0
Terminal-based visual rendering for workflow state, skills, and outputs

Usage:
    python canvas.py state          # Visual workflow state
    python canvas.py skills         # Skills map with status
    python canvas.py neurobox       # 6D Neuro-Box visualization
    python canvas.py track T2       # Track detail view
    python canvas.py mma            # MMA scorecard view
"""

import argparse
import json
from pathlib import Path

ULTRAMIND_ROOT = Path(__file__).parent.parent.parent
STATE_PATH = ULTRAMIND_ROOT / ".claude" / "SESSION_STATE.json"
MANIFEST_PATH = ULTRAMIND_ROOT / ".claude" / "SKILLS_MANIFEST.yaml"


def load_state() -> dict:
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {}


# ANSI color codes
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"

    # Track colors
    T1 = "\033[94m"  # Blue
    T2 = "\033[93m"  # Yellow
    T3 = "\033[92m"  # Green
    T4 = "\033[95m"  # Magenta

    # Status colors
    OK = "\033[92m"
    WARN = "\033[93m"
    ERR = "\033[91m"
    INFO = "\033[96m"

    # Dimension colors (Neuro-Box)
    MIND = "\033[94m"    # Blue (Left/Logic)
    SPIRIT = "\033[92m"  # Green (Right/Proof)
    BODY = "\033[91m"    # Red (Bottom/Safety)
    HEART = "\033[93m"   # Yellow (Top/Status)
    PSYCH = "\033[95m"   # Magenta (Back/Identity)
    COSMIC = "\033[96m"  # Cyan (Front/Action)
    SOUL = "\033[97m"    # White (Center)


def render_state():
    """Render workflow state as visual canvas."""
    state = load_state()

    # Header
    print(f"\n{C.BOLD}{'=' * 70}{C.RESET}")
    print(f"{C.BOLD}  SUPERMIND CANVAS - Session: {state.get('session_id', 'N/A')}{C.RESET}")
    print(f"{'=' * 70}\n")

    # 4-Track Progress Bar
    current_track = state.get("current_track", "T1")
    tracks = ["T1", "T2", "T3", "T4"]
    track_names = ["Research", "Drafts", "Production", "Polish"]

    print(f"  {C.DIM}4-TRACK WORKFLOW{C.RESET}")
    print("  ", end="")
    for i, (t, name) in enumerate(zip(tracks, track_names)):
        color = [C.T1, C.T2, C.T3, C.T4][i]
        if t == current_track:
            print(f"{color}{C.BOLD}[{t}]{C.RESET}", end="")
        elif tracks.index(t) < tracks.index(current_track):
            print(f"{C.OK}[{t}]{C.RESET}", end="")
        else:
            print(f"{C.DIM}[{t}]{C.RESET}", end="")

        if i < 3:
            print(f" {'─' * 8} ", end="")
    print("\n")

    # Context Meter
    ctx = state.get("context_usage_pct", 0)
    ctx_bar_len = 40
    ctx_filled = int(ctx / 100 * ctx_bar_len)
    ctx_color = C.OK if ctx < 50 else (C.WARN if ctx < 70 else C.ERR)

    print(f"  {C.DIM}CONTEXT{C.RESET}")
    print(f"  {ctx_color}[{'█' * ctx_filled}{'░' * (ctx_bar_len - ctx_filled)}]{C.RESET} {ctx}%")
    if ctx >= 70:
        print(f"  {C.ERR}⚠ GC RECOMMENDED{C.RESET}")
    print()

    # Loaded Skills
    skills = state.get("loaded_skills", [])
    print(f"  {C.DIM}LOADED SKILLS{C.RESET}")
    if skills:
        for skill in skills:
            print(f"  {C.INFO}▸ {skill}{C.RESET}")
    else:
        print(f"  {C.DIM}  (none){C.RESET}")
    print()

    # SSOT Status
    print(f"  {C.DIM}SSOT LOCKS{C.RESET}")
    ssots = state.get("locked_ssots", {})
    for ssot, checksum in ssots.items():
        status = f"{C.OK}LOCKED{C.RESET}" if checksum else f"{C.DIM}unlocked{C.RESET}"
        name = ssot.replace(".yaml", "")
        print(f"  [{status:20}] {name}")
    print()

    # MMA Scores
    mma = state.get("mma_scores", {})
    print(f"  {C.DIM}MMA QUALITY GATE{C.RESET}")
    if mma.get("last_run"):
        avg = mma.get("average", 0)
        avg_color = C.OK if avg >= 8.0 else (C.WARN if avg >= 7.0 else C.ERR)
        print(f"  Last Run:     {mma.get('last_run')}")
        print(f"  Average:      {avg_color}{avg:.1f}{C.RESET}")
        print(f"  Critical Min: {mma.get('critical_min', 'N/A')}")
    else:
        print(f"  {C.DIM}  No MMA run yet{C.RESET}")

    print(f"\n{'=' * 70}\n")


def render_neurobox():
    """Render 6D Neuro-Box visualization."""
    print(f"\n{C.BOLD}{'=' * 60}{C.RESET}")
    print(f"{C.BOLD}  NEURO-BOX 6D ARCHITECTURE{C.RESET}")
    print(f"{'=' * 60}\n")

    # ASCII art of the Neuro-Box (Windows-safe characters)
    lines = [
        f"                    {C.HEART}HEART (Top){C.RESET}",
        f"                  PRODUCTION / Status",
        f"                        ^",
        f"                        |",
        f"        {C.MIND}MIND{C.RESET} <----- {C.SOUL}SOUL{C.RESET} -----> {C.SPIRIT}SPIRIT{C.RESET}",
        f"      RESONANCE      CENTER       PERSUASION",
        f"       Logic        ORCHESTRATION    Proof",
        f"                        |",
        f"                        v",
        f"                    {C.BODY}BODY (Bottom){C.RESET}",
        f"                  AUTOMATION / Safety",
        f"",
        f"        {C.PSYCH}PSYCH (Back){C.RESET}: DEVELOPMENT / Identity",
        f"       {C.COSMIC}COSMIC (Front){C.RESET}: DESIGN / Action",
    ]
    for line in lines:
        print(line)

    # Axis descriptions
    print(f"\n  {C.DIM}AXES:{C.RESET}")
    print(f"  {C.MIND}X-AXIS:{C.RESET} MIND <-> SPIRIT (Resonance <-> Persuasion)")
    print(f"  {C.BODY}Y-AXIS:{C.RESET} BODY <-> HEART (Automation <-> Production)")
    print(f"  {C.PSYCH}Z-AXIS:{C.RESET} PSYCH <-> COSMIC (Development <-> Design)")

    print(f"\n{'=' * 60}\n")


def render_skills():
    """Render skills map."""
    state = load_state()
    loaded = state.get("loaded_skills", [])

    print(f"\n{C.BOLD}{'=' * 60}{C.RESET}")
    print(f"{C.BOLD}  SKILLS INVENTORY{C.RESET}")
    print(f"{'=' * 60}\n")

    # Categories from manifest
    categories = {
        "META/ORCHESTRATION": ["zpwo", "mma", "skill_builder"],
        "COPY/PERSUASION": ["copy_lead", "copy_director", "lfva", "sfvw", "hpe", "nra"],
        "RESEARCH": ["market_scout", "research_ops", "mis"],
        "DESIGN": ["strategic_design_master", "ui_ux_pro_max"],
        "PRODUCT": ["product_creation", "offer_architect"]
    }

    for cat, skills in categories.items():
        print(f"  {C.BOLD}{cat}{C.RESET}")
        for skill in skills:
            if skill in loaded:
                status = f"{C.OK}LOADED{C.RESET}"
            else:
                status = f"{C.DIM}ready{C.RESET}"
            print(f"    [{status:18}] {skill}")
        print()

    print(f"{'=' * 60}\n")


def render_track(track: str):
    """Render detailed track view."""
    tracks_config = {
        "T1": {
            "name": "Research & Plan",
            "color": C.T1,
            "commands": ["/intake", "/research", "/synthesize"],
            "skills": ["market_scout", "research_ops", "mis"],
            "outputs": ["PROJECT_BRIEF", "MESSAGE_SPINE", "EVIDENCE_PACK"],
            "gate": "Human approval of SSOTs"
        },
        "T2": {
            "name": "Drafts & Development",
            "color": C.T2,
            "commands": ["/draft", "/strategy", "/vsl", "/salespage"],
            "skills": ["copy_lead", "copy_director", "lfva", "sfvw"],
            "outputs": ["Draft assets", "Angle variations"],
            "gate": "Human approval + MMA M1 >= 7.0"
        },
        "T3": {
            "name": "Production & Refine",
            "color": C.T3,
            "commands": ["/produce", "/build", "/validate"],
            "skills": ["active_skill_production", "mma"],
            "outputs": ["Production assets", "MMA scorecard"],
            "gate": "MMA M2 >= 8.0 or human override"
        },
        "T4": {
            "name": "Polish & Perfect",
            "color": C.T4,
            "commands": ["/polish", "/skeptic", "/resonance"],
            "skills": ["skeptic_avatar", "hpe", "nra"],
            "outputs": ["Final assets", "SHIP_PACKAGE"],
            "gate": "MMA M4 >= 9.0 + human final"
        }
    }

    config = tracks_config.get(track)
    if not config:
        print(f"Unknown track: {track}")
        return

    print(f"\n{config['color']}{C.BOLD}{'=' * 60}{C.RESET}")
    print(f"{config['color']}{C.BOLD}  {track}: {config['name']}{C.RESET}")
    print(f"{config['color']}{'=' * 60}{C.RESET}\n")

    print(f"  {C.DIM}COMMANDS:{C.RESET}")
    for cmd in config["commands"]:
        print(f"    {cmd}")

    print(f"\n  {C.DIM}SKILLS CHAIN:{C.RESET}")
    for skill in config["skills"]:
        print(f"    ▸ {skill}")

    print(f"\n  {C.DIM}OUTPUTS:{C.RESET}")
    for output in config["outputs"]:
        print(f"    → {output}")

    print(f"\n  {C.DIM}GATE:{C.RESET}")
    print(f"    {config['gate']}")

    print(f"\n{'=' * 60}\n")


def render_mma():
    """Render MMA scorecard template."""
    print(f"\n{C.BOLD}{'=' * 60}{C.RESET}")
    print(f"{C.BOLD}  MMA 7-DIMENSION SCORECARD{C.RESET}")
    print(f"{'=' * 60}\n")

    dimensions = [
        ("D1", "Strategy Alignment", 0.15, 8.0, "CRITICAL"),
        ("D2", "Proof Discipline", 0.20, 9.0, "CRITICAL"),
        ("D3", "CTA Integrity", 0.15, 9.0, "CRITICAL"),
        ("D4", "Voice Consistency", 0.15, 8.0, "HIGH"),
        ("D5", "Clarity + Structure", 0.10, 8.0, "HIGH"),
        ("D6", "Resonance", 0.15, 8.0, "HIGH"),
        ("D7", "Ethical Guardrails", 0.10, 9.0, "CRITICAL")
    ]

    state = load_state()
    mma = state.get("mma_scores", {})

    print(f"  {'DIM':<4} {'NAME':<22} {'WEIGHT':<8} {'THRESH':<8} {'PRIORITY':<10}")
    print(f"  {'-' * 56}")

    for dim_id, name, weight, thresh, priority in dimensions:
        priority_color = C.ERR if priority == "CRITICAL" else C.WARN
        print(f"  {dim_id:<4} {name:<22} {weight:<8.0%} {thresh:<8.1f} {priority_color}{priority:<10}{C.RESET}")

    print(f"\n  {C.DIM}VERDICT LOGIC:{C.RESET}")
    print(f"  {C.OK}PASS{C.RESET}: Weighted avg >= 8.0 AND all CRITICAL >= threshold")
    print(f"  {C.WARN}FIX{C.RESET}:  Weighted avg 6.5-7.9 OR any dim 5.0-6.9")
    print(f"  {C.ERR}ESCALATE{C.RESET}: Weighted avg < 6.5 OR CRITICAL < threshold")

    print(f"\n{'=' * 60}\n")


def main():
    parser = argparse.ArgumentParser(description="SUPERMIND Canvas")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("state", help="Workflow state view")
    subparsers.add_parser("skills", help="Skills inventory")
    subparsers.add_parser("neurobox", help="Neuro-Box 6D visualization")
    subparsers.add_parser("mma", help="MMA scorecard template")

    track_parser = subparsers.add_parser("track", help="Track detail view")
    track_parser.add_argument("track_id", choices=["T1", "T2", "T3", "T4"])

    args = parser.parse_args()

    if args.command == "state":
        render_state()
    elif args.command == "skills":
        render_skills()
    elif args.command == "neurobox":
        render_neurobox()
    elif args.command == "mma":
        render_mma()
    elif args.command == "track":
        render_track(args.track_id)


if __name__ == "__main__":
    main()

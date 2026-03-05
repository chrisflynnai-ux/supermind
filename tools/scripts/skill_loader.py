#!/usr/bin/env python3
"""
SUPERMIND Skill Loader v1.0.0
Loads XML skills with progressive disclosure (L1-L4 layers)

Usage:
    python skill_loader.py <skill_id> [--layer 2] [--format markdown|xml]
    python skill_loader.py --list
    python skill_loader.py --manifest
"""

import argparse
import json
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

# Paths relative to ULTRAMIND root
ULTRAMIND_ROOT = Path(__file__).parent.parent.parent
SKILLS_DIR = ULTRAMIND_ROOT / ".claude" / "skills"
MANIFEST_PATH = ULTRAMIND_ROOT / ".claude" / "SKILLS_MANIFEST.yaml"
SUPERMIND_DIR = Path(os.environ.get("SUPERMIND_PROJECT",
    Path.home() / "OneDrive" / "Desktop" / "SUPERMIND PROJECT"))


def find_skill_file(skill_id: str) -> Path | None:
    """Find skill XML file by skill_id or partial match."""
    # Search patterns
    patterns = [
        f"**/*{skill_id}*.xml",
        f"**/*{skill_id.replace('_', '-')}*.xml",
        f"**/*{skill_id.replace('-', '_')}*.xml",
    ]

    # Search in .claude/skills first
    for pattern in patterns:
        matches = list(SKILLS_DIR.glob(pattern))
        if matches:
            return matches[0]

    # Search in SUPERMIND PROJECT
    if SUPERMIND_DIR.exists():
        for pattern in patterns:
            matches = list(SUPERMIND_DIR.glob(pattern))
            if matches:
                return matches[0]

    return None


def extract_layers(xml_path: Path, max_layer: int = 4) -> dict:
    """Extract skill layers from XML file."""
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.ParseError as e:
        return {"error": f"XML parse error: {e}"}

    # Extract metadata
    skill_data = {
        "skill_id": root.get("skill_id", "unknown"),
        "name": root.get("name", "Unknown Skill"),
        "version": root.get("version", "0.0.0"),
        "status": root.get("status", "unknown"),
        "file": str(xml_path),
        "layers": {}
    }

    # Extract layers (L1, L2, L3, L4 or Layer elements)
    for layer_num in range(1, max_layer + 1):
        layer_elem = root.find(f".//L{layer_num}") or root.find(f'.//Layer[@level="{layer_num}"]')
        if layer_elem is not None:
            # Convert element to string
            layer_content = ET.tostring(layer_elem, encoding="unicode", method="xml")
            skill_data["layers"][f"L{layer_num}"] = {
                "content": layer_content,
                "tokens_estimate": len(layer_content) // 4  # Rough token estimate
            }

    return skill_data


def format_as_markdown(skill_data: dict, max_layer: int) -> str:
    """Format skill data as markdown for context injection."""
    lines = [
        f"# {skill_data['name']} v{skill_data['version']}",
        f"**Skill ID:** `{skill_data['skill_id']}`",
        f"**Status:** {skill_data['status']}",
        f"**Source:** `{skill_data['file']}`",
        "",
        "---",
        ""
    ]

    for layer_key in [f"L{i}" for i in range(1, max_layer + 1)]:
        if layer_key in skill_data.get("layers", {}):
            layer = skill_data["layers"][layer_key]
            lines.extend([
                f"## {layer_key} (~{layer['tokens_estimate']} tokens)",
                "",
                "```xml",
                layer["content"],
                "```",
                ""
            ])

    return "\n".join(lines)


def list_skills() -> list[dict]:
    """List all available skills."""
    skills = []

    # Scan .claude/skills
    for xml_file in SKILLS_DIR.rglob("*.xml"):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()
            skills.append({
                "id": root.get("skill_id", xml_file.stem),
                "name": root.get("name", xml_file.stem),
                "status": root.get("status", "unknown"),
                "path": str(xml_file.relative_to(ULTRAMIND_ROOT))
            })
        except:
            skills.append({
                "id": xml_file.stem,
                "name": xml_file.stem,
                "status": "parse_error",
                "path": str(xml_file.relative_to(ULTRAMIND_ROOT))
            })

    # Scan SUPERMIND PROJECT
    if SUPERMIND_DIR.exists():
        for xml_file in SUPERMIND_DIR.glob("*.xml"):
            try:
                tree = ET.parse(xml_file)
                root = tree.getroot()
                skills.append({
                    "id": root.get("skill_id", xml_file.stem),
                    "name": root.get("name", xml_file.stem),
                    "status": root.get("status", "unknown"),
                    "path": str(xml_file)
                })
            except:
                pass

    return skills


def main():
    parser = argparse.ArgumentParser(description="SUPERMIND Skill Loader")
    parser.add_argument("skill_id", nargs="?", help="Skill ID to load")
    parser.add_argument("--layer", "-l", type=int, default=2,
                        help="Max layer to load (1-4, default: 2)")
    parser.add_argument("--format", "-f", choices=["markdown", "xml", "json"],
                        default="markdown", help="Output format")
    parser.add_argument("--list", action="store_true", help="List all skills")
    parser.add_argument("--manifest", action="store_true", help="Show skill manifest")

    args = parser.parse_args()

    if args.list:
        skills = list_skills()
        print(f"Found {len(skills)} skills:\n")
        for s in skills:
            print(f"  [{s['status']:10}] {s['id']}: {s['name']}")
        return

    if args.manifest:
        if MANIFEST_PATH.exists():
            print(MANIFEST_PATH.read_text())
        else:
            print(f"Manifest not found at {MANIFEST_PATH}")
        return

    if not args.skill_id:
        parser.print_help()
        return

    # Find and load skill
    skill_path = find_skill_file(args.skill_id)
    if not skill_path:
        print(f"Skill not found: {args.skill_id}", file=sys.stderr)
        sys.exit(1)

    skill_data = extract_layers(skill_path, args.layer)

    if "error" in skill_data:
        print(f"Error: {skill_data['error']}", file=sys.stderr)
        sys.exit(1)

    if args.format == "json":
        print(json.dumps(skill_data, indent=2))
    elif args.format == "markdown":
        print(format_as_markdown(skill_data, args.layer))
    else:  # xml
        for layer_key, layer in skill_data.get("layers", {}).items():
            print(f"<!-- {layer_key} -->")
            print(layer["content"])


if __name__ == "__main__":
    main()

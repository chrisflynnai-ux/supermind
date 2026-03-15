#!/usr/bin/env python3
"""
Threadex Memory Layer CLI v1.0.0

File-based agentic memory with expertise + production axes.
Seven-stage SIMS lifecycle (observed -> validated -> candidate -> golden | contested | deprecated | forbidden).

Usage:
    python tools/tx.py init                    # Create .threadex/ structure
    python tools/tx.py record writer/headlines "pattern content" --type pattern
    python tools/tx.py prime writer            # Output golden + recent as XML
    python tools/tx.py status                  # Show health summary
"""

import argparse
import json
import os
import re
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


# ============================================================
# PATH CONSTANTS
# ============================================================

ROOT = Path(__file__).parent.parent
THREADEX_DIR = ROOT / ".threadex"
EXPERTISE_DIR = THREADEX_DIR / "expertise"
PRODUCTION_DIR = THREADEX_DIR / "production"
CONFIG_PATH = THREADEX_DIR / "threadex.config.yaml"


# ============================================================
# SCHEMA CONSTANTS
# ============================================================

RECORD_TYPES = ("convention", "pattern", "failure", "decision", "reference", "insight")
RECORD_STATUSES = ("observed", "validated", "candidate", "golden", "contested", "deprecated", "forbidden")
COGNITIVE_STAGES = ("evolving", "refined", "wisdom")
GRAPH_RELATIONS = ("DEPENDS_ON", "CONFLICTS_WITH", "SUPERSEDES", "COMPLEMENTS", "DERIVES_FROM")


# ============================================================
# SEED DOMAINS
# ============================================================

SEED_DOMAINS = {
    "writer": {
        "family": "copywriting",
        "description": "Writer / Copywriter family — headlines, hooks, CTAs, voice",
        "siblings": {"brother": "researcher", "sister": "editor"},
        "track": "resonance",
        "progression": {"analysis": "researcher", "synthesis": "strategist", "genesis": "writer"},
        "sub_domains": ["headlines", "hooks", "ctas", "voice"]
    },
    "researcher": {
        "family": "research",
        "description": "Research & Discovery family — market analysis, competitor intel, evidence",
        "siblings": {"brother": "strategist", "sister": "writer"},
        "track": "resonance",
        "progression": {"analysis": "researcher", "synthesis": "strategist", "genesis": "writer"},
        "sub_domains": ["market_analysis", "competitor_intel", "evidence_synthesis"]
    },
    "strategist": {
        "family": "strategy",
        "description": "Strategy / Planner family — offer design, funnel architecture, positioning",
        "siblings": {"brother": "researcher", "sister": "designer"},
        "track": "production",
        "progression": {"analysis": "researcher", "synthesis": "strategist", "genesis": "designer"},
        "sub_domains": ["offer_design", "funnel_architecture", "positioning"]
    },
    "designer": {
        "family": "design",
        "description": "Design / Producer family — layout patterns, color systems, components",
        "siblings": {"brother": "developer", "sister": "strategist"},
        "track": "design",
        "progression": {"analysis": "strategist", "synthesis": "designer", "genesis": "developer"},
        "sub_domains": ["layout_patterns", "color_systems", "component_library"]
    }
}


# ============================================================
# DEFAULT CONFIG
# ============================================================

DEFAULT_CONFIG = {
    "threadex": {
        "version": "1.0",
        "decay": {
            "alpha": 0.15,
            "lambda_": 0.01,
            "forbidden_threshold": 0.3,
            "golden_review_days": 180,
            "episodic_archive_days": 30
        },
        "compaction": {
            "max_records_per_file": 10000,
            "soft_context_warning": 0.50,
            "hard_context_flush": 0.70,
            "emergency_flush": 0.85
        },
        "slicing": {
            "method": "action_boundaries",
            "fallback": "token_chunks",
            "max_chunk_tokens": 4000
        },
        "synch_pulse": {
            "interval_turns": 5,
            "enabled": False
        }
    }
}


# ============================================================
# YAML HELPERS (PyYAML optional with string fallback)
# ============================================================

def _write_yaml_string(data, indent=0):
    """Convert dict to YAML string without PyYAML."""
    lines = []
    prefix = "  " * indent
    for key, val in data.items():
        if isinstance(val, dict):
            lines.append(f"{prefix}{key}:")
            lines.append(_write_yaml_string(val, indent + 1))
        elif isinstance(val, list):
            lines.append(f"{prefix}{key}:")
            for item in val:
                if isinstance(item, dict):
                    first = True
                    for k, v in item.items():
                        if first:
                            lines.append(f"{prefix}  - {k}: {_yaml_val(v)}")
                            first = False
                        else:
                            lines.append(f"{prefix}    {k}: {_yaml_val(v)}")
                else:
                    lines.append(f"{prefix}  - {_yaml_val(item)}")
        else:
            lines.append(f"{prefix}{key}: {_yaml_val(val)}")
    return "\n".join(lines)


def _yaml_val(v):
    """Format a value for YAML output."""
    if v is None:
        return "null"
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        return str(v)
    if isinstance(v, str) and ('"' in v or "'" in v or ':' in v or '#' in v or v != v.strip()):
        return f'"{v}"'
    return str(v) if v else '""'


def _write_yaml(data, filepath):
    """Write dict to YAML file."""
    if HAS_YAML:
        filepath.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False), encoding="utf-8")
    else:
        filepath.write_text(_write_yaml_string(data) + "\n", encoding="utf-8")


def _load_yaml(filepath):
    """Load YAML file to dict."""
    content = filepath.read_text(encoding="utf-8")
    if HAS_YAML:
        return yaml.safe_load(content)
    return _parse_flat_yaml(content)


def _parse_flat_yaml(content):
    """Minimal YAML parser for flat and simple nested structures."""
    result = {}
    current_key = None
    current_list = None
    for line in content.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        if indent == 0 and ":" in stripped:
            key, _, val = stripped.partition(":")
            val = val.strip().strip('"').strip("'")
            if val:
                result[key.strip()] = val
            else:
                result[key.strip()] = {}
                current_key = key.strip()
            current_list = None
        elif indent > 0 and current_key:
            if stripped.startswith("- "):
                item = stripped[2:].strip().strip('"').strip("'")
                if not isinstance(result[current_key], list):
                    result[current_key] = []
                result[current_key].append(item)
            elif ":" in stripped:
                k, _, v = stripped.partition(":")
                v = v.strip().strip('"').strip("'")
                if isinstance(result[current_key], dict):
                    result[current_key][k.strip()] = v
    return result


# ============================================================
# ADVISORY LOCKING
# ============================================================

def acquire_lock(filepath, timeout=5.0):
    """Advisory file lock. Returns True if acquired, False if busy."""
    lock = filepath.with_suffix(filepath.suffix + ".lock")
    if lock.exists():
        try:
            age = time.time() - lock.stat().st_mtime
            if age > timeout:
                lock.unlink()  # stale lock
            else:
                return False
        except OSError:
            return False
    try:
        lock.write_text(str(os.getpid()), encoding="utf-8")
        return True
    except OSError:
        return False


def release_lock(filepath):
    """Release advisory file lock."""
    lock = filepath.with_suffix(filepath.suffix + ".lock")
    try:
        if lock.exists():
            lock.unlink()
    except OSError:
        pass


# ============================================================
# RECORD OPERATIONS
# ============================================================

def make_record(domain, content, record_type="pattern", status="observed", **kwargs):
    """Create a new JSONL record with defaults + UUID + timestamps."""
    now = datetime.now(timezone.utc).isoformat()
    record = {
        "id": str(uuid.uuid4()),
        "type": record_type,
        "status": status,
        "cognitive_stage": "evolving",
        "domain": domain,
        "content": content,
        "context": kwargs.get("context", ""),
        "source_project": kwargs.get("source_project", ""),
        "evidence_count": kwargs.get("evidence_count", 0),
        "evidence_contexts": kwargs.get("evidence_contexts", []),
        "mma_score": kwargs.get("mma_score"),
        "created_at": now,
        "updated_at": now,
        "created_by": kwargs.get("created_by", "orchestrator"),
        "provenance": kwargs.get("provenance", ""),
        "model_id": kwargs.get("model_id", ""),
        "model_version": kwargs.get("model_version", ""),
        "harness_id": kwargs.get("harness_id", ""),
        "harness_version": kwargs.get("harness_version", ""),
        "skill_version": kwargs.get("skill_version", ""),
        "prompt_checksum": kwargs.get("prompt_checksum"),
        "last_accessed": None,
        "num_recalled": 0,
        "utility_score": kwargs.get("utility_score", 0.5),
        "tags": kwargs.get("tags", []),
        "conflict_reason": None,
        "conflicting_pattern_id": None,
        "deprecated_reason": None,
        "superseded_by": None,
        "threadex_graph": kwargs.get("threadex_graph", [])
    }
    return record


def validate_record(record):
    """Validate a record dict. Returns (valid: bool, errors: list[str])."""
    errors = []
    if not record.get("id"):
        errors.append("Missing 'id'")
    if record.get("type") not in RECORD_TYPES:
        errors.append(f"Invalid type: {record.get('type')}. Must be one of {RECORD_TYPES}")
    if record.get("status") not in RECORD_STATUSES:
        errors.append(f"Invalid status: {record.get('status')}. Must be one of {RECORD_STATUSES}")
    if not record.get("content"):
        errors.append("Missing 'content'")
    if not record.get("domain"):
        errors.append("Missing 'domain'")
    if not record.get("created_at"):
        errors.append("Missing 'created_at'")
    return (len(errors) == 0, errors)


def make_graph_edge(target, rel="DEPENDS_ON", strength=0.5, phase=None, tags=None):
    """Create a threadex_graph entry."""
    return {
        "target": target,
        "rel": rel,
        "strength": strength,
        "phase": phase,
        "tags": tags or []
    }


def read_jsonl(filepath):
    """Read all records from a JSONL file. Returns list of dicts."""
    if not filepath.exists():
        return []
    records = []
    for line in filepath.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    return records


def append_record(filepath, record):
    """Append a JSONL record with advisory locking."""
    filepath.parent.mkdir(parents=True, exist_ok=True)
    retries = 3
    for i in range(retries):
        if acquire_lock(filepath):
            try:
                with open(filepath, "a", encoding="utf-8") as f:
                    f.write(json.dumps(record, default=str) + "\n")
                return True
            finally:
                release_lock(filepath)
        time.sleep(0.2)
    print(f"Warning: Could not acquire lock for {filepath} after {retries} retries", file=sys.stderr)
    # Fallback: write without lock
    with open(filepath, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, default=str) + "\n")
    return True


def find_record_by_id(filepath, record_id):
    """Find record by ID. Returns (line_index, record) or (None, None)."""
    if not filepath.exists():
        return None, None
    for i, line in enumerate(filepath.read_text(encoding="utf-8").splitlines()):
        line = line.strip()
        if not line:
            continue
        try:
            record = json.loads(line)
            if record.get("id") == record_id:
                return i, record
        except json.JSONDecodeError:
            continue
    return None, None


def update_record_in_file(filepath, line_index, updated_record):
    """Replace record at line_index in JSONL file with locking."""
    retries = 3
    for i in range(retries):
        if acquire_lock(filepath):
            try:
                lines = filepath.read_text(encoding="utf-8").splitlines()
                lines[line_index] = json.dumps(updated_record, default=str)
                filepath.write_text("\n".join(lines) + "\n", encoding="utf-8")
                return True
            finally:
                release_lock(filepath)
        time.sleep(0.2)
    return False


# ============================================================
# CONFIG LOADER
# ============================================================

def load_config():
    """Load threadex.config.yaml. Returns DEFAULT_CONFIG if not found."""
    if CONFIG_PATH.exists():
        try:
            return _load_yaml(CONFIG_PATH)
        except Exception:
            return DEFAULT_CONFIG
    return DEFAULT_CONFIG


# ============================================================
# INDEX & SIMS OPERATIONS
# ============================================================

def update_index(domain_path):
    """Rescan JSONL files in domain_path and update _index.yaml counts.

    Args:
        domain_path: Path to a domain directory (e.g. .threadex/expertise/writer/)

    Returns:
        dict: pattern_counts keyed by status
    """
    index_file = domain_path / "_index.yaml"
    if not index_file.exists():
        return {}

    index = _load_yaml(index_file)
    if not index:
        return {}

    # Reset pattern counts
    pattern_counts = {s: 0 for s in RECORD_STATUSES}

    # Rebuild sub_domains from actual JSONL files on disk
    # (resilient to flat YAML parser returning strings instead of dicts)
    raw_subs = index.get("sub_domains", [])
    rebuilt_subs = []
    for sd in raw_subs:
        if isinstance(sd, dict):
            name = sd.get("name", "")
            filename = sd.get("file", f"{name}.jsonl")
        elif isinstance(sd, str):
            # Flat YAML parser returns strings like "name: headlines"
            name = sd.split(":", 1)[-1].strip() if ":" in sd else sd.strip()
            filename = f"{name}.jsonl"
        else:
            continue

        sd_file = domain_path / filename
        records = read_jsonl(sd_file)
        record_count = len(records)
        golden_count = sum(1 for r in records if r.get("status") == "golden")

        rebuilt_subs.append({
            "name": name,
            "file": filename,
            "record_count": record_count,
            "golden_count": golden_count,
        })

        for r in records:
            status = r.get("status", "observed")
            if status in pattern_counts:
                pattern_counts[status] += 1

    index["pattern_counts"] = pattern_counts
    index["sub_domains"] = rebuilt_subs
    index["last_updated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    _write_yaml(index, index_file)
    return pattern_counts


def apply_sims_rules(record, config=None):
    """Apply SIMS auto-extraction heuristics to a record.

    Rules:
    - MMA score >= 9.0 -> auto-promote to candidate (never auto-golden)
    - type=failure + evidence_count >= 3 -> auto-mark forbidden
    - utility_score < forbidden_threshold -> add _low_utility_flag tag

    Args:
        record: dict -- a JSONL record
        config: dict -- threadex config (uses DEFAULT_CONFIG if None)

    Returns:
        dict: the modified record
    """
    if config is None:
        config = DEFAULT_CONFIG

    # Extract threshold from config (nested under threadex.decay or flat)
    cfg_root = config.get("threadex", config)
    decay = cfg_root.get("decay", {})
    if isinstance(decay, dict) and "forbidden_threshold" in decay:
        forbidden_threshold = float(decay.get("forbidden_threshold", 0.3))
    else:
        # Flat YAML fallback: forbidden_threshold may be a sibling key
        forbidden_threshold = float(cfg_root.get("forbidden_threshold", 0.3))

    mma_score = record.get("mma_score")
    record_type = record.get("type", "")
    evidence_count = record.get("evidence_count", 0)
    utility_score = record.get("utility_score")
    tags = record.get("tags", [])
    if not isinstance(tags, list):
        tags = []

    # Rule 1: High MMA -> auto-promote to candidate (never golden)
    if mma_score is not None and mma_score >= 9.0:
        if record.get("status") in ("observed", "validated"):
            record["status"] = "candidate"

    # Rule 2: Repeated failure -> forbidden
    if record_type == "failure" and evidence_count >= 3:
        record["status"] = "forbidden"

    # Rule 3: Low utility -> flag
    if utility_score is not None and utility_score < forbidden_threshold:
        if "_low_utility_flag" not in tags:
            tags.append("_low_utility_flag")
            record["tags"] = tags

    return record



# ============================================================
# COMMANDS
# ============================================================

def cmd_init(args):
    """Create .threadex/ folder structure + config + seed domains."""
    if THREADEX_DIR.exists() and not getattr(args, 'force', False):
        print(f"Error: {THREADEX_DIR} already exists. Use --force to overwrite.", file=sys.stderr)
        sys.exit(1)

    created_dirs = 0
    created_files = 0
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Create expertise domains
    for domain_name, domain_info in SEED_DOMAINS.items():
        domain_dir = EXPERTISE_DIR / domain_name
        golden_dir = domain_dir / "golden"
        golden_dir.mkdir(parents=True, exist_ok=True)
        created_dirs += 2

        # Create _index.yaml
        index_data = {
            "domain": domain_name,
            "family": domain_info["family"],
            "description": domain_info["description"],
            "siblings": domain_info["siblings"],
            "track": domain_info["track"],
            "progression": domain_info["progression"],
            "sub_domains": [
                {"name": sd, "file": f"{sd}.jsonl", "record_count": 0, "golden_count": 0}
                for sd in domain_info["sub_domains"]
            ],
            "pattern_counts": {s: 0 for s in RECORD_STATUSES},
            "created_at": now,
            "last_updated": now
        }
        _write_yaml(index_data, domain_dir / "_index.yaml")
        created_files += 1

        # Create empty JSONL files
        for sd in domain_info["sub_domains"]:
            jsonl_file = domain_dir / f"{sd}.jsonl"
            if not jsonl_file.exists():
                jsonl_file.touch()
                created_files += 1

    # Create _shared
    shared_dir = EXPERTISE_DIR / "_shared"
    shared_golden = shared_dir / "golden"
    shared_golden.mkdir(parents=True, exist_ok=True)
    created_dirs += 2

    shared_index = {
        "domain": "_shared",
        "family": "cross_domain",
        "description": "Cross-domain patterns promoted via Private > Client > Collective gradient",
        "sub_domains": [
            {"name": "anti_patterns", "file": "anti_patterns.jsonl", "record_count": 0, "golden_count": 0},
            {"name": "frameworks", "file": "frameworks.jsonl", "record_count": 0, "golden_count": 0}
        ],
        "pattern_counts": {s: 0 for s in RECORD_STATUSES},
        "created_at": now,
        "last_updated": now
    }
    _write_yaml(shared_index, shared_dir / "_index.yaml")
    (shared_dir / "anti_patterns.jsonl").touch()
    (shared_dir / "frameworks.jsonl").touch()
    created_files += 3

    # Create production
    archive_dir = PRODUCTION_DIR / "_archive"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / ".gitkeep").touch()
    created_dirs += 2
    created_files += 1

    # Write config
    _write_yaml(DEFAULT_CONFIG, CONFIG_PATH)
    created_files += 1

    # Write .gitattributes
    gitattr_path = ROOT / ".gitattributes"
    gitattr_content = "# Threadex JSONL files — merge=union avoids conflicts on append-only logs\n*.jsonl merge=union\n"
    if not gitattr_path.exists():
        gitattr_path.write_text(gitattr_content, encoding="utf-8")
        created_files += 1
        print("Created .gitattributes with JSONL merge=union")
    else:
        existing = gitattr_path.read_text(encoding="utf-8")
        if "merge=union" not in existing:
            with open(gitattr_path, "a", encoding="utf-8") as f:
                f.write("\n" + gitattr_content)
            print("Updated .gitattributes with JSONL merge=union")

    print("\nThreadex initialized successfully!")
    print(f"  Directories created: {created_dirs}")
    print(f"  Files created: {created_files}")
    print(f"  Expertise domains: {', '.join(SEED_DOMAINS.keys())}, _shared")
    print(f"  Config: {CONFIG_PATH}")
    print(f"  Root: {THREADEX_DIR}")


def cmd_record(args):
    """Append a memory record to a domain/subdomain JSONL file."""
    target = args.target
    parts = target.split("/", 1)
    if len(parts) != 2:
        print("Error: target must be domain/subdomain (e.g. writer/headlines)", file=sys.stderr)
        sys.exit(1)

    domain, subdomain = parts[0], parts[1]
    config = load_config()

    # Resolve filepath
    if args.project:
        project_dir = PRODUCTION_DIR / args.project
        project_dir.mkdir(parents=True, exist_ok=True)
        filepath = project_dir / f"{subdomain}.jsonl"
        domain_path = project_dir
    else:
        domain_path = EXPERTISE_DIR / domain
        if not domain_path.exists():
            print(f"Error: Domain '{domain}' not found in {EXPERTISE_DIR}", file=sys.stderr)
            print(f"  Available: {', '.join(d.name for d in EXPERTISE_DIR.iterdir() if d.is_dir())}", file=sys.stderr)
            sys.exit(1)
        filepath = domain_path / f"{subdomain}.jsonl"

    # Parse tags
    tags = []
    if args.tags:
        tags = [t.strip() for t in args.tags.split(",") if t.strip()]

    # Create record
    record = make_record(
        domain=target,
        content=args.content,
        record_type=args.type,
        status=args.status,
        mma_score=args.mma_score,
        source_project=args.source or "",
        provenance=args.provenance or "",
        created_by=args.agent,
        tags=tags,
    )

    # Apply SIMS auto-extraction rules
    record = apply_sims_rules(record, config)

    # Validate
    valid, errors = validate_record(record)
    if not valid:
        print(f"Error: Invalid record -- {'; '.join(errors)}", file=sys.stderr)
        sys.exit(1)

    # Append to JSONL
    append_record(filepath, record)

    # Update index (only for expertise domains, not production)
    if not args.project:
        update_index(domain_path)

    # Output
    if args.json:
        print(json.dumps(record, indent=2, default=str))
    else:
        print(record["id"])



# ============================================================
# MAIN ENTRY POINT
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        prog="tx",
        description="Threadex Memory Layer CLI v1.0 — File-based agentic memory"
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # init
    init_parser = subparsers.add_parser("init", help="Create .threadex/ folder structure + config")
    init_parser.add_argument("--force", action="store_true", help="Overwrite existing .threadex/")

    # record
    record_parser = subparsers.add_parser("record", help="Append a memory record")
    record_parser.add_argument("target", help="domain/subdomain (e.g. writer/headlines)")
    record_parser.add_argument("content", help="Record content text")
    record_parser.add_argument("--type", choices=RECORD_TYPES, default="pattern")
    record_parser.add_argument("--status", choices=RECORD_STATUSES, default="observed")
    record_parser.add_argument("--project", help="Project ID (routes to production/)")
    record_parser.add_argument("--tags", help="Comma-separated tags")
    record_parser.add_argument("--mma-score", type=float, help="MMA quality score")
    record_parser.add_argument("--source", help="Source project ID")
    record_parser.add_argument("--provenance", help="File ref (e.g. file.md#L42)")
    record_parser.add_argument("--agent", default="orchestrator", help="Creating agent")
    record_parser.add_argument("--json", action="store_true", help="Output as JSON")

    args = parser.parse_args()

    commands = {
        "init": cmd_init,
        "record": cmd_record,
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

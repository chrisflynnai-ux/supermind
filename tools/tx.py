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
import hashlib
import json
import math
import os
import re
import sqlite3
import sys
import time
import uuid
from datetime import datetime, timezone
from pathlib import Path
from dataclasses import dataclass, field
import xml.etree.ElementTree as ET

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
# SQLITE SCHEMA (Tier 2/3: The Edge Store)
# ============================================================

GRAPH_DB_PATH = THREADEX_DIR / "graph.db"

CREATE_EDGES_TABLE = """
CREATE TABLE IF NOT EXISTS edges (
    edge_id TEXT PRIMARY KEY,
    source_uri TEXT NOT NULL,
    target_uri TEXT NOT NULL,
    relation_type TEXT NOT NULL,
    weight REAL DEFAULT 1.0,
    utility_score REAL DEFAULT 1.0,
    last_traversed_at TEXT,
    origin_phase INTEGER DEFAULT 1,
    created_at TEXT DEFAULT (strftime('%Y-%m-%dT%H:%M:%SZ', 'now')),
    tags TEXT DEFAULT '[]'
);
"""

CREATE_EDGES_INDICES = """
CREATE INDEX IF NOT EXISTS idx_edges_source ON edges(source_uri);
CREATE INDEX IF NOT EXISTS idx_edges_target ON edges(target_uri);
CREATE INDEX IF NOT EXISTS idx_edges_rel_type ON edges(relation_type);
CREATE INDEX IF NOT EXISTS idx_edges_pru ON edges(utility_score, weight);
"""

CREATE_CONTENT_INDEX = """
CREATE VIRTUAL TABLE IF NOT EXISTS content_index USING fts5(
    record_id,
    domain,
    content,
    tags,
    tokenize='porter unicode61'
);
"""

DB_SCHEMA_VERSION = 1


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
# SKILLML REFACTOR SCHEMAS
# ============================================================

@dataclass
class SkillIdentity:
    skill_id: str
    name: str
    version: str
    tier: str = ""
    status: str = ""
    domain: str = ""
    track: str = ""
    model: str = ""
    neurobox_position: str = ""
    trigger_commands: list = field(default_factory=list)
    source_xml: str = ""

@dataclass
class SkillLayer:
    layer_id: str
    name: str = ""
    token_budget: int = 0
    load_priority: str = "always"
    content: str = ""
    frameworks: list = field(default_factory=list)

@dataclass
class SkillContract:
    inputs_required: list = field(default_factory=list)
    inputs_optional: list = field(default_factory=list)
    outputs_primary: list = field(default_factory=list)
    outputs_secondary: list = field(default_factory=list)
    quality_gates: dict = field(default_factory=dict)
    circuit_breakers: dict = field(default_factory=dict)

@dataclass
class SkillEdge:
    target_id: str
    relation: str = "DEPENDS_ON"
    priority: str = "medium"
    direction: str = "upstream"
    strength: float = 1.0

@dataclass
class RefactorResult:
    identity: SkillIdentity = None
    layers: list = field(default_factory=list)
    contract: SkillContract = None
    edges: list = field(default_factory=list)
    guardrails: list = field(default_factory=list)
    warnings: list = field(default_factory=list)
    markdown_path: str = ""
    records_created: int = 0
    edges_created: int = 0


# ============================================================
# DOMAIN ROUTING & KNOWN FRAMEWORKS
# ============================================================

DOMAIN_ROUTING = {
    "meta":        ("meta",        "strategist",  "offer_design"),
    "copy":        ("copy",        "writer",      "headlines"),
    "design":      ("design",      "designer",    "layout_patterns"),
    "research":    ("research",    "researcher",  "market_analysis"),
    "product":     ("product",     "strategist",  "offer_design"),
    "email":       ("email",       "writer",      "hooks"),
    "systems":     ("systems",     "_shared",     "frameworks"),
    "automations": ("automations", "_shared",     "frameworks"),
    "ads":         ("ads",         "writer",      "ctas"),
    "leadgen":     ("leadgen",     "strategist",  "funnel_architecture"),
}

KNOWN_FRAMEWORKS = [
    "AwarenessFramework", "BeliefLadder", "ValueEquationFramework",
    "FailureModePlaybook", "ReasoningFramework", "FastDecisionTree",
    "PowerTrioMapping", "MMAGateContract", "CircuitBreaker",
]


# ============================================================
# XML EXTRACTION HELPERS
# ============================================================

def _get_text(element, tag, default=""):
    """Safely find child element and return its .text or default."""
    child = element.find(tag)
    if child is not None and child.text:
        return child.text.strip()
    return default


def _get_all_text(element):
    """Recursively get ALL text content from element and children, stripping tags."""
    parts = []
    if element.text:
        parts.append(element.text.strip())
    for child in element:
        parts.append(_get_all_text(child))
        if child.tail:
            parts.append(child.tail.strip())
    return " ".join(p for p in parts if p).strip()


def _detect_frameworks(element):
    """Detect known frameworks within an element tree."""
    found = []
    for name in KNOWN_FRAMEWORKS:
        el = element.find(".//" + name)
        if el is not None:
            found.append({"name": name, "content": _get_all_text(el)})
    return found


# ============================================================
# XML EXTRACTION FUNCTIONS
# ============================================================

def _extract_identity(root, xml_path=""):
    """Extract SkillIdentity from root attributes and <Meta> children."""
    skill_id = root.get("skill_id", "")
    name = root.get("name", "")
    version = root.get("version", "")

    tier = ""
    status = ""
    model = ""
    domain = ""
    track = ""
    neurobox_position = ""
    trigger_commands = []

    meta = root.find("Meta")
    if meta is not None:
        tier = _get_text(meta, "Tier")
        status = _get_text(meta, "Status")
        model = _get_text(meta, "Model")
        domain = _get_text(meta, "Domain")
        track = _get_text(meta, "Track")
        nba = meta.find("NeuroBoxAlignment")
        if nba is not None:
            neurobox_position = _get_text(nba, "Position")
        tc = meta.find("TriggerCommands")
        if tc is not None and tc.text:
            trigger_commands = [cmd.strip() for cmd in tc.text.split(",") if cmd.strip()]

    return SkillIdentity(
        skill_id=skill_id,
        name=name,
        version=version,
        tier=tier,
        status=status,
        domain=domain,
        track=track,
        model=model,
        neurobox_position=neurobox_position,
        trigger_commands=trigger_commands,
        source_xml=str(xml_path),
    )


def _extract_layers(root):
    """Extract SkillLayer list using 3-strategy fallback."""
    layers = []

    # Strategy 1: Explicit L1, L2, L3, L4 tags
    for n in range(1, 5):
        tag = "L%d" % n
        el = root.find(tag)
        if el is not None:
            layers.append(SkillLayer(
                layer_id="L%d" % n,
                content=_get_all_text(el),
                frameworks=_detect_frameworks(el),
            ))

    if layers:
        return layers

    # Strategy 2: <ProgressiveDisclosure> -> <Layer> children
    pd = root.find("ProgressiveDisclosure")
    if pd is not None:
        for i, layer_el in enumerate(pd.findall("Layer"), start=1):
            layers.append(SkillLayer(
                layer_id=layer_el.get("id", "L%d" % i),
                name=layer_el.get("name", ""),
                content=_get_all_text(layer_el),
                frameworks=_detect_frameworks(layer_el),
            ))

    if layers:
        return layers

    # Strategy 3: Fallback -- use Contract as L1, ExecutionProtocol as L2, Guardrails as L3
    contract_el = root.find("Contract")
    if contract_el is not None:
        layers.append(SkillLayer(
            layer_id="L1",
            name="Contract",
            content=_get_all_text(contract_el),
            frameworks=_detect_frameworks(contract_el),
        ))
    exec_el = root.find("ExecutionProtocol")
    if exec_el is not None:
        layers.append(SkillLayer(
            layer_id="L2",
            name="ExecutionProtocol",
            content=_get_all_text(exec_el),
            frameworks=_detect_frameworks(exec_el),
        ))
    guard_el = root.find("Guardrails")
    if guard_el is not None:
        layers.append(SkillLayer(
            layer_id="L3",
            name="Guardrails",
            content=_get_all_text(guard_el),
            frameworks=_detect_frameworks(guard_el),
        ))

    return layers


def _extract_contract(root):
    """Extract SkillContract from <Contract> element."""
    contract_el = root.find("Contract")
    if contract_el is None:
        return SkillContract()

    def _extract_io_list(parent, section_tag, child_tag):
        result = []
        section = parent.find(section_tag)
        if section is not None:
            for el in section.findall(child_tag):
                result.append({
                    "name": _get_text(el, "Name"),
                    "format": el.get("format", ""),
                    "type": el.get("type", ""),
                    "description": _get_text(el, "Description"),
                })
        return result

    inputs_required = _extract_io_list(contract_el, "InputsRequired", "Input")
    inputs_optional = _extract_io_list(contract_el, "InputsOptional", "Input")
    outputs_primary = _extract_io_list(contract_el, "OutputsPrimary", "Output")
    outputs_secondary = _extract_io_list(contract_el, "OutputsSecondary", "Output")

    quality_gates = {}
    mma = contract_el.find(".//MMAGateContract")
    if mma is not None:
        for ms in mma.findall("MinScore"):
            track_name = ms.get("track", "")
            if track_name and ms.text:
                try:
                    quality_gates[track_name] = float(ms.text)
                except (ValueError, TypeError):
                    pass

    circuit_breakers = {}
    cb = contract_el.find(".//CircuitBreaker")
    if cb is not None:
        max_fix = _get_text(cb, "MaxFixLoops")
        if max_fix:
            circuit_breakers["max_fix_loops"] = max_fix
        on_exhausted = _get_text(cb, "OnExhausted")
        if on_exhausted:
            circuit_breakers["on_exhausted"] = on_exhausted

    return SkillContract(
        inputs_required=inputs_required,
        inputs_optional=inputs_optional,
        outputs_primary=outputs_primary,
        outputs_secondary=outputs_secondary,
        quality_gates=quality_gates,
        circuit_breakers=circuit_breakers,
    )


def _extract_dependencies(root):
    """Extract SkillEdge list from <Dependencies> and SSOT inputs."""
    edges = []

    deps = root.find("Dependencies")
    if deps is not None:
        upstream = deps.find("UpstreamDependencies")
        if upstream is not None:
            for skill_el in upstream.findall("Skill"):
                if skill_el.text and skill_el.text.strip():
                    edges.append(SkillEdge(
                        target_id=skill_el.text.strip(),
                        relation="DEPENDS_ON",
                        priority=skill_el.get("priority", "medium"),
                        direction="upstream",
                    ))

        downstream = deps.find("DownstreamConsumers")
        if downstream is not None:
            for skill_el in downstream.findall("Skill"):
                if skill_el.text and skill_el.text.strip():
                    edges.append(SkillEdge(
                        target_id=skill_el.text.strip(),
                        relation="COMPLEMENTS",
                        direction="downstream",
                    ))

    # Also derive SSOT dependencies from Contract inputs with type="ssot"
    contract_el = root.find("Contract")
    if contract_el is not None:
        ir = contract_el.find("InputsRequired")
        if ir is not None:
            for inp in ir.findall("Input"):
                if inp.get("type", "") == "ssot":
                    input_name = _get_text(inp, "Name")
                    if input_name:
                        edges.append(SkillEdge(
                            target_id="ssot://" + input_name,
                            relation="DEPENDS_ON",
                            priority="critical",
                        ))

    return edges


def _extract_guardrails(root):
    """Extract guardrails as list of strings from <Guardrails> or <Rules>."""
    guardrails_list = []

    gr = root.find("Guardrails")
    if gr is not None:
        for g_el in gr.findall("Guardrail"):
            rule = _get_text(g_el, "Rule")
            description = _get_text(g_el, "Description")
            if rule:
                if description:
                    guardrails_list.append("%s: %s" % (rule, description))
                else:
                    guardrails_list.append(rule)

    if guardrails_list:
        return guardrails_list

    # Fallback: try <Rules> -> <Rule>
    rules = root.find("Rules")
    if rules is not None:
        for r_el in rules.findall("Rule"):
            if r_el.text and r_el.text.strip():
                guardrails_list.append(r_el.text.strip())

    return guardrails_list


# ============================================================
# MAIN XML PARSING FUNCTION
# ============================================================

def parse_skill_xml(xml_path):
    """Parse a SkillML XML file and return a RefactorResult.

    Args:
        xml_path: Path to the XML file.

    Returns:
        RefactorResult with identity, layers, contract, edges, guardrails.

    Raises:
        ValueError: If critical fields (skill_id, name, version) are missing.
    """
    tree = ET.parse(str(xml_path))
    root = tree.getroot()

    identity = _extract_identity(root, xml_path)
    layers = _extract_layers(root)
    contract = _extract_contract(root)
    edges = _extract_dependencies(root)
    guardrails = _extract_guardrails(root)
    warnings = []

    # Validate critical fields
    if not identity.skill_id or not identity.name or not identity.version:
        missing = []
        if not identity.skill_id:
            missing.append("skill_id")
        if not identity.name:
            missing.append("name")
        if not identity.version:
            missing.append("version")
        raise ValueError("Missing critical identity fields: %s" % ", ".join(missing))

    # Warnings for missing important fields
    if not identity.domain:
        warnings.append("Missing domain -- defaulting to 'unknown'")
        identity.domain = "unknown"
    if not identity.track:
        warnings.append("Missing track")
    if not identity.tier:
        warnings.append("Missing tier")

    return RefactorResult(
        identity=identity,
        layers=layers,
        contract=contract,
        edges=edges,
        guardrails=guardrails,
        warnings=warnings,
    )




# ============================================================
# MASTERY DOCUMENT GENERATOR
# ============================================================

MASTERY_DIR = THREADEX_DIR / "mastery"


def _write_frontmatter(identity, mode, records=None):
    """Generate YAML frontmatter block for a mastery document.

    Uses simple string formatting (no PyYAML dependency).
    Returns the complete ``--- ... ---`` delimited string.
    """
    if records is None:
        records = []
    triggers_str = "[%s]" % ", ".join(identity.trigger_commands) if identity.trigger_commands else "[]"
    from datetime import datetime, timezone
    refactored_at = datetime.now(timezone.utc).isoformat()
    lines = [
        "---",
        "skill_id: %s" % identity.skill_id,
        "name: %s" % identity.name,
        "version: %s" % identity.version,
        "tier: %s" % (identity.tier or ""),
        "status: %s" % (identity.status or ""),
        "domain: %s" % (identity.domain or ""),
        "track: %s" % (identity.track or ""),
        "model: %s" % (identity.model or ""),
        "neurobox: %s" % (identity.neurobox_position or ""),
        "triggers: %s" % triggers_str,
        "source_xml: %s" % (identity.source_xml or ""),
        "mode: %s" % mode,
        "refactored_at: %s" % refactored_at,
        "threadex_records: %s" % ("[]" if not records else "[%s]" % ", ".join(str(r) for r in records)),
        "---",
    ]
    return "\n".join(lines) + "\n"


def generate_mastery_doc(result, mode="draft"):
    """Generate a full Markdown mastery document from a RefactorResult.

    Args:
        result: A RefactorResult dataclass instance.
        mode: One of ``"draft"``, ``"review"``, ``"final"``.

    Returns:
        A Markdown string ready to be written to disk.
    """
    parts = []
    identity = result.identity
    layers = result.layers or []
    contract = result.contract
    edges = result.edges or []
    guardrails = result.guardrails or []

    # --- Frontmatter ---
    parts.append(_write_frontmatter(identity, mode))

    # --- Title ---
    parts.append("# %s (v%s)\n" % (identity.name, identity.version))

    # --- Description (first line of L1 content) ---
    l1_layers = [l for l in layers if l.layer_id == "L1"]
    if l1_layers and l1_layers[0].content:
        first_line = l1_layers[0].content.split("\n")[0].strip()
        if first_line:
            parts.append("> %s\n" % first_line)

    # --- Layer sections ---
    layer_map = {l.layer_id: l for l in layers}
    all_layer_ids = ["L1", "L2", "L3", "L4"]
    for lid in all_layer_ids:
        if lid in layer_map:
            layer = layer_map[lid]
            header = "%s: %s" % (lid, layer.name) if layer.name else lid
            parts.append("## %s\n" % header)
            if layer.content:
                parts.append("%s\n" % layer.content.strip())
            if layer.frameworks:
                parts.append("### Frameworks\n")
                for fw in layer.frameworks:
                    fw_name = fw.get("name", "Unknown") if isinstance(fw, dict) else str(fw)
                    fw_content = fw.get("content", "") if isinstance(fw, dict) else ""
                    parts.append("**%s:** %s\n" % (fw_name, fw_content))
        else:
            parts.append("## %s: (missing)\n" % lid)
            parts.append("> _This layer was not present in the source XML. Add content during review._\n")

    # --- Contract ---
    parts.append("## Contract\n")
    if contract:
        # Required Inputs
        parts.append("### Required Inputs\n")
        if contract.inputs_required:
            for inp in contract.inputs_required:
                name = inp.get("name", "?")
                fmt = inp.get("format", "")
                desc = inp.get("description", "")
                parts.append("- **%s** (%s) \u2014 %s" % (name, fmt, desc))
            parts.append("")
        else:
            parts.append("(none extracted)\n")

        # Optional Inputs
        parts.append("### Optional Inputs\n")
        if contract.inputs_optional:
            for inp in contract.inputs_optional:
                name = inp.get("name", "?")
                fmt = inp.get("format", "")
                desc = inp.get("description", "")
                parts.append("- **%s** (%s) \u2014 %s" % (name, fmt, desc))
            parts.append("")
        else:
            parts.append("(none extracted)\n")

        # Primary Outputs
        parts.append("### Primary Outputs\n")
        if contract.outputs_primary:
            for out in contract.outputs_primary:
                name = out.get("name", "?")
                fmt = out.get("format", "")
                desc = out.get("description", "")
                parts.append("- **%s** (%s) \u2014 %s" % (name, fmt, desc))
            parts.append("")
        else:
            parts.append("(none extracted)\n")

        # Quality Gates
        parts.append("### Quality Gates\n")
        if contract.quality_gates:
            for gate_key, gate_val in contract.quality_gates.items():
                parts.append("- **%s:** %s" % (gate_key, gate_val))
            parts.append("")
        else:
            parts.append("(none extracted)\n")

        # Circuit Breakers
        parts.append("### Circuit Breakers\n")
        if contract.circuit_breakers:
            for cb_key, cb_val in contract.circuit_breakers.items():
                parts.append("- **%s:** %s" % (cb_key, cb_val))
            parts.append("")
        else:
            parts.append("(none extracted)\n")
    else:
        parts.append("(no contract extracted)\n")

    # --- Dependencies ---
    parts.append("## Dependencies\n")
    upstream = [e for e in edges if e.direction == "upstream"]
    downstream = [e for e in edges if e.direction == "downstream"]

    parts.append("### Upstream\n")
    if upstream:
        for e in upstream:
            parts.append("- `%s` \u2014 %s (%s, strength=%s)" % (e.target_id, e.relation, e.priority, e.strength))
        parts.append("")
    else:
        parts.append("(none extracted)\n")

    parts.append("### Downstream\n")
    if downstream:
        for e in downstream:
            parts.append("- `%s` \u2014 %s (%s, strength=%s)" % (e.target_id, e.relation, e.priority, e.strength))
        parts.append("")
    else:
        parts.append("(none extracted)\n")

    # --- Guardrails ---
    parts.append("## Guardrails\n")
    if guardrails:
        for i, g in enumerate(guardrails, 1):
            parts.append("%d. %s" % (i, g))
        parts.append("")
    else:
        parts.append("(none extracted)\n")

    # --- Graph Edges ---
    parts.append("## Graph Edges\n")
    if edges:
        parts.append("```yaml")
        parts.append("edges:")
        for e in edges:
            parts.append("  - target: %s" % e.target_id)
            parts.append("    rel: %s" % e.relation)
            parts.append("    priority: %s" % e.priority)
            parts.append("    strength: %s" % e.strength)
        parts.append("```\n")
    else:
        parts.append("(no edges extracted)\n")

    return "\n".join(parts)


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
# SQLITE DB INITIALIZATION
# ============================================================

def init_db(db_path=None):
    """Initialize or migrate the SQLite graph database.
    Creates edges table, indices, and FTS5 content_index.
    Safe to call multiple times (uses IF NOT EXISTS).
    """
    if db_path is None:
        db_path = GRAPH_DB_PATH
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(db_path))
    conn.execute("PRAGMA journal_mode=WAL")
    conn.execute("PRAGMA foreign_keys=ON")
    conn.execute(CREATE_EDGES_TABLE)
    for stmt in CREATE_EDGES_INDICES.strip().split(";"):
        stmt = stmt.strip()
        if stmt:
            conn.execute(stmt)
    try:
        conn.execute(CREATE_CONTENT_INDEX)
    except sqlite3.OperationalError as e:
        print(f"Warning: FTS5 not available ({e})", file=sys.stderr)
    conn.execute("CREATE TABLE IF NOT EXISTS meta (key TEXT PRIMARY KEY, value TEXT)")
    conn.execute("INSERT OR REPLACE INTO meta (key, value) VALUES ('schema_version', ?)",
                 (str(DB_SCHEMA_VERSION),))
    conn.commit()
    return conn


def get_db(db_path=None):
    """Get a connection to the graph database. Creates if not exists."""
    if db_path is None:
        db_path = GRAPH_DB_PATH
    if not db_path.exists():
        return init_db(db_path)
    conn = sqlite3.connect(str(db_path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn



# ============================================================
# EDGE SHREDDER & CONTENT INDEXING
# ============================================================


def make_edge_id(source_uri, target_uri, relation_type):
    """Create a deterministic edge ID from source+target+relation. Uses MD5 hash."""
    raw = f"{source_uri}|{target_uri}|{relation_type}"
    return hashlib.md5(raw.encode("utf-8")).hexdigest()


def shred_to_edges(record, source_uri=None):
    """Extract threadex_graph pointers from a JSONL record into edge dicts."""
    graph_pointers = record.get("threadex_graph", [])
    if not graph_pointers:
        return []
    if source_uri is None:
        domain = record.get("domain", "unknown")
        record_id = record.get("id", "unknown")
        source_uri = f"threadex://{domain}/{record_id}"
    edges = []
    for pointer in graph_pointers:
        if not isinstance(pointer, dict):
            continue
        target = pointer.get("target", "")
        rel = pointer.get("rel", "DEPENDS_ON")
        if not target:
            continue
        edge_id = make_edge_id(source_uri, target, rel)
        edges.append({
            "edge_id": edge_id,
            "source_uri": source_uri,
            "target_uri": target,
            "relation_type": rel,
            "weight": float(pointer.get("strength", 1.0)),
            "utility_score": float(record.get("utility_score", 0.5)),
            "origin_phase": int(pointer.get("phase", 1)),
            "tags": json.dumps(pointer.get("tags", []))
        })
    return edges


def insert_edges(conn, edges):
    """Batch insert/replace edges into SQLite."""
    if not edges:
        return 0
    count = 0
    for edge in edges:
        conn.execute("""
            INSERT OR REPLACE INTO edges
            (edge_id, source_uri, target_uri, relation_type, weight,
             utility_score, origin_phase, tags)
            VALUES (:edge_id, :source_uri, :target_uri, :relation_type,
                    :weight, :utility_score, :origin_phase, :tags)
        """, edge)
        count += 1
    conn.commit()
    return count


def index_record_content(conn, record):
    """Index a record's content into FTS5 for keyword search."""
    try:
        record_id = record.get("id", "")
        domain = record.get("domain", "")
        content = record.get("content", "")
        tags = ", ".join(record.get("tags", []))
        conn.execute("DELETE FROM content_index WHERE record_id = ?", (record_id,))
        conn.execute(
            "INSERT INTO content_index (record_id, domain, content, tags) VALUES (?, ?, ?, ?)",
            (record_id, domain, content, tags))
        conn.commit()
        return True
    except sqlite3.OperationalError:
        return False


# ============================================================
# PRU HUB SCORING
# ============================================================

def calculate_pru(conn, node_uri, alpha=None, lmbda=None):
    """Calculate PRU (Priority-Ranked Utility) score for a node."""
    if alpha is None:
        config = load_config()
        cfg_root = config.get("threadex", config)
        decay_cfg = cfg_root.get("decay", {})
        alpha = float(decay_cfg.get("alpha", 0.15)) if isinstance(decay_cfg, dict) else 0.15
    if lmbda is None:
        config = load_config()
        cfg_root = config.get("threadex", config)
        decay_cfg = cfg_root.get("decay", {})
        lmbda = float(decay_cfg.get("lambda_", 0.01)) if isinstance(decay_cfg, dict) else 0.01

    cursor = conn.execute("SELECT COUNT(*) FROM edges WHERE target_uri = ?", (node_uri,))
    degree = cursor.fetchone()[0]
    cursor = conn.execute("SELECT COUNT(*) FROM edges WHERE source_uri = ?", (node_uri,))
    out_degree = cursor.fetchone()[0]
    cursor = conn.execute(
        "SELECT AVG(utility_score), MAX(last_traversed_at) FROM edges WHERE target_uri = ?", (node_uri,))
    row = cursor.fetchone()
    avg_utility = row[0] if row[0] is not None else 0.5
    last_traversed = row[1]

    hours_since = 0.0
    if last_traversed:
        try:
            last_dt = datetime.fromisoformat(last_traversed.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            hours_since = (now - last_dt).total_seconds() / 3600.0
        except (ValueError, TypeError):
            hours_since = 0.0

    decay = math.exp(-lmbda * hours_since)
    pru_score = (alpha * degree) + ((1 - alpha) * avg_utility * decay)

    return {
        "uri": node_uri,
        "pru_score": round(pru_score, 4),
        "in_degree": degree,
        "out_degree": out_degree,
        "avg_utility": round(avg_utility, 4),
        "hours_since_last": round(hours_since, 1),
        "decay_factor": round(decay, 4),
    }


def get_all_nodes(conn):
    """Get all unique node URIs from the edges table."""
    nodes = set()
    for row in conn.execute("SELECT DISTINCT source_uri FROM edges"):
        nodes.add(row[0])
    for row in conn.execute("SELECT DISTINCT target_uri FROM edges"):
        nodes.add(row[0])
    return nodes




# ============================================================
# FTS5 SEARCH & FALLBACK
# ============================================================

def search_fts5(conn, query, domain=None, limit=20):
    """FTS5 full-text search on content_index. Returns list of result dicts or None if unavailable."""
    try:
        # Escape query for FTS5: wrap each term in double quotes for safe matching
        safe_terms = []
        for term in query.strip().split():
            # Remove any existing quotes and re-wrap
            clean = term.strip('"').strip("'")
            if clean:
                safe_terms.append(f'"{clean}"')
        if not safe_terms:
            return []
        fts_query = " ".join(safe_terms)

        if domain:
            rows = conn.execute(
                "SELECT record_id, domain, "
                "snippet(content_index, 2, '<b>', '</b>', '...', 32) as snippet, "
                "rank FROM content_index "
                "WHERE content_index MATCH ? AND domain = ? "
                "ORDER BY rank LIMIT ?",
                (fts_query, domain, limit)
            ).fetchall()
        else:
            rows = conn.execute(
                "SELECT record_id, domain, "
                "snippet(content_index, 2, '<b>', '</b>', '...', 32) as snippet, "
                "rank FROM content_index "
                "WHERE content_index MATCH ? "
                "ORDER BY rank LIMIT ?",
                (fts_query, limit)
            ).fetchall()

        results = []
        for row in rows:
            results.append({
                "record_id": row[0],
                "domain": row[1],
                "snippet": row[2],
                "rank": round(float(row[3]), 4),
            })
        return results

    except sqlite3.OperationalError:
        # FTS5 table missing or unavailable
        return None


def search_jsonl_fallback(query, domain=None, limit=20):
    """Case-insensitive substring scan of JSONL files. Fallback when FTS5 is unavailable."""
    results = []
    query_lower = query.lower()

    dirs_to_scan = []
    if domain:
        # Check both expertise and production for the domain
        exp_domain = EXPERTISE_DIR / domain
        if exp_domain.exists():
            dirs_to_scan.append(exp_domain)
        prod_domain = PRODUCTION_DIR / domain
        if prod_domain.exists():
            dirs_to_scan.append(prod_domain)
    else:
        # Scan all domains
        if EXPERTISE_DIR.exists():
            for d in EXPERTISE_DIR.iterdir():
                if d.is_dir():
                    dirs_to_scan.append(d)
        if PRODUCTION_DIR.exists():
            for d in PRODUCTION_DIR.iterdir():
                if d.is_dir():
                    dirs_to_scan.append(d)

    for dir_path in dirs_to_scan:
        for jsonl_file in dir_path.glob("*.jsonl"):
            records = read_jsonl(jsonl_file)
            for record in records:
                content_text = record.get("content", "")
                tags_text = " ".join(record.get("tags", []))
                searchable = f"{content_text} {tags_text}".lower()

                if query_lower in searchable:
                    snippet = content_text[:200]
                    if len(content_text) > 200:
                        snippet += "..."
                    results.append({
                        "record_id": record.get("id", "unknown"),
                        "domain": record.get("domain", dir_path.name),
                        "snippet": snippet,
                        "rank": 0,
                    })
                    if len(results) >= limit:
                        return results

    return results


def search_graph_context(conn, record_ids):
    """Enrich search results with edge counts from the graph.

    Returns dict mapping record_id -> {in_edges: int, out_edges: int}.
    """
    context = {}
    for rid in record_ids:
        uri_pattern = f"threadex://%/{rid}"
        try:
            in_count = conn.execute(
                "SELECT COUNT(*) FROM edges WHERE target_uri LIKE ?",
                (uri_pattern,)
            ).fetchone()[0]
            out_count = conn.execute(
                "SELECT COUNT(*) FROM edges WHERE source_uri LIKE ?",
                (uri_pattern,)
            ).fetchone()[0]
        except sqlite3.OperationalError:
            in_count = 0
            out_count = 0
        context[rid] = {"in_edges": in_count, "out_edges": out_count}
    return context

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


def filter_for_priming(records, max_recent=10):
    """Filter records into golden, recent, and guard buckets for context priming.

    Args:
        records: list of record dicts
        max_recent: max number of recent records to include

    Returns:
        dict with keys: golden, recent, guards
    """
    golden = []
    guards = []
    eligible = []

    for r in records:
        status = r.get("status", "observed")
        if status == "golden":
            golden.append(r)
        elif status == "forbidden":
            guards.append(r)
        elif status not in ("deprecated",):
            eligible.append(r)

    # Sort eligible by updated_at descending (newest first)
    eligible.sort(key=lambda r: r.get("updated_at", ""), reverse=True)
    recent = eligible[:max_recent]

    return {"golden": golden, "recent": recent, "guards": guards}


def _escape_xml(text):
    """Escape XML special characters in text content."""
    if not isinstance(text, str):
        text = str(text)
    text = text.replace("&", "&amp;")
    text = text.replace("<", "&lt;")
    text = text.replace(">", "&gt;")
    text = text.replace('"', "&quot;")
    text = text.replace("'", "&apos;")
    return text


def records_to_xml(filtered, domain):
    """Convert filtered records dict to ThreadexMemory XML string.

    Args:
        filtered: dict from filter_for_priming (golden, recent, guards)
        domain: domain name string

    Returns:
        str: XML string
    """
    now = datetime.now(timezone.utc).isoformat()
    golden = filtered.get("golden", [])
    recent = filtered.get("recent", [])
    guards = filtered.get("guards", [])

    lines = []
    lines.append(f'<ThreadexMemory domain="{_escape_xml(domain)}" primed_at="{now}">')

    # Golden patterns
    lines.append(f'  <GoldenPatterns count="{len(golden)}">')
    for r in golden:
        mma = r.get("mma_score")
        mma_attr = f' mma="{mma}"' if mma is not None else ""
        lines.append(f'    <Record id="{_escape_xml(r.get("id", ""))}" type="{_escape_xml(r.get("type", ""))}" status="golden"{mma_attr}>')
        lines.append(f'      <Content>{_escape_xml(r.get("content", ""))}</Content>')
        tags = r.get("tags", [])
        if tags:
            lines.append(f'      <Tags>{_escape_xml(", ".join(tags))}</Tags>')
        lines.append('    </Record>')
    lines.append('  </GoldenPatterns>')

    # Recent patterns
    lines.append(f'  <RecentPatterns count="{len(recent)}">')
    for r in recent:
        mma = r.get("mma_score")
        mma_attr = f' mma="{mma}"' if mma is not None else ""
        lines.append(f'    <Record id="{_escape_xml(r.get("id", ""))}" type="{_escape_xml(r.get("type", ""))}" status="{_escape_xml(r.get("status", ""))}"{mma_attr}>')
        lines.append(f'      <Content>{_escape_xml(r.get("content", ""))}</Content>')
        tags = r.get("tags", [])
        if tags:
            lines.append(f'      <Tags>{_escape_xml(", ".join(tags))}</Tags>')
        lines.append('    </Record>')
    lines.append('  </RecentPatterns>')

    # Guard patterns (only if non-empty)
    if guards:
        lines.append(f'  <GuardPatterns count="{len(guards)}">')
        for r in guards:
            mma = r.get("mma_score")
            mma_attr = f' mma="{mma}"' if mma is not None else ""
            lines.append(f'    <Record id="{_escape_xml(r.get("id", ""))}" type="{_escape_xml(r.get("type", ""))}" status="forbidden"{mma_attr}>')
            lines.append(f'      <Content>{_escape_xml(r.get("content", ""))}</Content>')
            tags = r.get("tags", [])
            if tags:
                lines.append(f'      <Tags>{_escape_xml(", ".join(tags))}</Tags>')
            lines.append('    </Record>')
        lines.append('  </GuardPatterns>')

    lines.append('</ThreadexMemory>')
    return "\n".join(lines)


def records_to_json(filtered, domain):
    """Convert filtered records dict to JSON string with domain and timestamp.

    Args:
        filtered: dict from filter_for_priming (golden, recent, guards)
        domain: domain name string

    Returns:
        str: JSON string
    """
    output = {
        "domain": domain,
        "primed_at": datetime.now(timezone.utc).isoformat(),
        "golden": filtered.get("golden", []),
        "recent": filtered.get("recent", []),
        "guards": filtered.get("guards", []),
    }
    return json.dumps(output, indent=2, default=str)


def records_to_text(filtered, domain):
    """Convert filtered records dict to plain text summary for terminal display.

    Args:
        filtered: dict from filter_for_priming (golden, recent, guards)
        domain: domain name string

    Returns:
        str: plain text summary
    """
    golden = filtered.get("golden", [])
    recent = filtered.get("recent", [])
    guards = filtered.get("guards", [])

    lines = []
    lines.append(f"=== Threadex Memory Prime: {domain} ===")
    lines.append(f"Primed at: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append("")

    lines.append(f"--- Golden Patterns ({len(golden)}) ---")
    for r in golden:
        mma = r.get("mma_score")
        mma_str = f" [MMA {mma}]" if mma is not None else ""
        lines.append(f"  [{r.get('type', '?')}]{mma_str} {r.get('content', '')}")
    if not golden:
        lines.append("  (none)")
    lines.append("")

    lines.append(f"--- Recent Patterns ({len(recent)}) ---")
    for r in recent:
        mma = r.get("mma_score")
        mma_str = f" [MMA {mma}]" if mma is not None else ""
        status = r.get("status", "?")
        lines.append(f"  [{r.get('type', '?')}] ({status}){mma_str} {r.get('content', '')}")
    if not recent:
        lines.append("  (none)")
    lines.append("")

    if guards:
        lines.append(f"--- Guard Patterns ({len(guards)}) ---")
        for r in guards:
            lines.append(f"  [FORBIDDEN] {r.get('content', '')}")
        lines.append("")

    total = len(golden) + len(recent) + len(guards)
    lines.append(f"Total records in prime: {total}")
    return "\n".join(lines)


def _slugify(name):
    """Convert a name to a URL-safe slug."""
    slug = name.lower()
    slug = slug.replace(" ", "-")
    slug = re.sub(r"[^a-z0-9\-]", "", slug)
    slug = re.sub(r"-{2,}", "-", slug)
    slug = slug.strip("-")
    return slug


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

    # Initialize SQLite graph database
    conn = init_db()
    conn.close()
    created_files += 1
    print(f"  Graph DB: {GRAPH_DB_PATH}")

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

    # Shred graph pointers into SQLite if --graph flag set
    if getattr(args, 'graph', False):
        try:
            conn = get_db()
            edges = shred_to_edges(record)
            edge_count = insert_edges(conn, edges)
            index_record_content(conn, record)
            conn.close()
            if not args.json and edge_count > 0:
                print(f"  Edges shredded: {edge_count}")
        except Exception as e:
            print(f"Warning: Edge shredding failed: {e}", file=sys.stderr)

    # Output
    if args.json:
        print(json.dumps(record, indent=2, default=str))
    else:
        print(record["id"])


def cmd_prime(args):
    """Output a memory context block (golden + recent patterns) for skill priming.

    Loads records from the specified domain, filters them through SIMS lifecycle
    rules, and outputs a formatted context block (XML, JSON, or text).
    """
    domain = args.domain

    # Determine base directory
    if args.project:
        base_dir = PRODUCTION_DIR / args.project
    else:
        base_dir = EXPERTISE_DIR / domain

    if not base_dir.exists():
        print(f"Error: Domain path not found: {base_dir}", file=sys.stderr)
        if not args.project:
            available = [d.name for d in EXPERTISE_DIR.iterdir() if d.is_dir()]
            print(f"  Available domains: {', '.join(available)}", file=sys.stderr)
        sys.exit(1)

    # Collect records
    all_records = []

    if args.subdomain:
        # Load only the specified subdomain file
        sd_file = base_dir / f"{args.subdomain}.jsonl"
        if not sd_file.exists():
            print(f"Error: Subdomain file not found: {sd_file}", file=sys.stderr)
            sys.exit(1)
        all_records.extend(read_jsonl(sd_file))
    else:
        # Load all JSONL files in the domain directory
        for f in sorted(base_dir.glob("*.jsonl")):
            all_records.extend(read_jsonl(f))

    # Load sibling domains if requested
    if args.siblings and not args.project:
        seed = SEED_DOMAINS.get(domain, {})
        siblings = seed.get("siblings", {})
        for role, sib_domain in siblings.items():
            sib_dir = EXPERTISE_DIR / sib_domain
            if sib_dir.exists():
                for f in sorted(sib_dir.glob("*.jsonl")):
                    all_records.extend(read_jsonl(f))

    # Filter
    filtered = filter_for_priming(all_records, max_recent=args.max_recent)

    # Remove guards unless --with-guards
    if not args.with_guards:
        filtered["guards"] = []

    # Format output
    fmt = args.format
    if fmt == "xml":
        output = records_to_xml(filtered, domain)
    elif fmt == "json":
        output = records_to_json(filtered, domain)
    elif fmt == "text":
        output = records_to_text(filtered, domain)
    else:
        output = records_to_xml(filtered, domain)

    print(output)


def cmd_contest(args):
    """Mark an existing record as contested."""
    target = args.target
    parts = target.split("/", 1)
    if len(parts) != 2:
        print("Error: target must be domain/subdomain", file=sys.stderr)
        sys.exit(1)
    domain, subdomain = parts

    if args.project:
        filepath = PRODUCTION_DIR / args.project / f"{subdomain}.jsonl"
        domain_path = PRODUCTION_DIR / args.project
    else:
        domain_path = EXPERTISE_DIR / domain
        filepath = domain_path / f"{subdomain}.jsonl"

    line_index, record = find_record_by_id(filepath, args.record_id)
    if record is None:
        print(f"Error: Record {args.record_id} not found in {filepath}", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc).isoformat()
    record["status"] = "contested"
    record["conflict_reason"] = args.reason
    record["updated_at"] = now

    if not update_record_in_file(filepath, line_index, record):
        print("Error: Failed to update record (file locked)", file=sys.stderr)
        sys.exit(1)

    if not args.project:
        update_index(domain_path)

    print(f"Contested: {args.record_id}")


def cmd_deprecate(args):
    """Mark an existing record as deprecated."""
    target = args.target
    parts = target.split("/", 1)
    if len(parts) != 2:
        print("Error: target must be domain/subdomain", file=sys.stderr)
        sys.exit(1)
    domain, subdomain = parts

    if args.project:
        filepath = PRODUCTION_DIR / args.project / f"{subdomain}.jsonl"
        domain_path = PRODUCTION_DIR / args.project
    else:
        domain_path = EXPERTISE_DIR / domain
        filepath = domain_path / f"{subdomain}.jsonl"

    line_index, record = find_record_by_id(filepath, args.record_id)
    if record is None:
        print(f"Error: Record {args.record_id} not found in {filepath}", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc).isoformat()
    record["status"] = "deprecated"
    record["deprecated_reason"] = args.reason
    if args.superseded_by:
        record["superseded_by"] = args.superseded_by
    record["updated_at"] = now

    if not update_record_in_file(filepath, line_index, record):
        print("Error: Failed to update record (file locked)", file=sys.stderr)
        sys.exit(1)

    if not args.project:
        update_index(domain_path)

    print(f"Deprecated: {args.record_id}")


def cmd_forbid(args):
    """Mark an existing record as forbidden."""
    target = args.target
    parts = target.split("/", 1)
    if len(parts) != 2:
        print("Error: target must be domain/subdomain", file=sys.stderr)
        sys.exit(1)
    domain, subdomain = parts

    if args.project:
        filepath = PRODUCTION_DIR / args.project / f"{subdomain}.jsonl"
        domain_path = PRODUCTION_DIR / args.project
    else:
        domain_path = EXPERTISE_DIR / domain
        filepath = domain_path / f"{subdomain}.jsonl"

    line_index, record = find_record_by_id(filepath, args.record_id)
    if record is None:
        print(f"Error: Record {args.record_id} not found in {filepath}", file=sys.stderr)
        sys.exit(1)

    now = datetime.now(timezone.utc).isoformat()
    record["status"] = "forbidden"
    record["conflict_reason"] = args.reason
    record["updated_at"] = now

    if not update_record_in_file(filepath, line_index, record):
        print("Error: Failed to update record (file locked)", file=sys.stderr)
        sys.exit(1)

    if not args.project:
        update_index(domain_path)

    print(f"Forbidden: {args.record_id}")


def cmd_decay(args):
    """Check/apply utility decay flags to records below threshold."""
    config = load_config()

    # Extract forbidden_threshold from config
    cfg_root = config.get("threadex", config)
    decay_cfg = cfg_root.get("decay", {})
    if isinstance(decay_cfg, dict) and "forbidden_threshold" in decay_cfg:
        threshold = float(decay_cfg.get("forbidden_threshold", 0.3))
    else:
        threshold = float(cfg_root.get("forbidden_threshold", 0.3))

    # Allow CLI override
    if args.threshold is not None:
        threshold = args.threshold

    if not EXPERTISE_DIR.exists():
        print("Error: .threadex/expertise/ not found. Run 'tx init' first.", file=sys.stderr)
        sys.exit(1)

    # Determine which domains to scan
    if args.domain:
        domain_dirs = [EXPERTISE_DIR / args.domain]
        if not domain_dirs[0].exists():
            print(f"Error: Domain '{args.domain}' not found in {EXPERTISE_DIR}", file=sys.stderr)
            sys.exit(1)
    else:
        domain_dirs = [d for d in sorted(EXPERTISE_DIR.iterdir()) if d.is_dir()]

    total_flagged = 0
    total_scanned = 0
    domains_scanned = 0

    for domain_path in domain_dirs:
        domain_name = domain_path.name
        domains_scanned += 1
        jsonl_files = sorted(domain_path.glob("*.jsonl"))

        for jsonl_file in jsonl_files:
            records = read_jsonl(jsonl_file)
            file_modified = False

            for line_idx, record in enumerate(records):
                total_scanned += 1
                utility = record.get("utility_score")
                if utility is None:
                    continue

                if utility < threshold:
                    tags = record.get("tags", [])
                    if not isinstance(tags, list):
                        tags = []
                    already_flagged = "_low_utility_flag" in tags

                    if args.check:
                        flag_marker = " (already flagged)" if already_flagged else ""
                        print(f"  [{domain_name}] {jsonl_file.stem}/{record.get('id', '?')[:8]}... "
                              f"utility={utility:.2f} < {threshold:.2f}{flag_marker}")
                        if not already_flagged:
                            total_flagged += 1
                    elif args.apply:
                        if not already_flagged:
                            tags.append("_low_utility_flag")
                            record["tags"] = tags
                            record["updated_at"] = datetime.now(timezone.utc).isoformat()
                            file_modified = True
                            total_flagged += 1
                            print(f"  Flagged: [{domain_name}] {jsonl_file.stem}/{record.get('id', '?')[:8]}... "
                                  f"utility={utility:.2f}")

            # Rewrite file if modified
            if args.apply and file_modified:
                if acquire_lock(jsonl_file):
                    try:
                        lines = [json.dumps(r, default=str) for r in records]
                        jsonl_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
                    finally:
                        release_lock(jsonl_file)
                else:
                    print(f"  Warning: Could not acquire lock for {jsonl_file}", file=sys.stderr)

    # Summary
    mode = "CHECK" if args.check else ("APPLY" if args.apply else "INFO")
    print(f"\nDecay {mode}: {total_flagged} records flagged | "
          f"{total_scanned} scanned | {domains_scanned} domains | threshold={threshold:.2f}")

    if not args.check and not args.apply:
        print("  Use --check for dry run or --apply to flag records.")


def cmd_compact(args):
    """Archive deprecated/forbidden records to a _compacted/ subdirectory."""
    target = args.target
    parts = target.split("/", 1)
    if len(parts) != 2:
        print("Error: target must be domain/subdomain (e.g. writer/headlines)", file=sys.stderr)
        sys.exit(1)

    domain, subdomain = parts[0], parts[1]

    # Resolve filepath
    if args.project:
        domain_path = PRODUCTION_DIR / args.project
        filepath = domain_path / f"{subdomain}.jsonl"
    else:
        domain_path = EXPERTISE_DIR / domain
        filepath = domain_path / f"{subdomain}.jsonl"

    if not filepath.exists():
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    # Read all records
    records = read_jsonl(filepath)
    if not records:
        print(f"No records in {filepath}")
        return

    # Separate active from archived
    active = []
    archived = []
    for r in records:
        status = r.get("status", "observed")
        if status in ("deprecated", "forbidden"):
            archived.append(r)
        else:
            active.append(r)

    if not archived:
        print(f"No deprecated/forbidden records to compact in {target}")
        return

    if args.dry_run:
        print(f"DRY RUN -- {target}:")
        print(f"  Total records:    {len(records)}")
        print(f"  Active (keep):    {len(active)}")
        print(f"  Archived (move):  {len(archived)}")
        for r in archived:
            print(f"    [{r.get('status')}] {r.get('id', '?')[:8]}... {r.get('content', '')[:60]}")
        return

    # Create _compacted/ subdirectory
    compacted_dir = domain_path / "_compacted"
    compacted_dir.mkdir(parents=True, exist_ok=True)

    # Write archived records to timestamped file
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    archive_file = compacted_dir / f"{subdomain}_{timestamp}.jsonl"
    archive_lines = [json.dumps(r, default=str) for r in archived]
    archive_file.write_text("\n".join(archive_lines) + "\n", encoding="utf-8")

    # Rewrite original file with only active records
    if acquire_lock(filepath):
        try:
            if active:
                active_lines = [json.dumps(r, default=str) for r in active]
                filepath.write_text("\n".join(active_lines) + "\n", encoding="utf-8")
            else:
                filepath.write_text("", encoding="utf-8")
        finally:
            release_lock(filepath)
    else:
        print("Error: Could not acquire lock for rewrite", file=sys.stderr)
        sys.exit(1)

    # Update index
    if not args.project:
        update_index(domain_path)

    print(f"Compacted {target}:")
    print(f"  Archived: {len(archived)} records -> {archive_file.name}")
    print(f"  Remaining: {len(active)} active records")


def cmd_status(args):
    """Show Threadex health summary across all domains and projects."""
    if not THREADEX_DIR.exists():
        print("Error: .threadex/ not found. Run 'tx init' first.", file=sys.stderr)
        sys.exit(1)

    print("=" * 60)
    print("THREADEX STATUS \u2014 v1.0")
    print("=" * 60)

    total_records = 0
    total_golden = 0
    total_forbidden = 0
    total_low_utility = 0

    # --- Expertise Domains ---
    print("EXPERTISE DOMAINS:")
    if EXPERTISE_DIR.exists():
        domain_dirs = sorted([d for d in EXPERTISE_DIR.iterdir() if d.is_dir()])
        if not domain_dirs:
            print("  (none)")
        else:
            # Collect data for alignment
            domain_rows = []
            for domain_path in domain_dirs:
                domain_name = domain_path.name
                # Skip _compacted dirs at domain level
                if domain_name == "_compacted":
                    continue

                # Count subdomains: JSONL files in domain
                jsonl_files = sorted(domain_path.glob("*.jsonl"))
                subdomain_count = len(jsonl_files)

                domain_records = 0
                domain_golden = 0
                domain_forbidden = 0
                domain_low_utility = 0

                for jsonl_file in jsonl_files:
                    records = read_jsonl(jsonl_file)
                    domain_records += len(records)
                    for r in records:
                        if r.get("status") == "golden":
                            domain_golden += 1
                        if r.get("status") == "forbidden":
                            domain_forbidden += 1
                        tags = r.get("tags", [])
                        if isinstance(tags, list) and "_low_utility_flag" in tags:
                            domain_low_utility += 1

                total_records += domain_records
                total_golden += domain_golden
                total_forbidden += domain_forbidden
                total_low_utility += domain_low_utility

                domain_rows.append((
                    domain_name, subdomain_count, domain_records,
                    domain_golden, domain_forbidden
                ))

            # Find max widths for alignment
            max_name = max(len(r[0]) for r in domain_rows) if domain_rows else 12
            for name, subs, recs, gold, forb in domain_rows:
                print(f"  {name:<{max_name}}  {subs} subdomains  "
                      f"{recs:>4} records  {gold:>3} golden  {forb:>3} forbidden")
    else:
        print("  (not initialized)")

    print()

    # --- Production Projects ---
    print("PRODUCTION PROJECTS:")
    if PRODUCTION_DIR.exists():
        project_dirs = sorted([
            d for d in PRODUCTION_DIR.iterdir()
            if d.is_dir() and d.name not in ("_archive", "_compacted")
        ])
        if not project_dirs:
            print("  (none)")
        else:
            for proj_dir in project_dirs:
                manifest = proj_dir / "_manifest.yaml"
                if manifest.exists():
                    try:
                        mdata = _load_yaml(manifest)
                        status = mdata.get("status", "unknown")
                        print(f"  {proj_dir.name}  status={status}")
                    except Exception:
                        print(f"  {proj_dir.name}  (manifest unreadable)")
                else:
                    jsonl_count = len(list(proj_dir.glob("*.jsonl")))
                    print(f"  {proj_dir.name}  {jsonl_count} files")
    else:
        print("  (not initialized)")

    print()

    # --- Health Summary ---
    print(f"HEALTH: {total_records} total records | {total_golden} golden | "
          f"{total_forbidden} forbidden | {total_low_utility} low-utility")
    print("=" * 60)


def cmd_project_dispatch(args):
    """Dispatch project sub-commands."""
    if args.project_command == "create":
        cmd_project_create(args)
    else:
        print(f"Unknown project command: {args.project_command}")
        sys.exit(1)


def cmd_project_create(args):
    """Create a new production project scaffold."""
    project_id = _slugify(args.name)
    if not project_id:
        print("ERROR: Project name produces empty slug")
        sys.exit(1)

    project_dir = PRODUCTION_DIR / project_id
    if project_dir.exists():
        print(f"ERROR: Project '{project_id}' already exists at {project_dir}")
        sys.exit(1)

    # Create project directory and track subdirectories
    project_dir.mkdir(parents=True, exist_ok=True)
    for track in ["t1", "t2", "t3", "t4"]:
        (project_dir / track).mkdir(exist_ok=True)

    # Parse team
    team = []
    if args.team:
        team = [t.strip() for t in args.team.split(",") if t.strip()]

    # Build manifest
    now = datetime.now(timezone.utc).isoformat()
    manifest = {
        "project_id": project_id,
        "project_name": args.name,
        "created_at": now,
        "status": "active",
        "team": team,
        "tracks": {
            "t1": {"status": "active", "records": 0},
            "t2": {"status": "pending", "records": 0},
            "t3": {"status": "pending", "records": 0},
            "t4": {"status": "pending", "records": 0},
        },
    }

    manifest_path = project_dir / "_manifest.yaml"
    _write_yaml(manifest, manifest_path)

    # Create empty evals.jsonl
    evals_path = project_dir / "evals.jsonl"
    evals_path.write_text("", encoding="utf-8")

    print(f"Project '{project_id}' created at {project_dir}")
    print(f"  Tracks: t1/ t2/ t3/ t4/")
    print(f"  Manifest: _manifest.yaml")
    print(f"  Evals: evals.jsonl")
    if team:
        print(f"  Team: {', '.join(team)}")


def cmd_handoff(args):
    """Create a track handoff record in a project."""
    project_dir = PRODUCTION_DIR / args.project_id
    if not project_dir.exists():
        print(f"ERROR: Project '{args.project_id}' not found at {project_dir}")
        sys.exit(1)

    handoff_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()

    handoff = {
        "handoff_id": handoff_id,
        "project_id": args.project_id,
        "from_track": args.from_track,
        "to_track": args.to_track,
        "created_at": now,
        "created_by": args.agent,
        "status": "pending",
        "deliverables": [],
        "acceptance_criteria": [],
        "notes": "",
        "blockers": [],
    }

    filename = f"handoff_{args.from_track}_{args.to_track}.yaml"
    handoff_path = project_dir / filename
    _write_yaml(handoff, handoff_path)

    print(f"Handoff created: {filename}")
    print(f"  {args.from_track} -> {args.to_track}")
    print(f"  ID: {handoff_id}")
    print(f"  Agent: {args.agent}")


def cmd_postmortem(args):
    """Create a project postmortem template."""
    project_dir = PRODUCTION_DIR / args.project_id
    if not project_dir.exists():
        print(f"ERROR: Project '{args.project_id}' not found at {project_dir}")
        sys.exit(1)

    postmortem_id = str(uuid.uuid4())
    now = datetime.now(timezone.utc).isoformat()

    postmortem = {
        "postmortem_id": postmortem_id,
        "project_id": args.project_id,
        "created_at": now,
        "created_by": args.agent,
        "status": "draft",
        "duration_days": 0,
        "tracks_completed": {
            "t1": False,
            "t2": False,
            "t3": False,
            "t4": False,
        },
        "wins": [],
        "failures": [],
        "lessons_learned": [],
        "patterns_to_promote": [],
        "patterns_to_deprecate": [],
        "next_actions": [],
    }

    postmortem_path = project_dir / "_postmortem.yaml"
    _write_yaml(postmortem, postmortem_path)

    print(f"Postmortem template created: _postmortem.yaml")
    print(f"  Project: {args.project_id}")
    print(f"  ID: {postmortem_id}")
    print(f"  Agent: {args.agent}")


# ============================================================
# MAIN ENTRY POINT
# ============================================================


# ============================================================
# DB COMMANDS
# ============================================================

def cmd_db_dispatch(args):
    """Dispatch db sub-commands."""
    if args.db_command == "init":
        cmd_db_init(args)
    else:
        print(f"Unknown db command: {args.db_command}")
        sys.exit(1)


def cmd_db_init(args):
    """Initialize or reset the graph database."""
    if getattr(args, 'reset', False) and GRAPH_DB_PATH.exists():
        GRAPH_DB_PATH.unlink()
        print(f"Deleted existing graph.db")
    conn = init_db()
    cursor = conn.execute("SELECT COUNT(*) FROM edges")
    edge_count = cursor.fetchone()[0]
    try:
        conn.execute("SELECT COUNT(*) FROM content_index")
        fts5_status = "available"
    except sqlite3.OperationalError:
        fts5_status = "not available"
    conn.close()
    print(f"Graph DB initialized: {GRAPH_DB_PATH}")
    print(f"  Edges: {edge_count}")
    print(f"  FTS5: {fts5_status}")
    print(f"  WAL mode: enabled")



# ============================================================
# GRAPH COMMANDS
# ============================================================


def cmd_graph_dispatch(args):
    """Dispatch graph sub-commands."""
    dispatch = {
        "sync": cmd_graph_sync,
        "neighbors": cmd_graph_neighbors,
        "broken": cmd_graph_broken,
    }
    handler = dispatch.get(args.graph_command)
    if handler:
        handler(args)
    else:
        print(f"Unknown graph command: {args.graph_command}")
        sys.exit(1)


def cmd_graph_sync(args):
    """Rebuild SQLite edges + content index from all JSONL records."""
    conn = get_db()

    # Clear existing data for clean rebuild
    conn.execute("DELETE FROM edges")
    try:
        conn.execute("DELETE FROM content_index")
    except sqlite3.OperationalError:
        pass
    conn.commit()

    total_records = 0
    total_edges = 0
    total_indexed = 0
    sources = []

    # Collect JSONL sources
    if getattr(args, 'domain', None):
        domain_path = EXPERTISE_DIR / args.domain
        if domain_path.exists():
            sources.extend(sorted(domain_path.glob("*.jsonl")))
    elif getattr(args, 'project', None):
        project_path = PRODUCTION_DIR / args.project
        if project_path.exists():
            sources.extend(sorted(project_path.glob("**/*.jsonl")))
    else:
        # All expertise domains
        if EXPERTISE_DIR.exists():
            for domain_dir in sorted(EXPERTISE_DIR.iterdir()):
                if domain_dir.is_dir():
                    sources.extend(sorted(domain_dir.glob("*.jsonl")))
        # All production projects
        if PRODUCTION_DIR.exists():
            for proj_dir in sorted(PRODUCTION_DIR.iterdir()):
                if proj_dir.is_dir() and proj_dir.name not in ("_archive", "_compacted"):
                    sources.extend(sorted(proj_dir.glob("**/*.jsonl")))

    for jsonl_file in sources:
        records = read_jsonl(jsonl_file)
        for record in records:
            total_records += 1
            edges = shred_to_edges(record)
            if edges:
                total_edges += insert_edges(conn, edges)
            if index_record_content(conn, record):
                total_indexed += 1

    conn.close()

    print(f"Graph sync complete:")
    print(f"  Records scanned: {total_records}")
    print(f"  Edges shredded:  {total_edges}")
    print(f"  Content indexed: {total_indexed}")
    print(f"  Sources: {len(sources)} JSONL files")


def cmd_graph_neighbors(args):
    """Show incoming and outgoing edges for a node URI."""
    conn = get_db()
    uri = args.uri

    # Incoming edges (where this node is the target)
    incoming = conn.execute(
        "SELECT source_uri, relation_type, weight, utility_score FROM edges WHERE target_uri = ? ORDER BY weight DESC",
        (uri,)
    ).fetchall()

    # Outgoing edges (where this node is the source)
    outgoing = conn.execute(
        "SELECT target_uri, relation_type, weight, utility_score FROM edges WHERE source_uri = ? ORDER BY weight DESC",
        (uri,)
    ).fetchall()

    if not incoming and not outgoing:
        print(f"No edges found for: {uri}")
        conn.close()
        return

    if getattr(args, 'json', False):
        result = {
            "uri": uri,
            "incoming": [dict(r) for r in incoming],
            "outgoing": [dict(r) for r in outgoing],
        }
        print(json.dumps(result, indent=2, default=str))
    else:
        print(f"Node: {uri}")
        print(f"\n  INCOMING ({len(incoming)}):")
        if incoming:
            for r in incoming:
                print(f"    <- [{r['relation_type']}] {r['source_uri']}  "
                      f"(weight={r['weight']:.2f}, utility={r['utility_score']:.2f})")
        else:
            print(f"    (none)")
        print(f"\n  OUTGOING ({len(outgoing)}):")
        if outgoing:
            for r in outgoing:
                print(f"    -> [{r['relation_type']}] {r['target_uri']}  "
                      f"(weight={r['weight']:.2f}, utility={r['utility_score']:.2f})")
        else:
            print(f"    (none)")

    # Update last_traversed_at for all edges involving this node
    now = datetime.now(timezone.utc).isoformat()
    conn.execute("UPDATE edges SET last_traversed_at = ? WHERE target_uri = ? OR source_uri = ?",
                 (now, uri, uri))
    conn.commit()
    conn.close()


def cmd_graph_broken(args):
    """Detect broken edges -- targets that don't exist as sources anywhere."""
    conn = get_db()

    broken = conn.execute("""
        SELECT DISTINCT e1.target_uri, e1.relation_type, e1.source_uri
        FROM edges e1
        LEFT JOIN edges e2 ON e1.target_uri = e2.source_uri
        WHERE e2.source_uri IS NULL
        ORDER BY e1.target_uri
    """).fetchall()

    if not broken:
        print("No broken edges detected. All targets have outgoing edges.")
        conn.close()
        return

    # Group by target
    by_target = {}
    for row in broken:
        target = row[0]
        if target not in by_target:
            by_target[target] = []
        by_target[target].append({"rel": row[1], "source": row[2]})

    if getattr(args, 'json', False):
        print(json.dumps(by_target, indent=2))
    else:
        print(f"BROKEN EDGES: {len(by_target)} orphan targets")
        print(f"{'='*60}")
        for target, refs in by_target.items():
            print(f"\n  Target: {target}")
            for ref in refs:
                print(f"    Referenced by: {ref['source']} [{ref['rel']}]")
        print(f"\n{'='*60}")
        print(f"Total: {len(by_target)} orphan targets, {len(broken)} broken edges")

    conn.close()

def cmd_hubs(args):
    """Show top-N hub nodes ranked by PRU score."""
    conn = get_db()
    nodes = get_all_nodes(conn)

    if not nodes:
        print("No nodes in graph. Run 'tx graph sync' first.")
        conn.close()
        return

    scored = []
    for uri in nodes:
        result = calculate_pru(conn, uri)
        scored.append(result)

    scored.sort(key=lambda x: x["pru_score"], reverse=True)

    top_n = getattr(args, 'top', 10) or 10
    scored = scored[:top_n]

    if getattr(args, 'json', False):
        print(json.dumps(scored, indent=2))
    else:
        print(f"{'='*60}")
        print(f"TOP {len(scored)} HUBS BY PRU SCORE")
        print(f"{'='*60}")
        print(f"{'#':>3}  {'PRU':>7}  {'In':>3}  {'Out':>3}  {'Util':>5}  URI")
        print(f"{chr(0x2500)*3}  {chr(0x2500)*7}  {chr(0x2500)*3}  {chr(0x2500)*3}  {chr(0x2500)*5}  {chr(0x2500)*30}")
        for i, h in enumerate(scored, 1):
            print(f"{i:>3}  {h['pru_score']:>7.4f}  {h['in_degree']:>3}  "
                  f"{h['out_degree']:>3}  {h['avg_utility']:>5.2f}  {h['uri']}")
        print(f"{'='*60}")

    conn.close()


def cmd_search(args):
    """Search memory records by keyword with optional graph context."""
    query = args.query
    domain = getattr(args, 'domain', None)
    limit = getattr(args, 'limit', 20) or 20
    with_graph = getattr(args, 'with_graph', False)
    as_json = getattr(args, 'json', False)

    # Try FTS5 first
    conn = get_db()
    results = search_fts5(conn, query, domain=domain, limit=limit)
    search_method = "FTS5"

    # Fallback to JSONL scan if FTS5 unavailable
    if results is None:
        search_method = "JSONL"
        results = search_jsonl_fallback(query, domain=domain, limit=limit)

    if not results:
        if as_json:
            print(json.dumps({"results": [], "method": search_method, "query": query}, indent=2))
        else:
            print(f"No results for '{query}' (via {search_method})")
        conn.close()
        return

    # Enrich with graph context if requested
    graph_ctx = {}
    if with_graph:
        record_ids = [r["record_id"] for r in results]
        graph_ctx = search_graph_context(conn, record_ids)
        for r in results:
            ctx = graph_ctx.get(r["record_id"], {"in_edges": 0, "out_edges": 0})
            r["in_edges"] = ctx["in_edges"]
            r["out_edges"] = ctx["out_edges"]

    conn.close()

    if as_json:
        print(json.dumps({
            "results": results,
            "method": search_method,
            "query": query,
            "count": len(results),
        }, indent=2))
    else:
        print(f"{'='*70}")
        print(f"SEARCH: '{query}' -- {len(results)} results (via {search_method})")
        print(f"{'='*70}")

        # Build header
        hdr = f"{'#':>3}  {'ID':8}  {'Domain':12}  {'Rank':>7}  "
        sep = f"{'---'}  {'--------'}  {'------------'}  {'-------'}  "
        if with_graph:
            hdr += f"{'In':>3}  {'Out':>3}  "
            sep += f"{'---'}  {'---'}  "
        hdr += "Snippet"
        sep += '-' * 30

        print(hdr)
        print(sep)

        for i, r in enumerate(results, 1):
            rid = r["record_id"][:8]
            dom = r["domain"][:12]
            rank = f"{r['rank']:>7.4f}"
            snip = r["snippet"][:50].replace("\n", " ")
            if len(r["snippet"]) > 50:
                snip += "..."

            line = f"{i:>3}  {rid:8}  {dom:12}  {rank}  "
            if with_graph:
                line += f"{r.get('in_edges', 0):>3}  {r.get('out_edges', 0):>3}  "
            line += snip
            print(line)

        print(f"{'='*70}")



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
    record_parser.add_argument("--graph", action="store_true",
                               help="Shred threadex_graph pointers into SQLite edges")

    # prime
    prime_parser = subparsers.add_parser("prime", help="Output memory context block")
    prime_parser.add_argument("domain", help="Domain to prime (e.g. writer)")
    prime_parser.add_argument("--subdomain", help="Specific subdomain")
    prime_parser.add_argument("--project", help="Project ID for production memory")
    prime_parser.add_argument("--all", action="store_true", help="All sub-domains")
    prime_parser.add_argument("--siblings", action="store_true", help="Include sibling domains")
    prime_parser.add_argument("--with-guards", action="store_true", help="Include forbidden patterns")
    prime_parser.add_argument("--max-recent", type=int, default=10)
    prime_parser.add_argument("--format", choices=["xml", "json", "text"], default="xml")

    # contest
    contest_parser = subparsers.add_parser("contest", help="Mark record as contested")
    contest_parser.add_argument("target", help="domain/subdomain (e.g. writer/headlines)")
    contest_parser.add_argument("--record-id", required=True, help="Record UUID to contest")
    contest_parser.add_argument("--reason", required=True, help="Why this record is contested")
    contest_parser.add_argument("--project", help="Project ID (routes to production/)")

    # deprecate
    deprecate_parser = subparsers.add_parser("deprecate", help="Mark record as deprecated")
    deprecate_parser.add_argument("target", help="domain/subdomain (e.g. writer/headlines)")
    deprecate_parser.add_argument("--record-id", required=True, help="Record UUID to deprecate")
    deprecate_parser.add_argument("--reason", required=True, help="Why this record is deprecated")
    deprecate_parser.add_argument("--superseded-by", help="ID of replacement record")
    deprecate_parser.add_argument("--project", help="Project ID (routes to production/)")

    # forbid
    forbid_parser = subparsers.add_parser("forbid", help="Mark record as forbidden")
    forbid_parser.add_argument("target", help="domain/subdomain (e.g. writer/headlines)")
    forbid_parser.add_argument("--record-id", required=True, help="Record UUID to forbid")
    forbid_parser.add_argument("--reason", required=True, help="Why this record is forbidden")
    forbid_parser.add_argument("--project", help="Project ID (routes to production/)")

    # decay
    decay_parser = subparsers.add_parser("decay", help="Check/apply utility decay flags")
    decay_parser.add_argument("--domain", help="Specific domain to scan")
    decay_parser.add_argument("--check", action="store_true", help="Dry-run: show flagged records")
    decay_parser.add_argument("--apply", action="store_true", help="Apply _low_utility_flag to records")
    decay_parser.add_argument("--threshold", type=float, help="Override forbidden_threshold")

    # compact
    compact_parser = subparsers.add_parser("compact", help="Archive deprecated/forbidden records")
    compact_parser.add_argument("target", help="domain/subdomain (e.g. writer/headlines)")
    compact_parser.add_argument("--dry-run", action="store_true", help="Show what would be compacted")
    compact_parser.add_argument("--project", help="Project ID (routes to production/)")

    # status
    status_parser = subparsers.add_parser("status", help="Show Threadex health summary")

    # db
    db_parser = subparsers.add_parser("db", help="Database management")
    db_sub = db_parser.add_subparsers(dest="db_command", required=True)
    db_init_parser = db_sub.add_parser("init", help="Initialize/reset graph database")
    db_init_parser.add_argument("--reset", action="store_true", help="Drop and recreate all tables")

    # graph
    graph_parser = subparsers.add_parser("graph", help="Graph operations")
    graph_sub = graph_parser.add_subparsers(dest="graph_command", required=True)
    sync_parser = graph_sub.add_parser("sync", help="Rebuild edges from all JSONL records")
    sync_parser.add_argument("--domain", help="Sync specific domain only")
    sync_parser.add_argument("--project", help="Sync specific project only")

    neighbors_parser = graph_sub.add_parser("neighbors", help="Show edges for a node")
    neighbors_parser.add_argument("uri", help="Node URI to inspect")
    neighbors_parser.add_argument("--json", action="store_true", help="Output as JSON")

    broken_parser = graph_sub.add_parser("broken", help="Detect broken/orphan edges")
    broken_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # hubs
    hubs_parser = subparsers.add_parser("hubs", help="Show top hub nodes by PRU score")
    hubs_parser.add_argument("--top", type=int, default=10, help="Number of top hubs (default: 10)")
    hubs_parser.add_argument("--json", action="store_true", help="Output as JSON")


    # search
    search_parser = subparsers.add_parser("search", help="Search memory records by keyword")
    search_parser.add_argument("query", help="Search query (keywords)")
    search_parser.add_argument("--domain", help="Filter to specific domain")
    search_parser.add_argument("--limit", type=int, default=20, help="Max results (default: 20)")
    search_parser.add_argument("--with-graph", action="store_true", help="Include graph edge counts")
    search_parser.add_argument("--json", action="store_true", help="Output as JSON")

    # project
    project_parser = subparsers.add_parser("project", help="Production project management")
    project_sub = project_parser.add_subparsers(dest="project_command", required=True)
    create_parser = project_sub.add_parser("create", help="Create a new project scaffold")
    create_parser.add_argument("name", help="Project name (will be slugified)")
    create_parser.add_argument("--team", help="Comma-separated team domains (e.g. writer,researcher)")

    # handoff
    handoff_parser = subparsers.add_parser("handoff", help="Create a track handoff record")
    handoff_parser.add_argument("project_id", help="Project ID")
    handoff_parser.add_argument("from_track", help="Source track (e.g. t1)")
    handoff_parser.add_argument("to_track", help="Target track (e.g. t2)")
    handoff_parser.add_argument("--agent", default="orchestrator", help="Creating agent")

    # postmortem
    postmortem_parser = subparsers.add_parser("postmortem", help="Create project postmortem template")
    postmortem_parser.add_argument("project_id", help="Project ID")
    postmortem_parser.add_argument("--agent", default="orchestrator", help="Creating agent")

    args = parser.parse_args()

    commands = {
        "init": cmd_init,
        "record": cmd_record,
        "prime": cmd_prime,
        "contest": cmd_contest,
        "deprecate": cmd_deprecate,
        "forbid": cmd_forbid,
        "decay": cmd_decay,
        "compact": cmd_compact,
        "status": cmd_status,
        "db": cmd_db_dispatch,
        "graph": cmd_graph_dispatch,
        "hubs": cmd_hubs,
        "search": cmd_search,
        "project": cmd_project_dispatch,
        "handoff": cmd_handoff,
        "postmortem": cmd_postmortem,
    }

    handler = commands.get(args.command)
    if handler:
        handler(args)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Validate automations_master_architect_v4_0_0.xml against design requirements."""
import xml.etree.ElementTree as ET
import sys
from pathlib import Path

def validate_maa(xml_path: str) -> list[str]:
    """Validate MAA XML against design requirements. Returns list of errors."""
    errors = []

    # 1. Parse XML
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
    except ET.ParseError as e:
        return [f"XML PARSE ERROR: {e}"]
    except FileNotFoundError:
        return [f"FILE NOT FOUND: {xml_path}"]

    # 2. Check root element
    if root.tag != "Skill":
        errors.append(f"Root element must be 'Skill', got '{root.tag}'")

    # 3. Check required root attributes
    for attr in ["skill_id", "name", "version", "tier", "status", "model"]:
        if attr not in root.attrib:
            errors.append(f"Missing root attribute: {attr}")

    # 4. Check required top-level sections
    required_sections = [
        "Meta", "Doctrine", "Purpose", "Identity", "Scope",
        "SSOT", "Dependencies", "ProgressiveDisclosure",
        "Contracts", "RelationalOps", "HCTSLibrary",
        "MMAIntegration", "MasterPrompt", "VersionHistory"
    ]
    for section in required_sections:
        if root.find(section) is None:
            errors.append(f"Missing required section: <{section}>")

    # 5. Check Progressive Disclosure layers
    pd = root.find("ProgressiveDisclosure")
    if pd is not None:
        layers = pd.findall("Layer")
        layer_ids = [l.get("id") for l in layers]
        for required_layer in ["L1", "L2", "L3", "L4"]:
            if required_layer not in layer_ids:
                errors.append(f"Missing Progressive Disclosure layer: {required_layer}")

    # 6. Check required contracts
    contracts = root.find("Contracts")
    if contracts is not None:
        contract_names = [c.get("name") for c in contracts.findall("Contract")]
        required_contracts = [
            "AUTOMATION_BLUEPRINT", "FLOWGRAM_SPEC", "HANDOFF_PACKAGE",
            "PATCH_REQUEST", "MEMORY_SEAM_NOTE", "LEARNING_ARTIFACT"
        ]
        for rc in required_contracts:
            if rc not in contract_names:
                errors.append(f"Missing required contract: {rc}")

        # Check future seams
        seam_names = [s.get("name") for s in contracts.findall("Seam")]
        for rs in ["ACP_MESSAGE", "SKILL_EVAL_REQUEST"]:
            if rs not in seam_names:
                errors.append(f"Missing required future seam: {rs}")

    # 7. Check relational ops
    rel_ops = root.find("RelationalOps")
    if rel_ops is not None:
        for rel_type in ["DelegatesTo", "DependsOn", "Complements", "Reviews"]:
            if rel_ops.find(rel_type) is None:
                errors.append(f"Missing relational op: <{rel_type}>")

    # 8. Check heuristics count
    pd = root.find("ProgressiveDisclosure")
    if pd is not None:
        l2 = None
        for layer in pd.findall("Layer"):
            if layer.get("id") == "L2":
                l2 = layer
                break
        if l2 is not None:
            heuristics = l2.find("Heuristics")
            if heuristics is not None:
                h_count = len(heuristics.findall("Heuristic"))
                if h_count < 12:
                    errors.append(f"Need 12 heuristics, found {h_count}")

            anti_patterns = l2.find("AntiPatterns")
            if anti_patterns is not None:
                ap_count = len(anti_patterns.findall("AntiPattern"))
                if ap_count < 10:
                    errors.append(f"Need 10 anti-patterns, found {ap_count}")

    # 9. Check MMA integration
    mma = root.find("MMAIntegration")
    if mma is not None:
        dims = mma.find("QualityDimensions")
        if dims is not None:
            d_count = len(dims.findall("Dimension"))
            if d_count < 7:
                errors.append(f"Need 7+ MMA dimensions, found {d_count}")

    # 10. Check memory seams
    if pd is not None:
        l4 = None
        for layer in pd.findall("Layer"):
            if layer.get("id") == "L4":
                l4 = layer
                break
        if l4 is not None:
            mem = l4.find("MemorySeams")
            if mem is None:
                errors.append("Missing <MemorySeams> in L4")

    return errors


if __name__ == "__main__":
    xml_path = sys.argv[1] if len(sys.argv) > 1 else str(
        Path(__file__).parent / "automations_master_architect_v4_0_0.xml"
    )
    errors = validate_maa(xml_path)
    if errors:
        print(f"VALIDATION FAILED ({len(errors)} errors):")
        for i, e in enumerate(errors, 1):
            print(f"  {i}. {e}")
        sys.exit(1)
    else:
        print("VALIDATION PASSED: All required sections present.")
        sys.exit(0)

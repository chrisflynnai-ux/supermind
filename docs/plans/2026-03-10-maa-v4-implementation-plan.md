# Master Automations Architect v4.0.0 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build `automations_master_architect_v4_0_0.xml` — the doctrine hub and control surface for the SUPERMIND automation ecosystem, as a SkillML V1.4 XML skill.

**Architecture:** Hub + Spokes model where MAA is the doctrine hub that classifies automation requests, selects tool topologies, designs typed contracts, specifies Flowgrams, and routes work to downstream spoke skills (M2-M8). Uses Progressive Disclosure (L1-L4) to keep context lean. Preserves strongest doctrine from Modules 1-3 while aligning to relational agentics, memory seams, and living systems patterns.

**Tech Stack:** SkillML V1.4 XML format, YAML for embedded contract schemas, CDATA blocks for prompts/templates/code examples. No runtime dependencies — this is a pure doctrine skill.

**Design Doc:** `docs/plans/2026-03-10-maa-v4-design.md`

**Target File:** `.agents/skills/automations/automations_master_architect_v4_0_0.xml`

**Reference Files:**
- SkillML examples: `power_trio_router_v1.0.xml` (610 lines), `MODULE_3_WORKFLOW_TRANSLATOR_v1_1_0.xml` (1,677 lines)
- Seed content: `MODULE-ONE-MASTER-AUTOMATIONS-ARCHITECT-V1.1.0-COMPLETE (2).md`, `MODULE-TWO-AUTOMATION-BUILDER-V1.0.0-COMPLETE (2).md`
- Rebuild specs: `CLAUDE_MAA_REBUILD_HANDOFF_V4.md`, `MAA_SOURCE_PRIORITY_V4.md`
- Patch: `PATCH_master_automations_architect_ground_up_rebuild_v2_1_0.md`

**Estimated Total Lines:** ~1,200-1,500 XML lines
**Estimated Build Time:** ~14 tasks, each 5-15 minutes

---

## Task 1: Create XML Skeleton + Validation Script

**Files:**
- Create: `.agents/skills/automations/automations_master_architect_v4_0_0.xml`
- Create: `.agents/skills/automations/validate_maa_xml.py`

**Step 1: Write the XML validation script**

This script checks that the MAA XML is well-formed and contains all required sections per the design doc.

```python
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
```

**Step 2: Run validation to confirm it works (expect failure — no XML yet)**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: Error (file not found or parse error)

**Step 3: Create the XML skeleton with root element and all top-level section stubs**

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!--
  ╔══════════════════════════════════════════════════════════════════╗
  ║  MASTER AUTOMATIONS ARCHITECT v4.0.0                           ║
  ║  Doctrine Hub for SUPERMIND Automation Ecosystem                ║
  ║                                                                 ║
  ║  Role: Classify → Topology → Blueprint → Route → Learn         ║
  ║  Type: Doctrine (does NOT execute)                              ║
  ║  Family: automations                                            ║
  ║  Architecture: Hub + Spokes                                     ║
  ║                                                                 ║
  ║  Rebuilt from Modules 1-3 seeds:                                ║
  ║  - M1 v1.1.0: Heuristics, Anti-Patterns, Double-II             ║
  ║  - M2 v1.0.0: Builder Contracts, PCE, Self-Annealing           ║
  ║  - M3 v1.1.0: Translation, HCTS, Flowgrams                    ║
  ║                                                                 ║
  ║  SkillML V1.4 | SkillCard: SC-AUTO-001                         ║
  ╚══════════════════════════════════════════════════════════════════╝
-->
<Skill
  skill_id="automations.master_architect"
  name="Master Automations Architect"
  version="4.0.0"
  tier="production"
  status="active"
  model="claude-sonnet"
>

  <Meta>
    <!-- Task 2 -->
  </Meta>

  <Doctrine>
    <!-- Task 3 -->
  </Doctrine>

  <Purpose>
    <!-- Task 3 -->
  </Purpose>

  <Identity>
    <!-- Task 3 -->
  </Identity>

  <Scope>
    <!-- Task 3 -->
  </Scope>

  <SSOT>
    <!-- Task 4 -->
  </SSOT>

  <Dependencies>
    <!-- Task 4 -->
  </Dependencies>

  <ProgressiveDisclosure>
    <Layer id="L1" name="Zero-Point" token_budget="600">
      <!-- Task 5 -->
    </Layer>
    <Layer id="L2" name="Core Doctrine" token_budget="3000">
      <!-- Task 6 -->
    </Layer>
    <Layer id="L3" name="Advanced Patterns" token_budget="2500">
      <!-- Task 7 -->
    </Layer>
    <Layer id="L4" name="Technical Specifications" token_budget="2000">
      <!-- Task 8 -->
    </Layer>
  </ProgressiveDisclosure>

  <Contracts>
    <!-- Task 9 -->
  </Contracts>

  <RelationalOps>
    <!-- Task 10 -->
  </RelationalOps>

  <HCTSLibrary>
    <!-- Task 11 -->
  </HCTSLibrary>

  <MMAIntegration>
    <!-- Task 12 -->
  </MMAIntegration>

  <MasterPrompt>
    <!-- Task 13 -->
  </MasterPrompt>

  <VersionHistory>
    <!-- Task 13 -->
  </VersionHistory>

</Skill>
```

**Step 4: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: Multiple errors about missing child content, but XML should PARSE successfully. The structure exists but sections are empty stubs.

**Step 5: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml .agents/skills/automations/validate_maa_xml.py
git commit -m "feat(maa): scaffold v4.0.0 XML skeleton + validation script"
```

---

## Task 2: Meta Block

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace `<Meta>` stub)

**Step 1: Replace the Meta stub with full provenance block**

Replace the `<Meta><!-- Task 2 --></Meta>` stub with:

```xml
  <Meta>
    <Name>Master Automations Architect</Name>
    <Subtitle>Doctrine Hub for SUPERMIND Automation Ecosystem</Subtitle>
    <Description>Strategic brain that classifies automation requests, selects tool/execution topologies, designs typed contracts for downstream builders, specifies visual Flowgrams, and manages self-improvement loops. Does NOT execute — it architects.</Description>
    <Family>automations</Family>
    <Owner>SUPERMIND</Owner>
    <CreatedBy>
      <agent_or_human>both</agent_or_human>
      <agent_id>claude-opus</agent_id>
      <human_id>cfar7</human_id>
    </CreatedBy>
    <DateCreated>2026-03-10</DateCreated>
    <LastUpdated>2026-03-10</LastUpdated>
    <Tier>production</Tier>
    <Status>active</Status>
    <SkillType>superskill</SkillType>
    <KnowledgeSources>
      <Source name="M1 Master Automations Architect v1.1.0" contribution="Heuristics, anti-patterns, Double-II framework, tool decision matrix"/>
      <Source name="M2 Automation Builder v1.0.0" contribution="PCE framework, builder contracts, self-annealing, sandbox filtering"/>
      <Source name="M3 Workflow Translator v1.1.0" contribution="HCTS library, conversion mappings, flowgram templates, case studies"/>
      <Source name="Automations Architect Master Planner" contribution="Original 8-module doctrine, Operation Automation Factory"/>
      <Source name="MAA Strategic Review v2" contribution="Execution tiers, governance bridge"/>
      <Source name="STRATEGIC_UPDATE_2026-03-08" contribution="Relational agentics, Skill Evaluator, Flowgrams, multi-model direction"/>
    </KnowledgeSources>
    <PatchHistory>
      <Patch id="automations_patch_002" description="Ground-up rebuild from M1-M3 seeds" date="2026-03-10" status="applied"/>
    </PatchHistory>
    <Tags>
      <Tag>automation</Tag>
      <Tag>doctrine</Tag>
      <Tag>architecture</Tag>
      <Tag>hub</Tag>
      <Tag>classification</Tag>
      <Tag>topology</Tag>
      <Tag>contracts</Tag>
      <Tag>flowgrams</Tag>
      <Tag>relational-agentics</Tag>
      <Tag>platform-enhancer</Tag>
    </Tags>
    <ConstitutionalCompliance>aligned</ConstitutionalCompliance>
  </Meta>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: Fewer errors (Meta section now populated). Remaining errors for other empty stubs.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add Meta block with provenance and knowledge sources"
```

---

## Task 3: Doctrine + Purpose + Identity + Scope

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace Doctrine, Purpose, Identity, Scope stubs)

**Step 1: Replace the Doctrine stub**

Source: Upgrade the 6 Core Pains and 5 Core Principles from M1 v1.1. Reframe for Hub + Spokes and platform enhancement.

```xml
  <Doctrine>
    <TheCrisis><![CDATA[
THE 6 AUTOMATION PAINS (Why This Skill Exists)

1. VISUAL SPAGHETTI SYNDROME
   Workflows with 20+ nodes nobody can debug. Move logic into SOPs + scripts (Double-II).

2. SCHEMA BLOAT AT ZERO-POINT
   AI accuracy degrades as tools stack up (15 MCPs = 71% accuracy vs 96% at Zero-Point).
   Keep only tiny descriptors loaded; heavy schemas on demand.

3. TOOL-FIRST ARCHITECTURE
   Design starts with "what tools?" instead of "what workflow?"
   Start from information model and scripts, not tool inventory.

4. LLM-ONLY EXECUTION
   Same automation produces different results each run (73% consistency).
   Back every interaction with deterministic scripts (99% consistency).

5. STATIC NON-LEARNING AUTOMATIONS
   67% error recurrence. Attach logs, self-annealing hooks, and patch proposals.

6. INTERMEDIATE RESULT ROT
   Context fills with 40K+ raw tokens the agent only needs 5% of.
   Enforce Sandbox Filtering: scripts return answers/refs, never raw data.
    ]]></TheCrisis>
    <CoreTheses>
      <Thesis id="T1" source="M1-H2">
        <Claim>Skills + Scripts greater-than MCPs</Claim>
        <Evidence>80% of MCPs can be replaced with on-demand scripts at zero token overhead</Evidence>
      </Thesis>
      <Thesis id="T2" source="M1-Principle">
        <Claim>Zero-Point Context is Default</Claim>
        <Evidence>~600 token footprint enables classification without context bloat</Evidence>
      </Thesis>
      <Thesis id="T3" source="M1-H12">
        <Claim>Double-II Architecture separates intent from execution</Claim>
        <Evidence>Agent updates Information freely; updates Implementation only when logic is proven wrong</Evidence>
      </Thesis>
      <Thesis id="T4" source="new">
        <Claim>Hub + Spokes over flat module catalogs</Claim>
        <Evidence>Doctrine hub with typed contracts enables independent spoke evolution</Evidence>
      </Thesis>
      <Thesis id="T5" source="new">
        <Claim>Platform Enhancement over replacement</Claim>
        <Evidence>Make Claude better at automation design via structured doctrine and contracts</Evidence>
      </Thesis>
    </CoreTheses>
  </Doctrine>
```

**Step 2: Replace the Purpose stub**

```xml
  <Purpose>
    <PrimeDirective><![CDATA[
You are the DOCTRINE HUB for the SUPERMIND automation ecosystem.

Your job:
1. CLASSIFY automation requests (complexity x domain x autonomy)
2. SELECT tool/execution topology (Tier 0-4)
3. CHECK anti-patterns before designing
4. DESIGN the AUTOMATION_BLUEPRINT with typed contracts
5. SPECIFY the FLOWGRAM (Excalidraw-first visual)
6. ROUTE work to the correct spoke skill via HANDOFF_PACKAGE
7. DECLARE memory seams for anything worth remembering
8. GENERATE learning artifacts for self-improvement

You do NOT execute. You do NOT build. You architect.
    ]]></PrimeDirective>
    <CorePhilosophy>
      <Principle id="P1" name="ScriptsOverMCPs">Deterministic scripts before agentic tools, always</Principle>
      <Principle id="P2" name="ZeroPointDefault">Load heavy context only when classification demands it</Principle>
      <Principle id="P3" name="SandboxFiltering">Scripts return summaries and references, never raw data</Principle>
      <Principle id="P4" name="SelfAnnealing">Automations learn from failures via structured loops</Principle>
      <Principle id="P5" name="ContractBeforeCode">Typed contracts before any implementation begins</Principle>
      <Principle id="P6" name="LeanTeams">1-3 specialists plus orchestrator, not agent swarms</Principle>
      <Principle id="P7" name="LivingSystems">Automations self-improve via Generator-Reflector-Curator but never auto-apply patches</Principle>
    </CorePhilosophy>
  </Purpose>
```

**Step 3: Replace the Identity stub**

```xml
  <Identity>
    <WhoYouAre>The Master Automations Architect — doctrine hub and control surface for the SUPERMIND automation ecosystem. You make Claude better at designing automation architectures by providing structured decision frameworks, anti-patterns, and typed contracts.</WhoYouAre>
    <WhatYouDo>
      <Item>Classify automation requests across complexity, domain, and autonomy dimensions</Item>
      <Item>Select optimal tool topology tier (T0 deterministic through T4 multi-agent)</Item>
      <Item>Design typed AUTOMATION_BLUEPRINTs with full contract schemas</Item>
      <Item>Specify Excalidraw-first FLOWGRAM visualizations</Item>
      <Item>Route work to downstream spoke skills via HANDOFF_PACKAGEs</Item>
      <Item>Detect and correct automation anti-patterns before they ship</Item>
      <Item>Declare memory seams for pattern retention across sessions</Item>
      <Item>Generate learning artifacts for self-improvement loops</Item>
      <Item>Govern doctrine compliance for all automation-family skills</Item>
      <Item>Maintain relational graph with depends_on, delegates_to, complements links</Item>
    </WhatYouDo>
  </Identity>
```

**Step 4: Replace the Scope stub**

```xml
  <Scope>
    <WhenToUse>
      <Trigger>User requests an automation workflow design</Trigger>
      <Trigger>User needs to classify or route an automation task</Trigger>
      <Trigger>User asks which tools or topology to use for an automation</Trigger>
      <Trigger>User needs an AUTOMATION_BLUEPRINT for a downstream builder</Trigger>
      <Trigger>User wants to visualize a workflow as a Flowgram</Trigger>
      <Trigger>An automation anti-pattern needs detection or correction</Trigger>
      <Trigger>A spoke skill needs doctrine compliance review</Trigger>
    </WhenToUse>
    <NotFor>
      <Item>Executing automations (use Builder M2 or spoke skills)</Item>
      <Item>Writing code directly (use Builder M2)</Item>
      <Item>Managing memory backends (use future memory layer)</Item>
      <Item>Evaluating SkillML compliance (use future Skill Evaluator)</Item>
      <Item>Copy, content, or design work (use respective skill families)</Item>
      <Item>Harness-specific configuration (remain harness-agnostic)</Item>
    </NotFor>
  </Scope>
```

**Step 5: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: Fewer errors. Doctrine, Purpose, Identity, Scope now populated.

**Step 6: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add Doctrine, Purpose, Identity, Scope sections"
```

---

## Task 4: SSOT + Dependencies

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace SSOT and Dependencies stubs)

**Step 1: Replace the SSOT stub**

```xml
  <SSOT>
    <Required>
      <Input id="automation_request" type="text_or_yaml">Natural language or structured request describing the automation need</Input>
      <Input id="context" type="yaml">Optional project context: existing workflows, constraints, preferences</Input>
    </Required>
    <Optional>
      <Input id="existing_blueprint" type="yaml">Previous AUTOMATION_BLUEPRINT for iteration or upgrade</Input>
      <Input id="domain_expertise" type="markdown">Domain-specific expertise file for the target vertical</Input>
      <Input id="constraint_set" type="yaml">Hard constraints: budget, timeline, platform limits</Input>
    </Optional>
    <Outputs>
      <Output id="AUTOMATION_BLUEPRINT" type="yaml" required="true">Complete architecture specification</Output>
      <Output id="FLOWGRAM_SPEC" type="excalidraw_or_mermaid" required="true">Visual workflow diagram specification</Output>
      <Output id="HANDOFF_PACKAGE" type="yaml" required="true">Typed delivery spec for downstream spoke skill</Output>
      <Output id="PATCH_REQUEST" type="yaml" required="false">Generated when improvement opportunities detected</Output>
      <Output id="MEMORY_SEAM_NOTE" type="yaml" required="false">Generated when patterns worth remembering are identified</Output>
      <Output id="LEARNING_ARTIFACT" type="yaml" required="false">Post-execution reflection for self-improvement loop</Output>
    </Outputs>
  </SSOT>
```

**Step 2: Replace the Dependencies stub**

```xml
  <Dependencies>
    <DownstreamSkills>
      <Skill ref="automations.builder" card="SC-AUTO-002" relation="delegates_to">Receives AUTOMATION_BLUEPRINT + HANDOFF_PACKAGE, builds executable packages</Skill>
      <Skill ref="automations.workflow_translator" card="SC-AUTO-003" relation="delegates_to">Receives FLOWGRAM_SPEC + translation requests, converts between formats</Skill>
      <Skill ref="automations.browser_orchestrator" card="SC-AUTO-004" relation="delegates_to" status="future">Receives browser-specific HANDOFF_PACKAGE for web automation</Skill>
      <Skill ref="automations.content_analyzer" card="SC-AUTO-005" relation="delegates_to" status="future">Receives content analysis HANDOFF_PACKAGE</Skill>
      <Skill ref="automations.outreach_orchestrator" card="SC-AUTO-006" relation="delegates_to" status="future">Receives outreach campaign HANDOFF_PACKAGE</Skill>
    </DownstreamSkills>
    <UpstreamDependencies>
      <Skill ref="meta.mma" card="SC-META-MMA" relation="depends_on">Quality validation via 7D scoring</Skill>
      <Skill ref="meta.skill_evaluator" card="SC-META-EVAL" relation="depends_on" status="future">19-check SkillML validation</Skill>
      <Skill ref="system.memory_layer" card="SC-SYS-MEM" relation="depends_on" status="future">Pattern retrieval and session state</Skill>
    </UpstreamDependencies>
    <Complements>
      <Skill ref="meta.skill_builder" card="SC-META-BUILD" relation="complements">MAA designs, skill_builder scaffolds</Skill>
      <Skill ref="meta.power_trio_router" card="SC-META-PTR" relation="complements">MAA governs automation domain, PTR routes across all domains</Skill>
    </Complements>
  </Dependencies>
```

**Step 3: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: Fewer errors. SSOT and Dependencies now populated.

**Step 4: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add SSOT contracts and Dependencies graph"
```

---

## Task 5: L1 Zero-Point Layer

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace L1 stub)

**Step 1: Replace the L1 Layer stub**

This is the ~600-token ultra-compressed identity that loads on every invocation. Source: design doc Section 3 L1, plus upgraded content from M1 heuristics and anti-patterns.

```xml
    <Layer id="L1" name="Zero-Point" token_budget="600">
      <LoadPriority>always</LoadPriority>
      <ZeroPoint><![CDATA[
MASTER AUTOMATIONS ARCHITECT v4.0.0 — ZERO-POINT

IDENTITY: Doctrine hub for SUPERMIND automation ecosystem
ROLE: Classify → Select Topology → Blueprint → Route → Learn
CONSTRAINT: Does NOT execute, build, store memory, or commit to a harness

TOOL TOPOLOGY (5 tiers — always prefer lowest viable tier):
  T0 DETERMINISTIC: Python/Bash scripts — default, fully testable, zero token cost
  T1 CONSTRAINED:   API calls with rate limiting, structured queries — ~100 tokens
  T2 ASSISTED:      LLM with guardrails, human-in-loop checkpoints — ~150 tokens
  T3 AUTONOMOUS:    Self-healing loops, recursive annealing, circuit breakers — ~200 tokens
  T4 COMPOSITION:   1-3 agents + orchestrator, 4-track cycling with clock — ~500 tokens

CLASSIFICATION AXES:
  Complexity: Simple (single tool) | Compound (pipeline) | Complex (multi-agent)
  Domain:     LeadGen | Outreach | Content | Browser | Interface | Onboarding | Custom
  Autonomy:   Manual | Scheduled | Event-Driven | Living System (self-improving)

ANTI-PATTERN SENTINEL (check before every design):
  AP1 No MCP-first (Scripts > MCPs)
  AP2 No monolithic workflows (decompose > 5 steps)
  AP3 No context flooding (quarantine > 5K operations)
  AP4 No browser before API check
  AP5 No flat skill catalogs (relational graph required)
  AP6 No premature harness lock
  AP7 No memory backend commitment (seams only)
  AP8 No visual debt (Flowgrams must sync with blueprints)
  AP9 No agent swarms (lean teams: 1-3 + orchestrator)
  AP10 No copy-paste architecture (parameterize, don't duplicate)

CONTRACTS: AUTOMATION_BLUEPRINT | FLOWGRAM_SPEC | HANDOFF_PACKAGE | PATCH_REQUEST | MEMORY_SEAM_NOTE | LEARNING_ARTIFACT
SEAMS: ACP_MESSAGE (future) | SKILL_EVAL_REQUEST (future)

LOAD MORE: L2 (Core Doctrine) for heuristics + classification details
           L3 (Advanced Patterns) for sub-domain packs, lean teams, living systems
           L4 (Tech Specs) for contract schemas, memory seams, ACP
      ]]></ZeroPoint>
    </Layer>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: L1 layer now populated.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add L1 Zero-Point layer (~600 tokens)"
```

---

## Task 6: L2 Core Doctrine Layer

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace L2 stub)

**Step 1: Replace the L2 Layer stub**

This is the core doctrine loaded when classifying requests and designing blueprints. Contains the 12 heuristics, 10 anti-patterns (with full detail), classification engine, and tool topology details. Source: M1 v1.1 heuristics (upgraded), M1 anti-patterns (upgraded), design doc Section 4.

```xml
    <Layer id="L2" name="Core Doctrine" token_budget="3000">
      <LoadPriority>when_classifying_or_designing</LoadPriority>

      <ClassificationEngine><![CDATA[
REQUEST CLASSIFICATION ENGINE

Step 1: Parse the automation request into structured dimensions:

  COMPLEXITY ASSESSMENT:
    Simple    — Single tool, linear flow, 1-3 steps
    Compound  — Multi-tool pipeline, sequential + light parallel, 4-10 steps
    Complex   — Multi-agent composition, heavy parallel, branching, 10+ steps

  DOMAIN MAPPING:
    LeadGen     — Discovery, enrichment, verification, scoring
    Outreach    — Email sequences, LinkedIn, social campaigns
    Content     — Scraping, analysis, repurposing, publishing
    Browser     — Web automation where no API exists
    Interface   — Human-in-loop UIs, approval workflows, dashboards
    Onboarding  — Welcome sequences, account setup, data migration
    Custom      — Does not fit standard domains

  AUTONOMY LEVEL:
    Manual      — Human triggers each run
    Scheduled   — Cron-based recurring execution
    EventDriven — Webhook/polling trigger on external events
    LivingSystem — Self-improving with Generator/Reflector/Curator loop

Step 2: Select tool topology tier based on classification:
  Simple + Manual      → T0 (deterministic scripts)
  Compound + Scheduled → T1-T2 (constrained + assisted)
  Complex + EventDriven → T2-T3 (assisted + autonomous)
  Any + LivingSystem   → T3-T4 (autonomous + composition)

Step 3: Check anti-pattern sentinel (all 10) before proceeding to design.
      ]]></ClassificationEngine>

      <ToolTopology><![CDATA[
5-TIER TOOL TOPOLOGY (expanded from M1's 5-level decision matrix)

TIER 0 — DETERMINISTIC SCRIPTS (DEFAULT)
  When: Standard operations, file manipulation, data processing — 80% of use cases
  How:  Python/Bash scripts, CLI execution
  Cost: 0 tokens
  Rule: Always try T0 first. If it works, stop here.

TIER 1 — CONSTRAINED SEARCH
  When: External service interaction with official SDK
  How:  API calls with rate limiting, NPM/PIP package wrappers
  Cost: ~100 tokens
  Rule: Wrap official SDKs, don't write custom fetch wrappers

TIER 2 — AGENT-ASSISTED
  When: Task requires LLM reasoning with guardrails
  How:  Claude/Gemini with structured output, human-in-loop checkpoints
  Cost: ~150 tokens
  Rule: Always include circuit breakers and validation gates

TIER 3 — AUTONOMOUS EXECUTION
  When: Self-healing loops, recurring optimization, pattern learning
  How:  Recursive annealing (Error → Diagnose → Fix → Test → Commit)
  Cost: ~200 tokens
  Rule: Max 3 retry loops, then HALT + PATCH_REQUEST. Never auto-apply patches.

TIER 4 — MULTI-AGENT COMPOSITION
  When: Complex workflows requiring specialized teams
  How:  1-3 specialists + orchestrator, cycling across 4 tracks with clock
  Cost: ~500 tokens
  Rule: Lean teams only. Orchestrator evaluates phase completion. 8-10 agents max across lifecycle.
      ]]></ToolTopology>

      <Heuristics>
        <Heuristic id="H1" name="DecomposeFirst" source="M1-AP1">
          <Condition>Workflow has more than 5 steps</Condition>
          <Action>Break into sub-workflows, each with its own contract</Action>
          <Avoid>Monolithic workflows that resist debugging</Avoid>
        </Heuristic>
        <Heuristic id="H2" name="ScriptsOverMCPs" source="M1-H1-H2">
          <Condition>Operation uses standard libraries or has SDK</Condition>
          <Action>Use CLI script (T0) or package wrapper (T1) — deterministic before agentic</Action>
          <Avoid>Reaching for MCPs or browser tools when scripts suffice</Avoid>
        </Heuristic>
        <Heuristic id="H3" name="ContextQuarantine" source="M1-H9">
          <Condition>Operation would produce more than 5K tokens of output</Condition>
          <Action>Spawn sub-agent with fresh context. Return only summary + reference ID.</Action>
          <Avoid>Loading heavy data into main agent context</Avoid>
        </Heuristic>
        <Heuristic id="H4" name="APIFirst" source="M1-H3-H4">
          <Condition>Operation requires external system interaction</Condition>
          <Action>Check API availability BEFORE considering browser automation</Action>
          <Avoid>Defaulting to browser for everything</Avoid>
        </Heuristic>
        <Heuristic id="H5" name="SandboxFiltering" source="M1-H6">
          <Condition>Script returns data that will enter LLM context</Condition>
          <Action>Return only answer, count, sample, or reference ID — never raw data</Action>
          <Avoid>Passing full JSON, HTML, or document content to context</Avoid>
        </Heuristic>
        <Heuristic id="H6" name="IdempotencyRequired" source="M2-principle">
          <Condition>Any script that may run multiple times</Condition>
          <Action>Design for safe re-execution. Check-before-create. Dedup on write.</Action>
          <Avoid>Scripts that create duplicates or fail on re-run</Avoid>
        </Heuristic>
        <Heuristic id="H7" name="ContractBeforeCode" source="new">
          <Condition>Starting any implementation task</Condition>
          <Action>Define typed contracts (inputs, outputs, validation, error handling) before writing code</Action>
          <Avoid>Starting code without knowing what the handoff looks like</Avoid>
        </Heuristic>
        <Heuristic id="H8" name="ProgressiveDisclosure" source="M1-H4-H10">
          <Condition>Loading any skill, schema, or context</Condition>
          <Action>Load L1 first (~600 tokens). Only escalate to L2-L4 when needed.</Action>
          <Avoid>Loading full skill content into context by default</Avoid>
        </Heuristic>
        <Heuristic id="H9" name="DoubleIISeparation" source="M1-H12">
          <Condition>Designing any reusable automation</Condition>
          <Action>Separate Information (.md = brain, freely updatable) from Implementation (.py = body, update only when proven wrong)</Action>
          <Avoid>Mixing intent and execution in same files</Avoid>
        </Heuristic>
        <Heuristic id="H10" name="LeanTeams" source="new">
          <Condition>Designing multi-agent workflows</Condition>
          <Action>1-3 specialists + 1 orchestrator per active phase. 8-10 agents max across full lifecycle.</Action>
          <Avoid>Agent swarms, unbounded spawning, orchestrator-less teams</Avoid>
        </Heuristic>
        <Heuristic id="H11" name="PlatformEnhancement" source="new">
          <Condition>Designing any automation that uses LLMs</Condition>
          <Action>Enhance Claude/Gemini's native capabilities with structured doctrine and contracts. Don't try to replace the model.</Action>
          <Avoid>Building custom reasoning from scratch when the model already handles it</Avoid>
        </Heuristic>
        <Heuristic id="H12" name="LivingSystems" source="new">
          <Condition>Automation will run repeatedly and should improve over time</Condition>
          <Action>Add Generator/Reflector/Curator loop. Generate PATCH_REQUEST for improvements. Never auto-apply.</Action>
          <Avoid>Static automations that make the same errors forever</Avoid>
        </Heuristic>
      </Heuristics>

      <AntiPatterns>
        <AntiPattern id="AP1" name="MCPFirstDesign" severity="high">
          <Signal>Design starts with MCP server selection</Signal>
          <Fix>Redesign from workflow needs. Use scripts (T0) and packages (T1) first.</Fix>
        </AntiPattern>
        <AntiPattern id="AP2" name="MonolithicWorkflow" severity="high">
          <Signal>Workflow exceeds 15 steps or 20+ visual nodes</Signal>
          <Fix>Decompose into sub-workflows with typed contracts between them</Fix>
        </AntiPattern>
        <AntiPattern id="AP3" name="ContextFlooding" severity="critical">
          <Signal>Raw data (JSON, HTML, logs) loaded directly into LLM context</Signal>
          <Fix>Apply Sandbox Filtering: process in script, return summary + reference only</Fix>
        </AntiPattern>
        <AntiPattern id="AP4" name="BrowserBeforeAPI" severity="medium">
          <Signal>Browser automation attempted without checking API availability</Signal>
          <Fix>Check for official API/SDK first. Browser is fallback (T1 before T3).</Fix>
        </AntiPattern>
        <AntiPattern id="AP5" name="FlatSkillCatalog" severity="medium">
          <Signal>Skills listed without relational metadata (no depends_on, delegates_to)</Signal>
          <Fix>Add relational operations. Skills are a connected graph, not a flat list.</Fix>
        </AntiPattern>
        <AntiPattern id="AP6" name="PrematureHarnessLock" severity="high">
          <Signal>Automation design assumes specific harness product</Signal>
          <Fix>Remain harness-agnostic. Use contracts and seams, not harness-specific APIs.</Fix>
        </AntiPattern>
        <AntiPattern id="AP7" name="MemoryBackendCommitment" severity="medium">
          <Signal>Design hardcodes a specific memory database or backend</Signal>
          <Fix>Use memory seams with temperature declarations. Backend choice is deferred.</Fix>
        </AntiPattern>
        <AntiPattern id="AP8" name="VisualDebt" severity="medium">
          <Signal>Flowgram diagram out of sync with AUTOMATION_BLUEPRINT</Signal>
          <Fix>Flowgrams must update when blueprints change. Treat as coupled artifacts.</Fix>
        </AntiPattern>
        <AntiPattern id="AP9" name="AgentSwarm" severity="high">
          <Signal>Design uses unbounded agent spawning or more than 3 specialists per phase</Signal>
          <Fix>Lean teams: 1-3 specialists + orchestrator. 8-10 max across full lifecycle.</Fix>
        </AntiPattern>
        <AntiPattern id="AP10" name="CopyPasteArchitecture" severity="medium">
          <Signal>Same logic duplicated across multiple scripts or workflows</Signal>
          <Fix>Parameterize shared logic. Extract to utility functions or shared scripts.</Fix>
        </AntiPattern>
      </AntiPatterns>

    </Layer>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: L2 layer now populated with 12 heuristics and 10 anti-patterns.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add L2 Core Doctrine — 12 heuristics, 10 anti-patterns, classification engine"
```

---

## Task 7: L3 Advanced Patterns Layer

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace L3 stub)

**Step 1: Replace the L3 Layer stub**

This is the advanced patterns layer loaded for complex design tasks. Source: design doc Section 5, M2 builder patterns, M3 conversion patterns.

```xml
    <Layer id="L3" name="Advanced Patterns" token_budget="2500">
      <LoadPriority>when_designing_complex</LoadPriority>

      <SubDomainPacks><![CDATA[
SUB-DOMAIN PACK ARCHITECTURE

Each Superskill can contain compartmentalized expertise modules:

STRUCTURE:
  InternalRouter    — Mini-librarian that shifts tracks and serves contextual memory zones
  SubDomainPacks    — Compartmentalized expertise (e.g., LeadGen has: LinkedIn, Email, Enrichment, Scoring)
  AgentSpawning     — When pack exceeds complexity threshold, spawn dedicated sub-agent
  PackContract      — Each pack declares: inputs, outputs, token_budget, spawn_threshold

LOADING RULE:
  1. Router classifies which sub-domain pack is needed
  2. Load only that pack (not the entire skill's deep context)
  3. If pack token_budget exceeds 2K, consider spawning sub-agent instead
  4. Sub-agent returns result via typed contract, then context is released

EXAMPLE (LeadGen Superskill):
  Pack: linkedin_scraping    — inputs: [search_criteria] outputs: [lead_list] budget: 800
  Pack: email_enrichment     — inputs: [lead_list] outputs: [enriched_leads] budget: 600
  Pack: lead_scoring         — inputs: [enriched_leads] outputs: [scored_leads] budget: 400
  Pack: verification         — inputs: [scored_leads] outputs: [verified_leads] budget: 1200 → SPAWN
      ]]></SubDomainPacks>

      <LeanTeamOrchestration><![CDATA[
LEAN TEAM ORCHESTRATION MODEL

TEAM STRUCTURE:
  Specialists:  1-3 per active phase (domain experts)
  Orchestrator: 1 (cycles across all phases, manages clock)
  Total:        8-10 agents contributing across full lifecycle

PHASE CYCLING (4-Track Model):
  T1 RESEARCH    → Orchestrator + 1-2 research specialists
  T2 DRAFT       → Orchestrator + 1-2 creative specialists
  T3 PRODUCTION  → Orchestrator + 2-3 builder specialists
  T4 POLISH      → Orchestrator + 1-2 quality specialists

CLOCK MECHANISM:
  - Each phase has entry gate (prerequisites met?) and exit gate (quality threshold passed?)
  - Orchestrator evaluates exit criteria using MMA 7D scoring
  - Auto-advance when exit gate passes; hold and request help when stuck
  - Circuit breaker: 3 failed exit attempts → HALT + PATCH_REQUEST

HANDOFF PROTOCOL:
  - Phase N produces typed HANDOFF_PACKAGE
  - Orchestrator routes to Phase N+1 specialists
  - Previous phase specialists release context (lean teams, not persistent swarms)
      ]]></LeanTeamOrchestration>

      <BlueprintPatterns><![CDATA[
BLUEPRINT DESIGN PATTERNS

PIPELINE (Linear):
  A → B → C → D
  Use when: Steps are strictly sequential, each feeds the next
  Contract: Each step produces typed output consumed by next step
  Example: Scrape → Clean → Enrich → Store

FAN-OUT / FAN-IN (Parallel):
  A → [B1, B2, B3] → C (merge)
  Use when: Multiple independent operations can run concurrently
  Contract: Fan-out produces array of typed results; fan-in merges + deduplicates
  Example: Scrape 3 sources in parallel → Merge and deduplicate

EVENT-DRIVEN (Reactive):
  Trigger → Handler → [conditional branches]
  Use when: Automation responds to external events (webhooks, file changes, schedules)
  Contract: Trigger produces typed event; handler classifies and routes
  Example: New email → Classify → Route to reply / archive / escalate

LIVING SYSTEM (Self-Improving):
  Generator → Reflector → Curator → [loop or exit]
  Use when: Automation should improve quality over time
  Contract: Generator produces output; Reflector evaluates; Curator decides what to keep
  Example: Content generation → Quality scoring → Pattern library update

HYBRID (Combined):
  Mix of above patterns with clear phase boundaries
  Use when: Complex workflows that don't fit a single pattern
  Rule: Each sub-pattern must have its own typed contracts at boundaries
      ]]></BlueprintPatterns>

      <FlowgramSystem><![CDATA[
FLOWGRAM SPECIFICATION SYSTEM

VISUAL TARGETS (priority order):
  1. Excalidraw (PRIMARY) — Human-friendly, aesthetically pleasing, shareable
  2. Mermaid (TERMINAL)   — For in-terminal rendering, CI/CD, text-based review
  3. Draw.io (SECONDARY)  — For formal documentation export

NODE MODEL:
  Every Flowgram node carries:
    id:               Unique node identifier
    type:             trigger | action | decision | merge | output | error
    label:            Human-readable description (max 40 chars)
    tier:             T0-T4 (which tool topology tier)
    inputs:           Typed input contract reference
    outputs:          Typed output contract reference
    estimated_tokens: Token cost estimate for this operation

EDGE MODEL:
  Every connection carries:
    from:      Source node id
    to:        Target node id
    condition: Optional condition for decision branches (e.g., "count > 100")
    contract:  Contract name being passed (e.g., HANDOFF_PACKAGE)

SYNC RULE:
  Flowgram MUST update when AUTOMATION_BLUEPRINT changes.
  Treat them as coupled artifacts — never let them drift.

GENERATION ORDER:
  1. Design AUTOMATION_BLUEPRINT first
  2. Generate Mermaid from blueprint (quick validation)
  3. Specify Excalidraw layout from Mermaid structure
  4. Export Draw.io only if formal documentation is needed
      ]]></FlowgramSystem>

      <DocumentIntelligence><![CDATA[
3-PHASE DOCUMENT INTELLIGENCE

For analyzing existing workflows, systems, or documentation:

PHASE 1 — PARALLEL SCAN (Quick Classification)
  Read all relevant documents in parallel
  Classify each: canonical | seed | historical | irrelevant
  Output: Prioritized reading list with confidence scores

PHASE 2 — DEEP DIVE (Full Analysis)
  Analyze highest-priority documents thoroughly
  Extract: patterns, anti-patterns, contracts, frameworks, heuristics
  Output: Structured findings with source attribution

PHASE 3 — BACKTRACK (Gap Fill)
  Return to lower-priority documents for specific gaps
  Only mine what was missing from Phase 2
  Output: Supplementary findings merged into Phase 2 results
      ]]></DocumentIntelligence>

      <LivingSystemsPatterns><![CDATA[
LIVING SYSTEMS PATTERNS

Automations that self-improve without full autonomy:

GENERATOR-REFLECTOR-CURATOR LOOP:
  Generator  — Produces initial automation output
  Reflector  — Evaluates output against quality criteria (MMA 7D scoring)
  Curator    — Decides what patterns to preserve, what to discard, what to patch
  Rule:      Curator generates PATCH_REQUEST, NEVER auto-applies changes

RECURSIVE ANNEALING (from M1/M2):
  1. CAPTURE — Full traceback, inputs, coordinator state, timestamp
  2. CLASSIFY — Root cause: logic_error | environment_error | data_error | ambiguity_error
  3. APPLY FIX:
     logic_error      → Patch implementation (flag for human review)
     environment_error → Exponential backoff retry (auto)
     data_error        → Add validation step to SOP (auto)
     ambiguity_error   → Clarify expertise.md instructions (auto)
  4. PERSIST — Write to annealing_log, update Dynamic Memory in SOP
  5. RETRY — Max 3 attempts, then HALT + PATCH_REQUEST

CIRCUIT BREAKERS:
  - Max 3 fix loops per error type
  - Max 500 results per discovery operation
  - Context budget check before every L2+ load
  - MMA score check before every phase transition
      ]]></LivingSystemsPatterns>

    </Layer>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: L3 layer now populated.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add L3 Advanced Patterns — sub-domain packs, lean teams, flowgrams, living systems"
```

---

## Task 8: L4 Technical Specifications Layer

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace L4 stub)

**Step 1: Replace the L4 Layer stub**

This is the technical specification layer loaded for implementation details. Source: design doc Section 6, M2 output contracts, M3 conversion mappings.

```xml
    <Layer id="L4" name="Technical Specifications" token_budget="2000">
      <LoadPriority>when_generating_deliverables</LoadPriority>

      <MemorySeams><![CDATA[
MEMORY SEAM DECLARATIONS

Temperature-based memory model (backend-agnostic):

HOT (active session — always available):
  - active_blueprint:   Current AUTOMATION_BLUEPRINT being designed
  - active_contracts:    Contracts currently in flight
  - session_context:     Current phase, track, fix_count, token_usage

WARM (recent — available on request):
  - recent_blueprints:   Last 5 automation designs (summary + reference)
  - pattern_library:     Frequently used patterns from Curator decisions
  - team_state:          Current agent assignments and phase positions

COLD (historical — available via search):
  - historical_blueprints: All past designs (indexed by domain + complexity)
  - anti_pattern_log:      Violations detected over time (for trend analysis)
  - performance_metrics:   Success rates by pattern type, tier, and domain
  - annealing_history:     Self-healing events and outcomes

BACKEND CONSTRAINT:
  This is a seam declaration only. No specific database, file format, or
  storage backend is assumed. The memory layer (when built) will implement
  these seams. MAA only declares what to remember and at what temperature.

RECORDING RULE:
  Generate MEMORY_SEAM_NOTE whenever:
  - A new pattern is discovered during blueprint design
  - An anti-pattern violation is corrected
  - A self-annealing loop produces a novel fix
  - A blueprint scores notably high or low on MMA
      ]]></MemorySeams>

      <ContractSchemas><![CDATA[
CONTRACT SCHEMAS (YAML format embedded in XML)

AUTOMATION_BLUEPRINT:
  inputs:
    requirement:
      who: string          # Target user/system
      what: string         # What the automation does
      when: string         # Trigger conditions
      success_criteria: string  # How to measure success
    context:
      existing_workflows: list[string]  # Current manual or semi-auto processes
      constraints: object               # Budget, timeline, platform limits
      preferences: object               # Tool preferences, team structure
  outputs:
    classification:
      complexity: Simple | Compound | Complex
      domain: LeadGen | Outreach | Content | Browser | Interface | Onboarding | Custom
      autonomy: Manual | Scheduled | EventDriven | LivingSystem
      tier: T0 | T1 | T2 | T3 | T4
    tool_decisions:
      - operation: string
        tier: T0-T4
        rationale: string
        package: string (optional)
        script: string
        token_cost: integer
    pce_architecture:
      planning: list[string]      # SOP files
      coordination: string        # Coordinator script path
      execution: list[string]     # Step scripts
    double_ii_design:
      information_layer: list[string]   # .md files
      implementation_layer: list[string] # .py files
    integration_map:
      data_flows: list[object]    # Source → transform → destination
      handoff_targets: list[string] # Which spoke skills receive work
  validation:
    mma_threshold: 8.0            # Average score required
    critical_threshold: 9.0       # Critical dimension minimum
    anti_pattern_check: true      # Must pass all 10 AP checks
  error_handling:
    on_mma_fail: generate PATCH_REQUEST
    on_anti_pattern: halt and report violation
    max_fix_loops: 3
  idempotency: true               # Safe to regenerate blueprint

FLOWGRAM_SPEC:
  inputs:
    blueprint_ref: string         # Reference to AUTOMATION_BLUEPRINT
    target_format: excalidraw | mermaid | drawio
  outputs:
    nodes: list[FlowgramNode]
    edges: list[FlowgramEdge]
    layout: object                # Position hints for visual rendering
  validation:
    sync_check: true              # Must match current blueprint
    node_label_max: 40            # Characters per node label

HANDOFF_PACKAGE:
  inputs:
    source_skill: string          # Skill producing the handoff
    target_skill: string          # Skill receiving the handoff
    blueprint_ref: string         # Reference to source blueprint
  outputs:
    task_spec: object             # What the target skill must do
    input_data: object            # Data the target skill needs
    quality_gates: list[string]   # Criteria the target must meet
    timeout: integer              # Max seconds for completion
  validation:
    target_exists: true           # Target skill must be registered
    contract_compatible: true     # Input types must match target's SSOT

PATCH_REQUEST:
  inputs:
    source: string                # What generated this patch request
    target: string                # What should be patched
    category: doctrine | heuristic | anti_pattern | contract | implementation
    description: string           # What needs to change and why
    evidence: string              # What triggered this request
  outputs:
    patch_id: string              # Unique identifier
    priority: critical | high | medium | low
    estimated_effort: string      # Time/complexity estimate

MEMORY_SEAM_NOTE:
  inputs:
    pattern_type: success | failure | anti_pattern | novel_approach
    temperature: hot | warm | cold
    content: string               # What to remember
    source_blueprint: string      # Which blueprint generated this
  outputs:
    seam_id: string               # Unique identifier
    ttl: string                   # How long to retain (session | week | permanent)

LEARNING_ARTIFACT:
  inputs:
    blueprint_ref: string         # Which blueprint was executed
    execution_result: object      # What happened
    mma_scores: object            # Quality scores achieved
  outputs:
    patterns_identified: list[string]  # What worked well
    failures_identified: list[string]  # What went wrong
    patch_proposals: list[string]      # Suggested improvements
    curator_decision: preserve | discard | patch
      ]]></ContractSchemas>

      <MultiModelRouting><![CDATA[
MULTI-MODEL ROUTING SEAMS

MODEL PREFERENCES (harness-agnostic):
  Primary:   Claude (Opus/Sonnet) — reasoning, copy, strategy, orchestration
  Secondary: Gemini — design, video, parallel research, large context
  Tertiary:  Codex — code generation, testing, batch refactoring

ROUTING RULE:
  MAA declares model preference per task type in HANDOFF_PACKAGE.
  The orchestrator (or harness) resolves to actual model instance.
  MAA never directly invokes a model — it specifies the capability needed.

CAPABILITY MAPPING:
  reasoning:      → Claude (primary)
  copy_writing:   → Claude (primary)
  code_generation: → Codex (tertiary) or Claude (fallback)
  visual_design:  → Gemini (secondary)
  research:       → Gemini (secondary, large context) or Claude
  orchestration:  → Claude (primary)
  evaluation:     → Claude (primary) with MMA skill

ROUTER:
  OpenRouter or equivalent model router handles actual dispatch.
  MAA remains agnostic to specific router implementation.
      ]]></MultiModelRouting>

      <SkillTaxonomy><![CDATA[
SKILL TAXONOMY

SUPERSKILLS (Deep Agentic):
  Definition:     Deep skills with internal routers, sub-domain packs, self-improvement
  Characteristics: 500+ lines, L1-L4 disclosure, relational ops, typed contracts
  Examples:       MAA itself, Content Analyzer, Outreach Orchestrator
  Build Rule:     Requires brainstorming + design doc + implementation plan

PRODUCTION SKILLS (Standard Execution):
  Definition:     Standard skills for specific tasks within a domain
  Characteristics: 200-500 lines, L1-L3 disclosure, typed contracts
  Examples:       Advertorial Copy Master, Sales Page Writer, Lead Scorer
  Build Rule:     Requires design brief + contracts

LIGHT SKILLS (Prompt-Level Shareable):
  Definition:     Simple prompt-level skills, often shareable as markdown
  Characteristics: Less than 200 lines, L1-L2 only, minimal contracts
  Examples:       Formatting guides, checklist skills, quick validators
  Build Rule:     Can be authored directly without formal design process
      ]]></SkillTaxonomy>

      <ACPSeam><![CDATA[
ACP (AGENT COMMUNICATION PROTOCOL) — SEAM ONLY

This is a future capability. MAA declares the seam but does not implement it.

PURPOSE:
  Typed messages between agents in a lean team (1-3 specialists + orchestrator)

MESSAGE TYPES (planned):
  TASK_ASSIGNMENT:    Orchestrator → Specialist (what to do, input data, deadline)
  TASK_RESULT:        Specialist → Orchestrator (output, quality score, issues)
  QUALITY_CHECK:      Specialist → MMA (request quality validation)
  PHASE_TRANSITION:   Orchestrator → All (phase complete, moving to next track)
  PATCH_PROPOSAL:     Any Agent → Patch Registry (improvement suggestion)

TRANSPORT:
  TBD — could be function calls, file-based messaging, or A2A protocol.
  MAA does not commit to transport mechanism.

CONSTRAINT:
  Seam declaration only. Full ACP spec deferred until harness selection and
  multi-agent composition patterns are validated in production.
      ]]></ACPSeam>

    </Layer>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: L4 layer now populated with MemorySeams present.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add L4 Tech Specs — memory seams, contract schemas, multi-model, ACP, taxonomy"
```

---

## Task 9: Contracts + Seams

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace Contracts stub)

**Step 1: Replace the Contracts stub**

```xml
  <Contracts>
    <Contract name="AUTOMATION_BLUEPRINT" type="yaml" required="true">
      <Description>Complete architecture specification for an automation workflow</Description>
      <Producer>Master Automations Architect</Producer>
      <Consumer>Automation Builder (M2), Workflow Translator (M3)</Consumer>
      <Fields>requirement, classification, tool_decisions, pce_architecture, double_ii_design, integration_map</Fields>
      <Validation>MMA score at least 8.0 average, 9.0 on critical dimensions</Validation>
    </Contract>
    <Contract name="FLOWGRAM_SPEC" type="excalidraw_or_mermaid" required="true">
      <Description>Visual workflow diagram specification synchronized with blueprint</Description>
      <Producer>Master Automations Architect</Producer>
      <Consumer>Human review, Automation Builder (M2)</Consumer>
      <Fields>nodes, edges, layout, target_format</Fields>
      <Validation>Must match current AUTOMATION_BLUEPRINT; node labels max 40 chars</Validation>
    </Contract>
    <Contract name="HANDOFF_PACKAGE" type="yaml" required="true">
      <Description>Typed delivery specification for downstream spoke skills</Description>
      <Producer>Master Automations Architect</Producer>
      <Consumer>Any spoke module (M2-M8)</Consumer>
      <Fields>source_skill, target_skill, blueprint_ref, task_spec, input_data, quality_gates, timeout</Fields>
      <Validation>Target skill must exist; input types must match target SSOT</Validation>
    </Contract>
    <Contract name="PATCH_REQUEST" type="yaml" required="false">
      <Description>Structured request for skill or system improvements</Description>
      <Producer>Any agent in the automation ecosystem</Producer>
      <Consumer>Patch Registry</Consumer>
      <Fields>source, target, category, description, evidence, priority, estimated_effort</Fields>
      <Validation>Must include evidence and actionable description</Validation>
    </Contract>
    <Contract name="MEMORY_SEAM_NOTE" type="yaml" required="false">
      <Description>Declaration of what to remember and at what temperature</Description>
      <Producer>Master Automations Architect</Producer>
      <Consumer>Future memory layer</Consumer>
      <Fields>pattern_type, temperature, content, source_blueprint, ttl</Fields>
      <Validation>Temperature must be hot, warm, or cold; TTL must be specified</Validation>
    </Contract>
    <Contract name="LEARNING_ARTIFACT" type="yaml" required="false">
      <Description>Post-execution reflection for Generator-Reflector-Curator loop</Description>
      <Producer>Any agent after execution completes</Producer>
      <Consumer>Learning system, Curator</Consumer>
      <Fields>blueprint_ref, execution_result, mma_scores, patterns_identified, failures_identified, patch_proposals, curator_decision</Fields>
      <Validation>Must reference a real blueprint; curator_decision required</Validation>
    </Contract>
    <Seam name="ACP_MESSAGE" status="future">
      <Description>Agent Communication Protocol — typed messages between agents in a lean team</Description>
      <PlannedTypes>TASK_ASSIGNMENT, TASK_RESULT, QUALITY_CHECK, PHASE_TRANSITION, PATCH_PROPOSAL</PlannedTypes>
      <Constraint>Seam only; full spec deferred to harness selection</Constraint>
    </Seam>
    <Seam name="SKILL_EVAL_REQUEST" status="future">
      <Description>Request to Skill Evaluator for 19-check SkillML V1.4 validation</Description>
      <PlannedFields>skill_ref, eval_type, requested_checks</PlannedFields>
      <Constraint>Seam only; evaluator not yet built</Constraint>
    </Seam>
  </Contracts>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: All 6 contracts and 2 seams present. Contract-related errors should be cleared.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add 6 typed contracts + 2 future seams (ACP, Skill Evaluator)"
```

---

## Task 10: Relational Operations

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace RelationalOps stub)

**Step 1: Replace the RelationalOps stub**

```xml
  <RelationalOps>
    <DelegatesTo>
      <Relation target="automations.builder" card="SC-AUTO-002" contracts="AUTOMATION_BLUEPRINT, HANDOFF_PACKAGE">
        Receives blueprint and builds executable automation packages (Double-II structure)
      </Relation>
      <Relation target="automations.workflow_translator" card="SC-AUTO-003" contracts="FLOWGRAM_SPEC, HANDOFF_PACKAGE">
        Receives Flowgram specs and translates between formats (N8N, Python, Mermaid, Excalidraw)
      </Relation>
      <Relation target="automations.browser_orchestrator" card="SC-AUTO-004" contracts="HANDOFF_PACKAGE" status="future">
        Receives browser-specific handoff for web automation tasks (scraping, form filling, session management)
      </Relation>
      <Relation target="automations.content_analyzer" card="SC-AUTO-005" contracts="HANDOFF_PACKAGE" status="future">
        Receives content analysis handoff for data extraction, sentiment analysis, entity extraction
      </Relation>
      <Relation target="automations.outreach_orchestrator" card="SC-AUTO-006" contracts="HANDOFF_PACKAGE" status="future">
        Receives outreach campaign handoff for multi-channel sequence management
      </Relation>
      <Relation target="automations.interface_generator" card="SC-AUTO-007" contracts="HANDOFF_PACKAGE" status="future">
        Receives interface handoff for human-in-loop UI generation
      </Relation>
      <Relation target="automations.onboarding_automator" card="SC-AUTO-008" contracts="HANDOFF_PACKAGE" status="future">
        Receives onboarding handoff for client setup automation
      </Relation>
    </DelegatesTo>
    <DependsOn>
      <Relation target="meta.mma" card="SC-META-MMA" contracts="MMA_SCORE_REQUEST">
        Quality validation via 7-Dimension scoring (average threshold 8.0, critical 9.0)
      </Relation>
      <Relation target="system.memory_layer" card="SC-SYS-MEM" contracts="MEMORY_SEAM_NOTE" status="future">
        Pattern retrieval from warm/cold storage; session state management
      </Relation>
      <Relation target="meta.skill_evaluator" card="SC-META-EVAL" contracts="SKILL_EVAL_REQUEST" status="future">
        19-check SkillML V1.4 validation for MAA itself and all spoke skills
      </Relation>
    </DependsOn>
    <Complements>
      <Relation target="meta.skill_builder" card="SC-META-BUILD">
        MAA designs automation architecture; skill_builder scaffolds the skill XML structure
      </Relation>
      <Relation target="meta.power_trio_router" card="SC-META-PTR">
        MAA governs the automation domain; PTR routes tasks across all SUPERMIND domains
      </Relation>
    </Complements>
    <Reviews>
      <Relation target="automations.*" scope="family">
        MAA reviews all automation-family skills for doctrine compliance (heuristics, anti-patterns, contract schemas)
      </Relation>
    </Reviews>
  </RelationalOps>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: All 4 relational op types present. RelationalOps errors cleared.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add RelationalOps — delegates_to, depends_on, complements, reviews"
```

---

## Task 11: HCTS Library

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace HCTSLibrary stub)

**Step 1: Replace the HCTSLibrary stub**

Source: M3 v1.1 HCTS library (adapted for doctrine hub role), M1 expertise file patterns, M2 builder patterns.

```xml
  <HCTSLibrary>
    <!-- Hacks: Quick wins and shortcuts -->
    <Hacks>
      <Hack id="H1" name="ClassificationShortcut">
        <Technique>If request mentions specific tool (e.g., "scrape LinkedIn"), skip full classification — map directly to domain + tier</Technique>
        <When>Request contains explicit tool or platform references</When>
      </Hack>
      <Hack id="H2" name="BlueprintTemplate">
        <Technique>Start from closest existing blueprint pattern (Pipeline, FanOut, EventDriven, LivingSystem) rather than blank slate</Technique>
        <When>Request fits a known pattern category</When>
      </Hack>
      <Hack id="H3" name="MermaidFirst">
        <Technique>Generate Mermaid diagram first for quick validation before committing to full Excalidraw spec</Technique>
        <When>Blueprint complexity is uncertain; need quick visual validation</When>
      </Hack>
      <Hack id="H4" name="ContractInheritance">
        <Technique>Reuse contract schemas from similar past blueprints instead of defining from scratch</Technique>
        <When>Warm memory contains similar blueprint with compatible contracts</When>
      </Hack>
      <Hack id="H5" name="TierEscalationLadder">
        <Technique>Start at T0 and only escalate tier when current tier demonstrably cannot handle the requirement</Technique>
        <When>Always — this is the default strategy for tier selection</When>
      </Hack>
    </Hacks>
    <!-- Cracks: Known failure points and gotchas -->
    <Cracks>
      <Crack id="C1" name="ScopeCreep">
        <Symptom>Blueprint grows beyond original request scope during design</Symptom>
        <Fix>Re-check original AUTOMATION_REQUEST. If scope expanded, generate separate blueprint for additions.</Fix>
      </Crack>
      <Crack id="C2" name="TierInflation">
        <Symptom>Designer jumps to T3-T4 when T0-T1 would suffice</Symptom>
        <Fix>Apply H5 TierEscalationLadder. Document why lower tier was rejected.</Fix>
      </Crack>
      <Crack id="C3" name="ContractDrift">
        <Symptom>Blueprint and Flowgram specify different data flows</Symptom>
        <Fix>Always generate Flowgram FROM blueprint, never independently. Apply AP8 VisualDebt check.</Fix>
      </Crack>
      <Crack id="C4" name="OrchestrationOverhead">
        <Symptom>More time spent coordinating agents than doing work</Symptom>
        <Fix>Reduce team size. If 3 specialists are not enough, the decomposition is wrong — re-decompose.</Fix>
      </Crack>
      <Crack id="C5" name="MemoryOvercommit">
        <Symptom>Everything marked as "hot" memory, nothing in warm/cold</Symptom>
        <Fix>Apply temperature discipline: only active blueprint and contracts are hot. Everything else is warm or cold.</Fix>
      </Crack>
    </Cracks>
    <!-- Tracks: Proven execution paths -->
    <Tracks>
      <Track id="T1" name="LeadGenTrack">
        <Pattern>Discovery (T1) → Enrichment (T1) → Verification (T0) → Scoring (T0) → Handoff to Outreach</Pattern>
        <KeyRule>NEVER trust scraped data blindly. Always verify before outreach.</KeyRule>
      </Track>
      <Track id="T2" name="ContentRepurposingTrack">
        <Pattern>Extract (T0) → Process with Framework (T2) → Format (T0) → Save for Review (T0)</Pattern>
        <KeyRule>NEVER auto-publish. Always save to review queue first.</KeyRule>
      </Track>
      <Track id="T3" name="BrowserAutomationTrack">
        <Pattern>Check API (T1) → If no API, Browser Setup (T3) → Execute (T3) → Validate (T0)</Pattern>
        <KeyRule>API check is mandatory. Browser is always the fallback, never the first choice.</KeyRule>
      </Track>
      <Track id="T4" name="LivingSystemTrack">
        <Pattern>Generate (T2) → Reflect (T2) → Curate (T0) → Patch Proposal (T0) → Human Review</Pattern>
        <KeyRule>Patches are PROPOSALS only. Human approval required before applying.</KeyRule>
      </Track>
    </Tracks>
    <!-- Stacks: Technology combinations that work together -->
    <Stacks>
      <Stack id="ST1" name="PythonCoreStack">
        <Components>Python 3.11+ | httpx (HTTP) | pydantic (validation) | modal (deploy) | pytest (test)</Components>
        <When>Default stack for T0-T2 automations</When>
      </Stack>
      <Stack id="ST2" name="BrowserStack">
        <Components>Playwright | httpx (fallback) | pydantic (validation) | rotating proxies (stealth)</Components>
        <When>T3 browser automation when API is unavailable</When>
      </Stack>
      <Stack id="ST3" name="AgentStack">
        <Components>Claude API | structured output | MMA scoring | typed contracts | HANDOFF_PACKAGE</Components>
        <When>T2-T4 agent-assisted or multi-agent compositions</When>
      </Stack>
      <Stack id="ST4" name="VisualStack">
        <Components>Mermaid (terminal) | Excalidraw (primary) | Draw.io (export) | JSON metadata</Components>
        <When>Flowgram generation for any blueprint</When>
      </Stack>
    </Stacks>
  </HCTSLibrary>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: HCTSLibrary populated. Closer to full validation pass.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add HCTS Library — 5 hacks, 5 cracks, 4 tracks, 4 stacks"
```

---

## Task 12: MMA Integration

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace MMAIntegration stub)

**Step 1: Replace the MMAIntegration stub**

```xml
  <MMAIntegration>
    <QualityDimensions>
      <Dimension name="classification_accuracy" weight="0.15" threshold="8.0">Request correctly classified across all 3 axes (complexity, domain, autonomy)</Dimension>
      <Dimension name="topology_selection" weight="0.15" threshold="8.0">Correct tool tier selected with documented rationale</Dimension>
      <Dimension name="contract_completeness" weight="0.15" threshold="9.0">All required contract fields populated with valid types</Dimension>
      <Dimension name="anti_pattern_compliance" weight="0.15" threshold="9.0">Zero anti-pattern violations in the blueprint</Dimension>
      <Dimension name="decomposition_quality" weight="0.10" threshold="8.0">Workflow properly decomposed into manageable sub-workflows</Dimension>
      <Dimension name="flowgram_sync" weight="0.10" threshold="8.0">Flowgram accurately represents the blueprint data flows</Dimension>
      <Dimension name="context_hygiene" weight="0.10" threshold="8.0">Zero-Point maintained, no context bloat, sandbox filtering applied</Dimension>
      <Dimension name="relational_integrity" weight="0.10" threshold="7.0">Correct spoke skills identified with compatible contracts</Dimension>
    </QualityDimensions>
    <HardGates>
      <Gate name="no_mcp_first" severity="critical">Blueprint must not start design from MCP selection</Gate>
      <Gate name="no_monolith" severity="critical">No workflow exceeds 15 steps without decomposition</Gate>
      <Gate name="no_raw_data" severity="critical">No raw data (JSON, HTML, logs) flows into LLM context</Gate>
      <Gate name="contracts_typed" severity="high">All handoff contracts must have typed schemas</Gate>
      <Gate name="anti_patterns_checked" severity="high">All 10 anti-patterns checked before blueprint delivery</Gate>
      <Gate name="flowgram_present" severity="high">Every blueprint must have a corresponding Flowgram spec</Gate>
    </HardGates>
    <CircuitBreakers>
      <Breaker name="max_fix_loops" threshold="3">If MMA dimension fails 3 times, HALT and generate PATCH_REQUEST</Breaker>
      <Breaker name="context_budget" threshold="70">If context usage exceeds 70%, trigger garbage collection</Breaker>
      <Breaker name="discovery_cap" threshold="500">Discovery operations capped at 500 results before human review</Breaker>
    </CircuitBreakers>
  </MMAIntegration>
```

**Step 2: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: 8 quality dimensions detected (exceeds minimum 7). MMAIntegration errors cleared.

**Step 3: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add MMA Integration — 8 quality dimensions, 6 hard gates, 3 circuit breakers"
```

---

## Task 13: Master Prompt + Version History

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (replace MasterPrompt and VersionHistory stubs)

**Step 1: Replace the MasterPrompt stub**

```xml
  <MasterPrompt><![CDATA[
You are the MASTER AUTOMATIONS ARCHITECT — the doctrine hub and control surface for the SUPERMIND automation ecosystem.

Your mission: Make Claude better at designing automation architectures by applying structured doctrine, anti-patterns, and typed contracts.

## EXECUTION PROTOCOL

When you receive an automation request, follow these 10 steps:

### Step 1: LOAD ZERO-POINT
Load L1 (~600 tokens). You now have your identity, tier definitions, anti-pattern sentinel, and contract list.

### Step 2: CLASSIFY THE REQUEST
Parse the request across 3 dimensions:
- COMPLEXITY: Simple | Compound | Complex
- DOMAIN: LeadGen | Outreach | Content | Browser | Interface | Onboarding | Custom
- AUTONOMY: Manual | Scheduled | EventDriven | LivingSystem

If classification is ambiguous, load L2 (Core Doctrine) for the full Classification Engine.

### Step 3: SELECT TOOL TOPOLOGY TIER
Apply the Tier Escalation Ladder (H5): Start at T0 and escalate only when necessary.
- T0: Deterministic scripts (80% of use cases)
- T1: API calls with SDK wrappers
- T2: Agent-assisted with guardrails
- T3: Autonomous with self-healing
- T4: Multi-agent with lean team orchestration

Document WHY you selected this tier.

### Step 4: CHECK ANTI-PATTERNS
Run all 10 anti-pattern checks BEFORE designing the blueprint:
AP1-AP10. If any violation is detected, correct the design before proceeding.

### Step 5: DESIGN THE AUTOMATION_BLUEPRINT
Load L2 (Core Doctrine) if not already loaded. Apply the 12 heuristics.
Generate a complete AUTOMATION_BLUEPRINT with:
- Requirement (WHO/WHAT/WHEN/SUCCESS_CRITERIA)
- Classification result
- Tool decisions with rationale per operation
- PCE architecture (Planning/Coordination/Execution)
- Double-II design (Information + Implementation layers)
- Integration map (data flows + handoff targets)

For complex requests, load L3 (Advanced Patterns) for:
- Sub-domain pack architecture
- Blueprint design patterns (Pipeline, FanOut, EventDriven, LivingSystem, Hybrid)
- Lean team orchestration model

### Step 6: GENERATE FLOWGRAM_SPEC
Generate a visual workflow specification:
1. Create Mermaid diagram first (quick validation)
2. Specify Excalidraw layout from Mermaid structure
3. Ensure every node has: id, type, label, tier, inputs, outputs

SYNC RULE: Flowgram must match the blueprint exactly.

### Step 7: CREATE HANDOFF_PACKAGE
Identify which spoke skill(s) should receive this work:
- M2 Builder: For executable automation packages
- M3 Translator: For format conversion tasks
- M4-M8: For specialized domain execution (if available)

Package the handoff with: task_spec, input_data, quality_gates, timeout.

### Step 8: DECLARE MEMORY SEAMS
Generate MEMORY_SEAM_NOTE if:
- A new pattern was discovered
- An anti-pattern violation was corrected
- The blueprint uses a novel approach worth remembering
Assign temperature: hot (active session) | warm (recent) | cold (historical)

### Step 9: RUN MMA QUALITY CHECK
Score the blueprint against 8 quality dimensions:
- Average must be 8.0 or higher
- Critical dimensions (contract_completeness, anti_pattern_compliance) must be 9.0+
- If any dimension fails, fix and re-check (max 3 loops)
- After 3 failures: HALT and generate PATCH_REQUEST

### Step 10: GENERATE LEARNING ARTIFACT
Create a LEARNING_ARTIFACT reflecting on:
- What patterns worked well in this design
- What was challenging or novel
- What patch proposals should be considered
- Curator decision: preserve | discard | patch

## CONSTRAINTS
- You do NOT execute automations — you design them
- You do NOT commit to a specific harness — remain agnostic
- You do NOT hardcode memory backends — use seams only
- You do NOT auto-apply patches — generate PATCH_REQUESTs for human review
- You do NOT spawn agent swarms — lean teams only (1-3 + orchestrator)
  ]]></MasterPrompt>
```

**Step 2: Replace the VersionHistory stub**

```xml
  <VersionHistory>
    <Version number="4.0.0" date="2026-03-10" status="active">
      <Changes>
        <Change>Ground-up rebuild from M1 v1.1, M2 v1.0, M3 v1.1 seeds</Change>
        <Change>Hub + Spokes architecture replacing flat 8-module framing</Change>
        <Change>5-Tier Tool Topology (expanded from 3-tier original)</Change>
        <Change>12 Heuristics (upgraded from M1, 4 new: ContractBeforeCode, LeanTeams, PlatformEnhancement, LivingSystems)</Change>
        <Change>10 Anti-Patterns (upgraded from M1, 2 new: AgentSwarm, CopyPasteArchitecture)</Change>
        <Change>6 Typed Contracts + 2 Future Seams (ACP, Skill Evaluator)</Change>
        <Change>Full Relational Operations (delegates_to, depends_on, complements, reviews)</Change>
        <Change>Sub-Domain Pack Architecture for Superskills</Change>
        <Change>Lean Team Orchestration Model (1-3 + orchestrator, 4-track cycling)</Change>
        <Change>Memory Seam Declarations (hot/warm/cold, backend-agnostic)</Change>
        <Change>Flowgram Specification System (Excalidraw primary)</Change>
        <Change>Living Systems Patterns (Generator/Reflector/Curator)</Change>
        <Change>Multi-Model Routing Seams (harness-agnostic)</Change>
        <Change>HCTS Library (5 hacks, 5 cracks, 4 tracks, 4 stacks)</Change>
        <Change>SkillML V1.4 XML format (replacing SKILL.md legacy)</Change>
      </Changes>
    </Version>
    <Version number="1.1.0" date="2026-01-23" status="superseded">
      <Changes>
        <Change>Added Sandbox Filtering (H6, Pain 6)</Change>
        <Change>Added Double-II Framework as formal heuristic (H12)</Change>
        <Change>Added Menu Bloat anti-pattern (AP8)</Change>
        <Change>Refined token budgets and progressive disclosure</Change>
      </Changes>
    </Version>
    <Version number="1.0.0" date="2026-01-15" status="superseded">
      <Changes>
        <Change>Initial Master Automations Architect with 10 heuristics and 7 anti-patterns</Change>
        <Change>5-level tool decision matrix</Change>
        <Change>4-phase workflow (Discover, Design, Generate, Validate)</Change>
      </Changes>
    </Version>
  </VersionHistory>
```

**Step 3: Run validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: VALIDATION PASSED — all required sections present.

**Step 4: Commit**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml
git commit -m "feat(maa): add Master Prompt (10-step protocol) and Version History"
```

---

## Task 14: Final Validation + Patch Registry Update + Memory Update

**Files:**
- Modify: `.agents/skills/automations/automations_master_architect_v4_0_0.xml` (final review pass)
- Modify: `.agents/skills/automations/patches/PATCH_REGISTRY_V4.yaml`
- Modify: Memory files

**Step 1: Run final validation**

Run: `python .agents/skills/automations/validate_maa_xml.py`
Expected: `VALIDATION PASSED: All required sections present.`

If any errors, fix them now.

**Step 2: Count lines in the final XML**

Run: `wc -l .agents/skills/automations/automations_master_architect_v4_0_0.xml`
Expected: ~1,200-1,500 lines (verify this is in range)

**Step 3: Update PATCH_REGISTRY_V4.yaml**

Change `automations_patch_002` status from `planned` to `applied`:

```yaml
version: 4
family: automations
status: active
patches:
  - patch_id: automations_patch_001
    file: PATCH_master_automations_architect_reinvent_v2_0_0.md
    status: superseded
    target: Master Automations Architect
    note: initial rebuild brief; superseded by ground-up rebuild patch
  - patch_id: automations_patch_002
    file: PATCH_master_automations_architect_ground_up_rebuild_v2_1_0.md
    status: applied
    target: automations_master_architect_v4_0_0.xml
    note: ground-up rebuild completed 2026-03-10; M1-M3 seeds absorbed into Hub + Spokes architecture
    applied_date: 2026-03-10
```

**Step 4: Commit all final changes**

```bash
git add .agents/skills/automations/automations_master_architect_v4_0_0.xml .agents/skills/automations/patches/PATCH_REGISTRY_V4.yaml
git commit -m "feat(maa): complete MAA v4.0.0 build — validation passed, patch registry updated"
```

**Step 5: Generate post-build report**

Create a brief summary answering:
1. What was preserved from M1-M3 (list specific heuristics, patterns, frameworks)
2. What was discarded or reframed (list specific items)
3. Whether M4/M5 archives should be mined for a second pass
4. Whether companion files (AUTOMATION_CONTRACTS_V4.md, FLOWGRAM_VISUAL_CONTRACT_V4.md, MAA_RELATIONAL_OPS_V4.yaml) are needed now or can be deferred

---

## Summary

| Task | Section | Estimated Lines | Key Content |
|------|---------|----------------|-------------|
| 1 | Skeleton + Validator | ~80 + 90 | XML structure, Python validator |
| 2 | Meta | ~50 | Provenance, sources, tags |
| 3 | Doctrine + Purpose + Identity + Scope | ~120 | 5 theses, 7 principles, 10 capabilities, 7 triggers |
| 4 | SSOT + Dependencies | ~60 | Input/output contracts, skill graph |
| 5 | L1 Zero-Point | ~45 | ~600 token compressed identity |
| 6 | L2 Core Doctrine | ~200 | Classification engine, 12 heuristics, 10 anti-patterns |
| 7 | L3 Advanced Patterns | ~180 | Sub-domain packs, lean teams, flowgrams, living systems |
| 8 | L4 Tech Specs | ~200 | Memory seams, contract schemas, multi-model, ACP |
| 9 | Contracts + Seams | ~70 | 6 contracts, 2 seams |
| 10 | Relational Ops | ~50 | delegates_to, depends_on, complements, reviews |
| 11 | HCTS Library | ~100 | 5 hacks, 5 cracks, 4 tracks, 4 stacks |
| 12 | MMA Integration | ~50 | 8 dimensions, 6 gates, 3 breakers |
| 13 | Master Prompt + History | ~130 | 10-step protocol, version log |
| 14 | Validation + Cleanup | ~10 | Final pass, registry, memory |
| **Total** | | **~1,350** | |

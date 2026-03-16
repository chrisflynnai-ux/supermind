# OPENAI PRISM SYNTHESIS PROMPT
## LCP Skill Bundle Architecture Generator

**Paste this prompt into a new Prism workspace, then add your NotebookLM extraction below.**

---

# PRISM SYNTHESIS: LCP Skill Architecture

## ROLE DEFINITION

**ACT AS:** Lead Agentic Architect specializing in Lean Context Protocol (LCP)

**EXPERTISE:**
- ULTRAMIND skill architecture
- Zero-Point Context Strategy
- Python implementation with self-annealing patterns
- Mermaid.js visualization
- Production-ready documentation

**DOCTRINE:** "Skills + Scripts > MCPs" — Token discipline = Accuracy discipline

---

## CONTEXT

I am converting knowledge extractions into production-ready LCP Skill Bundles.

**Architecture Standard:** ULTRAMIND Lean Stack v2.0
**Skill Format:** XML with Progressive Disclosure (L1-L4)
**Implementation:** Python with Pydantic models + Tenacity retry

---

## INPUT DATA

[PASTE YOUR NOTEBOOKLM EXTRACTION OUTPUT HERE]

---

## SYNTHESIS OBJECTIVES

### OBJECTIVE 1: Generate SKILL.md (The Brain)

Create comprehensive skill documentation:

```markdown
# [SKILL NAME] v1.0.0
## [Subtitle capturing core capability]

**Domain:** [meta | copy | product | research | design | tools]
**Tier:** production
**Model:** sonnet (default) | opus (complex reasoning)

---

## ZERO-POINT SCHEMA (~100 tokens)

```json
{
  "skill": "[skill_id]",
  "desc": "[< 25 word description]",
  "triggers": ["[keyword1]", "[keyword2]", "[keyword3]"],
  "outputs": ["[output_type_1]", "[output_type_2]"]
}
```

---

## CORE THESIS

[2-3 paragraphs synthesizing the fundamental insight this skill embeds.
Draw from the key themes in the extraction. This should answer:
- What problem does this skill solve?
- What unique approach does it take?
- Why does this approach work?]

---

## WHEN TO USE

### Trigger Conditions
[List 3-5 specific conditions that should activate this skill]

### NOT For
[List 3-5 anti-patterns - what this skill should NOT be used for]

### Routing Rules
- If [condition A] → Use this skill
- If [condition B] → Route to [other skill] instead
- If [condition C] → Combine with [complementary skill]

---

## EXECUTION PATTERN

### Required Inputs
```yaml
required:
  - input_name: 
      type: [string | object | array]
      description: "[What this input provides]"
      example: "[Example value]"
```

### Optional Inputs  
```yaml
optional:
  - input_name:
      type: [string | object | array]
      default: "[Default value if not provided]"
      description: "[What this input provides]"
```

### Process Steps
1. **[Step Name]:** [Description of what happens]
   - Input: [What goes in]
   - Output: [What comes out]
   - Validation: [How to verify success]

2. **[Step Name]:** [Description]
   [Continue pattern...]

### Output Specification
```yaml
outputs:
  primary:
    type: [object | string | file]
    description: "[Main deliverable]"
    schema: 
      field_1: "[type and description]"
      field_2: "[type and description]"
  
  artifacts:
    - "[File or asset created]"
    - "[File or asset created]"
```

---

## LEARNED CONSTRAINTS

> Constraints discovered through extraction analysis and common failure patterns.

### LC-01: [Constraint Name]
- **Description:** [What the constraint is]
- **Failure Mode:** [What happens if violated]
- **Resolution:** [How to comply]

### LC-02: [Constraint Name]
[Continue pattern...]

---

## INTEGRATION POINTS

| Direction | Skill/System | Purpose |
|-----------|-------------|---------|
| Upstream | [ZPWO / other skill] | [What it provides] |
| Downstream | [MMA / other skill] | [What this skill feeds] |
| Peer | [Related skill] | [How they complement] |

---

## EXAMPLES

### Example 1: [Scenario Name]
**Input:**
```json
{
  "input_field": "example_value"
}
```

**Output:**
```json
{
  "output_field": "example_result"
}
```

### Example 2: [Scenario Name]
[Continue pattern...]

---

## VERSION HISTORY

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | [YYYY-MM-DD] | Initial release |
```

---

### OBJECTIVE 2: Generate implementation.py (The Body)

Create production-ready Python implementation:

```python
"""
[SKILL_NAME] Implementation
Version: 1.0.0
Purpose: [Brief description from skill]

Architecture: ULTRAMIND Lean Context Protocol
Doctrine: Skills + Scripts > MCPs
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
from pydantic import BaseModel, Field, validator
from tenacity import (
    retry,
    stop_after_attempt,
    wait_exponential,
    retry_if_exception_type
)
import logging

# ============================================================
# LOGGING CONFIGURATION
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# ============================================================
# PYDANTIC MODELS (Type Safety)
# ============================================================

class SkillInput(BaseModel):
    """
    Input schema for [SKILL_NAME].
    All fields validated at runtime.
    """
    # Required fields (from extraction)
    field_1: str = Field(..., description="[Description]")
    field_2: Dict[str, Any] = Field(..., description="[Description]")
    
    # Optional fields with defaults
    options: Optional[Dict[str, Any]] = Field(
        default_factory=dict,
        description="Additional options"
    )
    
    @validator('field_1')
    def validate_field_1(cls, v):
        """Custom validation logic"""
        if not v.strip():
            raise ValueError("field_1 cannot be empty")
        return v.strip()
    
    class Config:
        extra = "forbid"  # Reject unknown fields


class SkillOutput(BaseModel):
    """
    Output schema for [SKILL_NAME].
    Standardized for SSOT integration.
    """
    status: str = Field(..., description="success | error | partial")
    result: Dict[str, Any] = Field(..., description="Primary output data")
    summary: str = Field(..., description="Human-readable summary < 200 chars")
    artifacts: List[str] = Field(default_factory=list, description="Created file paths")
    metadata: Dict[str, Any] = Field(
        default_factory=lambda: {
            "skill_id": "[SKILL_ID]",
            "version": "1.0.0",
            "executed_at": datetime.now().isoformat()
        }
    )


class LearnedConstraint(BaseModel):
    """Constraint discovered through execution failure."""
    id: str
    description: str
    failure_mode: str
    resolution: str
    discovered_at: str = Field(default_factory=lambda: datetime.now().isoformat())

# ============================================================
# CORE IMPLEMENTATION
# ============================================================

class SkillExecutor:
    """
    Main execution class for [SKILL_NAME].
    Implements Zero-Point Context Strategy.
    """
    
    def __init__(self):
        self.constraints: List[LearnedConstraint] = []
        self._load_constraints()
    
    def _load_constraints(self):
        """Load learned constraints from file."""
        constraints_path = Path(__file__).parent / "docs" / "learned_constraints.json"
        if constraints_path.exists():
            with open(constraints_path) as f:
                data = json.load(f)
                self.constraints = [LearnedConstraint(**c) for c in data]
    
    def _save_constraint(self, constraint: LearnedConstraint):
        """Persist new constraint."""
        self.constraints.append(constraint)
        constraints_path = Path(__file__).parent / "docs" / "learned_constraints.json"
        constraints_path.parent.mkdir(exist_ok=True)
        with open(constraints_path, "w") as f:
            json.dump([c.dict() for c in self.constraints], f, indent=2)
    
    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=2, max=10),
        retry=retry_if_exception_type((ConnectionError, TimeoutError))
    )
    def execute(self, input_data: SkillInput) -> SkillOutput:
        """
        Main execution with self-annealing retry.
        
        Flow:
        1. Validate input
        2. Execute core logic
        3. Format output
        4. Log any issues
        """
        logger.info(f"Executing [SKILL_NAME] with input: {input_data.dict()}")
        
        try:
            # Step 1: Pre-process and validate
            validated = self._preprocess(input_data)
            
            # Step 2: Core logic (IMPLEMENT BASED ON EXTRACTION)
            result = self._core_logic(validated)
            
            # Step 3: Post-process and format
            output = self._postprocess(result)
            
            logger.info(f"Execution successful: {output.summary}")
            return output
            
        except Exception as e:
            logger.error(f"Execution failed: {str(e)}")
            self._log_failure(e, input_data)
            raise
    
    def _preprocess(self, input_data: SkillInput) -> Dict[str, Any]:
        """Validate and normalize input."""
        # [IMPLEMENT: Based on extraction validation rules]
        return input_data.dict()
    
    def _core_logic(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Core business logic.
        
        [IMPLEMENT: Based on extraction frameworks and patterns]
        """
        # TODO: Implement based on extracted patterns
        result = {
            "processed": True,
            "data": data
        }
        return result
    
    def _postprocess(self, result: Dict[str, Any]) -> SkillOutput:
        """Format into standard output."""
        return SkillOutput(
            status="success",
            result=result,
            summary=f"Processed successfully: {len(result)} items",
            artifacts=[]
        )
    
    def _log_failure(self, error: Exception, context: SkillInput):
        """Log failure for constraint learning."""
        constraint = LearnedConstraint(
            id=f"LC-{len(self.constraints)+1:03d}",
            description=f"Failure during execution",
            failure_mode=str(error),
            resolution="[NEEDS ANALYSIS]"
        )
        self._save_constraint(constraint)

# ============================================================
# SANDBOX MODE (Context Rot Prevention)
# ============================================================

def sandbox_execute(input_data: Dict[str, Any]) -> str:
    """
    Execute in sandbox mode - returns summary only.
    
    Use this for:
    - Testing without polluting main context
    - Getting quick status without full output
    - Preventing Context Rot in orchestration
    """
    executor = SkillExecutor()
    validated_input = SkillInput(**input_data)
    
    try:
        result = executor.execute(validated_input)
        return json.dumps({
            "status": result.status,
            "summary": result.summary[:200],
            "artifact_count": len(result.artifacts)
        })
    except Exception as e:
        return json.dumps({
            "status": "error",
            "summary": str(e)[:200],
            "artifact_count": 0
        })

# ============================================================
# CLI INTERFACE
# ============================================================

def main():
    """CLI entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="[SKILL_NAME] - [Brief description]"
    )
    parser.add_argument(
        "--input", "-i",
        type=str,
        required=True,
        help="Path to input JSON file"
    )
    parser.add_argument(
        "--output", "-o",
        type=str,
        default="output.json",
        help="Path to output JSON file"
    )
    parser.add_argument(
        "--sandbox",
        action="store_true",
        help="Run in sandbox mode (summary only)"
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    args = parser.parse_args()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    # Load input
    with open(args.input) as f:
        input_data = json.load(f)
    
    # Execute
    if args.sandbox:
        result = sandbox_execute(input_data)
        print(result)
    else:
        executor = SkillExecutor()
        validated_input = SkillInput(**input_data)
        output = executor.execute(validated_input)
        
        # Save output
        with open(args.output, "w") as f:
            json.dump(output.dict(), f, indent=2)
        
        print(f"Output saved to: {args.output}")
        print(f"Summary: {output.summary}")

if __name__ == "__main__":
    main()
```

---

### OBJECTIVE 3: Generate flowgram.mmd (The Bridge)

Create Mermaid.js visualization:

```mermaid
%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#e1f5fe', 'secondaryColor': '#fff3e0', 'tertiaryColor': '#e8f5e9'}}}%%

graph TD
    subgraph Input ["📥 INPUT LAYER"]
        A[Raw Input] --> B{Validate Schema}
        B -->|Valid| C[Normalized Data]
        B -->|Invalid| D[❌ Validation Error]
    end

    subgraph Core ["⚙️ CORE LOGIC"]
        C --> E[Step 1: [Name from extraction]]
        E --> F[Step 2: [Name from extraction]]
        F --> G[Step 3: [Name from extraction]]
        G --> H{Quality Check}
    end

    subgraph Output ["📤 OUTPUT LAYER"]
        H -->|Pass| I[Format Output]
        H -->|Fail| J[🔄 Retry Loop]
        J -->|< 3 attempts| E
        J -->|>= 3 attempts| K[❌ Circuit Break]
    end

    subgraph Quality ["✅ MMA VALIDATION"]
        I --> L{MMA Score}
        L -->|≥8.5| M[✅ PASS - Complete]
        L -->|7.0-8.5| N[⚠️ CONDITIONAL - Polish]
        L -->|<7.0| O[❌ FAIL - Specialist]
        N --> P[Load MWP Skill]
        O --> Q[Route to HPE/NRA]
    end

    subgraph Sandbox ["🔒 SANDBOX MODE"]
        C -.->|sandbox flag| R[Isolated Execution]
        R --> S[Summary Only]
        S --> T[Return Reference ID]
    end

    style Input fill:#e1f5fe,stroke:#0288d1
    style Core fill:#fff3e0,stroke:#f57c00
    style Output fill:#e8f5e9,stroke:#388e3c
    style Quality fill:#fce4ec,stroke:#c2185b
    style Sandbox fill:#f3e5f5,stroke:#7b1fa2
```

---

### OBJECTIVE 4: Generate zero_point.json (The Index)

Create minimal descriptor:

```json
{
  "skill_id": "skill.[domain].[name].v1_0_0",
  "name": "[Human-Readable Name]",
  "version": "1.0.0",
  "description": "[< 30 words - core capability statement]",
  
  "triggers": [
    "[primary keyword]",
    "[secondary keyword]",
    "[tertiary keyword]"
  ],
  
  "domain": "[meta|copy|product|research|design|tools]",
  "tier": "production",
  
  "inputs": {
    "required": [
      {
        "name": "[input_name]",
        "type": "[type]",
        "description": "[brief]"
      }
    ],
    "optional": [
      {
        "name": "[input_name]",
        "type": "[type]",
        "default": "[value]"
      }
    ]
  },
  
  "outputs": [
    {
      "name": "[output_name]",
      "type": "[type]",
      "description": "[brief]"
    }
  ],
  
  "dependencies": {
    "upstream": ["[skill_id that feeds this]"],
    "downstream": ["[skill_id that consumes output]"],
    "tools": ["[tool_name]"]
  },
  
  "token_budget": {
    "L1": 500,
    "L2": 1500,
    "L3": 3000,
    "L4": 6000
  },
  
  "cli": {
    "command": "python implementation.py",
    "sandbox": "python implementation.py --sandbox",
    "test": "pytest tests/"
  },
  
  "mma_criteria": {
    "clarity": "[What makes this clear]",
    "completeness": "[What makes this complete]",
    "correctness": "[How to validate correctness]"
  },
  
  "last_updated": "[ISO date]"
}
```

---

## ARCHITECTURAL RULES (Apply During Synthesis)

### Rule 1: The 80% Rule
Replace MCP tool-calling with file-system-based Skills for 80% of operations.
- ✅ Python script with CLI interface
- ✅ File-based input/output
- ❌ Always-on server process
- ❌ Complex MCP schema in context

### Rule 2: The 10-to-1 Rule
Cluster 10 visual nodes (n8n/Make) into 1 Python function.
- If extraction shows 10+ steps → combine into logical function
- Each function = one responsibility
- Functions compose into skill

### Rule 3: Sandbox Filtering
Scripts must return only summaries or reference IDs for main context.
- Full execution happens in isolation
- Return summary (< 200 chars) + reference ID
- Main orchestrator stays light

### Rule 4: Package-First Strategy
Use official SDKs over custom implementations.
```python
# ✅ Good
from anthropic import Anthropic
import requests

# ❌ Bad  
import custom_api_wrapper
```

### Rule 5: Self-Annealing Required
Every script must include retry decorators.
```python
@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=1, min=2, max=10)
)
def execute(self, input_data):
    ...
```

---

## OUTPUT CHECKLIST

Before completing synthesis, verify:

- [ ] SKILL.md contains all sections (Zero-Point, Thesis, Execution, Constraints)
- [ ] implementation.py has Pydantic models, retry decorators, CLI interface
- [ ] flowgram.mmd renders correctly in Mermaid preview
- [ ] zero_point.json is < 200 tokens when stringified
- [ ] All patterns from extraction are represented
- [ ] Learned constraints are pre-populated from extraction tensions
- [ ] Integration points match ULTRAMIND skill ecosystem

---

## DELIVERY FORMAT

Output as a zip-ready folder structure:

```
/[skill_name]/
├── SKILL.md
├── implementation.py
├── flowgram.mmd
├── zero_point.json
├── tests/
│   ├── test_implementation.py
│   └── fixtures/
│       └── sample_input.json
└── docs/
    ├── learned_constraints.json
    └── examples/
        └── example_1.md
```

---

*Prism Synthesis Template v1.0*
*Target: ULTRAMIND LCP Skill Bundles*
*Architecture: Lean Stack v2.0*

# MODULE TWO: AUTOMATION BUILDER
## Draft Architecture & Build Plan

**Version:** 0.1.0-DRAFT  
**Module Type:** Builder (Code Generation)  
**Receives From:** Module 1 (AUTOMATION_BLUEPRINT)  
**Outputs To:** Modules 4-8 (Execution Engines)  
**Integration:** Antigravity (Claude Code) + Codex 5.2 (Validation)  
**Build Date:** 2026-01-23 (Draft)

---

# PART 1: MODULE OVERVIEW

## 1.1 Role Definition

**MODULE TWO is the Code Factory.** It receives AUTOMATION_BLUEPRINT from Module 1 and produces:

```
AUTOMATION_BLUEPRINT (from Module 1)
         │
         ▼
┌─────────────────────────────────────────┐
│       MODULE 2: AUTOMATION BUILDER      │
│         (Code Generation Engine)        │
├─────────────────────────────────────────┤
│                                         │
│  GENERATES:                             │
│  ├── SOP.md (human-readable workflow)   │
│  ├── coordinator.py (orchestration)     │
│  ├── scripts/*.py (execution layer)     │
│  ├── tests/*.py (validation)            │
│  ├── config.yaml (parameters)           │
│  └── expertise.md (domain knowledge)    │
│                                         │
└─────────────────────────────────────────┘
         │
         ▼
    Ready-to-Execute Automation Package
```

## 1.2 Core Principle

> "Module 2 doesn't think about WHAT to build—that's Module 1's job. Module 2 thinks about HOW to build it correctly, following Double-II patterns and generating production-quality code."

## 1.3 Integration Points

| From | Artifact | Purpose |
|------|----------|---------|
| Module 1 | AUTOMATION_BLUEPRINT | What to build |
| Module 1 | TOOL_DECISIONS | Which tools/packages to use |
| Module 1 | INTERFACE_SPEC | UI requirements (if any) |

| To | Artifact | Purpose |
|----|----------|---------|
| Module 4 | Browser scripts | Playwright execution |
| Module 5 | Analysis scripts | Content processing |
| Module 6 | Outreach scripts | Campaign execution |
| Module 7 | Interface components | React generation |
| Module 8 | Onboarding flows | Nurture sequences |

---

# PART 2: FUNCTIONAL CONTEXT

## 2.1 Target Business Functions

MODULE TWO generates code for typical online business automations:

### Category 1: Lead Generation & Scraping

| Function | Input | Output | Complexity |
|----------|-------|--------|------------|
| LinkedIn Profile Discovery | Search criteria | LEAD_RAW_LIST | Medium |
| Instagram Influencer Scraping | Niche + follower range | CREATOR_LIST | Medium |
| YouTube Channel Analysis | Topic keywords | CHANNEL_LIST | Medium |
| Competitor Website Monitoring | URL list | CHANGE_LOG | Low |
| Reddit/Forum Scraping | Subreddit + keywords | POST_LIST | Medium |

### Category 2: Content Scraping & Analysis

| Function | Input | Output | Complexity |
|----------|-------|--------|------------|
| Blog Post Extraction | URL list | CONTENT_CORPUS | Low |
| Video Transcript Extraction | Video URLs | TRANSCRIPT_LIST | Medium |
| Social Media Post Scraping | Profile URLs | POST_ARCHIVE | Medium |
| Review/Testimonial Mining | Product pages | REVIEW_DATABASE | Medium |
| News/PR Monitoring | Keywords + sources | NEWS_FEED | Low |

### Category 3: Content Repurposing & Transformation

| Function | Input | Output | Complexity |
|----------|-------|--------|------------|
| Long-form → Short-form | Blog post | Social posts array | Medium |
| Video → Blog Post | Transcript | Article draft | Medium |
| Thread → Newsletter | Twitter thread | Email content | Low |
| Podcast → Show Notes | Transcript | Structured notes | Medium |
| Multi-source Synthesis | Multiple articles | Summary report | High |

### Category 4: Outreach & Distribution

| Function | Input | Output | Complexity |
|----------|-------|--------|------------|
| Cold Email Campaign | Lead list + templates | OUTREACH_LOG | Medium |
| LinkedIn Connection Requests | Lead list + message | CONNECTION_LOG | Medium |
| Instagram DM Sequence | Creator list + script | DM_LOG | Medium |
| Content Scheduling | Content queue | PUBLISH_LOG | Low |
| Follow-up Sequences | Response triggers | FOLLOWUP_LOG | Medium |

---

## 2.2 Complexity Tiers

### Tier 1: Single-Script Automations
- One input → one output
- No decision branching
- No parallelization needed
- Example: Scrape a single page, extract data

### Tier 2: Multi-Step Pipelines
- Multiple stages
- Linear flow with possible retries
- Light parallelization
- Example: Scrape → Clean → Enrich → Store

### Tier 3: Complex Orchestrations
- Multiple data sources
- Heavy parallelization
- Decision branching
- Human-in-loop checkpoints
- Example: Multi-platform lead gen with scoring and routing

---

# PART 3: IDEAL WORKFLOWS

## 3.1 The Generation Pipeline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MODULE 2 GENERATION PIPELINE                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  STAGE 1: BLUEPRINT PARSING                                                 │
│  ─────────────────────────────                                              │
│  • Validate AUTOMATION_BLUEPRINT schema                                     │
│  • Extract requirement summary                                              │
│  • Parse TOOL_DECISIONS for package requirements                            │
│  • Identify complexity tier                                                 │
│  • Map to generation templates                                              │
│                                                                              │
│  STAGE 2: INFORMATION LAYER GENERATION                                      │
│  ───────────────────────────────────────                                    │
│  • Generate SOP.md from requirement + steps                                 │
│  • Generate expertise.md with domain patterns                               │
│  • Generate config.yaml with parameters                                     │
│  • Generate error_handling.md with known issues                             │
│                                                                              │
│  STAGE 3: IMPLEMENTATION LAYER GENERATION                                   │
│  ─────────────────────────────────────────                                  │
│  • Scaffold coordinator.py structure                                        │
│  • Generate script files for each operation                                 │
│  • Add package imports based on TOOL_DECISIONS                              │
│  • Implement sandbox filtering (return answers, not data)                   │
│  • Add error handling and retry logic                                       │
│                                                                              │
│  STAGE 4: VALIDATION LAYER GENERATION                                       │
│  ───────────────────────────────────────                                    │
│  • Generate test files for each script                                      │
│  • Create mock data fixtures                                                │
│  • Add integration test scaffolds                                           │
│  • Generate validation checklist                                            │
│                                                                              │
│  STAGE 5: PACKAGE ASSEMBLY                                                  │
│  ────────────────────────────                                               │
│  • Organize into Double-II folder structure                                 │
│  • Generate requirements.txt / package.json                                 │
│  • Create README.md with quick start                                        │
│  • Bundle for handoff to execution modules                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 3.2 Output Folder Structure

```
automation_package/
│
├── information/                    # THE BRAIN (Double-II)
│   ├── SOP.md                      # Human-readable workflow
│   ├── expertise.md                # Domain knowledge + patterns
│   ├── error_handling.md           # Known issues + resolutions
│   └── config.yaml                 # Configurable parameters
│
├── implementation/                 # THE BODY (Double-II)
│   ├── coordinator.py              # Orchestration logic
│   ├── scripts/
│   │   ├── __init__.py
│   │   ├── step_1_fetch.py         # Data retrieval
│   │   ├── step_2_transform.py     # Data transformation
│   │   ├── step_3_output.py        # Result delivery
│   │   └── utils.py                # Shared utilities
│   └── requirements.txt            # Python dependencies
│
├── tests/                          # VALIDATION
│   ├── __init__.py
│   ├── test_step_1.py
│   ├── test_step_2.py
│   ├── test_step_3.py
│   ├── test_integration.py
│   └── fixtures/
│       └── mock_data.json
│
├── outputs/                        # RUNTIME ARTIFACTS
│   └── .gitkeep
│
└── README.md                       # Quick start guide
```

---

## 3.3 Generation Templates

### Template: SOP.md

```markdown
# [AUTOMATION_NAME] — Standard Operating Procedure

## Overview
[Auto-generated from blueprint.requirement.description]

## Prerequisites
- [ ] [Dependency 1 from blueprint.constraints]
- [ ] [Dependency 2]
- [ ] Environment variables configured

## Steps

### Step 1: [Step Name from blueprint.pce_architecture.execution.scripts[0]]
**Script:** `scripts/step_1_fetch.py`
**Input:** [From blueprint]
**Output:** [From blueprint]
**Sandbox Rule:** [Return summary, not raw data]

### Step 2: [Step Name]
...

## Error Handling
| Error Type | Detection | Recovery |
|------------|-----------|----------|
| [From blueprint.error_handling] | | |

## Success Criteria
[From blueprint.requirement.success_criteria]

## Manual Intervention Triggers
- [Condition requiring human review]
```

### Template: coordinator.py

```python
"""
[AUTOMATION_NAME] Coordinator
Generated by MODULE 2: Automation Builder
Blueprint: [blueprint_id]
Generated: [timestamp]
"""

import asyncio
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, Optional

# Import execution scripts
from scripts.step_1_fetch import execute as step_1_execute
from scripts.step_2_transform import execute as step_2_execute
from scripts.step_3_output import execute as step_3_execute

# Configuration
from information.config import CONFIG

logger = logging.getLogger(__name__)


class AutomationCoordinator:
    """
    Orchestrates the [AUTOMATION_NAME] workflow.
    
    Responsibilities:
    - Step sequencing
    - Parallelization (where applicable)
    - Retry logic with exponential backoff
    - State management
    - Logging and monitoring
    """
    
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or CONFIG
        self.state = {
            "run_id": None,
            "started_at": None,
            "current_step": None,
            "completed_steps": [],
            "failed_steps": [],
            "results": {}
        }
        self.max_retries = self.config.get("max_retries", 3)
        self.backoff_base = self.config.get("backoff_base", 2)
    
    async def run(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """Execute the full automation workflow."""
        self.state["run_id"] = f"run_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.state["started_at"] = datetime.now().isoformat()
        
        logger.info(f"Starting run: {self.state['run_id']}")
        
        try:
            # Step 1: [STEP_1_NAME]
            result_1 = await self._execute_step(
                "step_1",
                step_1_execute,
                input_data
            )
            
            # Step 2: [STEP_2_NAME]
            result_2 = await self._execute_step(
                "step_2",
                step_2_execute,
                result_1
            )
            
            # Step 3: [STEP_3_NAME]
            result_3 = await self._execute_step(
                "step_3",
                step_3_execute,
                result_2
            )
            
            return self._finalize_results(result_3)
            
        except Exception as e:
            logger.error(f"Run failed: {e}")
            return self._handle_failure(e)
    
    async def _execute_step(
        self,
        step_name: str,
        step_func,
        input_data: Dict
    ) -> Dict:
        """Execute a single step with retry logic."""
        self.state["current_step"] = step_name
        
        for attempt in range(self.max_retries):
            try:
                logger.info(f"Executing {step_name} (attempt {attempt + 1})")
                result = await step_func(input_data)
                
                self.state["completed_steps"].append(step_name)
                self.state["results"][step_name] = {
                    "status": "success",
                    "summary": self._summarize_result(result)
                }
                
                return result
                
            except Exception as e:
                logger.warning(f"{step_name} failed: {e}")
                if attempt < self.max_retries - 1:
                    wait_time = self.backoff_base ** attempt
                    await asyncio.sleep(wait_time)
                else:
                    self.state["failed_steps"].append(step_name)
                    raise
    
    def _summarize_result(self, result: Any) -> Dict:
        """Sandbox filtering: Return summary, not raw data."""
        if isinstance(result, list):
            return {"count": len(result), "sample": result[:2] if result else []}
        elif isinstance(result, dict):
            return {"keys": list(result.keys()), "status": "processed"}
        else:
            return {"type": type(result).__name__, "status": "processed"}
    
    def _finalize_results(self, final_result: Any) -> Dict:
        """Package final results with metadata."""
        return {
            "run_id": self.state["run_id"],
            "status": "success",
            "started_at": self.state["started_at"],
            "completed_at": datetime.now().isoformat(),
            "steps_completed": self.state["completed_steps"],
            "result_summary": self._summarize_result(final_result),
            "full_result_path": f"outputs/{self.state['run_id']}.json"
        }
    
    def _handle_failure(self, error: Exception) -> Dict:
        """Handle and report failures."""
        return {
            "run_id": self.state["run_id"],
            "status": "failed",
            "error": str(error),
            "failed_step": self.state["current_step"],
            "completed_steps": self.state["completed_steps"]
        }


# CLI Entry Point
if __name__ == "__main__":
    import json
    import sys
    
    input_file = sys.argv[1] if len(sys.argv) > 1 else "input.json"
    
    with open(input_file) as f:
        input_data = json.load(f)
    
    coordinator = AutomationCoordinator()
    result = asyncio.run(coordinator.run(input_data))
    
    print(json.dumps(result, indent=2))
```

### Template: Script (step_X.py)

```python
"""
[STEP_NAME] Script
Part of: [AUTOMATION_NAME]
Generated by MODULE 2: Automation Builder
"""

import logging
from typing import Dict, Any, List
from datetime import datetime

# Package imports based on TOOL_DECISIONS
# [CONDITIONAL: If L2_NPM_PACKAGE for this operation]
# import [package] 

# [CONDITIONAL: If L3_BROWSER_AUTOMATION for this operation]
# from playwright.async_api import async_playwright

logger = logging.getLogger(__name__)


async def execute(input_data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Execute [STEP_NAME].
    
    Args:
        input_data: [Description from blueprint]
    
    Returns:
        Dict containing:
        - status: success/failure
        - [output_field]: [description]
        - summary: Sandbox-filtered summary for context
    
    Raises:
        [ErrorType]: [When this happens]
    """
    logger.info(f"Starting [STEP_NAME]")
    
    try:
        # ═══════════════════════════════════════════════════════════════
        # IMPLEMENTATION
        # ═══════════════════════════════════════════════════════════════
        
        # [Generated based on blueprint.pce_architecture.execution.scripts[N]]
        
        result = []  # Placeholder
        
        # ═══════════════════════════════════════════════════════════════
        # SANDBOX FILTERING
        # Return summary for LLM context, store full data externally
        # ═══════════════════════════════════════════════════════════════
        
        return {
            "status": "success",
            "count": len(result),
            "sample": result[:3] if result else [],
            "processed_at": datetime.now().isoformat(),
            # Full result stored separately, not returned to context
            "_full_result_ref": f"outputs/step_X_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        }
        
    except Exception as e:
        logger.error(f"[STEP_NAME] failed: {e}")
        raise


# Standalone execution for testing
if __name__ == "__main__":
    import asyncio
    import json
    
    test_input = {
        # Test data
    }
    
    result = asyncio.run(execute(test_input))
    print(json.dumps(result, indent=2))
```

---

# PART 4: SCENARIOS

## 4.1 Scenario: LinkedIn Lead Discovery

**Business Context:** Agency wants to discover potential coaching clients on LinkedIn.

**Blueprint Input:**
```yaml
requirement:
  name: "LinkedIn Lead Discovery"
  description: "Find coaching prospects with 10K-50K followers"
  trigger: "Manual (weekly)"
  
tool_decisions:
  linkedin_scraping:
    level: L3_BROWSER_AUTOMATION
    tool: Playwright
    rationale: "No official API for profile scraping"
  
  data_storage:
    level: L1_CLI_SCRIPT
    tool: JSON file
    rationale: "Simple persistence, no database needed"
    
pce_architecture:
  execution:
    scripts:
      - name: "search_profiles.py"
        input: "search_criteria"
        output: "profile_urls"
      - name: "scrape_profiles.py"
        input: "profile_urls"
        output: "profile_data"
      - name: "filter_qualify.py"
        input: "profile_data"
        output: "qualified_leads"
```

**Generated Package:**
```
linkedin_lead_discovery/
├── information/
│   ├── SOP.md
│   ├── expertise.md          # LinkedIn scraping patterns
│   ├── config.yaml           # Search criteria, thresholds
│   └── error_handling.md     # Rate limit recovery
├── implementation/
│   ├── coordinator.py
│   ├── scripts/
│   │   ├── search_profiles.py
│   │   ├── scrape_profiles.py
│   │   └── filter_qualify.py
│   └── requirements.txt      # playwright, etc.
├── tests/
│   └── ...
└── README.md
```

---

## 4.2 Scenario: Content Repurposing Pipeline

**Business Context:** Creator wants to turn YouTube videos into blog posts and social threads.

**Blueprint Input:**
```yaml
requirement:
  name: "Video to Multi-Format Content"
  description: "Convert YouTube video to blog post + Twitter thread + LinkedIn post"
  trigger: "On new video upload (webhook)"
  
tool_decisions:
  transcript_extraction:
    level: L2_NPM_PACKAGE
    tool: youtube-transcript-api (pip)
    rationale: "Official-ish API wrapper, reliable"
  
  content_generation:
    level: INTERNAL_LLM
    tool: Claude API
    rationale: "Requires language understanding"
    
pce_architecture:
  execution:
    scripts:
      - name: "extract_transcript.py"
        input: "video_url"
        output: "transcript_text"
      - name: "generate_blog.py"
        input: "transcript_text"
        output: "blog_draft"
      - name: "generate_social.py"
        input: "blog_draft"
        output: "social_posts"
```

**Generated Package:**
```
video_repurpose/
├── information/
│   ├── SOP.md
│   ├── expertise.md          # Content transformation patterns
│   ├── config.yaml           # Tone, style, length settings
│   └── prompts/              # LLM prompt templates
│       ├── blog_prompt.md
│       └── social_prompt.md
├── implementation/
│   ├── coordinator.py
│   ├── scripts/
│   │   ├── extract_transcript.py
│   │   ├── generate_blog.py
│   │   └── generate_social.py
│   └── requirements.txt
├── tests/
│   └── ...
└── README.md
```

---

## 4.3 Scenario: Multi-Platform Lead Gen with Scoring

**Business Context:** Agency runs lead gen across LinkedIn, Instagram, and YouTube, needs unified scoring and routing.

**Blueprint Input:**
```yaml
requirement:
  name: "Multi-Platform Lead Engine"
  description: "Discover, enrich, score, and route leads from 3 platforms"
  trigger: "Daily (scheduled)"
  classification:
    scope: production
    complexity: high
    
tool_decisions:
  linkedin_scraping:
    level: L3_BROWSER_AUTOMATION
  instagram_scraping:
    level: L3_BROWSER_AUTOMATION
  youtube_api:
    level: L2_NPM_PACKAGE
    tool: googleapis (youtube)
  scoring:
    level: L1_CLI_SCRIPT
  dashboard:
    level: L4_CUSTOM_INTERFACE
    
pce_architecture:
  coordination:
    parallelization:
      - "linkedin_scrape || instagram_scrape || youtube_scrape"
    
  execution:
    scripts:
      - name: "scrape_linkedin.py"
      - name: "scrape_instagram.py"
      - name: "fetch_youtube.py"
      - name: "merge_dedupe.py"
      - name: "enrich_leads.py"
      - name: "score_leads.py"
      - name: "route_leads.py"
```

**Generated Package:**
```
multi_platform_leadgen/
├── information/
│   ├── SOP.md
│   ├── expertise.md
│   ├── config.yaml
│   ├── scoring_model.md      # Lead scoring criteria
│   └── routing_rules.md      # Where leads go based on score
├── implementation/
│   ├── coordinator.py        # Handles parallelization
│   ├── scripts/
│   │   ├── scrape_linkedin.py
│   │   ├── scrape_instagram.py
│   │   ├── fetch_youtube.py
│   │   ├── merge_dedupe.py
│   │   ├── enrich_leads.py
│   │   ├── score_leads.py
│   │   └── route_leads.py
│   └── requirements.txt
├── tests/
│   └── ...
├── interface/                 # For Module 7
│   └── INTERFACE_SPEC.yaml
└── README.md
```

---

## 4.4 Scenario: Cold Outreach Campaign

**Business Context:** Run personalized cold email campaign to qualified leads.

**Blueprint Input:**
```yaml
requirement:
  name: "Cold Email Campaign"
  description: "Send personalized outreach with follow-up sequences"
  trigger: "Manual (per campaign)"
  
tool_decisions:
  email_sending:
    level: L2_NPM_PACKAGE
    tool: resend (npm)
  template_rendering:
    level: L1_CLI_SCRIPT
  response_tracking:
    level: L2_NPM_PACKAGE
    tool: resend webhooks
    
pce_architecture:
  execution:
    scripts:
      - name: "render_templates.py"
        input: "lead_list + template"
        output: "personalized_emails"
      - name: "send_batch.py"
        input: "personalized_emails"
        output: "send_log"
      - name: "schedule_followup.py"
        input: "send_log"
        output: "followup_queue"
```

---

# PART 5: EDGE CASES & ERROR HANDLING

## 5.1 Edge Case Categories

### Category A: Input Validation Failures

| Edge Case | Detection | Handling |
|-----------|-----------|----------|
| Empty AUTOMATION_BLUEPRINT | Schema validation | Reject with clear error |
| Missing TOOL_DECISIONS | Field check | Reject with guidance |
| Invalid tool level | Enum validation | Reject with valid options |
| Conflicting requirements | Logic check | Flag for human review |

**Generated Handling:**
```python
# In coordinator.py preamble
def validate_blueprint(blueprint: Dict) -> Tuple[bool, List[str]]:
    """Validate blueprint before generation."""
    errors = []
    
    if not blueprint.get("requirement"):
        errors.append("Missing 'requirement' section")
    
    if not blueprint.get("tool_decisions"):
        errors.append("Missing 'tool_decisions' section")
    
    # ... more validations
    
    return len(errors) == 0, errors
```

### Category B: Generation Failures

| Edge Case | Detection | Handling |
|-----------|-----------|----------|
| Unknown package | Package registry check | Suggest alternatives |
| Unsupported tool level | Enum check | Map to closest supported |
| Template not found | File check | Use generic template |
| Circular dependencies | Graph analysis | Reject with explanation |

### Category C: Runtime Failures (for generated code)

| Edge Case | Detection | Handling |
|-----------|-----------|----------|
| Rate limiting | HTTP 429 | Exponential backoff |
| Auth failure | HTTP 401/403 | Refresh + retry |
| Network timeout | Timeout exception | Retry with longer timeout |
| Data format change | Schema validation | Log + partial continue |
| Browser detection | Page behavior | Rotate user agents |

**Generated Handling:**
```python
# Generated in each script
class RateLimitError(Exception):
    """Raised when rate limited by external service."""
    pass

async def execute_with_resilience(func, *args, **kwargs):
    """Wrapper with standard resilience patterns."""
    for attempt in range(MAX_RETRIES):
        try:
            return await func(*args, **kwargs)
        except RateLimitError:
            wait = BACKOFF_BASE ** attempt
            logger.warning(f"Rate limited, waiting {wait}s")
            await asyncio.sleep(wait)
        except AuthError:
            await refresh_credentials()
            # Retry once after refresh
        except TimeoutError:
            kwargs['timeout'] = kwargs.get('timeout', 30) * 2
    
    raise MaxRetriesExceeded()
```

---

## 5.2 Self-Annealing Integration

Generated code includes hooks for the Self-Annealing Loop (Pattern #12):

```python
# In coordinator.py
async def self_anneal(self, error: Exception, step: str, context: Dict):
    """
    Self-healing protocol from MODULE 1 Pattern #12.
    
    1. Capture traceback + inputs
    2. Classify root cause
    3. Apply appropriate fix
    4. Persist the fix
    5. Retry execution
    """
    annealing_log = {
        "timestamp": datetime.now().isoformat(),
        "step": step,
        "error": str(error),
        "traceback": traceback.format_exc(),
        "context_summary": self._summarize_result(context)
    }
    
    # Classify
    if isinstance(error, RateLimitError):
        cause = "environment_error"
        fix = {"action": "retry", "delay": self.backoff_base ** 2}
    elif isinstance(error, ValidationError):
        cause = "data_error"
        fix = {"action": "update_sop", "note": str(error)}
    elif isinstance(error, KeyError):
        cause = "ambiguity_error"
        fix = {"action": "update_expertise", "missing": error.args[0]}
    else:
        cause = "logic_error"
        fix = {"action": "flag_for_review", "requires_human": True}
    
    annealing_log["cause"] = cause
    annealing_log["fix"] = fix
    
    # Persist
    self._append_annealing_log(annealing_log)
    
    return fix
```

---

## 5.3 Sandbox Filtering Enforcement

All generated scripts enforce the Sandbox Filtering principle:

```python
# CORRECT: Sandbox-filtered return
return {
    "status": "success",
    "count": len(results),
    "sample": results[:3],
    "processed_at": datetime.now().isoformat(),
    "_full_data_ref": "outputs/run_123.json"  # Reference, not data
}

# WRONG: Context dumping (never generate this)
return {
    "status": "success",
    "data": results  # Full payload in context = BAD
}
```

---

# PART 6: BUILD PLAN

## 6.1 Module Structure

```
module_2_automation_builder/
│
├── information/                      # MODULE'S OWN DOUBLE-II
│   ├── SOP.md                        # How to use this module
│   ├── expertise.md                  # Code generation patterns
│   └── templates/                    # Generation templates
│       ├── sop_template.md
│       ├── coordinator_template.py
│       ├── script_template.py
│       ├── test_template.py
│       └── readme_template.md
│
├── implementation/
│   ├── generator.py                  # Main generation engine
│   ├── parser.py                     # Blueprint parser
│   ├── scaffolder.py                 # File/folder creation
│   ├── validators.py                 # Input validation
│   └── templates/                    # Jinja2 templates
│       ├── ...
│
├── tests/
│   ├── test_generator.py
│   ├── test_parser.py
│   ├── fixtures/
│   │   ├── sample_blueprint_simple.yaml
│   │   ├── sample_blueprint_complex.yaml
│   │   └── expected_outputs/
│
└── SKILL.md                          # Skill descriptor for Zero-Point
```

---

## 6.2 Implementation Phases

### Phase 1: Core Generator (Days 1-2)

**Deliverables:**
- Blueprint parser and validator
- Basic SOP.md generation
- Basic coordinator.py generation
- Simple script scaffolding

**Success Criteria:**
- Can generate Tier 1 (single-script) automations
- Output passes lint checks
- Generated code runs without errors

### Phase 2: Template Library (Days 3-4)

**Deliverables:**
- SOP template variations (by complexity tier)
- Script templates for each tool level (L1-L5)
- Coordinator templates (sequential, parallel, mixed)
- Test generation templates

**Success Criteria:**
- Cover all 4 business function categories
- Templates produce DRY, maintainable code
- Sandbox filtering enforced in all templates

### Phase 3: Advanced Features (Days 5-6)

**Deliverables:**
- Parallelization in coordinator
- Self-annealing hooks
- Expertise file generation
- Error handling patterns

**Success Criteria:**
- Can generate Tier 3 (complex orchestration) automations
- Self-annealing integration working
- Error recovery patterns functional

### Phase 4: Validation & Polish (Day 7)

**Deliverables:**
- Full test coverage
- Documentation
- Integration tests with Module 1 blueprints
- Edge case handling

**Success Criteria:**
- All scenarios from Part 4 generate successfully
- Generated code passes all tests
- Ready for NotebookLM expansion

---

## 6.3 NotebookLM Expansion Targets

After base module is complete, extract from video library:

| Topic | Expected Patches |
|-------|------------------|
| Playwright patterns | Script templates for browser automation |
| Error recovery patterns | Enhanced retry/backoff strategies |
| Parallelization patterns | Coordinator templates |
| Testing patterns | Test generation improvements |
| Package-specific patterns | NPM/PIP integration templates |

---

## 6.4 Integration Testing Matrix

| Blueprint Type | Complexity | Expected Output | Test Status |
|----------------|------------|-----------------|-------------|
| Single scrape | Tier 1 | 3 files | ⬜ |
| Linear pipeline | Tier 2 | 5 files | ⬜ |
| Parallel scrape | Tier 2 | 7 files | ⬜ |
| Full lead gen | Tier 3 | 12+ files | ⬜ |
| With interface | Tier 3 | 15+ files | ⬜ |

---

# PART 7: QUICK REFERENCE

## 7.1 Input → Output Summary

```
AUTOMATION_BLUEPRINT (from Module 1)
         │
         ├── requirement ──────────────► SOP.md
         ├── tool_decisions ───────────► scripts/*.py (imports)
         ├── pce_architecture ─────────► coordinator.py + scripts/
         ├── validation_plan ──────────► tests/*.py
         └── interface_spec ───────────► interface/SPEC.yaml (for Module 7)
```

## 7.2 Token Budget

| Layer | Content | Tokens |
|-------|---------|--------|
| L1 | Quick reference | 400 |
| L2 | Templates index | 800 |
| L3 | Full templates | 2,000 |
| L4 | Generation logic | 1,200 |
| **Total** | | **4,400** |

## 7.3 Key Principles

1. **Blueprint is truth** — Don't second-guess Module 1's decisions
2. **Double-II always** — Every package has Information + Implementation
3. **Sandbox filtering** — Scripts return summaries, store full data externally
4. **Self-annealing hooks** — Every coordinator can heal itself
5. **Test from day one** — Generated code includes tests

---

# APPENDIX: READY FOR NOTEBOOKLM

## Upload These Files for Expansion:

1. This draft document
2. MODULE-ONE-v1.1.0-COMPLETE.md
3. Video library sources on:
   - Code generation patterns
   - Playwright/browser automation
   - Error handling best practices
   - Testing strategies

## Extraction Prompt Focus:

```
Review video library for:
1. Script scaffolding patterns (especially Playwright)
2. Coordinator/orchestration patterns
3. Error handling and retry strategies
4. Test generation approaches
5. Package-specific integration patterns

Format as patches to MODULE TWO draft.
```

---

**END OF MODULE TWO DRAFT**

*Ready for NotebookLM expansion and full build*

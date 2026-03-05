# /run-research - T1 Research Team Dispatch

Execute the Research Team workflow for the current project.

## Team Composition
- **Lead:** Market Scout
- **Members:** Research Ops, MIS (Market Intelligence Synthesizer)

## Mission
Gather intelligence, synthesize research, build foundation SSOTs.

## Execution Steps

1. **Load Skills**
   - Load market_scout L1+L2
   - Load research_ops L1
   - Load mis L1

2. **Execute Research**
   - Run market intelligence gathering
   - Synthesize findings into structured insights
   - Identify key angles and opportunities

3. **Build SSOTs**
   - Create/update PROJECT_BRIEF.yaml
   - Create/update MESSAGE_SPINE.yaml
   - Create/update EVIDENCE_PACK.yaml

4. **Gate**
   - Present SSOTs for human approval
   - Lock approved SSOTs with checksums

## Output
- Completed SSOT objects
- Research synthesis document
- Recommended angles for T2

## Next
After approval, task moves to T2_drafts column.

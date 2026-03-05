# /run-draft - T2 Draft Team Dispatch

Execute the Draft Team workflow for strategic copy development.

## Team Composition
- **Lead:** Copy Lead
- **Members:** Copy Director, Assigned Specialist (LFVA/SFVW/SPC/etc.)

## Mission
Strategic copy direction, angle exploration, draft generation.

## Execution Steps

1. **Load Skills**
   - Load copy_lead L1+L2
   - Load copy_director L1+L2
   - Await specialist assignment

2. **Strategic Direction**
   - Copy Lead analyzes SSOTs
   - Identifies primary angle from MESSAGE_SPINE
   - Routes to Copy Director

3. **Angle Exploration**
   - Copy Director generates 3-10 angle variations
   - Evaluates angles against avatar pain points
   - Selects winning angle with rationale

4. **Specialist Assignment**
   - Based on asset type, assign specialist:
     - Long-form VSL -> LFVA
     - Short-form VSL -> SFVW
     - Sales Page -> SPC
     - Advertorial -> ACM
     - Email -> ECG

5. **Draft Generation**
   - Specialist creates initial draft
   - Follows skill-specific structure
   - References EVIDENCE_PACK for all claims

6. **Quality Check**
   - Run MMA M1 Quick Score
   - Threshold: >= 7.0 average
   - Fix loops if needed (max 3)

## Output
- Draft asset with structure
- Angle selection rationale
- MMA M1 scorecard
- Ready for T3 if PASS

## Next
After MMA PASS or human override, task moves to T3_production.

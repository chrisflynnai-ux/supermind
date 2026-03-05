# /run-production - T3 Production Team Dispatch

Execute the Production Team workflow for full asset creation.

## Team Composition
- **Lead:** Active Specialist (from T2)
- **Members:** MMA Master Monitor Agent

## Mission
Full asset production with continuous quality validation.

## Execution Steps

1. **Load Skills**
   - Load active specialist L1+L2+L3 (full depth)
   - Load MMA L1+L2
   - Reference all SSOTs

2. **Production Mode**
   - Specialist enters production mode
   - Full asset generation with all sections
   - Every claim grounded in EVIDENCE_PACK

3. **Continuous Validation**
   - MMA runs checks during production
   - Real-time feedback on quality dimensions
   - Fix issues as they arise

4. **Deep Audit**
   - Run MMA M2 Deep Audit
   - Threshold: >= 8.0 average
   - All CRITICAL dimensions >= threshold
   - Fix loops if needed (max 3)

5. **Proof Discipline Check**
   - Verify all claims have EVIDENCE_PACK backing
   - Flag any unsupported claims
   - Downgrade language or request evidence

## Circuit Breakers
- Max 3 fix loops per dimension
- If same issue fails twice, generate PATCH_REQUEST
- Escalate to human after 3 total failures

## Output
- Production-ready asset
- MMA M2 scorecard
- Fix log if any corrections made
- Ready for T4 if PASS

## Next
After MMA PASS (>= 8.0) or human override, task moves to T4_perfecting.

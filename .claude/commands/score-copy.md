# /score-copy - MMA M1 Quick Score

Run a rapid 7-dimension quality assessment on the current asset.

## Mode
MMA M1 - Quick Score (2-3 minutes)

## Process

1. **Load MMA**
   - Load mma_master_monitor_agent L1+L2
   - Reference relevant SSOTs

2. **Score Dimensions**
   Score each dimension 1-10:

   | DIM | Name | Weight | Threshold |
   |-----|------|--------|-----------|
   | D1 | Strategy Alignment | 15% | 8.0 |
   | D2 | Proof Discipline | 20% | 9.0 |
   | D3 | CTA Integrity | 15% | 9.0 |
   | D4 | Voice Consistency | 15% | 8.0 |
   | D5 | Clarity + Structure | 10% | 8.0 |
   | D6 | Resonance | 15% | 8.0 |
   | D7 | Ethical Guardrails | 10% | 9.0 |

3. **Calculate Verdict**
   - PASS: Weighted avg >= 8.0 AND all CRITICAL >= threshold
   - FIX: Weighted avg 6.5-7.9 OR any dim 5.0-6.9
   - ESCALATE: Weighted avg < 6.5 OR CRITICAL < threshold

4. **Generate Scorecard**
   ```
   MMA SCORECARD - M1 Quick Score
   ================================
   D1 Strategy:    [score] / 10
   D2 Proof:       [score] / 10 (CRITICAL)
   D3 CTA:         [score] / 10 (CRITICAL)
   D4 Voice:       [score] / 10
   D5 Clarity:     [score] / 10
   D6 Resonance:   [score] / 10
   D7 Ethics:      [score] / 10 (CRITICAL)
   ================================
   WEIGHTED AVG:   [avg] / 10
   VERDICT:        [PASS/FIX/ESCALATE]
   ```

## Output
- MMA_SCORECARD with all dimensions
- VERDICT with routing
- FIX recommendations if needed
- Update SESSION_STATE.json with scores

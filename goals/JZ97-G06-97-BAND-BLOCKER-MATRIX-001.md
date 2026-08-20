# JZ97-G06 — 97-Band Blocker Matrix

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G06-97-BAND-BLOCKER-MATRIX-001`  
ENGINE=`AGY pro Explorer/Critic, no product mutation`

## Admission

Requires G05 PASS.

## Mission

Translate calibrated v0.4.2 evidence into a seven-dimension integer blocker matrix. Freeze majority-5 dimensions, identify the exact reviewer-visible evidence missing for each majority-4 dimension, and classify any <=3 as a major blocker.

For each dimension record current majority band, disagreement, evidence, why-not-5, minimum bounded surgery, regression risk and expected reviewer-visible effect. Rank by rubric leverage and consensus.

97-class discipline: `brief_alignment=5` and `implementation_feasibility=5` are hard targets; no majority dimension may be <=3. Select at most two primary targets for G07.

## Exit

PASS when blockers are specific enough to drive bounded implementation rather than generic “improve quality” work. Update state to G07.

NEXT_ON_PASS=`JZ97-G07-V043-TARGETED-SURGERY-001`
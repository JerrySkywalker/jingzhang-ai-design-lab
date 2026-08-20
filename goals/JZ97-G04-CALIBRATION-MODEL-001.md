# JZ97-G04 — Calibration Model

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G04-CALIBRATION-MODEL-001`  
ENGINE=`AGY + deterministic Python/tooling`

## Admission

Requires G03 PASS with immutable anchor verdicts.

## Mission

Compute reviewer and consensus calibration against official anchor scores. Measure per-model bias, consensus MAE, rank-order accuracy, pairwise ordering accuracy and residuals. Use only conservative affine/isotonic methods justified by the small corpus; no complex overfit.

## C1 Gate

`C1_CALIBRATION_READY=PASS` if:
- anchor corpus remains valid and reproducible;
- no catastrophic inversion of low vs high anchors;
- official ordering/pairwise accuracy is useful (target >=80%);
- absolute consensus error is acceptable (target roughly <=5 points), OR absolute prediction is explicitly downgraded to `RELATIVE_ONLY` while rank/band use remains credible.

If absolute calibration fails but relative ordering is useful, continue with `LOCAL_ABSOLUTE_SCORE_UNTRUSTED=true` rather than inventing precision.

## Exit

Write calibration receipts, update C1 to PASS/FAIL, and set G05 only on PASS.

NEXT_ON_PASS=`JZ97-G05-V041A-V042-MEASUREMENT-001`  
NEXT_ON_FAIL=`CALIBRATION_REPAIR_OR_RELATIVE_ONLY_DECISION`
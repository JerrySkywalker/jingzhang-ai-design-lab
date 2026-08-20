# JZ97-G05 — v0.4.1a vs v0.4.2 Measurement

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G05-V041A-V042-MEASUREMENT-001`

## Admission

Requires `C1_CALIBRATION_READY=PASS`.

## Mission

Build neutral, reproducible packets for frozen v0.4.1a and current v0.4.2, then run the exact three-model isolated jury once per candidate/reviewer under the calibrated contract.

Produce raw integer vectors, deterministic weighted totals, calibrated/relative interpretation, reviewer disagreement and blind pairwise preference. Do not mutate either candidate during measurement.

## Exit

PASS only when both candidates have complete valid jury evidence and the comparison distinguishes real evidence from model noise. Update state to G06.

NEXT_ON_PASS=`JZ97-G06-97-BAND-BLOCKER-MATRIX-001`
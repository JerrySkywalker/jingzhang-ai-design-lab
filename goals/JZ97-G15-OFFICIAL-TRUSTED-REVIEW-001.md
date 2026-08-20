# JZ97-G15 — Official Trusted Review

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G15-OFFICIAL-TRUSTED-REVIEW-001`

## Admission

Requires `C4_RELEASE_SAFE=PASS`, a fully reconstructed exact release candidate, current official gates PASS and explicit Owner authorization to enter the official review queue.

## Mission

Submit exactly one final exact head through the official participant workflow, allow trusted validation/review to run, capture the exact-head trusted maintainer score/comment and reconcile it against the existing merged 77-point baseline. Do not rerun identical heads to fish for a better result.

The official maintainer result is the only official score. AGY jury, calibration and ChatGPT holdout remain advisory evidence.

## C5 closeout

- Official score >=97: `PROGRAM_DISPOSITION=TARGET_ACHIEVED`
- Official score 90–96 and safely replaces/improves baseline: `HIGH_SCORE_SUCCESS_TARGET_NOT_REACHED`
- Score below protected high-water: retain protected baseline and reject successor where official high-water mechanism supports this
- Any ambiguity in exact-head/trusted provenance: fail closed

## Exit

Write final Program closeout receipt, freeze final state and preserve all prior checkpoints.
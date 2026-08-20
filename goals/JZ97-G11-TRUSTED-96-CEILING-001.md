# JZ97-G11 — Trusted-96 Ceiling Blind Match

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G11-TRUSTED-96-CEILING-001`

## Admission

Requires one selected local winner with complete calibrated jury evidence and all product gates PASS.

## Mission

Blind-compare the final local winner against a verified trusted 96-point anchor under identical current packet semantics. Use the same exact three-model isolated jury. Reviewers must not know which packet is the 96 anchor.

Compare each rubric dimension and overall preference. Preserve minority opinions and confidence.

## 97-class test

A candidate is ceiling-credible only if the jury majority is `TIE_OR_BETTER` overall and there is no clear majority loss in critical dimensions, especially brief alignment and implementation feasibility.

## Exit

PASS sends the candidate to G12. Clear loss sets `97_CLASS=false` and returns to G06 for a bounded blocker decision rather than score-fishing.

NEXT_ON_PASS=`JZ97-G12-OPENAI-FAMILY-HOLDOUT-001`  
NEXT_ON_FAIL=`JZ97-G06-97-BAND-BLOCKER-MATRIX-001`
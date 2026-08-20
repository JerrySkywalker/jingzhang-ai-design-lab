# JZ97-G03 — Three-Model Anchor Jury

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`

## Admission

Requires G02 PASS, >=5 reproducible blind anchor packets, Windows Sandbox physical isolation qualified, and Owner available for fresh in-Sandbox authentication.

## Jury

Run one valid verdict per anchor with exact pinned models:
- A `claude-opus-4-6-thinking`
- B `claude-sonnet-4-6`
- C `gemini-3.7-flash-high`

No model fallback. No low-score rerolls. Retry only if no valid verdict was produced. Reviewers see identical current rubric/packet semantics and no score/chronology labels.

Each verdict returns integer 0–5 bands, evidence, blocker-to-next-band and confidence. Deterministic host tooling computes weighted totals.

## Exit

PASS when all planned anchor×reviewer verdicts are valid, isolated and immutable. Update state to G04; do not infer calibration until G04.

NEXT_ON_PASS=`JZ97-G04-CALIBRATION-MODEL-001`
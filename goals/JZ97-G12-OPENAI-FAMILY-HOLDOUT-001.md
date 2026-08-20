# JZ97-G12 — OpenAI-Family Holdout

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G12-OPENAI-FAMILY-HOLDOUT-001`  
ENGINE=`ChatGPT GPT-5.6 Sol`

## Admission

Requires G11 PASS and a neutral final-candidate packet plus neutral trusted-96 packet. This Goal is intentionally not delegated to AGY and does not require Codex CLI.

## Mission

Perform one blind GPT-5.6 Sol rubric review of the final candidate using the current official rubric/prompt contract, plus one blind pairwise comparison against the trusted-96 anchor. Do not expose candidate chronology, local AGY scores or desired score.

This is an `OPENAI_FAMILY_HOLDOUT`, not an official maintainer score. Do not rerun because the result is disappointing.

## C3 Gate

`C3_97_CLASS_READY=PASS` only when combined evidence supports near-97 integer band structure, brief/implementation majority=5, no dimension majority<=3, trusted-96 comparison is tie-or-better, and the GPT-5.6 Sol holdout exposes no major blocker.

## Exit

PASS updates state to G13. FAIL returns to G06 for a bounded blocker decision.

NEXT_ON_PASS=`JZ97-G13-FINAL-RELEASE-RECONSTRUCTION-001`  
NEXT_ON_FAIL=`JZ97-G06-97-BAND-BLOCKER-MATRIX-001`
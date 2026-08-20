# JZ97-G01 — Official Rubric and Packet Lock

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G01-OFFICIAL-RUBRIC-AND-PACKET-LOCK-001`  
ENGINE=`AGY gemini-3.7-flash-high`

## Admission

Requires `C0_CONTENT_BASELINE=PASS`. No content mutation. No official PR mutation.

## Mission

Fetch latest `open-city-ai/haidian` and pin the exact current review contract: rubric dimensions/weights, integer 0–5 schema, mandatory rejection, four gates, AI-review prompt, packet composition, image/PDF/HTML visibility, weighted formula and queue decision semantics.

## Required outputs

Write a run receipt containing:
- upstream exact SHA
- exact files/SHAs inspected
- `CURRENT_OFFICIAL_RUBRIC.{md,json}`
- `CURRENT_REVIEW_PACKET_CONTRACT.md`
- `CURRENT_QUEUE_POLICY.md`
- change classification vs prior assumptions

Fractional formal bands are forbidden. Host advisory fractions must never enter formal-jury records.

## Exit

PASS only if rubric, packet, score schema and queue semantics are pinned to exact upstream evidence. Update Program state to `current_goal=G02` and keep C1 pending.

NEXT_ON_PASS=`JZ97-G02-TRUSTED-ANCHOR-CORPUS-001`  
NEXT_ON_FAIL=`OWNER_REQUIRED_OR_RETRY_G01`
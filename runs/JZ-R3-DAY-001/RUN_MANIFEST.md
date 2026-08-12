# JZ-R3-DAY-001 Run Manifest

## Identity

- `RUN_ID`: `JZ-R3-DAY-001`
- `STATUS`: `COMPLETE_EARLY`
- `STARTED_LOCAL_DATE`: `2026-08-12`
- `STARTING_MAIN`: `a1d5c7f22ef6defa9203d8a30e99ed49f0b3da7e`
- `STARTING_OVERNIGHT_HEAD`: `78843cec67498b8930f0cf0bb776665772cee788`
- `BASE_SHA`: `78843cec67498b8930f0cf0bb776665772cee788`
- `DAY_BRANCH`: `day/r3-spatial-admission-001`
- `WORKTREE`: `V:\\src\\_worktrees\\JZ-R3-DAY-001`
- `OFFICIAL_REPO`: `open-city-ai/haidian`
- `OFFICIAL_HEAD_START`: `e9741a415aeb5cf09ca27608f6c97c33145a589f`
- `OFFICIAL_HEAD_END`: `a332d7f1ef0e126d525a56247855a439d410c573`

## Authorized scope

`DECISION` — Build one common contextual spatial evidence base; test C01 spatial admission and C02 H2/H3/H4+/Corridor+N on that same base; prepare non-binding pre-downselect evidence and professional handoff.

## Mutation boundary

- Writable: this worktree and `day/r3-spatial-admission-001` only.
- Read-only: `main`, `overnight/r2-c01-c02-falsification-001`, and `open-city-ai/haidian`.
- Forbidden: formal submission, submission fork/scaffold, official PR/Issue/comment/review, force push, external outreach, private/restricted data.

## Starting decisions

- `DECISION` — C01 starts as `ADVANCE_WITH_MAJOR_REWRITE` (non-binding).
- `DECISION` — C02 starts as `HOLD` (non-binding).
- `DECISION` — C03 remains killed as a standalone candidate and survives only as the Living Systems review lens.
- `DECISION` — `FINAL_WINNER=OWNER_DECISION_REQUIRED`.
- `DECISION` — Candidate 04 will not be generated in this run.

## Evidence discipline

All spatial layers and claims must remain labelled `official`, `provisional`, `contextual`, `derived`, or `concept`. Contextual open data is not authoritative planning data. Synthetic model output is not site-calibrated performance evidence.

## Provisional output state

- `C01_SPATIAL_ADMISSION`: `PASS` at conceptual urban-program level
- `C01_PROVISIONAL_DISPOSITION`: `ADVANCE_WITH_MAJOR_REWRITE`
- `C02_H3_RESULT`: `NOT_SUPPORTED`
- `C02_PROVISIONAL_DISPOSITION`: `KILL`
- `CANDIDATE_04_TRIGGER`: `TRIGGER_IF_C01_FAILS`
- `DOWNSELECT_CONFIDENCE`: `MEDIUM`
- `FINAL_WINNER`: `OWNER_DECISION_REQUIRED`
- `FORMAL_MIGRATION_READINESS`: `NOT_READY_TO_FORK`

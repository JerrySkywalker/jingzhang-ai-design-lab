# Current Program

Canonical Program: [`JZ-97-CONVERGENCE-TRAIN-001`](programs/JZ-97-CONVERGENCE-TRAIN.md)

## Current status

- Program: `JZ-97-CONVERGENCE-TRAIN-001`
- Program state: `ACTIVE`
- Current train: `A_CALIBRATION_FOUNDATION`
- Last completed goal: `JZ97-G02-TRUSTED-ANCHOR-CORPUS-001`
- Current goal: `JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`
- Next goal: `JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`
- C0 `CONTENT_BASELINE`: `PASS`
- C1 `CALIBRATION_READY`: `PENDING`
- C2 `CANDIDATE_LIFT`: `BLOCKED`
- C3 `97_CLASS_READY`: `BLOCKED`
- C4 `RELEASE_SAFE`: `BLOCKED`
- C5 `TRUSTED_RESULT`: `BLOCKED`

## Anchors

- Official trusted head: `1d5cb1aaa9d76edc3532e593c803cb936070a744`
- Official trusted score: `77`
- Frozen v0.4.1a: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- Current local v0.4.2: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- Calibration Anchor Corpus: 7 exact-head trusted anchors established under G02 (`N4`, `X8`, `B2`, `W7`, `J9`, `L5`, `P3`).
- Draft successor PR #2774 remains a release-track artifact and must not be mutated by calibration/content Goals.

## Operating rule

Before starting any Goal, read:

1. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`
2. `state/JZ97_PROGRAM_STATE.json`
3. the selected `goals/JZ97-*.md`
4. `docs/PROGRAM_CONTROL_AIRLOCK.md`

If the Goal admission requirements do not match current state, stop with `DISPOSITION=BLOCKED_PROGRAM_STATE` rather than improvising around the roadmap.

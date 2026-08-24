# Current Program

Canonical Program: [`JZ-97-CONVERGENCE-TRAIN-001`](programs/JZ-97-CONVERGENCE-TRAIN.md)

## Current status

- Program: `JZ-97-CONVERGENCE-TRAIN-001`
- Program state: `ACTIVE`
- Compound Train: `JZ97-CODEX-NATIVE-CONVERGENCE-TRAIN-001`
- Execution Architecture: `CODEX_NATIVE_DUAL_PROFILE_PANEL`
- Current stage: `A2_SINGLE_EXPRESSION_PATCH_ADMITTED`
- Last completed goal: `JZ97-CODEX-NATIVE-CUTOVER-AND-CONVERGENCE-001`
- Current active goal: `JZ97-A2-EXPRESSION-COMPLETENESS-SINGLE-PATCH-001`
- Formal measured winner: `INCONCLUSIVE`
- Calibration mode: `UNTRUSTED` (`LOCAL_ABSOLUTE_SCORE_TRUSTED=false`, `LOCAL_RELATIVE_ORDER_TRUSTED=false`)
- Frozen shadow: AI planning innovation target solved; expression completeness target not solved; feasibility regression risk active.
- QuickScore bootstrap: `tools/jz_quickscore.py` (DEV_ADVISORY ONLY)
- C0 `CONTENT_BASELINE`: `PASS`
- C1 `CALIBRATION_READY`: `FAIL`
- C2 `CANDIDATE_LIFT`: `BLOCKED`
- C3 `97_CLASS_READY`: `BLOCKED`
- C4 `RELEASE_SAFE`: `BLOCKED`
- C5 `TRUSTED_RESULT`: `BLOCKED`

## Anchors & Calibration Corpus

- Official trusted head: `1d5cb1aaa9d76edc3532e593c803cb936070a744` (Score: `77`)
- Frozen v0.4.1a: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- Certified local v0.4.2: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- Core Calibration Anchors: 5 exact-head trusted anchors (`N4`=77, `X8`=86, `B2`=90, `W7`=90, `J9`=96)
- Diagnostic Reserve Anchors: `L5` (90), `P3` (91)
- Draft successor PR #2774 remains a release-track artifact and must not be mutated.

## Operating Rule

Before starting any Goal or Compound Train phase, read:

1. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`
2. `state/JZ97_PROGRAM_STATE.json`
3. the selected `goals/JZ97-*.md`
4. `docs/PROGRAM_CONTROL_AIRLOCK.md`

The active formal-local runtime is `tools/codex_jury/`; legacy AGY/WSB runtime files are preserved but not current execution paths. If the Goal admission requirements do not match current state, stop with `DISPOSITION=BLOCKED_PROGRAM_STATE` rather than improvising around the roadmap.

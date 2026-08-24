# JZ97 Codex-native cutover and convergence

Run ID: `JZ97-CODEX-NATIVE-CUTOVER-AND-CONVERGENCE-001`

Active train: `JZ97-CODEX-NATIVE-CONVERGENCE-TRAIN-001`

## Mission

Retire the AGY and Windows Sandbox formal-jury execution path without deleting its history. Replace it with a minimal dual-profile Codex-native panel, calibrate once against the five frozen anchors, measure frozen v0.4.1a and v0.4.2, derive at most two blocker targets, and compare the frozen shadow head against those targets.

## Immutable safety boundary

- Product heads `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`, `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`, and `31d9ee0dba3fc81ca3d9c4a09d9dad86474d328f` are read-only inputs.
- PR #2774 and both product repositories remain unmodified.
- No official review is requested and the draft PR is not marked Ready.
- Each reviewer/packet pair gets one fresh process and at most one attempt.
- A holdout is admitted only for calibrated disagreement, material pairwise conflict, or final release qualification.

## Exit

Exit requires 10 anchor scorecards, calibration metrics, two scorecards for each frozen candidate, a seven-dimension blocker matrix, frozen-shadow target status, regression assessment, and an explicit A2 mode.

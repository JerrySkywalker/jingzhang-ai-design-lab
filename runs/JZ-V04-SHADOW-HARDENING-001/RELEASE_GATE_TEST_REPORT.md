# Release gate test report

FAST: Python compilation passed. CORE: 9 release-gate unit tests passed, including all
required Cases A–I and a mocked read-only GitHub backend. FULL: the complete new-tool suite
passed (12 tests) and `git diff --check` passed.

The live, read-only configuration observed PR #2774 as open/draft at `ac2a41c`, scope-limited
to the expected submission directory; baseline PR #2744 as merged at `1d5cb1a` with trusted
score 77; Draft validation skip; threshold 60; and no active high-water guard on current main.

Result: `CURRENT_STATE=SAFE_WAIT`, `SAFE_TO_MARK_READY=false`,
`HISTORICAL_BEST_PROVEN=true`, `SCORE_GUARD_ACTIVE=false`, and
`TOOLING_DRIFT_CLASS=PEER_SUBMISSIONS_ONLY`. The JSON records are `release-gate.json` and
`release-gate-live.json`.

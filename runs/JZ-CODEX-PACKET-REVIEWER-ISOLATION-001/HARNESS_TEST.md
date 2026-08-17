# Disposable harness test

STATUS=OWNER_REQUIRED

After the Owner-authenticated confinement and memory probe passes, launch the separate fresh `harness-test-a.wsb` instance and run `./reviewer-runner.ps1 -Reviewer A -Mode HarnessTest`. It requires a new in-Sandbox subscription sign-in, a new `C:\CodexHome`, and `codex exec --ephemeral`; it cannot resume or reuse the probe session.

The only accepted output filename is `harness-test-only.json`. Its schema requires `run_classification=HARNESS_TEST_ONLY` and `discard_for_score_trajectory=true`. The output is disposable, must never be labelled or counted as a candidate score, and cannot produce a v0.4.1a trajectory entry.

Accept only if the schema validates, visual attachments are readable, output is in `output-a`, no external context is used, and the preceding memory-contamination result is clean.

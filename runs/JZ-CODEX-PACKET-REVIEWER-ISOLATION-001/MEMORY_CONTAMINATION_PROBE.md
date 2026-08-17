# Memory-contamination probe

STATUS=OWNER_REQUIRED

The non-scoring `reviewer-runner.ps1 -Mode Probe` asks a neutral candidate question and requires `project_history_or_prior_review_facts_used`. Host validation passes only when the result identifies `CANDIDATE-X`, says `none` for those facts, reports no external lookup, and contains no material fact absent from the fixed packet but present only in a host repository or prior design-lab receipt.

The physical platform probes show that host project paths, prior receipts, host Codex home, and canary directory are not visible. They do not substitute for a Codex-output contamination check. Any material leakage is `MEMORY_CONTAMINATION=FAIL` and blocks the harness.

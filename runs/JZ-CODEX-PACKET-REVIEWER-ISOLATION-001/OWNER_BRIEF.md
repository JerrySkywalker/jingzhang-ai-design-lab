# Owner brief

The packet and physical Windows Sandbox boundary are ready. Three fresh platform probes passed, but no person or process may treat this as a candidate score or start the jury yet.

1. Launch `reviewer-a.wsb`.
2. Inside it, run `./reviewer-runner.ps1 -Reviewer A -Mode Probe` and complete normal ChatGPT/Codex device sign-in.
3. Close the Sandbox after the non-scoring `reviewer-confinement-probe.txt` is written.
4. Let the host validate the probe for filesystem confinement and memory contamination.
5. Only after that PASS, launch fresh `harness-test-a.wsb`, repeat the in-Sandbox sign-in, and run `./reviewer-runner.ps1 -Reviewer A -Mode HarnessTest`.
6. Close it and provide only `output-a\harness-test-only.json` for host validation.

Do not use an API key, copy credentials, launch a host-side Codex session, score a candidate, change product content, change #2774, or begin the three-jury loop. B and C configurations are prepared for the later baseline Goal only.

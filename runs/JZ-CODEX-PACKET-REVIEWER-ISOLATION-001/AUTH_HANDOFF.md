# Authentication handoff

1. On the host, verify the packet manifest and platform probes before opening an Owner-authenticated Sandbox.
2. Launch `V:\src\_review_isolation\sandbox\reviewer-a.wsb`; it maps only the read-only packet, read-only dedicated runtime, and writable `output-a`.
3. In the prepared Sandbox PowerShell, run `./reviewer-runner.ps1 -Reviewer A -Mode Probe`.
4. Complete the normal ChatGPT/Codex `--device-auth` sign-in entirely inside that fresh Sandbox. Do not select API-key or access-token login and do not copy credentials from the host.
5. Let the non-scoring probe write `C:\ReviewerOutput\reviewer-confinement-probe.txt`, then close the Sandbox. Its `C:\CodexHome` and credential state are discarded.
6. The host validates the returned output. Only after every probe gate passes, launch the separate fresh `harness-test-a.wsb` and run `./reviewer-runner.ps1 -Reviewer A -Mode HarnessTest`; sign in again inside that new Sandbox.
7. Close the Sandbox after `harness-test-only.json` is written. The host reads only the mapped output after the instance has closed.

Repeat the probe with B and C only under a future three-jury Goal. No token, auth file, browser profile, host Codex home, Git configuration, or API key is copied into the harness or receipts.

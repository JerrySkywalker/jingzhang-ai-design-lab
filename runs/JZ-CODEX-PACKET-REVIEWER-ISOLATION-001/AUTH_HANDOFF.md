# Authentication handoff

1. Launch one fresh `reviewer-a.wsb` configuration from `V:\src\_review_isolation\sandbox`.
2. Inside the Sandbox, open the prepared PowerShell window and run `./reviewer-runner.ps1 -Reviewer A`.
3. Complete normal ChatGPT/Codex device sign-in when the CLI requests it. Do not select API-key or access-token login.
4. The runner creates a new `C:\CodexHome`, uses `codex exec --ephemeral`, `--ignore-user-config`, and `--ignore-rules`, and writes only to `C:\ReviewerOutput`.
5. Close the Sandbox after the output is written. Its credential state is destroyed with the Sandbox.

No token, auth file, browser profile, or host Codex home is copied into the harness or receipts.

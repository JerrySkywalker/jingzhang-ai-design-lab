# Owner brief

Use these three commands only.  The launcher resolves the declared harness root directly and starts Reviewer A only.  After the Sandbox opens, complete the normal ChatGPT/Codex device sign-in inside that fresh Sandbox when prompted; do not use an API key or copy host credentials.  Close the Sandbox after the non-scoring probe completes before running the final host command.

## A. Host: launch Reviewer A Probe

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File V:\src\_review_isolation\Start-JZReviewerAProbe.ps1
```

## B. Sandbox: run Probe

```powershell
Set-Location C:\ReviewerRuntime; .\reviewer-runner.ps1 -Reviewer A -Mode Probe
```

## C. Host after closing Sandbox: inspect result

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File V:\src\_review_isolation\Get-JZReviewerProbeStatus.ps1
```

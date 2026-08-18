# Launcher validation

The host launcher and status script reside in the approved harness root:

```text
HOST_LAUNCHER=V:\src\_review_isolation\Start-JZReviewerAProbe.ps1
HOST_STATUS_SCRIPT=V:\src\_review_isolation\Get-JZReviewerProbeStatus.ps1
```

Host-side validation completed without launching an Owner-authenticated Sandbox:

| Check | Result |
| --- | --- |
| PowerShell parser, launcher | PASS |
| PowerShell parser, status script | PASS |
| Launcher functional dry-run with `Start-Process` mocked | PASS; selected only `C:\WINDOWS\System32\WindowsSandbox.exe` and `reviewer-a.wsb` |
| WSB XML and mapped-path validation | PASS |
| Runner parser | PASS |
| Windows Sandbox executable | PASS: `C:\WINDOWS\System32\WindowsSandbox.exe` |
| Windows Sandbox optional feature | PASS: `Containers-DisposableClientVM`, `InstallState=1` |
| Read-only status script | PASS; configuration, runner, packet, and `output-a` found |

The dry-run performed no Sandbox launch, no login, no Codex execution, and no candidate scoring.  It is not evidence of memory-contamination or harness-test qualification.  The only interactive step remains the Owner's normal ChatGPT/Codex device sign-in inside the disposable Sandbox.

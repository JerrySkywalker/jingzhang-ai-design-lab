# Isolation backend audit

WINDOWS_SANDBOX_STATE=WINDOWS_SANDBOX_READY

Read-only evidence: Windows 10 Pro; `C:\Windows\System32\WindowsSandbox.exe` exists; `Win32_OptionalFeature` reports `Containers-DisposableClientVM` install state `1` (enabled); Hyper-V services are running; and three new Sandbox instances completed the physical probes. The privileged DISM feature query was not used after it requested elevation. No Windows feature, service, policy, or network configuration was changed.

No ordinary-host Codex fallback is permitted. CLI-level `--sandbox read-only` remains defense in depth and is never accepted as physical packet confinement.

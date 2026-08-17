# Isolation backend audit

WINDOWS_SANDBOX_STATE=WINDOWS_SANDBOX_READY

Evidence: Windows 10 Pro, `C:\Windows\System32\WindowsSandbox.exe` present, and three newly launched Sandbox instances completed the physical confinement probe. The non-elevated optional-feature query was unavailable; no feature was enabled or changed.

No ordinary-host Codex fallback is permitted. The previous host-side `codex exec --sandbox read-only` approach remains invalid for packet confinement.

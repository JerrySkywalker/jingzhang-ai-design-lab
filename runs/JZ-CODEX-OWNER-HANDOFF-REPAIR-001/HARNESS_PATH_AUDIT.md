# Harness path audit

```text
HARNESS_ROOT=V:\src\_review_isolation
REVIEWER_A_WSB=V:\src\_review_isolation\sandbox\reviewer-a.wsb
REVIEWER_B_WSB=V:\src\_review_isolation\sandbox\reviewer-b.wsb
REVIEWER_C_WSB=V:\src\_review_isolation\sandbox\reviewer-c.wsb
REVIEWER_RUNNER=V:\src\_review_isolation\runtime\reviewer-runner.ps1
PACKET_ROOT=V:\src\_review_isolation\packet
RUNTIME_ROOT=V:\src\_review_isolation\runtime
OUTPUT_A=V:\src\_review_isolation\output-a
OUTPUT_B=V:\src\_review_isolation\output-b
OUTPUT_C=V:\src\_review_isolation\output-c
```

All listed paths passed `Test-Path`.  `reviewer-a.wsb`, `reviewer-b.wsb`, and `reviewer-c.wsb` each parse as XML and contain exactly three mapped folders:

| Configuration | Packet | Runtime | Reviewer output |
| --- | --- | --- | --- |
| `reviewer-a.wsb` | `packet` read-only to `C:\ReviewPacket` | `runtime` read-only to `C:\ReviewerRuntime` | `output-a` writable to `C:\ReviewerOutput` |
| `reviewer-b.wsb` | `packet` read-only to `C:\ReviewPacket` | `runtime` read-only to `C:\ReviewerRuntime` | `output-b` writable to `C:\ReviewerOutput` |
| `reviewer-c.wsb` | `packet` read-only to `C:\ReviewPacket` | `runtime` read-only to `C:\ReviewerRuntime` | `output-c` writable to `C:\ReviewerOutput` |

Every configured host mapping resolves below `V:\src\_review_isolation`; none maps `V:\`, `V:\src`, a host profile, host Codex state, Git/SSH state, browser state, or another reviewer output.  Protected Client is enabled; clipboard, printer, audio input, video input, and vGPU are disabled.  The network setting remains enabled only for the Owner's normal in-Sandbox Codex device sign-in; the runner disables Codex reviewer-tool network access before the non-scoring probe.

`REVIEW_PACKET_MANIFEST.json`, `reviewer-runner.ps1`, and `output-a` are present.  No harness configuration required modification.

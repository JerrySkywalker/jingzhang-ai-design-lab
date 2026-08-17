# Sandbox layout

Host root: `V:\src\_review_isolation`

| Sandbox path | Host path | Access |
| --- | --- | --- |
| `C:\ReviewPacket` | `packet` | Read-only |
| `C:\ReviewerRuntime` | `runtime` | Read-only |
| `C:\ReviewerOutput` | `output-a`, `output-b`, or `output-c` | Writable, reviewer-specific |

Six configurations exist: fresh `probe-a/b/c.wsb` instances for automatic non-auth confinement checks and fresh `reviewer-a/b/c.wsb` instances for the Owner-mediated Codex harness. No configuration maps `V:\src`, host home, host Codex state, Git/SSH state, browser state, prior receipt, or another output folder. Clipboard, printer, audio/video input, and vGPU are disabled. Networking is retained only for the Codex transport and remains a harness-test gate.

# Sandbox layout

Host root: `V:\src\_review_isolation`

| Sandbox path | Host path | Access |
| --- | --- | --- |
| `C:\ReviewPacket` | `packet` | Read-only |
| `C:\ReviewerRuntime` | `runtime` | Read-only |
| `C:\ReviewerOutput` | exactly one of `output-a`, `output-b`, or `output-c` | Writable |

`probe-a/b/c.wsb` are automatic physical-platform checks with networking disabled. `reviewer-a/b/c.wsb` are fresh Owner-authenticated Codex confinement probes. `harness-test-a.wsb` is a separate fresh disposable-scorecard test. Every configuration enables Protected Client and disables clipboard, printer, audio input, video input, and vGPU. Reviewer configurations enable networking solely for Codex transport; the runtime sets the CLI's direct reviewer-tool network-disable control after login.

No configuration maps `V:\src`, a host home/profile, host Codex state, Git/SSH state, browser state, prior receipts, or another reviewer output folder. The `.wsb` files themselves are host launch configuration, not Sandbox mappings.

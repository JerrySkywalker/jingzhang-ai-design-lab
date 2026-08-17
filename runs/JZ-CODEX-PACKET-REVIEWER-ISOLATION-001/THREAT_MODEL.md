# Threat model

## Protected host state

The reviewer must not read the host workspace, repositories, prior receipts, user profile, Codex home/configuration, Git/SSH state, browser state, or a different reviewer's output. Host canaries are outside every Sandbox mapping and their contents are absent from prompts, packets, and committed receipts.

## Trust boundary

The only host-derived folders mapped into a reviewer Sandbox are the fixed packet and a dedicated runtime, both read-only, plus that reviewer's writable output folder. Windows Sandbox provides the physical host-filesystem boundary; Codex `read-only` sandboxing is defense in depth only and is not accepted as the physical boundary.

## Residual risk and gate

The Sandbox network remains enabled for the Codex transport. The current CLI exposes an ephemeral session and a read-only execution sandbox but no documented `exec` flag that independently proves shell egress blocking while transport remains available. A fresh Owner-authenticated harness test must therefore prove packet-only behavior before any real jury is admitted.

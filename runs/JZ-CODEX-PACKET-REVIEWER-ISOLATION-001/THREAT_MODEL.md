# Threat model

## Protected host state

The reviewer must not read the host workspace, repositories, prior receipts, user profile, Codex home/configuration, Git/SSH state, browser state, or a different reviewer's output. The canary directory is outside all mappings; its contents are absent from packet, runtime prompt, and committed receipts.

## Physical boundary

Each fresh Windows Sandbox maps exactly three folders: fixed packet read-only, dedicated runtime read-only, and that reviewer's output writable. Protected Client is enabled. Windows Sandbox, not Codex's read-only sandbox, supplies physical host-filesystem confinement.

## Session and context boundary

The runner creates `C:\CodexHome` in the disposable VM and uses `codex exec --ephemeral --ignore-user-config --ignore-rules`, with no resume command. No authentication material is copied. A closed Sandbox deletes the in-VM credential state. A/B/C never map one another's output.

## Network boundary and fail-closed gate

Codex transport needs Sandbox networking. After in-Sandbox sign-in, the runner sets `CODEX_SANDBOX_NETWORK_DISABLED=1`, requests `sandbox_workspace_write.network_access=false`, keeps `--sandbox read-only`, and disables apps/plugins/hooks/browser/computer-use/remote-plugin/skill-search. The runtime exposes Windows restricted-token network-disable capability, but the Owner-authenticated probe must still demonstrate that Codex transport succeeds without reviewer tool egress. If the control blocks transport, allows external lookup, or cannot be shown to separate those paths, `ISOLATION_STATUS=BLOCKED_NO_APPROVED_BACKEND` for this runtime and no jury may run.

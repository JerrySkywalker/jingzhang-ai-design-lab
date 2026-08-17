# Confinement probe

Three fresh non-authenticated Windows Sandbox instances were rerun after hardening. Each used `ProtectedClient=Enable`, disabled networking, clipboard, printer, audio, video, and vGPU, and mapped only its own output directory.

| Check | A | B | C |
| --- | --- | --- | --- |
| Packet readable | PASS | PASS | PASS |
| Filesystem roots | `C:\` only | `C:\` only | `C:\` only |
| `V:\src` visible | false | false | false |
| Host profile visible | false | false | false |
| Host Codex home visible | false | false | false |
| Host canary directory visible | false | false | false |
| Other reviewer output visible | false | false | false |
| Dedicated runtime reports Codex 0.147.0 | PASS | PASS | PASS |

These platform probes record booleans and roots only; no canary content is included. `HOST_CANARY_NOT_VISIBLE=true`, `V_DRIVE_NOT_VISIBLE=true`, `HOST_CODEX_HOME_NOT_VISIBLE=true`, and `OTHER_REVIEW_OUTPUT_NOT_VISIBLE=true` are physically evidenced at the Windows Sandbox layer.

The separate Owner-authenticated Codex probe remains required. It must return the prescribed non-scoring fields, must report no project-history or prior-review facts, and must not score the proposal.

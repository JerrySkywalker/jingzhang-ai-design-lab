# Confinement probe

Three fresh non-authenticated Windows Sandbox instances completed the probe, one each for A, B, and C.

| Check | A | B | C |
| --- | --- | --- | --- |
| Packet readable | PASS | PASS | PASS |
| `V:\src` visible | false | false | false |
| Host profile visible | false | false | false |
| Host Codex home visible | false | false | false |
| Host canary directory visible | false | false | false |
| Other reviewer output visible | false | false | false |
| Dedicated runtime reports expected CLI version | PASS | PASS | PASS |

The probe reports only booleans and filesystem roots; no canary content is included. `HOST_CANARY_NOT_VISIBLE=true`, `V_DRIVE_NOT_VISIBLE=true`, `HOST_CODEX_HOME_NOT_VISIBLE=true`, and `OTHER_REVIEW_OUTPUT_NOT_VISIBLE=true` are physically evidenced at the Windows Sandbox layer.

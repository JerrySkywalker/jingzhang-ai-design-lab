# Final report

```text
HANDOFF_REPAIR_STATUS=PASS_HOST_SIDE_OWNER_HANDOFF_READY
RUN_ID=JZ-CODEX-OWNER-HANDOFF-REPAIR-001

ROOT_CAUSE=SEARCH_FAILURE: broad recursive Get-ChildItem with ErrorAction Stop terminated on unrelated AccessDenied before reviewer-a.wsb discovery

ISOLATION_RECEIPT_HEAD=b2885f57f7905ca5569b40784a8b5d7c115b12b3
HARNESS_ROOT=V:\src\_review_isolation

REVIEWER_A_WSB=V:\src\_review_isolation\sandbox\reviewer-a.wsb
REVIEWER_B_WSB=V:\src\_review_isolation\sandbox\reviewer-b.wsb
REVIEWER_C_WSB=V:\src\_review_isolation\sandbox\reviewer-c.wsb
REVIEWER_RUNNER=V:\src\_review_isolation\runtime\reviewer-runner.ps1

PACKET_ROOT=V:\src\_review_isolation\packet
RUNTIME_ROOT=V:\src\_review_isolation\runtime
OUTPUT_A=V:\src\_review_isolation\output-a

WINDOWS_SANDBOX_STATE=WINDOWS_SANDBOX_READY

WSB_CONFIG_VALID=true
MAPPED_PATHS_VALID=true
ISOLATION_CONTRACT_PRESERVED=true

HOST_LAUNCHER=V:\src\_review_isolation\Start-JZReviewerAProbe.ps1
HOST_STATUS_SCRIPT=V:\src\_review_isolation\Get-JZReviewerProbeStatus.ps1

HOST_LAUNCH_COMMAND=powershell.exe -NoProfile -ExecutionPolicy Bypass -File V:\src\_review_isolation\Start-JZReviewerAProbe.ps1
SANDBOX_PROBE_COMMAND=Set-Location C:\ReviewerRuntime; .\reviewer-runner.ps1 -Reviewer A -Mode Probe
HOST_RESULT_COMMAND=powershell.exe -NoProfile -ExecutionPolicy Bypass -File V:\src\_review_isolation\Get-JZReviewerProbeStatus.ps1

OWNER_INTERACTIVE_LOGIN_REQUIRED=true

MEMORY_CONTAMINATION=NOT_YET_PROVEN
HARNESS_TEST=NOT_YET_PROVEN

PRODUCT_MUTATED=false
PRODUCT_PUSHED=false
PR_2774_MUTATED=false
OFFICIAL_REPOSITORY_MUTATED=false

DESIGNLAB_BRANCH=runs/JZ-CODEX-OWNER-HANDOFF-REPAIR-001
DESIGNLAB_HEAD=COMMIT_CONTAINING_THIS_RECEIPT
DESIGNLAB_PUSH_STATUS=POST_COMMIT_PUSH_REQUIRED

NEXT_OWNER_ACTION=RUN_REVIEWER_A_PROBE
|
OWNER_REQUIRED
```

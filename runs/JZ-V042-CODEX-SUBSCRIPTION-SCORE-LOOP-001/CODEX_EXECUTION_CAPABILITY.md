# Codex execution capability

CODEX_VERSION=codex-cli 0.147.0
CLI_ISOLATED_REVIEW_SESSION_FEATURES_SUPPORTED=true
ISOLATED_REVIEW_SESSION_SUPPORTED=false
SELECTED_EXECUTION_METHOD=`codex exec --ephemeral --skip-git-repo-check --sandbox read-only --output-schema <schema> -C <neutral-packet>`
AUTH_MODE=EXISTING_CODEX_SUBSCRIPTION
API_KEY_USED=false

`codex exec --help` documents non-interactive execution, ephemeral sessions, read-only sandboxing, structured output, and a separate working directory. It does not expose `--ask-for-approval`; the selected command therefore uses only its documented options.

Execution conclusion: the documented CLI features launched separate ephemeral read-only processes, but packet-only isolation was not achieved because a reviewer attempted to inspect host memory outside the neutral packet. The incomplete outputs are invalid and were stopped; no score may be accepted or retried under the anti-score-fishing contract.

# Codex runtime capability

CODEX_VERSION=codex-cli 0.147.0
CODEX_EXEC_AVAILABLE=true
EPHEMERAL_SUPPORTED=true
SANDBOX_FLAGS_AVAILABLE=true
WORKING_DIRECTORY_SUPPORTED=true
JSON_SUPPORTED=true
OUTPUT_SCHEMA_SUPPORTED=true
IGNORE_USER_CONFIG_SUPPORTED=true
IGNORE_RULES_SUPPORTED=true
MCP_PLUGIN_DISABLE_SUPPORTED=true

Observed `codex exec` flags: `--ephemeral`, `--sandbox read-only`, `--cd`, `--skip-git-repo-check`, `--ignore-user-config`, `--ignore-rules`, `--output-schema`, `--output-last-message`, `--json`, image inputs, and repeated `--disable`. `codex resume` is a separate subcommand and is prohibited by the harness.

Observed `codex sandbox` capability: a Windows restricted-token command with explicit readable roots and `--sandbox-state-disable-network`; a smoke command ran under its constrained language mode. This is defense in depth, not the physical confinement boundary. The reviewer runner additionally sets `CODEX_SANDBOX_NETWORK_DISABLED=1` after interactive login and passes `sandbox_workspace_write.network_access=false` before each read-only execution. The Owner test is still the authority for whether this installed runtime maintains Codex transport while refusing reviewer-tool egress.

The runtime bundle contains only Node 24.19.0, Codex CLI 0.147.0 and its required platform package, plus harness scripts. It contains no host Codex configuration, auth file, Git configuration, SSH material, browser state, or plugin/MCP configuration. The fresh Sandbox runner creates `C:\CodexHome`, uses `--ephemeral --ignore-user-config --ignore-rules`, disables apps, plugins, hooks, browser, computer-use, remote-plugin, and skill-search features, and never invokes resume.

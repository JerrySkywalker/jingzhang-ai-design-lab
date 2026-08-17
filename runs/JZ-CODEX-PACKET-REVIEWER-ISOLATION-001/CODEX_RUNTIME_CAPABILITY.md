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

Observed `codex exec` flags: `--ephemeral`, `--sandbox read-only`, `--cd`, `--skip-git-repo-check`, `--ignore-user-config`, `--ignore-rules`, `--output-schema`, `--output-last-message`, `--json`, and image inputs. `codex resume` is a separate subcommand and is prohibited by the harness.

Observed `codex sandbox` capability: a Windows restricted-token command with explicit readable roots and a `--sandbox-state-disable-network` option. It is not used as a substitute for Windows Sandbox. The reviewer command uses a new `CODEX_HOME` inside the Sandbox and never maps or copies host Codex state.

The generated reviewer command explicitly disables the CLI features apps, plugins, browser_use, browser_use_external, computer_use, in_app_browser, remote_plugin, and skill_search; it retains --sandbox read-only for model-generated shell commands. Runtime layout contains only a copied Node executable, the installed Codex npm package, and harness scripts. No host Codex configuration, auth file, Git config, SSH material, or browser profile is copied.

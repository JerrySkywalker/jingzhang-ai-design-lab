# JZ97 Codex-native panel migration

Active train: `JZ97-CODEX-NATIVE-CONVERGENCE-TRAIN-001`

`LEGACY_G03_G06_EXECUTION=SUPERSEDED_BY_CODEX_NATIVE_PANEL`

The current formal-local evaluation path is `tools/codex_jury/Invoke-CodexJury.ps1`. It uses a dual-profile, non-interactive Codex panel with one fresh `codex exec` process per reviewer and packet, structured output, deterministic weighting, blind sanitized packet views, and at-most-once review receipts.

The following historical assets remain preserved but are not current execution paths:

| Historical surface | State |
| --- | --- |
| AGY formal reviewer execution | `LEGACY_FROZEN` / `NOT_CURRENT_EXECUTION_PATH` |
| Windows Sandbox `.wsb` orchestration | `LEGACY_FROZEN` / `NOT_CURRENT_EXECUTION_PATH` |
| Google OAuth device authentication | `LEGACY_FROZEN` / `NOT_CURRENT_EXECUTION_PATH` |
| WSB GUID lifecycle tracking | `LEGACY_FROZEN` / `NOT_CURRENT_EXECUTION_PATH` |
| Guest bootstrap and shutdown automation | `LEGACY_FROZEN` / `NOT_CURRENT_EXECUTION_PATH` |

Historical files and receipts are intentionally retained. No legacy WSB test expansion is part of this train.

The official rubric, integer `0..5` schema, weights, anchor provenance, blind packet assets, deterministic formula, and useful aggregation/calibration logic remain active inputs. Local results remain formal local evidence, never official scores.

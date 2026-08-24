# Codex-native JZ97 panel

`Invoke-CodexJury.ps1` is the current non-interactive formal-local evaluation path.

It prepares identity-sanitized packet views, validates the installed model catalog, launches one fresh `codex exec` process per reviewer and packet, validates structured scorecards, and computes calibration/candidate/blocker results. Every review uses `--ephemeral`, `--sandbox read-only`, `--ignore-user-config`, `--ignore-rules`, `--output-schema`, an explicit model, and an explicit reasoning setting.

The reviewer runs from an empty working directory and sees only a neutral packet id (`P01` through `P08`), a bounded text evidence envelope on stdin, explicitly attached packet images, the rubric, and the scoring prompt. Coordinator mappings and official anchor scores stay outside reviewer inputs.

```powershell
pwsh -NoProfile -File tools/codex_jury/Invoke-CodexJury.ps1 -Action All
```

Existing attempt receipts make review execution at-most-once. A failed invocation is evidence and is not automatically rerun.

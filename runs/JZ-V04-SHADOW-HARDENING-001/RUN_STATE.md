# JZ-V04-SHADOW-HARDENING-001 — run state

## Admission

- `TRUSTED_BASELINE_HEAD=1d5cb1aaa9d76edc3532e593c803cb936070a744`
- `TRUSTED_BASELINE_SCORE=77`
- `CERTIFIED_V04_HEAD=ac2a41c7f07721349d975ded8ad550a8795bb438`
- `V04_IMMUTABLE=true`
- `V04_BRANCH_MUTATED=false`
- `PR_2774_MUTATED=false`
- `OFFICIAL_REPO_MUTATED=false`

Both commit objects were locally present. Live read-only GitHub evidence refreshed #2774 as OPEN/Draft at the certified head with 24 paths wholly under `submissions/JerrySkywalker/jingzhang-in-place/`. Baseline #2744 is MERGED and carries the exact-head 77/100 trusted review.

## Workspace boundary

Product evidence was archived read-only beneath local ignored `snapshots/`; no proposal content was added to the design-lab Git history. Durable tooling and receipts are on `runs/JZ-V04-SHADOW-HARDENING-001`, based on design-lab `origin/main@a542fd7f3538a793b6fadfd74ee13467c4942e12`.

The only experiment is a separate local haidian worktree from the exact certified SHA: `experiment/JZ-V041-SHADOW-HARDENING-001`. It has never been pushed and never affected the certified branch.

## Current official-policy observation

- upstream main observed: `43c946113afc03ed9f50bdf83940362b7941b7fe`
- current validation still skips Draft PRs
- current auto-review absolute threshold: 60
- active deployed high-water protection for the Jing-Zhang directory/77 score: not proven; current source shows none
- intervening current-main paths from locally trusted tooling snapshot `2d44121b…` were peer submissions only

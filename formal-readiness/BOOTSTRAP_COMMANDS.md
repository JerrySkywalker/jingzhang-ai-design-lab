# Bootstrap Commands

## Rehearsal command actually exercised

This no-fork command is for the disposable scratch rehearsal only. It clones canonical as `origin`, creates a local dummy branch and never pushes.

```powershell
$officialRepo = 'V:\src\_worktrees\JZ-C04-OFFICIAL-READONLY-001'
$scratchRepo = 'V:\src\_scratch\JZ-FORMAL-REHEARSAL'

git -C $officialRepo fetch origin main
git -C $officialRepo show origin/main:scripts/bootstrap_participant_workspace.py |
  py -V:Astral\CPython3.12.13 - `
    --repo-url https://github.com/open-city-ai/haidian `
    --upstream-url https://github.com/open-city-ai/haidian.git `
    --github-login r5-rehearsal `
    --proposal-slug dummy-formal-rehearsal `
    --work-branch rehearsal/r5-formal-dummy `
    --target $scratchRepo `
    --json
```

Receipt: shallow sparse partial clone (`blob:none`) succeeded at `9407689a4bb5d083e885ac5696dc95db7477b0eb`; no fork, commit, push or PR was made.

## Review dependencies

```powershell
Set-Location V:\src\_scratch\JZ-FORMAL-REHEARSAL
uv venv --python 3.12 .venv
uv pip install --python .venv\Scripts\python.exe -r requirements-review.txt
$rehearsalPython = '.venv\Scripts\python.exe'
```

Frozen rehearsal versions:

```text
Python=3.12.13
jsonschema=4.26.0
Pillow=12.3.0
pyproj=3.7.2
shapely=2.1.2
numpy=2.5.2
```

## Scaffold and incremental build

```powershell
$pkg = 'submissions/r5-rehearsal/dummy-formal-rehearsal'
& $rehearsalPython scripts/scaffold_ai_submission.py $pkg `
  --stage formal `
  --agent-id r5-rehearsal `
  --agent-name 'R5 Formal Rehearsal Agent' `
  --proposal-title 'R5 Formal Rehearsal Dummy'
& $rehearsalPython scripts/render_proposal_html.py $pkg
```

Both commands succeeded. The scaffold is intentionally invalid until real bilingual content, geometry, figures and PDFs replace placeholders.

## Candidate-lock change

After Owner lock, replace dummy identity/slug and use the Owner's actual fork URL as `repo-url`. Do not reuse the no-fork rehearsal origin for a real submission. Reinspect the helper at current official main before execution.

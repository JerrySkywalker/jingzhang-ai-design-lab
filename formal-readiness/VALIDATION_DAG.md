# Validation DAG

## Exact rehearsal sequence

```powershell
& $rehearsalPython scripts/finalize_submission.py $pkg
& $rehearsalPython scripts/validate_local_submission.py $pkg --repo-root . --pr-author r5-rehearsal --json
& $rehearsalPython scripts/spatial_review.py $pkg --repo-root . --json
& $rehearsalPython scripts/visual_review.py $pkg --json
& $rehearsalPython scripts/professional_review.py $pkg --repo-root . --json
& $rehearsalPython scripts/self_check_submission.py $pkg --repo-root . --pr-author r5-rehearsal --json
& $rehearsalPython scripts/participant_preflight.py $pkg --repo-root . --pr-author r5-rehearsal --skip-self-check --allow-canonical-origin --json
& $rehearsalPython scripts/participant_preflight.py $pkg --repo-root . --pr-author r5-rehearsal --allow-canonical-origin --json
```

Never use `--check-push` during rehearsal; it calls `git push --dry-run origin`. Never use `--mark-self-checked` on a dummy.

## Rehearsal receipt

| Gate | Exit | Interpretation |
|---|---:|---|
| bootstrap | 0 | PASS |
| scaffold | 0 | PASS |
| render primary HTML | 0 | PASS |
| finalize | 1 | EXPECTED FAIL: unchanged scaffold, placeholder figures/PDFs, bilingual twins absent |
| deterministic validation | 1 | EXPECTED FAIL: scaffold contract and bilingual/PDF failures |
| spatial review | 0 | PASS with three provisional-key-area minor issues |
| visual review | 0 | PASS on placeholder structure only; not evidence of finished graphics |
| professional review | 0 | PASS on scaffold reference/matrix structure only; not formal readiness |
| self-check | 1 | EXPECTED FAIL because deterministic validation fails |
| preflight `--skip-self-check` | 0 | PASS: workspace/scope/origin mechanics work |
| full preflight | 1 | EXPECTED FAIL solely because self-check/content is incomplete |

```text
VALIDATOR_REHEARSAL_RESULT=EXECUTED_EXPECTED_SCAFFOLD_REJECTION
```

## Production order

Run deterministic, spatial, visual and professional reviews incrementally. At feature freeze:

1. render both proposal HTML files;
2. finalize only after all real bilingual artifacts replace placeholders;
3. run all four reviews via self-check;
4. after PASS, run `--mark-self-checked` once on the exact intended head;
5. run full participant preflight without `--allow-canonical-origin` against the real fork;
6. audit hashes/status again before push/PR.

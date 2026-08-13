# Validation ledger — crash-recovery tail

All entries below are from this recovery session and the current upstream toolchain at `64f424a7026e1e4e1d5d9fbe61e89a53467abf44`.

| Check | Result | Evidence / handling |
| --- | --- | --- |
| `render_proposal_html.py` | PASS | Regenerated paired offline `report/proposal.html` and `report/proposal.en.html` after the latest merge. |
| `finalize_submission.py` | EXPECTED_READY_PACKAGE_GUARD | It exits with `package_state must be scaffold before finalization`; the package was already `ready_for_review`. No hand edit or rollback was made. |
| `refresh_submission_manifest.py --json` | PASS | Official refresh ran after bounded figure/PDF/copyright/changelog changes and set self-check false as designed. |
| deterministic validation | PASS | No errors; one existing provisional-boundary warning. |
| spatial review | PASS | Three `KEY_AREA_PROVISIONAL` minor notices only; content scoring remains eligible and official-area claims are not made. |
| visual review | PASS | Offline visual page and displayed metrics passed. |
| professional evidence review | PASS | 5 standard-matrix items, 15/15 complete depth items, and v2 evidence contract passed. |
| `self_check_submission.py --mark-self-checked --json` | PASS | `ok=true`, `review_status=formal-review-ready`, `can_enter_formal_review=true`, manifest self-check persisted. |
| `participant_preflight.py --check-push` | PASS | Scope, package size, fork/upstream checks, current self-check and remote push dry-run all passed. |
| bilingual audit | PASS | `audit_bilingual_backfill.py` reported one paired bilingual submission audited successfully. |
| `git diff --check` | PASS for non-PDF content; PDF-stream notice logged | The full PR diff returns exit 2 only because ReportLab ASCII85 PDF streams contain valid end-of-line whitespace. Excluding the four binary PDFs returns exit 0; JSON/GeoJSON/text changes are clean. |

## Recoverable local toolchain event

The first current self-check found missing local Python review dependencies (`jsonschema`, `shapely`, `pyproj`). They were installed from the repository's `requirements-review.txt`, then the unchanged package passed all four gates. This was a local environment gap, not a package schema or design failure.

## Final current state

- `package_state=ready_for_review`
- `validation_claim.self_checked=true`
- `self_check.ok=true`
- `review_status=formal-review-ready`
- `can_enter_formal_review=true`

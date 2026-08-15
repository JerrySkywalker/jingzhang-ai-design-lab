# v0.4.1a validation report

All commands ran locally in the v0.4.1a experiment worktree.

| Check | Result |
| --- | --- |
| `validate_local_submission.py` | PASS |
| `self_check_submission.py` | PASS; formal-review-ready |
| `spatial_review.py` | PASS; three pre-existing provisional-key-area notices only |
| `visual_review.py` | PASS |
| `professional_review.py` | PASS |
| `jz_review_packet` v0.4 → v0.4.1a | PASS; 8 files, +35 text bytes, no stop-ship regression |
| `jz_review_packet` v0.4.1 → v0.4.1a | PASS; 8 files, +10 text bytes, no stop-ship regression |
| `jz_release_gate` fixture suite | PASS; 9 tests |
| all reusable-tool tests | PASS; 12 tests |
| Python compilation / `git diff --check` | PASS |

The changed-file set is exactly: `proposal.md`, `proposal.en.md`,
`report/copyright_statement.md`, `visual/assets/ai-spatial-admission.json`, both rendered
proposal HTML files, `manifest.json`, and `self_check.json`.

`FIGURE_HASHES_UNCHANGED=true` and `PDF_HASHES_UNCHANGED=true` by direct SHA-256 comparison.
`GEOMETRY_UNCHANGED=true` by Git-normalized blob hash comparison; raw Windows checkout bytes
have CRLF representation differences but no Git-stored geometry change. `STATUS_ACTION`,
12-to-3/S01-S04-S07, NO BUILD count, and AI-off-city all remain preserved.

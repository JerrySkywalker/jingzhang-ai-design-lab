# Current upstream delta and convergence

The branch carried `56a21c92e9f961359d868fabde30ae85e139857f` as its previous
upstream ancestor. Fresh admission resolved `upstream/main` to `b8e630…`.

The `56a21c…...b8e630…` delta contained 1,316 files: 1,304 peer-submission
files and these 12 non-peer files:

| Class | Paths |
| --- | --- |
| Participant workflow / validator / review tooling | `scripts/finalize_submission.py`, `scripts/refresh_submission_manifest.py`, `scripts/spatial_review.py`, `scripts/validate_submission.py`, `scripts/visual_review.py` |
| Supporting official helper modules | `scripts/git_blob_hashes.py`, `scripts/metric_types.py` |
| Official regression tests | `tests/test_agent_scaffold_and_self_check.py`, `tests/test_git_blob_hashes.py`, `tests/test_metric_types.py`, `tests/test_spatial_review.py`, `tests/test_visual_review.py` |

There were no canonical brief, schema, source registry, guide, rubric, or
requirements-review changes in that non-peer set. The official hash and numeric
rules are participant-facing, so one normal auditable merge was required and
performed (`b837f4e…`).

Terminal fetch moved `upstream/main` to `90a61c6…`. The final
`b8e630…...90a61c…` delta has 267 paths, all under `submissions/`.
Classification: **PEER_SUBMISSIONS_ONLY**. It was intentionally not merged.

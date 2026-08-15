# Upstream drift audit

The v0.4 certification merge base was `cdc56d33f322e01477c4b29adba0f1dae4524e41`. At rehearsal start, `upstream/main` was `6ee92a35ae6d3be0bbec2954009c7298901a4e13`.

`cdc56d33..6ee92a35` changed 584 paths: 581 peer-submission paths plus `scripts/manifest_schema.py`, `skills/urban-design-ai-submission/SKILL.md`, and `tests/test_manifest_schema.py`. The strict aggregate classifier is `UNKNOWN`; the manifest-schema change is defensive for non-list `files` values and does not alter this valid manifest. Every current participant executable inspected for this rehearsal was byte-identical across those refs:

- `self_check_submission.py`, `validate_local_submission.py`, `spatial_review.py`, `visual_review.py`, `professional_review.py`, `participant_preflight.py`, and `refresh_submission_manifest.py`
- `github_pr_validation.py`, `ai_review_submission.py`, `auto_review_queue.py`, and `.github/workflows/submission-validation.yml`

Near the end of the run `upstream/main` advanced to `40c3db6e13064e3d24038f7b393f0f572c22e83c`. The `6ee92a35..40c3db6e` delta has 185 paths, all beneath other participants' `submissions/`; classifier: `PEER_SUBMISSIONS_ONLY`.

Conclusion: the current trusted tooling used for the rehearsal is unchanged. A future release must still fetch and reclassify then-current upstream before creating a successor branch.

# Current Official Queue Policy and High-Water Status

- Authority Source: `open-city-ai/haidian` (`scripts/auto_review_queue.py`)
- Upstream Head: `78db36c91e1c604c3fc5702f8cb7be4ac4b01e5a`

## 1. Queue Eligibility Criteria

A Pull Request is eligible for automated maintainer review when:
1. State is `OPEN` and `isDraft` is `false`.
2. Has label `review/queued`.
3. Mergeable state is NOT `CONFLICTING`.
4. GitHub Actions `submission-validation` check status is `COMPLETED` with conclusion `SUCCESS`.

## 2. Decision Logic and Acceptance Semantics

The automated worker executes `scripts/ai_review_submission.py` and applies `decide()`:
- Mandatory Rejection hit -> `request-changes` (reason: `mandatory rejection hit`)
- Any of the 4 gates FAIL -> `request-changes` (reason: `failed gates: <list>`)
- Score < 60.0 -> `low-quality` (changes requested; reason: `score below 60`)
- Score >= 60.0 and all gates PASS -> `accept` (merged with comment `<!-- haidian-auto-review:<head> -->`)

## 3. High-Water Protection Audit

- Code Inspection: `scripts/auto_review_queue.py` lines 140–165.
- Finding: The worker accepts any eligible PR with `score >= 60.0`. It does NOT check whether the author has a previously merged submission with a higher score.
- Status: `HIGH_WATER_GUARD_ACTIVE=false` in actual merged code/tests.
- Program Consequence: PR #2774 must remain in Draft and cannot be submitted to the queue until high-water protection is active or explicitly accepted.

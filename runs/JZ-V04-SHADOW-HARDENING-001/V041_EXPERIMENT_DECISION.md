# v0.4.1 experimental-lane decision

`V041_EXPERIMENT_CREATED=true`

Entry threshold was met: all three initial independent reviewers identified the same material
weakness — the package asserted `FINAL_WINNER=JINGZHANG_IN_PLACE` while its copyright and
authority contract required `OWNER_DECISION_REQUIRED`. It could undermine the expected band by
making a human-authority claim internally inconsistent.

Local-only branch: `experiment/JZ-V041-SHADOW-HARDENING-001`.
Local-only head: `00e99480ee4ce3922125b62b9f47a087bd0c3038`.

The change normalises only the final-winner marker in the bilingual proposals, rendered reports,
and canonical admission JSON, then refreshes manifest and self-check receipts. It does not alter
STATUS × ACTION, 12-to-3, S01/S04/S07, interfaces, contracts, AI mechanisms, geometry, costs,
or peer semantics.

All three one-pass re-reviewers accepted it: real improvement, no substantive regression, and
simpler rather than denser. The full repository-aware self-check and regression harness passed.

`V041_EXPERIMENT_DECISION=WORTH_OWNER_REVIEW`

This is not a replacement of v0.4, a push, a PR action, or release authority.

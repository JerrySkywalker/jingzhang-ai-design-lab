# Disposable harness test

STATUS=OWNER_REQUIRED

The required fresh-Sandbox physical confinement probe is PASS. The remaining disposable test requires Owner device sign-in inside a new reviewer Sandbox. It will use `HARNESS_TEST_ONLY`, `NOT_CANDIDATE_SCORE`, and `DISCARD_FOR_SCORE_TRAJECTORY=true`; its output cannot become a v0.4.1a score or trajectory entry.

Accept only if the JSON schema validates, all visual attachments are readable, output is captured in the reviewer-specific output mapping, and the memory-contamination review is clean.

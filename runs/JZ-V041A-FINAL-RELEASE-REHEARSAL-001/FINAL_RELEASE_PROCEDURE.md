# Future release procedure

Run this only after a fresh live gate proves `SCORE_GUARD_ACTIVE=true`, `HISTORICAL_BEST=77`, and `HISTORICAL_BEST_PROVEN=true`.

1. Fetch latest `upstream/main`.
2. Classify upstream tooling drift; stop for non-peer changes until their implications are reviewed.
3. Create a fresh Owner-fork branch from current `upstream/main`.
4. Restore only the frozen v0.4.1a submission subtree from `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`.
5. Prove frozen hash guards, then run current validator, spatial, visual, professional, manifest refresh, persisted self-check, and preflight.
6. Push the new Owner-fork branch only after all local gates pass.
7. Fresh-clone the remote branch and repeat current certification.
8. Create a successor Draft PR with only the declared submission subtree.
9. Run the live release gate.
10. Prove historical best 77 and the active same-directory high-water guard.
11. Obtain Owner authorization for Ready.
12. Mark the successor Ready.
13. Require GitHub submission-validation to pass at the exact successor head.
14. Await the trusted Review Agent.
15. If trusted score is below 77: HOLD; do not merge.
16. If trusted score is 77 or above: it is eligible for normal merge authority.

Steps 6–16 were not executed during this rehearsal.

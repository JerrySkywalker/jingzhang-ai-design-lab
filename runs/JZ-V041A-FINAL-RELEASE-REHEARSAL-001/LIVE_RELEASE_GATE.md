# Live release gate

The read-only live GitHub observation returned:

```text
CURRENT_STATE=SAFE_WAIT
SAFE_TO_MARK_READY=false
HISTORICAL_BEST=77
HISTORICAL_BEST_PROVEN=true
SCORE_GUARD_ACTIVE=false
TOOLING_DRIFT_CLASS=PEER_SUBMISSIONS_ONLY
```

It proves the merged PR #2744 exact-head trusted score of 77, and observes PR #2774 as open, Draft, and still at `ac2a41c7f07721349d975ded8ad550a8795bb438`.

Current policy facts: Draft validation is skipped; the auto-review absolute threshold is 60; active high-water protection is absent. Score-guard PR #1725 remains open and unmerged at `64ce333738c0d2f0341198947f020aa1c373a0c0`. Consequently the gate fails closed and no Ready action is authorized.

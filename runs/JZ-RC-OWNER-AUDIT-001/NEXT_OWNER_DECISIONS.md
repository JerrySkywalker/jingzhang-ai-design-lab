# Next Owner Decisions

Maximum decisions: 3. No other Owner choice is required before the bounded release path can proceed.

## Decision 1 — Final concept and name lock

Approve or reject the combined lock:

```text
FINAL_WINNER=JINGZHANG_IN_PLACE
DISPLAY_NAME=京张续城 / Jing-Zhang In Place
```

Recommendation: approve. The audit found no fundamental contradiction and no direct near duplicate.

Until approved, the authoritative state remains:

```text
FINAL_WINNER=OWNER_DECISION_REQUIRED
```

## Decision 2 — One bounded presentation release pass

Authorize or decline one presentation-only correction pass for the three MAJOR human-facing issues.

Recommendation: authorize with the boundaries in `PR_READINESS.md`. This is not a redesign Goal: content, evidence, geometry status, three-area roles, AI/NO-BUILD logic, and display name stay frozen.

If declined, RC1 remains reviewable but the release recommendation cannot advance beyond `LOCK_AFTER_MAJOR_FIX`.

## Decision 3 — Official PR authorization after exact-head acceptance

After the bounded pass produces a new exact SHA and all machine/PDF/human gates PASS, authorize or decline creation of the official PR.

Recommendation: defer this decision until the final exact-head receipt exists. This audit does not create or authorize the PR.

```text
OWNER_DECISIONS_REMAINING=3
OFFICIAL_PR_CREATED=false
```

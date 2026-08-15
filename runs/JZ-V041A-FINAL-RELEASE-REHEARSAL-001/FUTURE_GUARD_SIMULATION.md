# Future high-water-guard simulation

Fixture: `FUTURE_GUARD_FIXTURE.json` represents an open non-Draft successor with exact head, exact scope, merged exact-head baseline score 77, peer-only drift, and an active guard targeting this submission directory with historical score 77.

```text
CURRENT_STATE=READY_FOR_TRUSTED_RESCORE
HISTORICAL_BEST=77
HISTORICAL_BEST_PROVEN=true
SCORE_GUARD_ACTIVE=true
```

The high-water contract is deterministic:

| Candidate trusted score | Disposition |
| ---: | --- |
| 76 | HOLD / do not merge |
| 77 | eligible for normal intake |
| 85 | eligible for normal intake |

The fixture uses no official workflow change and does not imply that its guard is deployed.

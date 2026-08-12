# JZ-R3-DAY-001 Run State

```text
RUN_STATUS=IN_PROGRESS
CURRENT_WAVE=WAVE_4_C02_UNIT_HYPOTHESIS
BASE_SHA=78843cec67498b8930f0cf0bb776665772cee788
CURRENT_HEAD=d931f85_PENDING_C01_CHECKPOINT
OFFICIAL_HEAD=e9741a415aeb5cf09ca27608f6c97c33145a589f
COMPLETED=Wave 0 isolation/state/CP1; Wave 1 official/competition refresh; Wave 2 common base; Wave 3 C01 extended model, admission PASS, three sections, ordinary-day/living-systems gates and urban programme translation
OPEN_TASKS=C02 unit hypotheses; C01 complete city-design draft rewrite; specificity; end-head delta; professional handoff; formal readiness; red team; comparison; return brief
BLOCKERS=AUTHORITATIVE_DATA_MISSING official polygons; EVIDENCE_INSUFFICIENT Dazhongsi and park mismatch; NETWORK_FAILURE one clone and two text requests downgraded without global impact
NEXT_ACTION=commit/push C01 checkpoint, then test H2/H3/H4+/Corridor+N on the identical common snapshot
```

## Safe resume protocol

Read this file, `TASK_DAG.md`, and `git log --oneline -10` before resuming. Verify that `HEAD` remains on the day branch and that neither protected branch was changed.

## Current provisional conclusions

- C01: `ADVANCE_WITH_MAJOR_REWRITE` is only the Round-2 starting disposition; spatial admission is not yet established.
- C02: `HOLD`; H3 was not supported by Round-2 evidence and must face the shared-base one-shot test.
- Candidate 03: review lens only.
- Final winner: Owner decision required.

## Wave-2 receipts

- `OFFICIAL_REQUIREMENTS_CHANGED=false`
- `COMMON_BASE_SOURCE_COUNT=5`
- `CONTEXT_MAPS_GENERATED=6`
- bounded snapshot: 5,927 streets; 425 rail; 325 rail/transit points; 793 public-service objects; 589 selected commercial-service objects; 314 research/education objects; 1,404 green/water objects; 2,095 broad building footprints.
- These counts describe the snapshot only; they are not completeness, capacity or catchment metrics.
- Offline SVG regeneration was byte-deterministic and four Python tests passed.

## Wave-3 receipts

- `C01_SPATIAL_ADMISSION=PASS` at conceptual urban-program level; site/professional feasibility unproven.
- extended synthetic model covers seven demand profiles, eleven resource classes, four compatibility classes, and six failure modes; 11 tests PASS.
- distributed sharing wins only staggered/weekday profiles; dedicated provision wins coincident/event/recovery/low/high profiles.
- universal station deleted because it fails the correlated single-domain gate even when economically compact.
- three distinct conceptual SVG sections generated and parsed: Zhongzhiyuan backend; AI Origin civic front; Dazhongsi typological adoption edge.
- ordinary-day and Living Systems gates forced route/refuge/staff/logistics/drainage changes.

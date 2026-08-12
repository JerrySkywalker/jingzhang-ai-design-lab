# Common-Base Comparison Record

## Inputs held constant

| Input | Fixed value/status |
|---|---|
| official repository | `open-city-ai/haidian@e9741a415aeb5cf09ca27608f6c97c33145a589f` |
| official exact polygons | unavailable |
| provisional polygons | committed source snapshot, visibly provisional |
| contextual open data | one bounded OSM snapshot retrieved 2026-08-12, ODbL |
| geometry warnings | Issue #846 and #1029 |
| persona/state gate | eight personas, seven states, strict no-averaging contract |
| competition set | same 20 relevant proposals/PRs in `research/day3/OFFICIAL_REFRESH.md` |

## Snapshot inventory

The snapshot contains 5,927 selected streets, 425 rail features, 325 rail/transit stations/entrances, 793 mapped public-service objects, 589 selected commercial-service objects, 314 research/education objects, 1,404 green/water objects and 2,095 broad building footprints. Counts are inventory only.

### Provisional key-polygon intersections

| Provisional polygon | transit points | public-service objects | selected commercial objects | research/education objects |
|---|---:|---:|---:|---:|
| PROV-KEY-001 | 4 | 1 | 2 | 0 |
| PROV-KEY-002 | 6 | 7 | 2 | 5 |
| PROV-KEY-003 | 1 | 0 | 0 | 0 |

These values cannot be used to rank neighbourhood quality. They are affected by OSM completeness, polygon displacement, geometry representation and lack of access/hours/capacity. Their valid use is negative: they do not provide evidence that the three rectangles are equally or independently complete.

## No circle-buffer shortcut

No 15-minute circle was generated. Candidate units must eventually follow accessible network relationships, barriers, service clusters, transit thresholds, campus/institution edges and public-space continuity. The current snapshot does not validate those properties; therefore all drawn unit boundaries would be concept assumptions.

## What the base can decide

- H3 is not derived from evidence beyond the taskbook’s three projects.
- multiple/fewer units remain plausible;
- corridor continuity is the strongest common official spatial fact;
- exact Dazhongsi and formal catchment analysis are blocked;
- the lowest-risk architecture is Corridor+N with N explicitly unknown.

## What the base cannot decide

The final N, unit boundaries, actual ordinary-day completeness, service deficits, accessible routes, population/employment, institutional permeability, opening hours/capacity, ownership or statutory land use.

```text
SAME_EVIDENCE_BASE=true
FORMAL_CATCHMENT_ANALYSIS=false
FINAL_UNIT_COUNT=UNKNOWN
```

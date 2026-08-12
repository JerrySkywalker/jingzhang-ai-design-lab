# Shared Resource Taxonomy

## Rule

“Shared” is not a binary amenity label. Every resource must belong to exactly one compatibility class and one physical resource class. Sharing is permitted only when the task packet, reset rule, human duty and failure domain all pass.

## Four compatibility classes

| Class | Meaning | Synthetic examples | Urban consequence |
|---|---|---|---|
| `fully_shareable` | repeated use without task-specific room segregation after routine calibration | environmental probe | removable kit; no dedicated room solely for this item |
| `time_shareable` | sequential use after documented clearing/changeover | general bay, technical supervision, dry store, general cleaning, accountability interface, non-contact tools | booking/queue cap, changeover time, staff room and ordinary service access |
| `shareable_with_isolation` | common interface is allowed only through physical/digital isolation and reset | edge compute, low-voltage port, local lidar/UWB, clean payload store, general safe-recovery position | lockable zones, independent shutdown, calibration/reset, no shared single fire/power domain |
| `non_shareable` | duty, hygiene, hazard or certification forbids interchangeability | accessibility/event supervision, human-contact/hazard tools, hygiene/contaminated cleaning, human-contact/hazard stores and isolation | separate rooms/routes or separate facility; co-location may be rejected |

## Resource classes and programme effect

| Resource class | What may be shared | What must remain bounded | Programme consequence |
|---|---|---|---|
| energy | a compatible protected low-voltage interface | certified packs, high-energy systems, life safety and fire domain | ordinary electrical/service room first; removable port only after capacity/fire check |
| compute | general edge slot | tenant/data isolation, latency, offline safe state | small rack in service space; public route/service never depends on it |
| generic sensing | environment or aggregate modules where lawful | privacy reset, calibration, field-of-view and retention | removable modules; do not reserve landscape/street solely for sensors |
| special sensing | local lidar/UWB or task-specific kit | calibrated cell, safe mounting and test envelope | controlled court/room; no public test lane by default |
| tooling | non-contact tools/boxes can time-share | human-contact and hazardous tools | locked separate storage, checkout and waste/reset sequence |
| maintenance | clean general inspection/recovery bay | hazardous work, contamination and certified repair | ordinary workshop may suffice; specialised backend only when required |
| storage | dry/general and clean lockers under rules | human-contact and hazardous inventory | separate lockers/rooms; reduces theoretical pooling savings |
| cleaning | general wash-down | hygiene and contaminated processes | independent wash/waste route; may prohibit co-location |
| safe isolation | resettable general holding | human-contact/hazard incidents | multiple lockable cells and manual recovery route |
| human supervision | non-simultaneous technical work within span of control | accessibility duty and event command | real operator/welfare room and visible capacity limit |
| public accountability | one desk/status surface can explain sequential tasks | task-specific responsible person and appeal | human-facing frontage; not a screen-only pavilion |

## Model result by demand pattern

| Synthetic profile | Dedicated A | Distributed shared B | Universal C | Admissible lower-index result |
|---|---:|---:|---:|---|
| staggered ordinary day | 291.60 | **235.86** | 226.06, but failure gate fails | B |
| coincident event peak | **291.60** | 343.97 | 336.84, failure gate fails | A |
| weekday baseline | 201.40 | **198.06** | 189.48, failure gate fails | B, weak margin |
| event day | **390.20** | 403.88 | 394.79, failure gate fails | A |
| failure/recovery | **280.70** | 289.11 | 282.17, failure gate fails | A |
| low-demand future | **108.10** | 128.81 | 121.75, failure gate fails | A / build less |
| high-demand future | **608.30** | 618.37 | 610.16, failure gate fails | A / selective dedicated capacity |

Numbers are unitless synthetic cost-risk indices. They demonstrate conditionality only. They do not quantify Jing-Zhang cost, space or demand.

## Spatial conclusion

The data does not support a universal station or a citywide shared network. It supports a decision tree:

```text
ordinary service space already adequate? ── yes → use it; add no AI facility
                 │ no
real tasks compatible and peaks stagger? ── no → dedicated/specialised provision or do not deploy
                 │ yes
can at least two failure domains + manual recovery fit? ── no → do not share
                 │ yes
distributed shared cell, removable modules, capped demand
```

The urban design should show only the last node where evidence has passed. Everything else remains ordinary city fabric or a specialised backend.

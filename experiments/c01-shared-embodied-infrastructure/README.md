# C01 Shared Embodied Infrastructure — Minimal Falsification Model

```text
SYNTHETIC
NOT_SITE_CALIBRATED
NOT_PERFORMANCE_EVIDENCE
```

## Question

Can public tasks be translated into minimum state-information and physical-resource requirements, matched to heterogeneous platforms, and served by shared modular infrastructure without assuming that sharing always wins?

The Round-3 model compares:

- **A — dedicated infrastructure per task family:** each scenario reserves its own peak resources and station;
- **B — distributed shared modular infrastructure:** compatible modules and bays are pooled across at least two isolated cells, with explicit modularization, routing, changeover and correlated-failure penalties;
- **C — universal hub:** one pooled domain with lower fixed duplication but an explicit correlated-failure admission failure.

It evaluates staggered ordinary operations, coincident peak, weekday, event day, failure/recovery, low-demand future and high-demand future profiles. All capacities, costs, footprints, demand and accuracy values are synthetic indices chosen to expose structural behaviour. They are not estimates for Jing-Zhang.

## Reproduce

From this directory:

```powershell
python model.py --input synthetic_inputs.json --output results.json
python -m unittest discover -s tests -v
```

The model uses only the Python standard library and is deterministic.

## What is actually shared

The candidate can coherently share a bounded set of resources: compatible sensor modules, protected low-voltage interfaces, general edge-compute slots, standardized non-contact tools, general maintenance/recovery bays, some storage/cleaning/isolation positions, a public accountability interface and qualified staff across non-simultaneous tasks. The compatibility matrix in `results.json` distinguishes `fully_shareable`, `time_shareable`, `shareable_with_isolation` and `non_shareable` rather than treating co-location as interchangeability.

Human-contact assistive tools, hazardous maintenance tools, hygiene/contamination cleaning, controlled storage and differently qualified safety duties remain segregated. Co-location is not interchangeability.

## Minimum sensing inversion

Each task specifies states to know, maximum tolerable error and time-to-live. The model enumerates sensor bundles and selects the smallest-capital/lowest-privacy feasible bundle under a privacy ceiling. For example, synthetic low-speed delivery selects local lidar alone because it meets obstacle and localization requirements; adding a camera would not improve eligibility and would add privacy cost. This demonstrates a method, not the adequacy of a real sensor.

## Failure isolation and degraded modes

Dedicated stations bound a station failure to one task family in this abstraction. A pooled system exposes several tasks to one failure, so Candidate 01 must use at least two isolatable service cells and manual recovery. The universal hub sometimes has the lowest synthetic economic index but always fails the correlated single-domain admission gate; it is deleted as a citywide spatial type. The retained pattern is distributed cells, selected specialised backends and lightweight public accountability interfaces.

The failure matrix now covers one cell unavailable, power constraint, network loss, resource contamination/safety isolation and operator overload. It returns a physical response for each: independent shutdown, safe parking, offline service, segregated clean/human-contact/hazardous routes, visible queue caps and staffed supervision. These are requirements to test, not proof that a site can provide them.

## Falsification result

The experiment is expected to show both outcomes:

- staggered and some weekday profiles can make distributed B lower-index by avoiding duplicated idle modules;
- coincident/event/recovery, low-demand and high-demand profiles can make A lower-index once B needs similar peak capacity plus modular, routing and shared-failure overhead;
- C can appear economically compact, but that result cannot override its failure-domain gate.

If either test stops producing that contrast after input changes, the corresponding structural claim must be re-examined. Site adoption requires real task volumes, platform standards, travel distances, electrical/fire constraints, maintenance labour, procurement and field evidence.

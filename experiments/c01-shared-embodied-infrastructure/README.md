# C01 Shared Embodied Infrastructure — Minimal Falsification Model

```text
SYNTHETIC
NOT_SITE_CALIBRATED
NOT_PERFORMANCE_EVIDENCE
```

## Question

Can public tasks be translated into minimum state-information and physical-resource requirements, matched to heterogeneous platforms, and served by shared modular infrastructure without assuming that sharing always wins?

The model compares:

- **A — dedicated infrastructure per task family:** each scenario reserves its own peak resources and station;
- **B — shared modular infrastructure:** compatible modules and bays are pooled across time, with explicit modularization, routing, changeover and correlated-failure penalties.

It evaluates both a staggered ordinary-day profile and a coincident event peak. All capacities, costs, footprints, demand and accuracy values are synthetic indices chosen to expose structural behaviour. They are not estimates for Jing-Zhang.

## Reproduce

From this directory:

```powershell
python model.py --input synthetic_inputs.json --output results.json
python -m unittest discover -s tests -v
```

The model uses only the Python standard library and is deterministic.

## What is actually shared

The candidate can coherently share a bounded set of resources: compatible sensor modules, protected low-voltage interfaces, general edge-compute slots, standardized non-contact tools, general maintenance/recovery bays and qualified staff across non-simultaneous tasks. The compatibility matrix in `results.json` prevents the word “shared” from erasing platform differences.

Human-contact assistive tools, hazardous maintenance tools and differently qualified safety duties remain segregated. Co-location is not interchangeability.

## Minimum sensing inversion

Each task specifies states to know, maximum tolerable error and time-to-live. The model enumerates sensor bundles and selects the smallest-capital/lowest-privacy feasible bundle under a privacy ceiling. For example, synthetic low-speed delivery selects local lidar alone because it meets obstacle and localization requirements; adding a camera would not improve eligibility and would add privacy cost. This demonstrates a method, not the adequacy of a real sensor.

## Failure isolation and degraded modes

Dedicated stations bound a station failure to one task family in this abstraction. A pooled system exposes several tasks to one failure, so Candidate 01 must use at least two isolatable service cells and manual recovery; a single central mega-hub is rejected. When edge compute is unavailable, automated delivery pauses while accessibility, maintenance and event functions fall back to people and environmental probes log locally.

## Falsification result

The experiment is expected to show both outcomes:

- staggered peaks can make B lower-index by avoiding duplicated idle modules;
- coincident peaks can make A lower-index once B needs the same peak capacity plus modular, routing and shared-failure overhead.

If either test stops producing that contrast after input changes, the corresponding structural claim must be re-examined. Site adoption requires real task volumes, platform standards, travel distances, electrical/fire constraints, maintenance labour, procurement and field evidence.

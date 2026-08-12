# Common Base

## What is available

`research/site-context/` provides one pinned, reproducible evidence base used by both candidates. It includes the official textual scope, the repository's provisional overall/key-area geometry, a bounded OSM snapshot and two public issue records concerning geometry mismatch.

Six generated maps show scope context, rail/transit, daily-life services, green/water/open space, research/innovation context and a dedicated geometry-warning view. OSM attribution is embedded in every contextual figure.

## What can be judged

- broad north-south topology and contextual rail/street relationships;
- where public-service, research/education and green/water objects appear in the bounded snapshot;
- barrier, interface and field-observation questions;
- whether two hypotheses are being compared against identical inputs;
- typological differences among productive R&D, community/learning and metropolitan-adoption interfaces.

## What cannot be judged

- official site or key-area boundaries;
- ownership, legal access, statutory land use or development rights;
- population, service capacity, operating hours or user demand;
- precise walking catchments or station-area interventions;
- building condition, floorplate suitability, utilities or structural capacity;
- detailed flood, ecology, traffic, fire or loading feasibility.

## Critical warnings

`PROV-KEY-003` is not station/road anchored and sits in a contextual location inconsistent with a literal Dazhongsi station reading. Treat Section C as a metropolitan-interface typology, not a site-resolved design. The provisional overall polygon also has a recorded mismatch with mapped Jing-Zhang park context. Do not correct either geometry by eye.

## Reproduction

From the repository root:

```powershell
python research/site-context/build_context.py --offline
python -m unittest discover -s research/site-context/tests -v
```

The snapshot is `CONTEXTUAL`, the figures are `DERIVED`, and none is official survey or formal planning evidence.


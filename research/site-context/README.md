# Round-3 Common Spatial Evidence Base

This directory is the single contextual base used to pressure-test both C01 and C02. It is not a plan, official base map, formal catchment study, survey, land-use inventory, or submission geometry.

## Status contract

- `official` — authoritative text/source status only; no official competition polygon is currently available.
- `provisional` — repository-maintained rough polygons used only as temporary constraints.
- `contextual` — public open-data context such as OSM streets, rail, POIs and broad footprints.
- `derived` — reproducible calculations from the committed snapshots.
- `concept` — future design moves; none are encoded in the common base.

All OSM-derived files state `© OpenStreetMap contributors, ODbL 1.0`. No commercial map tiles or screenshots are used.

## Build

```powershell
python research/site-context/build_context.py --refresh --retrieval-date 2026-08-12
python research/site-context/build_context.py --offline --retrieval-date 2026-08-12
python -m unittest discover -s research/site-context/tests -v
```

`--refresh` performs bounded public GET/Overpass requests and writes normalized GeoJSON snapshots. `--offline` regenerates the summary and six SVGs deterministically from committed inputs.

## What this base can decide

- whether a spatial claim is compatible with a visible street/rail/open-space/service topology lead;
- whether competing hypotheses use the same source snapshot;
- which named places, barriers and interfaces require professional or field verification;
- where provisional geometry visibly conflicts with contextual anchors.

## What it cannot decide

Ownership, population, land-use legality, official redlines, service hours/capacity, universal accessibility, catchment membership, building condition, road hierarchy in law, utilities, ecology, drainage performance, transport demand, or engineering feasibility.

# Site Evidence v2

This pack expands the shared contextual base with current public, high-authority evidence that can change design choices. It is a research aid, not an official survey, statutory plan, title record, engineering model, or substitute for the organizer's missing exact polygons.

## Outputs

- `SOURCE_LEDGER.md` records 30 design-relevant sources and their limits.
- `SITE_FACT_PACK.md` converts only supportable facts into design constraints.
- `SITE_PROBLEM_ATLAS.md` separates verified conditions from contextual leads and unknowns before any premise is chosen.
- `generate_maps.py` deterministically rebuilds eight SVG evidence maps from committed vector snapshots in `research/site-context/`.
- `figures/` contains those eight maps; `figure-hashes.json` is the reproducibility receipt.

## Evidence boundary

The committed OSM snapshot is `CONTEXTUAL`: it can locate questions and compare morphology on one common base, but it cannot prove access, capacity, ownership, building condition, use, hours, legal status, or engineering feasibility. The organizer-provided repository polygons are still `PROVISIONAL` and are always drawn dashed and unfilled.

Government and institutional webpages in the ledger have no explicit open-media licence unless noted. This repository preserves links, metadata, short factual paraphrases, and original vector redrawings only; it does not copy source maps, photos, or long passages.

## Rebuild

```powershell
python research/site-evidence-v2/generate_maps.py
python research/site-evidence-v2/generate_maps.py --check
```

The builder is offline and uses only committed inputs. It emits no commercial map tiles, remote assets, scripts, fonts, or APIs.

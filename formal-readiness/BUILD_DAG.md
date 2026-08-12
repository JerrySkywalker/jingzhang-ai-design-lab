# Formal Build DAG

Target path:

```text
08-13 candidate lock
08-13/14 fork + schema-valid baseline
08-14/15 spatial + proposal deepening
08-15/16 core figures + metrics
08-16/17 bilingual + HTML + A3/A0
08-18 feature freeze
08-19 preflight/final audit
08-20 PR
```

## Dependency graph

```text
CANDIDATE LOCK + current contract refresh
 ├─ TEXT: proposal structure, sources, assumptions, matrices
 ├─ GEOMETRY: boundary disclosure, topology-safe nine layers
 ├─ BILINGUAL: glossary + section pairing (starts after section intent freezes)
 └─ FIGURE SYSTEM: pinned fonts, palette, sizes, exporter and hash receipt

GEOMETRY
 ├─ METRICS: recompute every geometry-derived value
 ├─ FIGURES: site / land use / key areas / mobility-blue-green / metrics-evidence
 └─ A3_A0: base drawing frames

TEXT + GEOMETRY + METRICS + FIGURES
 ├─ HTML: paired report and visual sites
 ├─ A3_A0: paired primary/English PDFs
 └─ VALIDATION: incremental four-gate runs

TEXT FREEZE + FIGURE FREEZE + BILINGUAL
 -> FINALIZE
 -> marked SELF-CHECK
 -> PARTICIPANT PREFLIGHT
 -> exact-head final audit
 -> PR
```

## Parallel lanes

| Lane | Can start | Blocks | Primary output |
|---|---|---|---|
| TEXT | candidate lock | translation/final HTML | proposal, narrative, sources, matrices |
| GEOMETRY | spatial structure lock | metrics/core figures | nine GeoJSON layers |
| METRICS | stable geometry per layer | metrics figure/final checks | metrics.json + citations |
| FIGURES | figure system + relevant geometry/text | A3/A0/visual | five core paired figures |
| BILINGUAL | glossary + section intent | final HTML/PDF pairing | proposal/display counterparts |
| HTML | proposal + paired assets | finalize | report/visual pairs |
| A3_A0 | figure/text layout freeze | finalize | four PDFs |
| VALIDATION | scaffold onward | final preflight | incremental and terminal receipts |

## Critical path

```text
candidate lock
→ spatial structure + three-area roles
→ topology-safe geometry
→ metrics/matrices
→ five core figures
→ bilingual text/display/PDF pairs
→ report + visual HTML
→ finalize
→ marked four-gate self-check
→ participant preflight
→ final audit/PR
```

The presently unowned risk on this path is the participant-grade figure/PDF generator; the official repository validates but does not generate final boards/figures.

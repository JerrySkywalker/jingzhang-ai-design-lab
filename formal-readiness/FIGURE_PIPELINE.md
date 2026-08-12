# Figure Pipeline

The official repository defines and validates five core figures but does not provide a participant-grade final figure generator.

## Required core figures

1. site/strategy overview;
2. land-use and renewal structure;
3. three key areas;
4. mobility plus blue-green/public realm;
5. metrics/evidence and implementation.

Each must be regenerated from candidate-controlled inputs, not the scaffold placeholder. Text-bearing figures require paired language versions.

## Deterministic production contract

- choose and pin one generator/exporter at candidate lock;
- pin fonts with bilingual glyph coverage, palette, page/image dimensions and colour profile;
- derive geometry from the nine GeoJSON layers, not hand-redrawn conflicting shapes;
- derive numbers from `metrics.json`, not manual labels;
- include evidence/provisional symbols and exact-geometry warning consistently;
- generate primary and English variants from a shared semantic manifest;
- hash source data, generator version and every output;
- render/inspect figures at target A3/A0 size before feature freeze.

## Current host/tool result

Available: Python 3.12, Pillow, Microsoft YaHei and Arial.  
Not detected/audited for the current host: Inkscape, ImageMagick, Pandoc, Typst and wkhtmltopdf. `reportlab` is not in the review environment. The production generator therefore remains an explicit lock-day decision; this is the largest formal readiness risk.

The R5 site-atlas SVG builder proves a deterministic vector-redraw pattern but is evidence-atlas code, not a final proposal figure generator and must not be migrated unchanged as candidate design.

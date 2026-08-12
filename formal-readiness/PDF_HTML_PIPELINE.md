# PDF and HTML Pipeline

## HTML

`scripts/render_proposal_html.py` successfully rendered the primary dummy proposal. Once the translated proposal exists, it emits both report HTML files. Final report and visual HTML must be fully offline: no remote tiles, scripts, fonts or APIs.

Production checks:

- links and section anchors;
- primary/English parity;
- local asset existence and hashes;
- readable maps/tables at desktop and narrow widths;
- print CSS and no clipped figures;
- exact metrics/source references.

## A3/A0 PDF

The scaffold PDFs are deliberately zero-page placeholders and validation rejects them. The official repository does not generate finished boards/booklets. The chosen production pipeline must:

- emit A3 booklet and A0 boards in both languages;
- embed or legally package fonts;
- preserve vector text/line work where possible;
- use the same figure/metric manifest as HTML;
- verify page count, physical page size, raster resolution and no clipping;
- render PDFs to page images for visual review before freeze;
- hash all four PDFs after final export.

`reportlab` and optional translation dependencies were not installed during the review-only rehearsal. Pin the selected PDF engine on lock day and run a one-page bilingual font/page-size smoke test before content layout.

## Freeze rule

After `08-18` feature freeze, any text, geometry or metric change invalidates affected figures, HTML, PDFs and self-check hashes. Rebuild the dependency subtree, not just the visible file.

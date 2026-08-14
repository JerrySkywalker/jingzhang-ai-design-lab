# Artifact integrity and regression check

Manifest inventory remains complete: 45 declared entries, 40 required entries,
44 declared hashes (the manifest intentionally does not hash itself), with no
duplicate/missing paths.

Present and paired:

- five Chinese and five English core figures (all 3600 × 2250 PNG);
- Chinese/English A3 booklets (12 pages each);
- Chinese/English A0 boards (3 pages each);
- Chinese/English visual HTML and proposal-report HTML;
- proposal, report, matrices, geometry, metric and portfolio evidence.

Against RC2 remote head `e333451…`, this release-stewardship work changes one
package file only: `manifest.json`. It changes zero design-bearing files and
zero PNG/PDF/HTML presentation artifacts. No rerender was necessary.

- `PRESENTATION_REGRESSION=false`
- `BILINGUAL_REGRESSION=false`

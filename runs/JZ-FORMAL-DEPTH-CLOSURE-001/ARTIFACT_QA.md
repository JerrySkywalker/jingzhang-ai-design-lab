# Artifact QA — crash-recovery tail

## Paired formal artifacts

- Chinese and English proposals, report HTML and offline visual HTML exist and pass bilingual audit.
- Five Chinese and five English core figures exist at `2400 × 1500` pixels: overview, land-use structure, key areas, mobility/blue-green, and metrics/evidence.
- A3 Chinese/English booklets: 10 non-empty A3 landscape pages each (`1190.55 × 841.89 pt`).
- A0 Chinese/English boards: 3 non-empty A0 landscape pages each (`3370.39 × 2383.94 pt`).
- All PDFs are unencrypted PDF 1.4. Extracted text was non-empty on each file; Chinese display subsets of Microsoft YaHei are embedded for legibility.

## Visual inspection

Direct PNG inspection found and repaired two human-readability issues without altering proposal, geometry, metrics or design logic:

1. The bottom conclusion panel in the land-use-structure pair was enlarged and lifted above the footer so its English text is not clipped.
2. English mobility/blue-green route labels were reduced and lifted so they no longer cross their route lines.

The affected PNGs and their embedded A3/A0 pages were re-exported. Raster checks covered A3 land-use pages, A3 mobility pages and A0 boards. They showed visible Chinese/English text, no blank page and no remaining observed clipping. Poppler emitted a local `No display font for Symbol` notice during rasterization, but rendered pages remained complete; it is recorded as a non-blocking local display-tool notice.

Git's raw full-range `diff --check` also emits trailing-whitespace notices inside the valid ReportLab ASCII85 PDF streams. The same check excluding the four PDF binary assets exits cleanly; this is a Git text-heuristic notice, not a package-content or rendered-PDF defect.

## Rights and offline consistency

- Source markers resolve to declared sources; provisional/background use remains disclosed.
- Copyright statement now accurately states that PDFs may contain display-only subset fonts while no standalone font files are redistributed.
- HTML pages remain offline: no CDN, remote font, API, iframe, form, tracker, remote media or online map tile dependency.
- No peer figures, commercial map screenshots, source photos or redistributed font files were introduced.

## Current package size

`4,251,745` bytes (about 4.1 MiB), below the preflight warning threshold.

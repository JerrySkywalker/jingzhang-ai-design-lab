# PDF QA — RC2

## Deliverables inspected

| PDF | Page count | Page size | Result |
| --- | ---: | --- | --- |
| `a3-booklet.pdf` | 12 | landscape A3, 1190.55 × 841.89 pt | PASS |
| `a3-booklet.en.pdf` | 12 | landscape A3, 1190.55 × 841.89 pt | PASS |
| `a0-boards.pdf` | 3 | landscape A0, 3370.39 × 2383.94 pt | PASS |
| `a0-boards.en.pdf` | 3 | landscape A0, 3370.39 × 2383.94 pt | PASS |

All 30 pages were rasterized at 150 DPI. Contact sheets and representative
full pages were visually checked for blank pages, clipping, overflow,
alignment, language mismatch, title hierarchy and balance. No blank page,
clipped figure, low-resolution core image, missing legend or font failure was
observed. `pdffonts` confirms embedded Microsoft YaHei subsets for Chinese
content and Helvetica for the shared PDF machinery.

Poppler issued a local `No display font for 'Symbol'` diagnostic during
rasterisation, but the produced page rasters were complete and visually clean;
it is a local display-font fallback diagnostic rather than a missing embedded
PDF font.

## QA evidence

```text
qa/final-pdf-raster-rc2/
qa/contact-sheets/a3-zh-contact-sheet.png
qa/contact-sheets/a3-en-contact-sheet.png
qa/contact-sheets/a0-zh-contact-sheet.png
qa/contact-sheets/a0-en-contact-sheet.png
```

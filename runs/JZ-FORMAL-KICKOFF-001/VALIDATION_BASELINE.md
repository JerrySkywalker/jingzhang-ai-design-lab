# Validation Baseline

Status: `PENDING_FINAL_COMMAND_RECEIPTS`

Expected state for formal baseline v0.1:

- bootstrap/scaffold/export/render: should PASS;
- finalization: should remain non-PASS while package state is `scaffold` and professional-depth/asset requirements are incomplete;
- deterministic/local validation: should expose schema, manifest, placeholder, cross-reference and data-boundary gaps;
- spatial review: should accept provisional flags but reject professional completeness where geometry remains typological;
- visual review: should recognize paired real baseline assets but not final design depth;
- professional review: should identify building, engineering, section and evidence gaps;
- self-check/preflight: should execute and fail on content readiness, not toolchain availability.

Every result will be classified as `EXPECTED_BASELINE_GAP`, `CONTENT_GAP`, `GEOMETRY_GAP`, `BILINGUAL_GAP`, `FIGURE_GAP`, `PDF_GAP`, `SCHEMA_ERROR`, `TOOLCHAIN_ERROR` or `REAL_BLOCKER`. `--mark-self-checked` is forbidden until all four gates actually pass.

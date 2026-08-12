# Formal Toolchain Rehearsal Receipt

```text
FORMAL_REHEARSAL_OFFICIAL_HEAD=9407689a4bb5d083e885ac5696dc95db7477b0eb
SCRATCH=V:\src\_scratch\JZ-FORMAL-REHEARSAL
BRANCH=rehearsal/r5-formal-dummy
PACKAGE=submissions/r5-rehearsal/dummy-formal-rehearsal

CAN_BOOTSTRAP_TODAY=true
FORMAL_BOOTSTRAP_WORKS=true
SCAFFOLD_WORKS=true
PRIMARY_HTML_RENDER_WORKS=true
CURRENT_VALIDATOR_CAN_RUN=true

FINALIZE=EXPECTED_FAIL
DETERMINISTIC_VALIDATION=EXPECTED_FAIL
SPATIAL_REVIEW=PASS_WITH_PROVISIONAL_MINOR_ISSUES
VISUAL_REVIEW=EXECUTED_PASS_ON_SCAFFOLD_STRUCTURE
PROFESSIONAL_REVIEW=EXECUTED_PASS_ON_SCAFFOLD_STRUCTURE
SELF_CHECK=EXPECTED_FAIL
WORKSPACE_PREFLIGHT_SKIP_SELF_CHECK=PASS
FULL_PREFLIGHT=EXPECTED_FAIL_SELF_CHECK_ONLY

VALIDATOR_REHEARSAL_RESULT=EXECUTED_EXPECTED_SCAFFOLD_REJECTION
PUSH_ATTEMPTED=false
COMMIT_CREATED=false
PR_CREATED=false
FORK_CREATED=false
```

## Missing dependencies and production tools

The isolated review environment now has all `requirements-review.txt` dependencies. Optional `reportlab`/translation dependencies were not installed. No participant-grade final figure/A3/A0 generator is supplied by the official repository, and Inkscape/ImageMagick/Pandoc/Typst/wkhtmltopdf were not detected in the audit. Production must pin a generator and bilingual font/export path on candidate-lock day.

## Deterministic outputs available now

- lightweight sparse bootstrap;
- formal scaffold/schema/matrices and provisional geometry baseline;
- proposal HTML rendering;
- deterministic, spatial, visual and professional validator execution;
- self-check and workspace/preflight classification.

Final candidate figures, visual HTML content and A3/A0 PDFs cannot be generated deterministically until the production exporter is selected and candidate content exists.

## Parallelism and critical path

TEXT and GEOMETRY can start in parallel after candidate lock; glossary/BILINGUAL and figure-system setup can also start early. METRICS follows relevant geometry, and FIGURES follow geometry/metrics. HTML and A3/A0 can proceed in parallel after stable paired content/assets. The terminal critical path is recorded in `BUILD_DAG.md`.

# Review-packet harness test report

FAST: Python compilation passed. CORE: 3 review-packet tests passed for canonical semantic
invariants, nested materialisation, and bilingual-figure stop-ship regression. FULL: all 12
new-tool tests and existing relevant design-lab tests passed.

The baseline-to-v0.4 comparison passed with 1 added file, 23 modified files, and no stop-ship
regression. v0.4 adds the canonical admission source and passes every required v0.4 invariant;
the baseline diagnostic gaps reflect that the source did not yet exist.

The v0.4-to-v0.4.1 comparison passed with 7 modified files, -181 text bytes, unchanged core
figure hashes, and passing semantic, bilingual, artifact, and first-window checks. Machine
records: `BASELINE_V04_DELTA.json` and `V041_V04_DELTA.json`.

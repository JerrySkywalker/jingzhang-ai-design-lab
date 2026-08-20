# JZ97-G02 — Trusted Anchor Corpus

PROGRAM=`JZ-97-CONVERGENCE-TRAIN-001`  
GOAL=`JZ97-G02-TRUSTED-ANCHOR-CORPUS-001`  
ENGINE=`AGY gemini-3.7-flash-high`

## Admission

Requires G01 PASS and current rubric/packet contract pinned. No product mutation.

## Mission

Build a reproducible calibration corpus of at least five exact-head submissions with trusted maintainer scores spanning approximately 77 / 86 / 90 / 90 / 96. Verify score provenance, exact reviewed head, review timestamp, trusted reviewer evidence and package/subtree identity.

Construct every anchor with the same current review packet builder and neutral IDs. Do not encode chronology, author preference or score in candidate IDs. Do not copy large competitor media into design-lab; keep only permitted metadata/analysis and local ephemeral packets.

## Required outputs

- `TRUSTED_ANCHOR_LEDGER.json`
- `TRUSTED_ANCHOR_PROVENANCE.md`
- blind-ID map kept out of reviewer packets
- packet hash/file-count ledger
- twice-built reproducibility proof for every anchor

## Exit

PASS requires >=5 trusted exact-head anchors, provenance PASS, packet reproducibility PASS and neutral blinding PASS. Update state to G03.

NEXT_ON_PASS=`JZ97-G03-THREE-MODEL-ANCHOR-JURY-001`
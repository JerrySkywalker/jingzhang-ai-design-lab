# JZ-97 Goal Contracts

These files are executable contracts for `JZ-97-CONVERGENCE-TRAIN-001`.

## Execution rule

Before any Goal, the agent must read:

1. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`
2. `docs/CURRENT_PROGRAM.md`
3. `state/JZ97_PROGRAM_STATE.json`
4. `docs/PROGRAM_CONTROL_AIRLOCK.md`
5. the selected Goal contract

Admission requirements are hard gates. If state does not satisfy them, return `DISPOSITION=BLOCKED_PROGRAM_STATE` without bypassing the Program DAG.

## Goal map

- G01 — official rubric and reviewer-packet truth lock
- G02 — trusted anchor corpus
- G03 — three-model isolated anchor jury
- G04 — deterministic calibration model / C1
- G05 — blind v0.4.1a vs v0.4.2 measurement
- G06 — 97-band blocker matrix
- G07 — v0.4.3 targeted surgery
- G08 — v0.4.3 certification and jury / C2
- G09 — optional v0.4.4 targeted surgery
- G10 — optional v0.4.4 certification and jury
- G11 — trusted-96 ceiling blind match
- G12 — GPT-5.6 Sol OpenAI-family holdout / C3
- G13 — final release reconstruction
- G14 — high-water release admission / C4
- G15 — official trusted review / C5

`JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001.md` is the approved combined unattended train for the next 8–12 hour run. It must preserve the individual G01/G02 exit criteria.
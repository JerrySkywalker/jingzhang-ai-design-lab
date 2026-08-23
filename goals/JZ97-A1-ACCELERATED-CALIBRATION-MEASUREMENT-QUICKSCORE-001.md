# JZ97-A1 — Accelerated Calibration, Measurement & QuickScore Bootstrap

**Program ID:** `JZ-97-CONVERGENCE-TRAIN-001`  
**Compound Train ID:** `JZ97-A1-ACCELERATED-CALIBRATION-MEASUREMENT-QUICKSCORE-001`  
**Composed Goals:** `G03 (Core Anchors)` + `G04 (Calibration Model)` + `G05 (Candidate Measurement)` + `G06 (97-Band Blocker Matrix)` + `QuickScore Bootstrap`  
**Primary Engine:** AGY `gemini-3.7-flash-high` (Host Coordinator)  
**Formal Jury:** Windows Sandbox Isolated Instances (Reviewer A `claude-opus-4-6-thinking`, Reviewer B `claude-sonnet-4-6`, Reviewer C `gemini-3.7-flash-high`, TieBreaker `gpt-oss-120b-medium`)  

---

## 1. Mission & Scope

Compound Train A1 replaces the slow one-goal-per-session cadence for the calibration and measurement phase by linking four foundational Goals and local scoring tooling into a single coherent workflow:

1. **Phase 0 — Program Reconciliation & Infrastructure Verification**: Fast-forward canonical `main` with durable G01/G02/G03-readiness receipts; verify 64/64 preflight suite.
2. **Phase 1 — Goal G03 (Core Anchor Formal Jury)**: Execute isolated, blinded 3-model jury scoring across 5 core anchors (`N4`=77, `X8`=86, `B2`=90, `W7`=90, `J9`=96) with memory purges between evaluations. Keep `L5` and `P3` as diagnostic reserves. Requires authentic Owner Sandbox execution.
3. **Phase 2 — Goal G04 (Calibration Model & Gate C1)**: Compute model bias, rank-order accuracy, pairwise consistency, and error bounds across core anchors. Evaluate Gate `C1_CALIBRATION_READY`.
4. **Phase 3 — Goal G05 (Candidate Baseline Measurement)**: Blind-evaluate frozen `v0.4.1a` vs certified `v0.4.2` with calibrated jury panel.
5. **Phase 4 — Goal G06 (97-Band Blocker Matrix)**: Map candidate performance against 7-dimension rubric, freeze majority-5 dimensions, identify precise evidence gaps for majority-4 dimensions, identify at most two surgical targets for A2.
6. **Phase 5 — QuickScore Bootstrap (`tools/jz_quickscore.py`)**: Implement and validate lightweight local iteration advisory scorer (Sonnet default).

---

## 2. Immutable Anchors & Baseline State

- **Official Merged Baseline**: `1d5cb1aaa9d76edc3532e593c803cb936070a744` (Trusted Score: 77)
- **Frozen Checkpoint v0.4.1a**: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- **Certified Local v0.4.2**: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- **Draft Successor PR**: `open-city-ai/haidian#2774` (Draft status strictly preserved)

### Core Calibration Corpus (5 Anchors)
| Neutral ID | Official Score | PR # | Commit SHA | Tier / Role |
|---|---|---|---|---|
| **N4** | 77 | #2744 | `1d5cb1aaa9d76edc3532e593c803cb936070a744` | Merged Baseline Anchor |
| **X8** | 86 | #2738 | `e5ec8ebcfd0aa29e71dd671752b07a514d7c88b9` | Strong Distinctive Anchor |
| **B2** | 90 | #2629 | `9622d10034440fa6e14713c7ba3dcf27756f7091` | High-Water Competitor 1 |
| **W7** | 90 | #2630 | `f32f3c7d678d92bc931f621a64f5ea7c9896085a` | High-Water Competitor 2 |
| **J9** | 96 | #2633 | `30a6f44d564177d5ff53b7501b44ecddb90ce8ca` | Exceptional Ceiling Anchor |

*Diagnostic reserves (scored only if calibration anomalies occur):* `L5` (90), `P3` (91).

---

## 3. Strict Safety & Airlock Boundaries

- **Zero Product Mutation**: No edits permitted to `JerrySkywalker/haidian` or `open-city-ai/haidian`.
- **No v0.4.3 Creation**: Candidate v0.4.3 creation is strictly deferred to Compound Train A2.
- **Formal Jury Confinement**: All formal jury scoring MUST run inside ephemeral Windows Sandbox instances. Host AGY session must NEVER execute formal jury scoring.
- **QuickScore Boundary**: `tools/jz_quickscore.py` is strictly `DEV_ADVISORY` (`FORMAL_EVIDENCE=false`). It must NEVER set gates C1, C2, C3, or C4 to PASS.

---

## 4. Admission Prerequisites

1. **G01 PASS**: Official rubric dimensions, weights, integer 0..5 bands locked.
2. **G02 PASS**: 7 trusted exact-head anchors compiled into neutral reproducible packets.
3. **G03 Readiness PASS**: WSB sandbox configurations, memory purge runner, dashboard, and preflight test suite verified (64/64 PASS).
4. **Git Reconciliation Clean**: Canonical `main` fast-forwarded with durable receipts.

---

## 5. Phase-by-Phase Execution & Gate Rules

### Phase 1: G03 Formal Core Jury
- Owner launches Sandboxes A, B, C via `Start-JZAnchorJury.ps1 -Reviewer All -Mode Score -Anchor Core`.
- Reviewers authenticate in Sandbox browser and execute `.\reviewer-runner-agy.ps1 -Reviewer <A|B|C> -Anchor Core -Mode Score`.
- Target: 15 validated scorecards (5 anchors × 3 reviewers).
- If spread > 15.0 pt on any anchor, execute TieBreaker (`gpt-oss-120b-medium`).

### Phase 2: G04 Calibration & Gate C1
- Run deterministic calibration script on the 15 scorecards.
- Check rank order accuracy (target >= 80%), MAE (target <= 5 pt), catastrophic inversion.
- If absolute error is high but order is preserved, set `C1_CALIBRATION_READY=PASS` with `LOCAL_ABSOLUTE_SCORE_UNTRUSTED=true`.

### Phase 3: G05 Candidate Measurement
- Build neutral packets for `v0.4.1a` and `v0.4.2`.
- Run formal 3-model jury on both candidates (6 scorecards).
- Compute deterministic total scores, dimensional deltas, and pairwise preference.

### Phase 4: G06 97-Band Blocker Matrix
- Analyze winning candidate integer bands across all 7 dimensions.
- Freeze majority-5 dimensions.
- For each majority-4 dimension, document exact deficiency and required intervention.
- Select at most two surgical targets (`V043_TARGET_1`, `V043_TARGET_2`).

### Phase 5: QuickScore Bootstrap & Validation
- Implement `tools/jz_quickscore.py`.
- Validate against G05 candidate directionality.

---

## 6. Exit Criteria & Handoff

A1 exits successfully when:
- 15 core anchor formal scorecards exist in `_review_isolation/output-*`.
- G04 calibration model and C1 gate evaluation are persisted.
- G05 measurement receipts for `v0.4.1a` vs `v0.4.2` are recorded.
- G06 blocker matrix and two surgical targets are defined.
- `tools/jz_quickscore.py` is tested and validated.
- All receipts committed to `runs/JZ97-A1-ACCELERATED-CALIBRATION-MEASUREMENT-QUICKSCORE-001/`.

**Next Compound Train:** `JZ97-A2-V043-SINGLE-SHOT-SCORE-LIFT-001`

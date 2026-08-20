# JZ-97 Convergence Train

**Program ID:** `JZ-97-CONVERGENCE-TRAIN-001`  
**Role:** canonical long-horizon control document for post-intake score convergence  
**Official product repo:** `JerrySkywalker/haidian`  
**Official canonical repo:** `open-city-ai/haidian`  
**Control/design-memory repo:** `JerrySkywalker/jingzhang-ai-design-lab`

## 1. Mission

Raise **京张续城 / Jing-Zhang In Place** from the merged trusted baseline of 77 toward a defensible **97-class** candidate without score-fishing, fabricated precision, official-repository drift, or regression below the accepted high-water.

The original submission implementation is complete. This Program governs only post-merge calibration, bounded score-lift, ceiling qualification, and safe official re-review.

## 2. Immutable anchors

- Official trusted baseline head: `1d5cb1aaa9d76edc3532e593c803cb936070a744`
- Official trusted score: `77`
- Official merged PR: `open-city-ai/haidian#2744`
- Frozen v0.4.1a checkpoint: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- Current local candidate v0.4.2: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- Existing draft successor PR: `open-city-ai/haidian#2774`, intentionally Draft until release admission is safe.

Never rewrite prior checkpoints. New repairs create new heads.

## 3. Execution model

### Host development

- Primary implementer: AGY `gemini-3.7-flash-high`
- Normal host invocation: `agy --dangerously-skip-permissions --model gemini-3.7-flash-high`
- Explorer/Critic subagents: `pro` tier
- Worker subagent: `inherit`
- Validator subagent: `flash`

### Formal local jury

Run only in physically isolated Windows Sandbox packets with exact model pinning:

- Reviewer A: `claude-opus-4-6-thinking`
- Reviewer B: `claude-sonnet-4-6`
- Reviewer C: `gemini-3.7-flash-high`
- Tie-breaker only when required: `gpt-oss-120b-medium`

Formal jury reviewers do **not** use host `--dangerously-skip-permissions` and do not see host history, GitHub, MCP, other reviewer outputs, or candidate chronology.

### OpenAI-family holdout

Reserve a single late-stage ChatGPT GPT-5.6 Sol holdout for G12. It is not an official score. The official maintainer review currently uses the official review pipeline/default OpenAI-family model and remains external to this Program.

Codex CLI is not a planned dependency; use only as an explicitly authorized scarce fallback.

## 4. Score semantics

Current official rubric must be re-pinned from latest upstream before calibration. Historical weights are:

| Dimension | Weight |
|---|---:|
| brief_alignment | 20 |
| originality | 10 |
| ai_planning_innovation | 15 |
| implementation_feasibility | 20 |
| public_interest_inclusion | 10 |
| risk_compliance | 10 |
| expression_completeness | 15 |

Formal local jury bands must be integers `0..5`; fractional host bands are advisory only.

A 97-class integer vector effectively requires exceptional performance in nearly every dimension. At minimum, `brief_alignment=5` and `implementation_feasibility=5`; no majority dimension may be <=3.

## 5. Program DAG

```mermaid
graph TD
    G00["G00 Program Control Bootstrap"] --> G01["G01 Official Rubric + Packet Lock"]
    G01 --> G02["G02 Trusted Anchor Corpus"]
    G02 --> G03["G03 Three-Model Anchor Jury"]
    G03 --> G04["G04 Calibration Model"]
    G04 --> C1{"C1 CALIBRATION_READY"}
    C1 -->|PASS| G05["G05 v0.4.1a vs v0.4.2 Measurement"]
    C1 -->|FAIL| R1["Relative-only calibration repair"]
    G05 --> G06["G06 97-Band Blocker Matrix"]
    G06 --> G07["G07 v0.4.3 Targeted Surgery"]
    G07 --> G08["G08 v0.4.3 Certification + Jury"]
    G08 --> C2{"C2 CANDIDATE_LIFT"}
    C2 -->|PASS and 97-class| G11["G11 Trusted-96 Ceiling Test"]
    C2 -->|PASS but blocker remains| G09["G09 v0.4.4 Targeted Surgery"]
    G09 --> G10["G10 v0.4.4 Certification + Jury"]
    G10 --> G11
    G11 --> G12["G12 OpenAI-Family Holdout"]
    G12 --> C3{"C3 97_CLASS_READY"}
    C3 -->|PASS| G13["G13 Final Release Reconstruction"]
    C3 -->|FAIL| G06
    G13 --> G14["G14 High-Water Admission Gate"]
    G14 --> C4{"C4 RELEASE_SAFE"}
    C4 -->|PASS| G15["G15 Official Trusted Review"]
    C4 -->|BLOCKED| WAIT["SAFE_WAIT: retain official 77"]
    G15 --> C5{"C5 TRUSTED_RESULT"}
```

## 6. Gate contract

| Gate | Purpose | PASS requirement | On failure/block |
|---|---|---|---|
| C0 CONTENT_BASELINE | certified local content exists | v0.4.2 gates PASS | repair locally, never rewrite official baseline |
| C1 CALIBRATION_READY | local jury has useful predictive/relative behavior | trusted anchors, reproducible packets, no catastrophic rank inversion; absolute score only if error is acceptable | use relative-only pairwise/bands; do not start blind score-chasing |
| C2 CANDIDATE_LIFT | new content is a real improvement | >=2/3 reviewers support target lift, no majority regression, all product gates PASS | keep previous candidate |
| C3 97_CLASS_READY | candidate merits ceiling/release treatment | near-97 integer band structure, calibrated support, final vs trusted-96 is tie-or-better, OpenAI-family holdout has no major blocker | return to blocker matrix, bounded surgery only |
| C4 RELEASE_SAFE | successor cannot silently replace 77 with a regression | actual current official high-water protection active, or explicit Owner risk acceptance | SAFE_WAIT |
| C5 TRUSTED_RESULT | official exact-head review closed | trusted maintainer result captured and reconciled | closeout per score/result |

All gates are one of `PASS`, `FAIL`, `BLOCKED`, `OWNER_REQUIRED`; avoid soft language such as “probably pass”.

## 7. Train A — Calibration Foundation

- **G01** locks latest official rubric, integer score schema, packet composition, visual exposure, and queue semantics.
- **G02** builds a trusted anchor corpus, target >=5 exact-head packages spanning roughly 77/86/90/90/96.
- **G03** runs one valid verdict per anchor per isolated reviewer. No rerolls for low scores.
- **G04** computes reviewer bias, aggregate error, rank/pairwise accuracy and a conservative calibration layer. No complex overfit on a five-anchor dataset.

No v0.4.3 content work before C1.

## 8. Train B — Measure Current Candidate

- **G05** blind-scores v0.4.1a and v0.4.2 with the calibrated jury.
- **G06** converts the result to an integer 97-band blocker matrix: freeze majority-5 dimensions, identify exact evidence needed for each majority-4, treat <=3 as major blockers.

## 9. Train C — Surgical Score Lift

- **G07/G08** create and judge v0.4.3 only from explicit blocker evidence; at most two primary surgeries.
- **G09/G10** are optional. v0.4.4 is admitted only if a specific blocker remains and at least two independent advisers agree the surgery is material and bounded.

Anti-bloat rule: do not raise page count, tables, KPIs, scenario cards or terminology unless they directly resolve a reviewer-visible deficiency. Prefer substitution/recomposition over accumulation.

Core design grammar to preserve unless evidence compels change:

`heterogeneous existing city -> STATUS × ACTION -> ordinary-space sufficiency -> AI spatial admission -> 12 tasks / 3 deep / 9 NO-BUILD -> minimum reversible spatial delta -> stop/reset -> ordinary city`

## 10. Train D — Ceiling Qualification

- **G11** blind-compares the final candidate against a trusted 96-point anchor under identical packet semantics. A 97-class candidate should be majority tie-or-better with no clear loss in critical dimensions.
- **G12** performs one GPT-5.6 Sol OpenAI-family holdout using neutral packets and the current official rubric/prompt contract. It is evidence, not an official score.

## 11. Train E — Safe Release

- **G13** reconstructs the winner on then-current upstream/main rather than pushing an experiment branch directly. Product subtree identity, clean-clone gates, manifest and packet hashes must match.
- **G14** inspects actual current official review-worker code/tests and release policy. PR state alone does not prove high-water protection.
- **G15** is the only official trusted re-review. Exactly one final candidate enters the queue; do not score-fish identical heads.

## 12. Cross-repository contract

This repository is the **Program/Control Plane**. `JerrySkywalker/haidian` is the **Submission/Product Plane**. `open-city-ai/haidian` is the **Official Canonical Plane**. `V:\src\_review_isolation` is the **local ephemeral jury runtime**.

Program roadmaps, goals, calibration, jury verdicts, benchmark strategy, agent instructions and run receipts must never be migrated into the official submission package. See `docs/PROGRAM_CONTROL_AIRLOCK.md`.

## 13. Timebox to 2026-08-31

Preferred sequence:

- Aug 20–21: G01–G02
- Aug 21–22: G03–G04 / C1
- Aug 22: G05–G06
- Aug 22–24: G07
- Aug 24–25: G08 / C2
- Aug 25–27: optional G09–G10
- Aug 27: G11
- Aug 27–28: G12 / C3
- Aug 28–29: G13
- Aug 29–30: G14 / C4
- Aug 30–31: G15 or SAFE_WAIT buffer

If release safety remains blocked, retain the merged official 77 rather than force a risky successor.

## 14. State authority

- Human-readable current pointer: `docs/CURRENT_PROGRAM.md`
- Machine-readable state: `state/JZ97_PROGRAM_STATE.json`
- Goal contracts: `goals/JZ97-G01-*.md` through `goals/JZ97-G15-*.md`
- Durable run evidence: `runs/<RUN_ID>/`

Each Goal must read this roadmap and machine state before mutation, enforce admission requirements, write receipts, and transition state only when exit criteria are proven.
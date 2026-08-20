# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室、Program Control Plane 与长期事实源。

本仓库保存 **JerrySkywalker 与 AI agents 的研究、需求拆解、benchmark、设计决策、候选演化、评分校准、Goal contracts 与 run receipts**。它与正式投稿仓库严格分离：最终参赛产品仅通过 `JerrySkywalker/haidian` 的 `submissions/JerrySkywalker/jingzhang-in-place/**` 进入 `open-city-ai/haidian`。

## 当前事实状态

- Owner-selected submission candidate: **京张续城 / Jing-Zhang In Place**
- Official merged baseline head: `1d5cb1aaa9d76edc3532e593c803cb936070a744`
- Official merged PR: `open-city-ai/haidian#2744`
- Trusted repository-intake score: **77 / 100**
- Frozen v0.4.1a checkpoint: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- Current certified local candidate v0.4.2: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- Existing successor PR #2774: intentionally **Draft** until release admission is safe
- Current long-horizon Program: **`JZ-97-CONVERGENCE-TRAIN-001`**
- Primary implementer: **AGY / Gemini 3.7 Flash High**
- Formal local jury: isolated AGY exact-model panel (Opus 4.6 Thinking / Sonnet 4.6 / Gemini 3.7 Flash High)
- Codex CLI: optional scarce fallback only
- Competition result / award / government adoption: **not determined; no such claim is made**

## Canonical Program control

Start here:

1. [`docs/programs/JZ-97-CONVERGENCE-TRAIN.md`](docs/programs/JZ-97-CONVERGENCE-TRAIN.md) — canonical roadmap + Program DAG + C0–C5 gates
2. [`docs/CURRENT_PROGRAM.md`](docs/CURRENT_PROGRAM.md) — current human-readable pointer
3. [`state/JZ97_PROGRAM_STATE.json`](state/JZ97_PROGRAM_STATE.json) — machine-readable state
4. [`goals/`](goals/) — executable G01–G15 Goal contracts
5. [`docs/PROGRAM_CONTROL_AIRLOCK.md`](docs/PROGRAM_CONTROL_AIRLOCK.md) — control/product repository boundary
6. [`decisions/ADR-JZ97-0001-adopt-program-control.md`](decisions/ADR-JZ97-0001-adopt-program-control.md) — adopted governance decision

Important: historical `runs/...` branches remain durable evidence even when they are not merged into `main`. Canonical governance lives on `main`; run branches carry run-specific receipts.

## Repository roles

```text
jingzhang-ai-design-lab
        Program / Control Plane
        roadmap + goals + state + research + receipts
                    |
                    | curated product outputs only
                    v
JerrySkywalker/haidian
        Submission / Product Plane
        submissions/JerrySkywalker/jingzhang-in-place/**
                    |
                    | scoped participant PR
                    v
open-city-ai/haidian
        Official Canonical Plane
```

`V:\src\_review_isolation` is a separate local ephemeral jury runtime, not submission content.

## Design doctrine

The selected proposal remains **京张续城 / Jing-Zhang In Place**. Its dominant design grammar is:

```text
heterogeneous existing city
→ STATUS × ACTION
→ ordinary-space sufficiency
→ AI spatial admission
→ 12 tasks / 3 deep / 9 NO-BUILD
→ minimum reversible spatial delta
→ human authority + stop/reset
→ ordinary city again
```

The Program protects this grammar from generic smart-city drift unless calibrated reviewer evidence justifies a bounded change.

## Evidence discipline

Where ambiguity matters, use:

- `FACT` — authoritative/cleared source
- `DERIVED` — reproducibly computed
- `ASSUMPTION` — necessary but unverified premise
- `CONCEPT` — design proposal
- `DECISION` — Owner-approved project decision

Never upgrade provisional geometry, benchmark results, design thresholds or generated ideas into official/statutory facts.

## Historical design memory

Candidate 01/02 and Candidate 03 standalone identities remain retired; their useful methods survive as design-review lenses. Candidate 05 became the Owner-selected submission candidate and was implemented/merged through the separate `haidian` fork. Historical concept, research, round and decision files remain available in their original directories and Git history.

## Current next step

Program state currently admits **Train A — Calibration Foundation** only. Do not start v0.4.3 until C1 `CALIBRATION_READY` passes.

The next approved unattended train is:

`goals/JZ97-G01-G02-OFFICIAL-TRUTH-AND-ANCHOR-CORPUS-001.md`

It locks current official reviewer truth and builds the trusted calibration anchor corpus; it does not modify submission content or run formal jury scoring.

## Licenses

- Software/scripts/config: [`LICENSE`](LICENSE) — Apache-2.0
- Original design/research docs: [`LICENSE-DOCS.md`](LICENSE-DOCS.md) — CC BY 4.0, subject to third-party source licenses

# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室、Program Control Plane 与长期事实源。

本仓库保存 **JerrySkywalker 与 AI agents 的研究、需求拆解、benchmark、设计决策、候选演化、评分校准、Goal contracts 与 run receipts**。它与正式投稿仓库严格分离：最终参赛产品仅通过 `JerrySkywalker/haidian` 的 `submissions/JerrySkywalker/jingzhang-in-place/**` 进入 `open-city-ai/haidian`。

## 当前事实状态

- Owner-selected submission: **京张续城 / Jing-Zhang In Place**
- Accepted official PR: `open-city-ai/haidian#4270`
- Accepted reviewed head: `4cb6b1bd7407781d5121fc51ce81e6c8a06c1de1`
- Accepted merge commit: `e0927ba94154e3bf3b66c720f61560b9adba877b`
- Trusted repository-intake score: **93 / 100**
- Trusted vector: `5,5,5,4,5,5,4`
- Current Program: **`JZ-FINAL100-AWARD-CONSOLIDATION-0830`**
- Current Goal: **`JZ100-G01-FINAL100-AWARD-CONSOLIDATION-001`**
- Final machine target: **100/100**
- Later human-panel target: **award-candidate**
- Competition result / award / government adoption: **not determined; no such claim is made**

Historical `JZ-97-CONVERGENCE-TRAIN-001` is retained as durable project memory but is superseded as the active deadline Program because its 77-point baseline/calibration gates no longer match the accepted 93-point official state.

## Canonical current control

Start here:

1. [`docs/programs/JZ-FINAL100-AWARD-CONSOLIDATION.md`](docs/programs/JZ-FINAL100-AWARD-CONSOLIDATION.md) — canonical final Program and unattended execution roadmap
2. [`docs/JINGZHANG_IN_PLACE_FINAL100_DESIGN_DOCTRINE.md`](docs/JINGZHANG_IN_PLACE_FINAL100_DESIGN_DOCTRINE.md) — final humanistic/spatial/visual design doctrine
3. [`docs/CURRENT_PROGRAM.md`](docs/CURRENT_PROGRAM.md) — current human-readable pointer
4. [`state/JZ100_PROGRAM_STATE.json`](state/JZ100_PROGRAM_STATE.json) — machine-readable state
5. [`goals/JZ100-G01-FINAL100-AWARD-CONSOLIDATION-001.md`](goals/JZ100-G01-FINAL100-AWARD-CONSOLIDATION-001.md) — one continuous final unattended Goal
6. [`docs/PROGRAM_CONTROL_AIRLOCK.md`](docs/PROGRAM_CONTROL_AIRLOCK.md) — control/product repository boundary
7. [`decisions/ADR-JZ100-0001-adopt-final100-award-consolidation.md`](decisions/ADR-JZ100-0001-adopt-final100-award-consolidation.md) — Owner adoption decision

Historical `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`, JZ97 state/Goals and historical run branches remain evidence; do not delete them.

## Repository roles

```text
jingzhang-ai-design-lab
        Program / Control Plane
        doctrine + roadmap + goals + state + research + receipts
                    |
                    | curated product instructions only
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

## Final owner-approved design doctrine

### Project

**京张续城 / Jing-Zhang In Place**

### Public slogan

**让未来生长，让城市相续。**

### Humanistic thesis

**技术属于时代，城市属于世代。**

### City philosophy

**城市不是技术的容器，而是代际生活的连续体。**

### Human-facing structure

- **续时 / 续生 / 续忆**
- **长久城市 / 可适应城市 / 暂居智能**
- **众智园=验证 / AI原点=共处 / 大钟寺=裁决**

### Protected professional grammar

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

The professional grammar remains; the final revision makes it subordinate to an urban-design-first human narrative.

## Final development strategy

The only remaining trusted-review score lifts are:

- `implementation_feasibility: 4→5` through one integrated S01 participant-authored P0 pre-feasibility bridge;
- `expression_completeness: 4→5` through identity, gallery cover, human-facing narrative, key-area spatialization, A0/HTML recomposition and real rendered bilingual visual QA.

All five already-5 dimensions are protected from broad redesign.

Preferred final implementation topology: **one Terra Ultra sole writer**, with Sol Ultra reserved for read-only architecture/Supervisor or an explicitly configured single-writer substitute.

Known local entry point:

```powershell
jcodex-role -Role implementer -WorkingDirectory 'V:\src\haidian'
```

The final Goal is designed to run unattended from fresh upstream admission through product implementation, pixel-level visual QA, compressed certification, one read-only Supervisor, one successor PR and bounded exact-review repairs. Routine Owner confirmation is not required.

## Evidence discipline

Where ambiguity matters, use:

- `FACT` — authoritative/cleared source
- `DERIVED` — reproducibly computed
- `ASSUMPTION` — necessary but unverified premise
- `CONCEPT` — design proposal
- `DECISION` — Owner-approved project decision

Never upgrade provisional geometry, benchmark results, design thresholds, P0 reference dimensions, capacities, ROM values or generated ideas into official/statutory/field facts.

## Historical design memory

Candidate 01/02 and Candidate 03 standalone identities remain retired; Candidate 05 became the Owner-selected submission. Historical concepts, comparisons, jury experiments, JZ97 calibration plans and run branches remain available in their original directories and Git history.

## Licenses

- Software/scripts/config: [`LICENSE`](LICENSE) — Apache-2.0
- Original design/research docs: [`LICENSE-DOCS.md`](LICENSE-DOCS.md) — CC BY 4.0, subject to third-party source licenses

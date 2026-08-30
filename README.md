# Jingzhang AI Design Lab

> 百年京张 AI 创新带城市设计的开放设计实验室、Program Control Plane 与长期事实源。

本仓库保存 **JerrySkywalker 与 AI agents 的研究、需求拆解、benchmark、设计决策、候选演化、评分校准、Goal contracts 与 run receipts**。它与正式投稿仓库严格分离：最终参赛产品仅通过 `JerrySkywalker/haidian` 的 `submissions/JerrySkywalker/jingzhang-in-place/**` 进入 `open-city-ai/haidian`。

## 当前事实状态

- Owner-selected submission: **京张续城 / Jing-Zhang In Place**
- Current accepted official PR: `open-city-ai/haidian#4285`
- Current reviewed head: `af75ac57f97f977f5f842dcf28a8b3263fb07e9a`
- Current merge commit: `17787b8581cc2f4b79f111277ae1930413673d67`
- Trusted repository-intake score: **93 / 100**
- Trusted vector: `5,5,5,4,5,5,4`
- Status: `formal-review-ready`, `featured-candidate`, no blocking repairs
- Current Program: **`JZ-FINAL100-AWARD-CONSOLIDATION-0830`**
- Current Goal: **`JZ100-A03-POST4285-PARTICIPANT-CLOSURE-001`**
- Current strategy: **A02 Strategy B — implementation readiness + reviewer visibility**
- Final machine target: **100/100**
- Later human-panel target: **award-candidate**
- Competition result / award / government adoption: **not determined; no such claim is made**

PR #4270, G01 and historical `JZ-97-CONVERGENCE-TRAIN-001` remain durable project memory but are no longer the active product baseline or execution Goal.

## Canonical current control

Start here:

1. [`AGENTS.md`](AGENTS.md) — current execution agreement and source-of-truth hierarchy
2. [`docs/CURRENT_PROGRAM.md`](docs/CURRENT_PROGRAM.md) — current post-#4285 program pointer and audit findings
3. [`docs/JINGZHANG_IN_PLACE_FINAL100_DESIGN_DOCTRINE.md`](docs/JINGZHANG_IN_PLACE_FINAL100_DESIGN_DOCTRINE.md) — frozen humanistic/spatial design doctrine
4. [`state/JZ100_PROGRAM_STATE.json`](state/JZ100_PROGRAM_STATE.json) — machine-readable current state
5. [`goals/JZ100-A03-POST4285-PARTICIPANT-CLOSURE-001.md`](goals/JZ100-A03-POST4285-PARTICIPANT-CLOSURE-001.md) — current overnight unattended Goal
6. [`docs/PROGRAM_CONTROL_AIRLOCK.md`](docs/PROGRAM_CONTROL_AIRLOCK.md) — control/product repository boundary
7. [`docs/programs/JZ-FINAL100-AWARD-CONSOLIDATION.md`](docs/programs/JZ-FINAL100-AWARD-CONSOLIDATION.md) — original Final100 Program governance/history; current A03 pointer overrides its stale G01-specific admission facts

Historical JZ97, G01, audits and run branches remain evidence; do not delete them.

## A02 post-#4285 machine-100 audit

The latest read-only gap audit concluded:

`AUDIT_COMPLETE__GO_STRATEGY_B__MACHINE_100_CREDIBLE_NOT_GUARANTEED`

Important verified findings:

- current scoring has **no hard external-evidence requirement** for Implementation 5;
- no explicit score cap was found for provisional/OFFLINE_READY/HOLD status;
- a current same-pipeline 100-point precedent exists with equivalent external gaps;
- its differentiator was deeper participant-authored delivery/readiness architecture;
- #4285 still lacks a single reviewer-visible integrated carrier/task/RACI/safety/operations/acceptance/rights/Day-1/Week-1 readiness dossier;
- Expression 4 is bounded by information density/small text and the fact that the reviewer sees only page one of each A0/A3 PDF plus fixed initial viewports;
- standalone custom JSON is not automatically supplied raw to the Trusted Review Agent, so material evidence must be synchronized into canonical scoring surfaces and genuine reviewer-visible human surfaces.

Current A03 target estimates from that audit:

- Implementation 5: `MEDIUM-HIGH`
- Expression 5: `MEDIUM-HIGH`
- Machine 100: `MEDIUM`
- active work: `4.5–6.5 h`
- unattended elapsed: `6–8 h`

These are planning judgments, not score assurances.

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

The professional grammar remains; human-facing design remains urban-design-first.

## Current development strategy

A03 is a bounded overnight successor train, not a new concept redesign.

It targets:

1. `implementation_feasibility: 4→5` through one integrated participant-controlled readiness dossier covering carrier screening, bounded reference task, role-type RACI/handoff, hazard/lockout/NO-GO, operations, acceptance, rights acquisition and Day-1/Week-1 HOLD closure, with material evidence synchronized into reviewer-visible canonical surfaces;
2. `expression_completeness: 4→5` by removing duplicate reading routes, simplifying the densest reviewer-visible diagrams/tables and making A0/A3 page one plus initial HTML viewports self-sufficient.

All five already-5 dimensions and the humanistic doctrine are frozen.

Preferred topology: **one Terra Ultra sole writer**, Sol Ultra only for final read-only Supervisor. No merge is authorized by A03.

Known launcher:

```powershell
jcodex-role -Role implementer -WorkingDirectory 'V:\src\haidian'
```

## Evidence discipline

Where ambiguity matters, use:

- `FACT` — authoritative/cleared source
- `DERIVED` — reproducibly computed
- `ASSUMPTION` — necessary but unverified premise
- `CONCEPT` — design proposal
- `DECISION` — Owner-approved project decision
- `PUBLIC_CONTEXT_ONLY` — public context that does not establish project rights/authority

Never upgrade provisional geometry, benchmark results, design thresholds, P0 reference dimensions, capacities, public context or generated ideas into official/statutory/field facts.

Keep `P0_GO=false`, `approved_budget=null`, `funding_commitment=null`, `market_quotation_count=0` and applicable `HOLD_EXTERNAL` states until real evidence exists.

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

## Licenses

- Software/scripts/config: [`LICENSE`](LICENSE) — Apache-2.0
- Original design/research docs: [`LICENSE-DOCS.md`](LICENSE-DOCS.md) — CC BY 4.0, subject to third-party source licenses

# ADR-JZ97-0001 — Adopt JZ-97 Program Control Plane

Status: **ACCEPTED**  
Decision owner: JerrySkywalker  
Program: `JZ-97-CONVERGENCE-TRAIN-001`

## Context

The original Jing-Zhang submission is complete and merged, but post-merge score-lift work has grown into a multi-stage calibration, candidate, jury and release-safety program. Keeping that logic only in chat prompts creates context drift and makes long unattended AGY runs difficult to resume safely.

The official participant repository also enforces submission-only PR scope, so Program governance must not be committed into `haidian` outside the participant package or mixed into the professional submission.

## Decision

1. `JerrySkywalker/jingzhang-ai-design-lab` is the canonical **Program/Control Plane and design-memory repository**.
2. `JerrySkywalker/haidian` is the **Submission/Product Plane**.
3. `open-city-ai/haidian` is the **Official Canonical Plane**.
4. `V:\src\_review_isolation` is the **local ephemeral jury runtime**.
5. Canonical roadmap: `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`.
6. Machine state: `state/JZ97_PROGRAM_STATE.json`.
7. Executable Goal contracts live under `goals/` and enforce admission/exit gates.
8. Program/control files are forbidden from the official submission diff; the airlock document defines the migration whitelist.
9. Primary implementation uses AGY; Codex CLI is not a planned dependency. Formal local jury uses exact-model isolated AGY processes. A single ChatGPT GPT-5.6 Sol holdout is reserved for late-stage OpenAI-family comparison.
10. The existing merged 77-point official baseline remains protected until actual official high-water release protection is proven active or the Owner explicitly accepts regression risk.

## Consequences

- Long runs can resume from repository state rather than chat context.
- Goal sequencing becomes machine-auditable.
- Product and control histories remain cleanly separated.
- Public design-lab visibility means no secrets/private/proprietary material may be committed.
- Historical run branches remain evidence; they need not all be merged into main to establish canonical Program governance.
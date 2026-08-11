# ADR-0002: Round-1 Candidate Downselect

- **Status:** Accepted for Round 2
- **Decision date:** 2026-08-12
- **Authority:** Human Owner instruction `JZ-R2-OVERNIGHT-001`
- **Scope:** design-lab exploration only; not a submission selection

## Context

Round 1 produced three complete but deliberately different urban-design candidates. The Owner accepted the Chief Architect / Jury assessment and authorized the following downselect to focus the next evidence budget on a head-to-head falsification rather than equal continuation.

## Decision

```text
C01 = KEEP_HARDEN
C02 = KEEP_CHALLENGER
C03 = KILL_STANDALONE / SALVAGE_REVIEW_LENS
ROUND_2 = C01_VS_C02_FALSIFICATION
NEW_CANDIDATE_REQUIRED = false
FORMAL_SUBMISSION_READY = false
```

This decision does not select a final winner. Candidate 03's source files remain intact; only its status and the disposition of its reusable reasoning change.

## Rationale

### Candidate 01 — KEEP_HARDEN

Its potential advantage is that the Owner's system-engineering practice could affect the core proposition rather than decorate it. In particular, shared physical urban infrastructure for changing heterogeneous embodied systems may have genuine depth if task requirements can determine minimum sensing, compute, energy, tool and maintenance resources and if the allocation survives degraded conditions.

Its burden of proof is severe. Urban LLMs, agents, robots, reconfiguration, fallback, open platforms and public testbeds are already crowded territories. The technical system currently risks overpowering the urban design. Round 2 must therefore remove occupied language, test the residual kernel and show non-generic spatial consequences.

### Candidate 02 — KEEP_CHALLENGER

Its advantage is ordinary-day completeness. The three key areas currently possess clearer civic roles, and the proposal is a useful stress test of whether Candidate 01 can become a good city rather than a technology programme.

Its burden of proof is equally severe. Complete neighbourhood, belonging, local-unit and fifteen-minute ideas are highly occupied. The three-neighbourhood structure may merely rename the three key areas prescribed by the taskbook. Round 2 must establish why there are exactly three spatially meaningful units and why their federation changes space and operations.

### Candidate 03 — KILL STANDALONE / SALVAGE REVIEW LENS

Candidate 03 will not receive further standalone-candidate development in this round. Its strongest value is converted into a candidate-neutral `Living Systems Gate` that tests existing living assets, soil, water, canopy, seasonal comfort, refuge, maintenance and recovery. This preserves its critical force without treating ecological review as a third branding system.

## Consequences

- Candidate 01 and Candidate 02 receive symmetric attempts at falsification; prior investment provides no protection.
- Candidate 03 remains in the repository as design memory and may not be presented as an active Round-2 candidate.
- A failure of either or both candidates is a valid research outcome.
- No material is migrated to `open-city-ai/haidian`, no formal submission is created and `main` is not changed by the overnight run.
- Final selection remains `OWNER_DECISION_REQUIRED`.

## Supersession condition

Only a subsequent explicit Owner decision recorded in the design-decision record may advance, kill, combine or select a candidate after Round 2.

# Future Subagent Development Loop & Score Aggregation Policy

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  

---

## 1. Future Host Development Loop (Phases A - F)

When active score-lift iterations begin in subsequent goals, the development team will operate under this deterministic 6-phase cycle:

```
[ PHASE A: Explorer Analysis ]
       │
       ▼
[ PHASE B: Critic Adversarial Review ]
       │
       ▼
[ PHASE C: Main Orchestrator Selection (Max 2 Surgeries) ]
       │
       ▼
[ PHASE D: Worker Targeted Implementation ]
       │
       ▼
[ PHASE E: Validator Gate & Consistency Check ]
       │
       ▼
[ PHASE F: Main Freezes Candidate Head ]
       │
       ▼
[ TRANSITION: Leave Host Workflow -> Enter Isolated Jury ]
```

### Phase Details:
1. **PHASE A (Explorer Analysis)**: `jz-explorer` (`model: pro`) scans `open-city-ai/haidian` and `jingzhang-ai-design-lab` against `CURRENT_OFFICIAL_RUBRIC.md` to identify discrete blockers and evidence gaps.
2. **PHASE B (Critic Adversarial Review)**: `jz-critic` (`model: pro`) rigorously challenges the blocker list, filtering out superficial or rubric-gaming proposals.
3. **PHASE C (Main Selection)**: Primary orchestrator (`gemini-3.7-flash-high`) selects at most **two high-leverage surgeries** for the iteration.
4. **PHASE D (Worker Implementation)**: `jz-worker` (`model: inherit`) executes surgical code, narrative, or data modifications.
5. **PHASE E (Validator Certification)**: `jz-validator` (`model: flash`) runs automated gates (schema checks, calculations, completeness rules).
6. **PHASE F (Head Freeze)**: Primary agent commits and tags the candidate head, exports the immutable packet to `_review_isolation\packet`, and hands off to the Sandbox jury.

---

## 2. Deterministic Jury Score Aggregation Policy

Models are **not** asked to calculate composite numerical scores or arbitrate weighted sums directly.

### Reviewer Output Contract:
Each independent reviewer outputs only:
- **Dimension Bands**: `score` (0 to 5) for each of the 7 rubric dimensions
- **Evidence**: Specific file paths and citations
- **Blocker to Next Band**: Qualitative criteria required for higher score
- **Confidence**: 0.0 to 1.0
- **Pairwise Preference**: Preference between new candidate and prior baseline

### Host Aggregator Responsibilities:
The host deterministic script calculates:
- **Median/Majority Dimension Score**: Consensus score per dimension
- **Weighted Total**: Using official dimension weights (Brief: 20, Originality: 10, AI Planning: 15, Feasibility: 20, Public Interest: 10, Risk/Compliance: 10, Expression: 15; Total = 100)
- **Jury Disagreement Index**: Variance between Opus, Sonnet, and Gemini
- **Promotion Decision**: Requires >= 2 model concurrence + pairwise majority + 0 gate regressions.

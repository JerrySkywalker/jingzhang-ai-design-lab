# AGY Isolated Jury Architecture

**Goal ID**: `JZ-AGY-HYBRID-SUBAGENT-JURY-MIGRATION-001`  
**Date**: 2026-08-20  
**Status**: ARCHITECTED & TESTED  

---

## 1. Architectural Philosophy

The Jing-Zhang evaluation system requires absolute isolation between the development team and the formal evaluation jury. 

1. **Development Environment (Host)**: 
   - Uses `agy --dangerously-skip-permissions` with custom workspace subagents (`jz-explorer`, `jz-worker`, `jz-critic`, `jz-validator`) for rapid, friction-free iterations.
2. **Jury Environment (Sandbox)**:
   - Uses completely isolated Windows Sandbox instances.
   - Runs headless AGY CLI with exact model pinning.
   - Forbids `--dangerously-skip-permissions` inside the Sandbox to maintain strict review boundaries.
   - Reviewer instances are physically segregated from the host workspace, past conversations, and each other.

---

## 2. Multi-Model Jury Composition

To prevent single-model bias, the formal jury consists of 3 distinct foundation model families:

```
+-------------------------------------------------------------------------+
|                           FORMAL LOCAL JURY                             |
+-------------------------------------------------------------------------+
| Reviewer A : Claude Opus 4.6 Thinking   (Anthropic Flagship Reasoning)  |
| Reviewer B : Claude Sonnet 4.6          (Anthropic Fast Analytical)     |
| Reviewer C : Gemini 3.7 Flash High      (Google High-Reasoning Flash)   |
+-------------------------------------------------------------------------+
| Tie-Breaker: GPT-OSS 120B Medium        (Open Model Dispute Resolution) |
+-------------------------------------------------------------------------+
```

---

## 3. Gemini Bias Mitigation Protocol

Because the host orchestrator and development loop leverage Google Gemini models, Reviewer C (`gemini-3.7-flash-high`) has strictly **one vote** among three.

### Candidate Promotion Rules:
A design candidate can only be promoted if:
1. **Multi-Model Concurrence**: At least two of the three independent jury models (e.g. Opus + Sonnet, or Opus + Gemini) agree that the candidate achieves material score improvement.
2. **Pairwise Majority**: Pairwise preference confirms the new candidate over the prior baseline across at least 2 reviewers.
3. **No Blocker Regressions**: Zero regressions on critical compliance, depth, or spatial admission gates.

Gemini raw total score alone is **never** sufficient evidence to declare a candidate improvement.

---

## 4. Tie-Breaker Invocation Criteria

`gpt-oss-120b-medium` is invoked **only** under the following edge conditions:
- Reviewers A, B, and C produce an unresolvable 1-1-1 split on a major rubric dimension band.
- Pairwise preference is deadlocked or uncalibrated.
- Material factual dispute arises regarding visible packet evidence.

The Tie-Breaker receives the exact same fixed packet (`C:\ReviewPacket`) and identical scorecard schema. Repeated scoring probes or score-fishing are prohibited.

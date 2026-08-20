# Agent Working Agreement

This repository is the persistent **Program/Control Plane, design-memory and research workspace** for the Centennial Jing-Zhang AI Innovation Belt project. It is not the final submission repository.

## 1. Source-of-truth hierarchy

When statements conflict, use this order:

1. latest canonical files in `open-city-ai/haidian` for official rules/tooling;
2. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md` for Program sequencing/governance;
3. `state/JZ97_PROGRAM_STATE.json` for current machine state;
4. official or cleared public primary sources;
5. reproducible derived calculations;
6. explicitly labelled assumptions/concepts.

Never upgrade an assumption, provisional geometry, benchmark claim or generated idea into official fact.

## 2. Current project state

- Owner-selected submission candidate: `JINGZHANG_IN_PLACE`
- Official merged baseline: `1d5cb1aaa9d76edc3532e593c803cb936070a744`
- Trusted repository-intake score: `77`
- Frozen v0.4.1a: `94c51f2011a365a1cb2674a62f8cc3af7aba59e5`
- Current certified local v0.4.2: `a489aa56e07a206e308fd53d6c3dbdf44dcf1f89`
- Program: `JZ-97-CONVERGENCE-TRAIN-001`
- Current train: Calibration Foundation; v0.4.3 is not admitted before C1 PASS.
- Competition/award/government adoption remains undetermined; never imply otherwise.

## 3. Mandatory Goal bootstrap

Before executing a JZ97 Goal, read:

1. `docs/programs/JZ-97-CONVERGENCE-TRAIN.md`
2. `docs/CURRENT_PROGRAM.md`
3. `state/JZ97_PROGRAM_STATE.json`
4. `docs/PROGRAM_CONTROL_AIRLOCK.md`
5. the selected file under `goals/`

Goal admission and exit rules are hard contracts. If prerequisites do not match, return `DISPOSITION=BLOCKED_PROGRAM_STATE` rather than skipping ahead.

## 4. Execution policy

- Primary host implementer: AGY `gemini-3.7-flash-high`
- Standard host mode: `agy --dangerously-skip-permissions --model gemini-3.7-flash-high`
- Explorer/Critic: `pro` subagent tier
- Worker: `inherit`
- Validator: `flash`
- Formal local jury: exact-model AGY processes inside physically isolated Windows Sandbox packets
- Jury A: `claude-opus-4-6-thinking`
- Jury B: `claude-sonnet-4-6`
- Jury C: `gemini-3.7-flash-high`
- Tie-break only: `gpt-oss-120b-medium`
- Codex CLI: no planned dependency; scarce fallback only
- ChatGPT GPT-5.6 Sol: reserved for G12 OpenAI-family holdout and Owner/architect guidance

Formal isolated reviewers do not inherit the host dangerous-permission mode.

## 5. Evidence labels

Use:
- `FACT`
- `DERIVED`
- `ASSUMPTION`
- `CONCEPT`
- `DECISION`

Precision-sensitive design thresholds must state whether they are verified facts, concept thresholds or field-validation requirements.

## 6. Repository boundary

Follow `docs/PROGRAM_CONTROL_AIRLOCK.md`.

- This repository may contain roadmap, goals, state, benchmark/calibration, decisions, experiments and run receipts.
- `JerrySkywalker/haidian` is product-only.
- Program/control files must never appear in the official participant PR diff.
- Do not mirror the full official repository or commit competitors' large media/PDFs here.
- Keep credentials, private data and proprietary planning material out of this public repository.

## 7. Change discipline

For material Program or design changes:

1. verify Goal admission;
2. create isolated worktree/branch where required;
3. preserve prior immutable heads;
4. write durable run receipts;
5. update relevant decision/evidence records;
6. transition machine state only when exit criteria are proven;
7. push only the repository/branch explicitly permitted by the Goal.

Do not erase rejected designs or failed experiments when they contain reusable evidence.

## 8. Scoring discipline

- Official-style dimension bands are integers 0..5.
- Fractional host estimates are `DEV_ADVISORY_ONLY`.
- No identical-head score rerolls to seek favorable output.
- Formal local score = isolated jury evidence + deterministic aggregation; it is not an official trusted score.
- Official score exists only when the official trusted maintainer pipeline reviews an exact head.
- High local score does not authorize release while C4 is blocked.

## 9. Design doctrine

Preserve the selected proposal's dominant grammar unless calibrated evidence requires a bounded change:

`heterogeneous existing city -> STATUS × ACTION -> ordinary-space sufficiency -> AI spatial admission -> 12/3/9 -> minimum reversible spatial delta -> human authority/stop/reset -> ordinary city`.

Do not replace complete urban design with a robotics, sensing, governance, simulation or agent topic. Avoid generic smart-city drift and rubric-driven document bloat.

## 10. Release safety

The merged 77-point official version is a protected historical anchor. Do not mark the draft successor Ready or enter trusted review merely because a local jury predicts a high score. G14 must prove actual current high-water protection in merged official code/tests, or the Owner must explicitly accept regression risk.

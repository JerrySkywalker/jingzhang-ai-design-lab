# JZ97 Codex-native cutover and convergence report

## Outcome

The Codex-native dual-profile panel is the current formal-local execution path. Historical AGY/Windows Sandbox assets are preserved and frozen. Ten required anchor scorecards, one tolerance-triggered anchor holdout, four frozen-candidate scorecards, and two frozen-shadow scorecards completed with structured output and deterministic totals.

The panel is not calibrated for absolute scores or relative ordering. Consensus MAE is `6.7`, pairwise ordering accuracy is `55.56%`, and major inversions exist. The only valid calibration mode is `UNTRUSTED`; local 96–97 totals must not be interpreted as predicted official scores.

Frozen V041A and V042 are indistinguishable under this panel: Primary ties them at `97`; Challenger places V042 one point higher (`97` versus `96`). With untrusted relative calibration, `FORMAL_MEASURED_WINNER=INCONCLUSIVE`.

## Blocker decision

Using V042 as the current-candidate blocker-matrix basis, five dimensions are 5/5. Two dimensions are reviewer disagreements:

1. `ai_planning_innovation` — Primary 5, Challenger 4. The deficiency is that rigorous admission/governance is stronger than demonstrated domain-specific AI capability and measured AI-service outcomes.
2. `expression_completeness` — Primary 4, Challenger 5. The deficiency is schematic, scale-free visual resolution, weak board hierarchy, small labels/plans, and limited site-specific ground-level/massing/experiential evidence.

Frozen shadow resolves the first target to 5/5. It does not resolve expression completeness, which remains 4/5 with the same visible deficiency. Shadow also introduces a feasibility disagreement (5/4), so `implementation_feasibility` is a non-regression guard.

`A2_MODE=ONE_TIGHTLY_TARGETED_EXPERIMENTAL_PATCH`. The admitted next action is one expression-only recomposition/substitution from the frozen shadow head, preserving the already-solved AI target and every majority-5 dimension.

## Evidence boundary

Every evidence-bearing scorecard ran in a fresh `codex exec` process with `--ephemeral`, `--sandbox read-only`, `--ignore-user-config`, `--ignore-rules`, `--output-schema`, explicit model, explicit reasoning, empty reviewer workdir, stdin neutral text evidence, and explicit images. No TUI, MCP, external search, subagent, reviewer history, official score, source mapping, or other reviewer output was supplied.

Three rejected infrastructure attempts occurred before the evidence-bearing P01 Primary evaluation: unsupported alias, invalid structured-output schema, and Windows read-only shell access. They produced no score and are preserved as coordinator preflight evidence. Schema/model probes and the stdin/image evidence path then passed. Raw model outputs remain preserved; normalized scorecards only enforce deterministic totals and an 800-character concision ceiling.

The inherited X8 packet contained a large public submission census. Strict identity redaction materially reduced that neutral view, so its 17-point Primary/Challenger spread triggered the allowed holdout. This is an additional reason not to trust the resulting calibration; it does not affect the frozen candidate/shadow packet mappings.

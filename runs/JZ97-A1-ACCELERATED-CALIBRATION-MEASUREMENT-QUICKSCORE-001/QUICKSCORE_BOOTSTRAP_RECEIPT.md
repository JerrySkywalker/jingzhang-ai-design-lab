# QuickScore Bootstrap Receipt — Phase 5

```text
RUN_ID=JZ97-A1-ACCELERATED-CALIBRATION-MEASUREMENT-QUICKSCORE-001
TOOL_PATH=tools/jz_quickscore.py
DISPOSITION=PASS
QUICKSCORE_IMPLEMENTED=true
QUICKSCORE_DEFAULT_MODEL=claude-sonnet-4-6
MODE=DEV_ADVISORY
FORMAL_EVIDENCE=false
ABSOLUTE_SCORE_UNTRUSTED=true
GATE_PASS_PROHIBITED=true
```

## 1. Tool Architecture & Design Principles

`tools/jz_quickscore.py` is a thin, robust CLI tool for rapid developmental iteration during design surgeries (A2/A3). It enforces strict safety boundaries:

1. **Rubric Fidelity**: Uses the official 7-dimension rubric and weights with integer 0..5 band scores:
   - `brief_alignment` (20)
   - `originality` (10)
   - `ai_planning_innovation` (15)
   - `implementation_feasibility` (20)
   - `public_interest_inclusion` (10)
   - `risk_compliance` (10)
   - `expression_completeness` (15)
2. **Deterministic Computation**: Total weighted score is calculated mathematically as $\sum (\text{score}_i / 5.0 \times \text{weight}_i)$, never trusting model arithmetic.
3. **Execution Confinement**: Runs via fresh temporary `GEMINI_HOME` and `ANTIGRAVITY_HOME` directories. MCP and subagents are explicitly disabled via environment variables. Working directory is locked to the candidate packet.
4. **Non-Self-Judging Default**: Default model is `claude-sonnet-4-6` (since the primary implementation engine on host is Gemini). Confirmatory dual-eval (`--mode confirm`) runs Sonnet + Gemini.
5. **Pairwise Differential Support**: Supports `--compare-with <packet_dir>` to compute dimensional and total score deltas against frozen winners (`v0.4.1a`, `v0.4.2`).
6. **Machine-Readable & Human Output**: Emits structured JSON and clear markdown/terminal tables.

## 2. Hard Governance Rules

- **DEV_ADVISORY ONLY**: QuickScore output is strictly developmental feedback.
- **Formal Evidence Prohibited**: QuickScore output may NEVER be cited as formal jury evidence or used to pass Gates C1, C2, C3, or C4.
- **Absolute Score Untrusted**: Pending formal calibration verification, absolute scores are marked untrusted and relative pairwise deltas take precedence.

## 3. CLI Invocation Syntax

```bash
# Fast evaluation (Sonnet 4.6 default)
python tools/jz_quickscore.py path/to/packet

# Confirmatory dual-eval (Sonnet 4.6 + Gemini 3.7)
python tools/jz_quickscore.py path/to/packet --mode confirm

# Pairwise comparison against baseline
python tools/jz_quickscore.py path/to/candidate_packet --compare-with path/to/baseline_packet --out-json results.json
```

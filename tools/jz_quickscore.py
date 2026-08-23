#!/usr/bin/env python3
"""
tools/jz_quickscore.py

Thin local iteration scorer for Jing-Zhang Centennial AI Innovation Belt.
ROLE: DEV_ADVISORY ONLY. Never produces formal evidence; never passes gates C1/C2/C3/C4.

Default FAST Reviewer: claude-sonnet-4-6
Default CONFIRM Reviewers: claude-sonnet-4-6 + gemini-3.7-flash-high

Requirements:
- Official current 7-dimension rubric (integer 0..5 scale)
- Deterministic weighted total calculation
- Fresh temporary AGY home/context per run (no history, no MCP, no subagents)
- Packet-only read scope
- Pairwise comparison support
- Machine-readable JSON + concise human-readable output
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

OFFICIAL_WEIGHTS: Dict[str, int] = {
    "brief_alignment": 20,
    "originality": 10,
    "ai_planning_innovation": 15,
    "implementation_feasibility": 20,
    "public_interest_inclusion": 10,
    "risk_compliance": 10,
    "expression_completeness": 15,
}

DIMENSION_DESCRIPTIONS: Dict[str, str] = {
    "brief_alignment": "Alignment with competition brief, spatial constraints, and urban requirements",
    "originality": "Originality of urban design concepts, morphology, and spatial synthesis",
    "ai_planning_innovation": "Depth, plausibility, and integration of AI spatial systems and workflows",
    "implementation_feasibility": "Engineering, phasing, regulatory feasibility, and realistic urban execution",
    "public_interest_inclusion": "Public realm quality, accessibility, citizen participation, and social benefit",
    "risk_compliance": "Risk mitigation, safety, statutory compliance, and operational fail-safes",
    "expression_completeness": "Clarity of technical documentation, figures, structured data, and deliverables",
}

SCORE_BAND_DESCRIPTIONS: Dict[int, str] = {
    0: "absent_or_invalid",
    1: "seriously_deficient",
    2: "weak",
    3: "adequate_compliant",
    4: "strong_distinctive",
    5: "exceptional_exemplary",
}


def build_scoring_prompt(packet_dir: Path, candidate_id: str, reviewer_id: str, model_name: str) -> str:
    manifest_path = packet_dir / "REVIEW_PACKET_MANIFEST.json"
    packet_hash = "UNKNOWN"
    if manifest_path.is_file():
        try:
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest_data = json.load(f)
                packet_hash = manifest_data.get("packet_hash", "UNKNOWN")
        except Exception:
            pass

    return f"""You are an expert urban planning, urban design, and AI systems reviewer evaluating a submission packet for the Centennial Jing-Zhang AI Belt competition.

You are acting as an ADVISORY REVIEWER ({reviewer_id}) using model: {model_name}.
Candidate ID: {candidate_id}
Packet Directory: {packet_dir}
Packet Hash: {packet_hash}

Carefully evaluate the candidate package files in {packet_dir} according to the 7 official rubric dimensions:
1. brief_alignment (Weight: 20): Alignment with Centennial Jing-Zhang brief and spatial constraints.
2. originality (Weight: 10): Novelty and distinctiveness of urban morphology and concepts.
3. ai_planning_innovation (Weight: 15): Integration and spatial depth of AI urban systems.
4. implementation_feasibility (Weight: 20): Realistic phasing, engineering, and statutory delivery.
5. public_interest_inclusion (Weight: 10): Civic accessibility, social equity, and public realm quality.
6. risk_compliance (Weight: 10): Safety controls, regulatory alignment, and reversibility/stop mechanisms.
7. expression_completeness (Weight: 15): Completeness of drawings, structured data, metrics, and report.

Score each dimension on an integer scale from 0 to 5:
0 = absent_or_invalid, 1 = seriously_deficient, 2 = weak, 3 = adequate_compliant, 4 = strong_distinctive, 5 = exceptional_exemplary.

For each dimension, supply:
- dimension_id: exact string identifier
- score: integer 0..5
- evidence: array of strings citing specific files and details in the packet
- blocker_to_next_band: string explaining what prevents a higher score
- confidence: number between 0.0 and 1.0
- regression_risk: one of "none", "low", "moderate", "high"

Compute total_weighted_score = sum(dimension_score / 5.0 * weight).

You must output a single valid JSON object adhering strictly to this JSON format without markdown wrapping outside the JSON object:

{{
  "mode": "DEV_ADVISORY",
  "formal_evidence": false,
  "candidate_id": "{candidate_id}",
  "reviewer_id": "{reviewer_id}",
  "model": "{model_name}",
  "rubric_scores": [
    {{
      "dimension_id": "brief_alignment",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "originality",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "ai_planning_innovation",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "implementation_feasibility",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "public_interest_inclusion",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "risk_compliance",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }},
    {{
      "dimension_id": "expression_completeness",
      "score": 4,
      "evidence": ["Citations from proposal/drawings"],
      "blocker_to_next_band": "Exact deficiency preventing 5",
      "confidence": 0.90,
      "regression_risk": "none"
    }}
  ],
  "total_weighted_score": 80.0,
  "rationale_markdown": "Professional critique summarizing strengths and deficiencies..."
}}
"""


def compute_deterministic_score(rubric_scores: List[Dict[str, Any]]) -> Tuple[float, Dict[str, int]]:
    total = 0.0
    dim_map: Dict[str, int] = {}
    for item in rubric_scores:
        dim_id = item.get("dimension_id", "")
        if dim_id in OFFICIAL_WEIGHTS:
            score = int(item.get("score", 0))
            score = max(0, min(5, score))
            weight = OFFICIAL_WEIGHTS[dim_id]
            dim_weighted = (score / 5.0) * weight
            total += dim_weighted
            dim_map[dim_id] = score
    return round(total, 2), dim_map


def run_single_model_review(
    packet_dir: Path,
    candidate_id: str,
    reviewer_id: str,
    model_name: str,
    agy_exe: str = "agy",
    timeout_sec: int = 300,
) -> Dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix=f"jz_quickscore_{reviewer_id}_") as tmp_home:
        env = os.environ.copy()
        env["GEMINI_HOME"] = tmp_home
        env["ANTIGRAVITY_HOME"] = tmp_home
        # Disable MCP and subagents
        env["ANTIGRAVITY_DISABLE_MCP"] = "1"
        env["ANTIGRAVITY_DISABLE_SUBAGENTS"] = "1"

        prompt = build_scoring_prompt(packet_dir, candidate_id, reviewer_id, model_name)

        cmd = [agy_exe, "--model", model_name, "--print", prompt]

        try:
            res = subprocess.run(
                cmd,
                cwd=str(packet_dir),
                env=env,
                capture_output=True,
                text=True,
                timeout=timeout_sec,
                encoding="utf-8",
                errors="replace",
            )
            raw_output = res.stdout + "\n" + res.stderr
        except subprocess.TimeoutExpired:
            return {
                "status": "TIMEOUT",
                "error": f"Review execution timed out after {timeout_sec}s",
                "model": model_name,
                "reviewer_id": reviewer_id,
            }
        except Exception as e:
            return {
                "status": "EXEC_ERROR",
                "error": str(e),
                "model": model_name,
                "reviewer_id": reviewer_id,
            }

        # Extract JSON from output
        json_match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if not json_match:
            return {
                "status": "JSON_PARSE_ERROR",
                "error": "No JSON block found in model output",
                "raw_output": raw_output[:2000],
                "model": model_name,
                "reviewer_id": reviewer_id,
            }

        try:
            parsed = json.loads(json_match.group(0))
        except Exception as e:
            return {
                "status": "JSON_PARSE_ERROR",
                "error": f"Failed to parse extracted JSON: {e}",
                "raw_output": raw_output[:2000],
                "model": model_name,
                "reviewer_id": reviewer_id,
            }

        rubric_scores = parsed.get("rubric_scores", [])
        deterministic_total, dim_map = compute_deterministic_score(rubric_scores)

        # Enforce canonical metadata
        parsed["mode"] = "DEV_ADVISORY"
        parsed["formal_evidence"] = False
        parsed["absolute_score_untrusted"] = True
        parsed["gate_pass_prohibited"] = True
        parsed["candidate_id"] = candidate_id
        parsed["reviewer_id"] = reviewer_id
        parsed["model"] = model_name
        parsed["total_weighted_score"] = deterministic_total
        parsed["dimension_scores"] = dim_map
        parsed["timestamp"] = datetime.now(timezone.utc).isoformat()
        parsed["status"] = "OK"

        return parsed


def evaluate_candidate(
    packet_path: Path,
    candidate_id: Optional[str] = None,
    mode: str = "fast",
    model_override: Optional[str] = None,
    agy_exe: str = "agy",
) -> Dict[str, Any]:
    packet_dir = packet_path.resolve()
    if not packet_dir.is_dir():
        raise FileNotFoundError(f"Packet directory not found: {packet_dir}")

    cid = candidate_id or packet_dir.name
    manifest_file = packet_dir / "REVIEW_PACKET_MANIFEST.json"
    if manifest_file.is_file():
        try:
            with open(manifest_file, "r", encoding="utf-8") as f:
                m = json.load(f)
                cid = m.get("neutral_id") or m.get("candidate_id") or cid
        except Exception:
            pass

    reviewers_to_run: List[Tuple[str, str]] = []
    if model_override:
        reviewers_to_run.append(("Reviewer_Custom", model_override))
    elif mode == "fast":
        reviewers_to_run.append(("Reviewer_Sonnet", "claude-sonnet-4-6"))
    elif mode == "confirm":
        reviewers_to_run.append(("Reviewer_Sonnet", "claude-sonnet-4-6"))
        reviewers_to_run.append(("Reviewer_Gemini", "gemini-3.7-flash-high"))
    else:
        raise ValueError(f"Unknown mode: {mode}")

    results: Dict[str, Any] = {
        "mode": "DEV_ADVISORY",
        "formal_evidence": False,
        "absolute_score_untrusted": True,
        "gate_pass_prohibited": True,
        "evaluation_mode": mode,
        "candidate_id": cid,
        "packet_path": str(packet_dir),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "reviews": {},
    }

    scores: List[float] = []
    dim_matrix: Dict[str, List[int]] = {k: [] for k in OFFICIAL_WEIGHTS.keys()}

    for rev_id, model in reviewers_to_run:
        rev_res = run_single_model_review(packet_dir, cid, rev_id, model, agy_exe=agy_exe)
        results["reviews"][rev_id] = rev_res
        if rev_res.get("status") == "OK":
            sc = rev_res.get("total_weighted_score", 0.0)
            scores.append(sc)
            for d_id, val in rev_res.get("dimension_scores", {}).items():
                if d_id in dim_matrix:
                    dim_matrix[d_id].append(val)

    if scores:
        results["consensus"] = {
            "mean_score": round(sum(scores) / len(scores), 2),
            "median_score": round(sorted(scores)[len(scores) // 2], 2),
            "score_spread": round(max(scores) - min(scores), 2) if len(scores) > 1 else 0.0,
            "dimension_majority": {
                k: (round(sum(v) / len(v), 2) if v else 0) for k, v in dim_matrix.items()
            },
        }
    else:
        results["consensus"] = None

    return results


def run_pairwise_comparison(
    target_result: Dict[str, Any],
    baseline_result: Dict[str, Any],
) -> Dict[str, Any]:
    target_cid = target_result.get("candidate_id", "Target")
    baseline_cid = baseline_result.get("candidate_id", "Baseline")

    target_cons = target_result.get("consensus") or {}
    baseline_cons = baseline_result.get("consensus") or {}

    t_mean = target_cons.get("mean_score", 0.0)
    b_mean = baseline_cons.get("mean_score", 0.0)
    delta = round(t_mean - b_mean, 2)

    dim_deltas: Dict[str, float] = {}
    t_dims = target_cons.get("dimension_majority", {})
    b_dims = baseline_cons.get("dimension_majority", {})

    for k in OFFICIAL_WEIGHTS.keys():
        t_v = t_dims.get(k, 0.0)
        b_v = b_dims.get(k, 0.0)
        dim_deltas[k] = round(t_v - b_v, 2)

    if delta > 1.0:
        pref = f"{target_cid} PREFERRED (+{delta} pt)"
    elif delta < -1.0:
        pref = f"{baseline_cid} PREFERRED ({delta} pt)"
    else:
        pref = f"TIE / INCONCLUSIVE ({delta} pt delta within noise margin)"

    return {
        "target_candidate": target_cid,
        "baseline_candidate": baseline_cid,
        "target_mean_score": t_mean,
        "baseline_mean_score": b_mean,
        "score_delta": delta,
        "dimension_deltas": dim_deltas,
        "pairwise_preference": pref,
        "disclaimer": "DEV_ADVISORY ONLY. Relative pairwise estimate; not formal jury evidence.",
    }


def print_human_report(eval_res: Dict[str, Any], comparison: Optional[Dict[str, Any]] = None) -> None:
    cid = eval_res.get("candidate_id", "Unknown")
    mode = eval_res.get("evaluation_mode", "fast")
    cons = eval_res.get("consensus") or {}

    print("\n" + "=" * 70)
    print(f" JZ QuickScore Advisory Report — Candidate: {cid}")
    print("=" * 70)
    print(f"MODE:                     DEV_ADVISORY (FORMAL_EVIDENCE=false)")
    print(f"ABSOLUTE_SCORE_UNTRUSTED: true")
    print(f"EVALUATION_TIER:          {mode.upper()}")
    print(f"TIMESTAMP:                {eval_res.get('timestamp')}")
    print("-" * 70)

    reviews = eval_res.get("reviews", {})
    for rev_id, rdata in reviews.items():
        st = rdata.get("status")
        if st == "OK":
            model = rdata.get("model")
            sc = rdata.get("total_weighted_score")
            print(f"[{rev_id}] {model}: Total = {sc:.2f} / 100")
            print("  Dimensions (0..5):")
            for dim_id, s in rdata.get("dimension_scores", {}).items():
                print(f"    - {dim_id:<28} : {s}  (Weight: {OFFICIAL_WEIGHTS.get(dim_id, 0)})")
        else:
            print(f"[{rev_id}] ERROR: {rdata.get('error')}")

    print("-" * 70)
    if cons:
        print(f"CONSENSUS (Advisory): Mean = {cons.get('mean_score'):.2f}, Median = {cons.get('median_score'):.2f}, Spread = {cons.get('score_spread'):.2f} pt")

    if comparison:
        print("-" * 70)
        print("PAIRWISE COMPARISON:")
        print(f"  Target:   {comparison.get('target_candidate')} ({comparison.get('target_mean_score'):.2f})")
        print(f"  Baseline: {comparison.get('baseline_candidate')} ({comparison.get('baseline_mean_score'):.2f})")
        print(f"  Delta:    {comparison.get('score_delta'):+0.2f} pt")
        print(f"  Outcome:  {comparison.get('pairwise_preference')}")
        print("  Dimensional Delta:")
        for dim_id, d in comparison.get("dimension_deltas", {}).items():
            print(f"    - {dim_id:<28} : {d:+0.2f}")

    print("=" * 70)
    print("SAFETY NOTICE: QuickScore output is strictly developmental advisory.")
    print("It may NOT be used to set Gates C1, C2, C3, C4 to PASS.")
    print("=" * 70 + "\n")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="JZ QuickScore — Fast Local Development Advisory Scorer"
    )
    parser.add_argument("packet", type=Path, help="Path to evaluation packet directory")
    parser.add_argument(
        "--mode",
        choices=["fast", "confirm"],
        default="fast",
        help="Scoring mode: fast (Sonnet only) or confirm (Sonnet + Gemini)",
    )
    parser.add_argument("--model", type=str, default=None, help="Override reviewer model")
    parser.add_argument("--candidate-id", type=str, default=None, help="Candidate ID override")
    parser.add_argument(
        "--compare-with",
        type=Path,
        default=None,
        help="Path to baseline packet directory for pairwise comparison",
    )
    parser.add_argument(
        "--out-json",
        type=Path,
        default=None,
        help="Path to save machine-readable JSON results",
    )
    parser.add_argument(
        "--agy-exe",
        type=str,
        default="agy",
        help="Path or command name for AGY CLI executable",
    )

    args = parser.parse_args()

    eval_result = evaluate_candidate(
        packet_path=args.packet,
        candidate_id=args.candidate_id,
        mode=args.mode,
        model_override=args.model,
        agy_exe=args.agy_exe,
    )

    comparison_result = None
    if args.compare_with:
        base_result = evaluate_candidate(
            packet_path=args.compare_with,
            mode=args.mode,
            model_override=args.model,
            agy_exe=args.agy_exe,
        )
        comparison_result = run_pairwise_comparison(eval_result, base_result)
        eval_result["pairwise_comparison"] = comparison_result

    print_human_report(eval_result, comparison_result)

    if args.out_json:
        args.out_json.parent.mkdir(parents=True, exist_ok=True)
        with open(args.out_json, "w", encoding="utf-8") as f:
            json.dump(eval_result, f, indent=2, ensure_ascii=False)
        print(f"Machine-readable output saved to: {args.out_json}")


if __name__ == "__main__":
    main()

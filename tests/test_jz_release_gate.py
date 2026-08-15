from __future__ import annotations

import unittest
from unittest.mock import patch

from tools.jz_release_gate.github_backend import observe_live
from tools.jz_release_gate.model import DriftClass, GateState, ReleaseGateInput, ReleaseSnapshot, ScoreDisposition
from tools.jz_release_gate.policy import classify_path, evaluate_release_gate, score_disposition


INPUTS = ReleaseGateInput(
    official_repo="open-city-ai/haidian",
    successor_pr=2774,
    expected_v04_head="ac2a41c7",
    baseline_pr=2744,
    expected_baseline_head="1d5cb1aa",
    protected_baseline_score=77,
    submission_directory="submissions/JerrySkywalker/jingzhang-in-place",
)


def snapshot(*, draft=True, guard=False, baseline_score=77, head="ac2a41c7", paths=None) -> ReleaseSnapshot:
    return ReleaseSnapshot.from_dict({
        "successor": {"exists": True, "state": "OPEN", "is_draft": draft, "head_sha": head, "changed_paths": paths or ["submissions/JerrySkywalker/jingzhang-in-place/proposal.md"]},
        "baseline": {"exists": True, "merged": True, "review_head_sha": "1d5cb1aa", "trusted_score": baseline_score},
        "policy": {"observed": True, "draft_validation_skipped": True, "auto_review_threshold": 60, "high_water_guard_active": guard, "guard_submission_directory": INPUTS.submission_directory if guard else None, "guard_historical_score": 77 if guard else None, "changed_paths": []},
    })


class ReleaseGateTests(unittest.TestCase):
    def test_case_a_draft_guard_absent_is_safe_wait(self):
        decision = evaluate_release_gate(INPUTS, snapshot(draft=True, guard=False))
        self.assertEqual(GateState.SAFE_WAIT, decision.current_state)
        self.assertFalse(decision.safe_to_mark_ready)

    def test_case_b_ready_guard_absent_is_blocked(self):
        self.assertEqual(GateState.BLOCKED_SCORE_GUARD_ABSENT, evaluate_release_gate(INPUTS, snapshot(draft=False)).current_state)

    def test_case_c_guard_and_history_is_ready_for_trusted_rescore(self):
        decision = evaluate_release_gate(INPUTS, snapshot(draft=False, guard=True))
        self.assertEqual(GateState.READY_FOR_TRUSTED_RESCORE, decision.current_state)
        self.assertTrue(decision.historical_best_proven)

    def test_case_d_ambiguous_history_is_blocked(self):
        self.assertEqual(GateState.BLOCKED_BASELINE_UNVERIFIED, evaluate_release_gate(INPUTS, snapshot(draft=False, guard=True, baseline_score=76)).current_state)

    def test_case_e_head_mismatch_is_blocked(self):
        self.assertEqual(GateState.BLOCKED_HEAD_MISMATCH, evaluate_release_gate(INPUTS, snapshot(head="wrong")).current_state)

    def test_case_f_outside_scope_is_blocked(self):
        self.assertEqual(GateState.BLOCKED_SCOPE, evaluate_release_gate(INPUTS, snapshot(paths=["README.md"])).current_state)

    def test_cases_g_h_i_high_water_contract(self):
        self.assertEqual(ScoreDisposition.HOLD, score_disposition(76, 77))
        self.assertEqual(ScoreDisposition.ELIGIBLE, score_disposition(77, 77))
        self.assertEqual(ScoreDisposition.ELIGIBLE, score_disposition(85, 77))

    def test_drift_classifier_is_independently_testable(self):
        self.assertEqual(DriftClass.PEER_SUBMISSIONS_ONLY, classify_path("submissions/Alice/x/proposal.md"))
        self.assertEqual(DriftClass.PARTICIPANT_TOOLING, classify_path("scripts/self_check_submission.py"))
        self.assertEqual(DriftClass.VALIDATION_CONTRACT, classify_path("scripts/github_pr_validation.py"))
        self.assertEqual(DriftClass.MANIFEST_SCHEMA, classify_path("brief/site-package/schemas/manifest.json"))
        self.assertEqual(DriftClass.REVIEW_POLICY, classify_path("scripts/auto_review_queue.py"))
        self.assertEqual(DriftClass.OFFICIAL_DATA, classify_path("data/source_registry.json"))
        self.assertEqual(DriftClass.UNKNOWN, classify_path("unclassified.txt"))

    def test_live_backend_is_mockable_and_uses_read_only_queries(self):
        calls = []

        def fake_gh(args):
            calls.append(args)
            if args[:3] == ["pr", "view", "2774"]:
                return '{"state":"OPEN","isDraft":true,"headRefOid":"ac2a41c7","files":[{"path":"submissions/JerrySkywalker/jingzhang-in-place/proposal.md"}]}'
            if args[:3] == ["pr", "view", "2744"]:
                return '{"state":"MERGED","mergedAt":"now","reviews":[{"body":"Review Agent score 77/100","commit":{"oid":"1d5cb1aa"}}]}'
            if "submission-validation.yml" in args[-1]:
                return "if: github.event.pull_request.draft == false"
            if "auto_review_queue.py" in args[-1]:
                return "parser.add_argument('--threshold', type=float, default=60.0)"
            return '{"sha":"main-sha"}'

        with patch("tools.jz_release_gate.github_backend._run_gh", side_effect=fake_gh):
            observed = observe_live(INPUTS)
        self.assertEqual("LIVE_GITHUB_READ_ONLY", observed.freshness)
        self.assertTrue(observed.successor.is_draft)
        self.assertEqual(77, observed.baseline.trusted_score)
        self.assertTrue(all(call[0] in {"pr", "api"} for call in calls))

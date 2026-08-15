"""Pure fail-closed policy for the Jing-Zhang release gate."""
from __future__ import annotations

from .model import DriftClass, GateState, ReleaseGateInput, ReleaseSnapshot, SafetyDecision, ScoreDisposition


def classify_path(path: str) -> DriftClass:
    """Classify one upstream path; precise contracts win before broad folders."""
    normalized = path.replace("\\", "/").lstrip("/")
    if normalized.startswith("submissions/"):
        return DriftClass.PEER_SUBMISSIONS_ONLY
    if normalized.startswith("brief/site-package/schemas/"):
        return DriftClass.MANIFEST_SCHEMA
    if normalized in {"scripts/github_pr_validation.py", "scripts/participant_preflight.py"}:
        return DriftClass.VALIDATION_CONTRACT
    if normalized in {"scripts/ai_review_submission.py", "scripts/auto_review_queue.py", "scripts/review_submission.py", "scripts/maintainer_review.py"}:
        return DriftClass.REVIEW_POLICY
    if normalized.startswith("data/") or normalized.startswith("brief/site-package/geometry/") or normalized.endswith("source_registry.json"):
        return DriftClass.OFFICIAL_DATA
    if (
        normalized.startswith(".github/workflows/")
        or normalized.startswith("skills/")
        or normalized.startswith("brief/site-package/")
        or normalized.startswith("docs/")
        or normalized == "requirements-review.txt"
        or normalized.startswith("scripts/self_check_submission.py")
        or normalized.startswith("scripts/validate")
    ):
        return DriftClass.PARTICIPANT_TOOLING
    return DriftClass.UNKNOWN


def classify_paths(paths: tuple[str, ...] | list[str]) -> DriftClass:
    """Return the single safe class, or UNKNOWN for a mixed/unknown change set."""
    if not paths:
        return DriftClass.PEER_SUBMISSIONS_ONLY
    classes = {classify_path(path) for path in paths}
    return next(iter(classes)) if len(classes) == 1 else DriftClass.UNKNOWN


def score_disposition(candidate_score: float, historical_best: float) -> ScoreDisposition:
    """The high-water contract: lower scores HOLD; equal/higher may continue."""
    return ScoreDisposition.HOLD if candidate_score < historical_best else ScoreDisposition.ELIGIBLE


def _baseline_proven(inputs: ReleaseGateInput, snapshot: ReleaseSnapshot) -> bool:
    baseline = snapshot.baseline
    return bool(
        baseline.exists
        and baseline.merged
        and baseline.review_head_sha == inputs.expected_baseline_head
        and baseline.trusted_score == inputs.protected_baseline_score
    )


def _guard_proven(inputs: ReleaseGateInput, snapshot: ReleaseSnapshot) -> bool:
    policy = snapshot.policy
    return bool(
        policy.high_water_guard_active
        and policy.guard_submission_directory == inputs.submission_directory
        and policy.guard_historical_score == inputs.protected_baseline_score
    )


def _scope_ok(inputs: ReleaseGateInput, snapshot: ReleaseSnapshot) -> bool:
    prefix = inputs.submission_directory.rstrip("/") + "/"
    paths = snapshot.successor.changed_paths
    return bool(paths) and all(path.replace("\\", "/").startswith(prefix) for path in paths)


def evaluate_release_gate(inputs: ReleaseGateInput, snapshot: ReleaseSnapshot) -> SafetyDecision:
    """Evaluate all known observations without mutating a PR or GitHub state."""
    evidence: list[str] = [f"freshness={snapshot.freshness}"]
    blockers: list[str] = []
    drift = classify_paths(snapshot.policy.changed_paths)
    baseline_proven = _baseline_proven(inputs, snapshot)
    guard_proven = _guard_proven(inputs, snapshot)
    successor = snapshot.successor

    if successor.exists is not True or successor.state is None or successor.is_draft is None or successor.head_sha is None:
        return SafetyDecision(GateState.UNKNOWN_EXTERNAL_STATE, False, inputs.protected_baseline_score, baseline_proven, guard_proven, drift, ("successor PR observation incomplete",), tuple(evidence), snapshot.freshness)
    if successor.head_sha != inputs.expected_v04_head:
        return SafetyDecision(GateState.BLOCKED_HEAD_MISMATCH, False, inputs.protected_baseline_score, baseline_proven, guard_proven, drift, ("successor PR head does not equal the certified v0.4 head",), tuple(evidence), snapshot.freshness)
    if not _scope_ok(inputs, snapshot):
        return SafetyDecision(GateState.BLOCKED_SCOPE, False, inputs.protected_baseline_score, baseline_proven, guard_proven, drift, ("successor PR changes outside the declared submission directory",), tuple(evidence), snapshot.freshness)
    if drift is not DriftClass.PEER_SUBMISSIONS_ONLY:
        return SafetyDecision(GateState.BLOCKED_TOOLING_DRIFT, False, inputs.protected_baseline_score, baseline_proven, guard_proven, drift, (f"current policy drift is {drift.value}",), tuple(evidence), snapshot.freshness)
    if not baseline_proven:
        return SafetyDecision(GateState.BLOCKED_BASELINE_UNVERIFIED, False, inputs.protected_baseline_score, False, guard_proven, drift, ("merged trusted exact-head score baseline is not proven",), tuple(evidence), snapshot.freshness)
    if successor.is_draft:
        safe = guard_proven
        blockers = [] if safe else ["active high-water guard for this directory and score is absent"]
        return SafetyDecision(GateState.SAFE_WAIT, safe, inputs.protected_baseline_score, True, guard_proven, drift, tuple(blockers), tuple(evidence), snapshot.freshness)
    if not guard_proven:
        return SafetyDecision(GateState.BLOCKED_SCORE_GUARD_ABSENT, False, inputs.protected_baseline_score, True, False, drift, ("non-draft intake could accept the absolute 60 threshold below historical best 77",), tuple(evidence), snapshot.freshness)
    if inputs.require_draft:
        return SafetyDecision(GateState.BLOCKED_PR_NOT_DRAFT, False, inputs.protected_baseline_score, True, True, drift, ("this invocation requires a Draft PR",), tuple(evidence), snapshot.freshness)
    return SafetyDecision(GateState.READY_FOR_TRUSTED_RESCORE, False, inputs.protected_baseline_score, True, True, drift, (), tuple(evidence), snapshot.freshness)

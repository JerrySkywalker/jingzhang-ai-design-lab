"""Data model for the participant-side release-safety gate.

The model deliberately contains observations, never GitHub mutation commands.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass, field
from enum import Enum
from typing import Any


class GateState(str, Enum):
    SAFE_WAIT = "SAFE_WAIT"
    READY_FOR_TRUSTED_RESCORE = "READY_FOR_TRUSTED_RESCORE"
    BLOCKED_HEAD_MISMATCH = "BLOCKED_HEAD_MISMATCH"
    BLOCKED_SCOPE = "BLOCKED_SCOPE"
    BLOCKED_TOOLING_DRIFT = "BLOCKED_TOOLING_DRIFT"
    BLOCKED_SCORE_GUARD_ABSENT = "BLOCKED_SCORE_GUARD_ABSENT"
    BLOCKED_BASELINE_UNVERIFIED = "BLOCKED_BASELINE_UNVERIFIED"
    BLOCKED_PR_NOT_DRAFT = "BLOCKED_PR_NOT_DRAFT"
    UNKNOWN_EXTERNAL_STATE = "UNKNOWN_EXTERNAL_STATE"


class DriftClass(str, Enum):
    PEER_SUBMISSIONS_ONLY = "PEER_SUBMISSIONS_ONLY"
    PARTICIPANT_TOOLING = "PARTICIPANT_TOOLING"
    VALIDATION_CONTRACT = "VALIDATION_CONTRACT"
    MANIFEST_SCHEMA = "MANIFEST_SCHEMA"
    REVIEW_POLICY = "REVIEW_POLICY"
    OFFICIAL_DATA = "OFFICIAL_DATA"
    UNKNOWN = "UNKNOWN"


class ScoreDisposition(str, Enum):
    HOLD = "HOLD"
    ELIGIBLE = "ELIGIBLE"


@dataclass(frozen=True)
class ReleaseGateInput:
    official_repo: str
    successor_pr: int
    expected_v04_head: str
    baseline_pr: int
    expected_baseline_head: str
    protected_baseline_score: float
    submission_directory: str
    require_draft: bool = False

    @classmethod
    def from_dict(cls, raw: dict[str, Any]) -> "ReleaseGateInput":
        return cls(
            official_repo=str(raw["official_repo"]),
            successor_pr=int(raw["successor_pr"]),
            expected_v04_head=str(raw["expected_v04_head"]),
            baseline_pr=int(raw["baseline_pr"]),
            expected_baseline_head=str(raw["expected_baseline_head"]),
            protected_baseline_score=float(raw["protected_baseline_score"]),
            submission_directory=str(raw["submission_directory"]).strip("/"),
            require_draft=bool(raw.get("require_draft", False)),
        )


@dataclass(frozen=True)
class PullRequestSnapshot:
    exists: bool | None = None
    state: str | None = None
    is_draft: bool | None = None
    head_sha: str | None = None
    changed_paths: tuple[str, ...] = ()

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "PullRequestSnapshot":
        raw = raw or {}
        return cls(
            exists=raw.get("exists"),
            state=raw.get("state"),
            is_draft=raw.get("is_draft", raw.get("isDraft")),
            head_sha=raw.get("head_sha", raw.get("headRefOid")),
            changed_paths=tuple(str(item) for item in raw.get("changed_paths", raw.get("files", []))),
        )


@dataclass(frozen=True)
class BaselineSnapshot:
    exists: bool | None = None
    merged: bool | None = None
    review_head_sha: str | None = None
    trusted_score: float | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "BaselineSnapshot":
        raw = raw or {}
        score = raw.get("trusted_score")
        return cls(
            exists=raw.get("exists"),
            merged=raw.get("merged"),
            review_head_sha=raw.get("review_head_sha"),
            trusted_score=float(score) if isinstance(score, (int, float)) else None,
        )


@dataclass(frozen=True)
class PolicySnapshot:
    observed: bool = False
    draft_validation_skipped: bool | None = None
    auto_review_threshold: float | None = None
    high_water_guard_active: bool | None = None
    guard_submission_directory: str | None = None
    guard_historical_score: float | None = None
    changed_paths: tuple[str, ...] = ()
    current_main_sha: str | None = None

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "PolicySnapshot":
        raw = raw or {}
        score = raw.get("guard_historical_score")
        threshold = raw.get("auto_review_threshold")
        return cls(
            observed=bool(raw.get("observed", False)),
            draft_validation_skipped=raw.get("draft_validation_skipped"),
            auto_review_threshold=float(threshold) if isinstance(threshold, (int, float)) else None,
            high_water_guard_active=raw.get("high_water_guard_active"),
            guard_submission_directory=raw.get("guard_submission_directory"),
            guard_historical_score=float(score) if isinstance(score, (int, float)) else None,
            changed_paths=tuple(str(item) for item in raw.get("changed_paths", ())),
            current_main_sha=raw.get("current_main_sha"),
        )


@dataclass(frozen=True)
class ReleaseSnapshot:
    successor: PullRequestSnapshot = field(default_factory=PullRequestSnapshot)
    baseline: BaselineSnapshot = field(default_factory=BaselineSnapshot)
    policy: PolicySnapshot = field(default_factory=PolicySnapshot)
    freshness: str = "OFFLINE_FIXTURE"

    @classmethod
    def from_dict(cls, raw: dict[str, Any] | None) -> "ReleaseSnapshot":
        raw = raw or {}
        return cls(
            successor=PullRequestSnapshot.from_dict(raw.get("successor")),
            baseline=BaselineSnapshot.from_dict(raw.get("baseline")),
            policy=PolicySnapshot.from_dict(raw.get("policy")),
            freshness=str(raw.get("freshness", "OFFLINE_FIXTURE")),
        )


@dataclass(frozen=True)
class SafetyDecision:
    current_state: GateState
    safe_to_mark_ready: bool
    historical_best: float
    historical_best_proven: bool
    score_guard_active: bool
    tooling_drift_class: DriftClass
    blockers: tuple[str, ...]
    evidence: tuple[str, ...]
    freshness: str

    def to_dict(self) -> dict[str, Any]:
        result = asdict(self)
        result["current_state"] = self.current_state.value
        result["tooling_drift_class"] = self.tooling_drift_class.value
        return result

"""Bounded read-only ``gh`` adapter used only when an operator asks for --live."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
from typing import Any

from .model import ReleaseGateInput, ReleaseSnapshot


class ReadOnlyBackendError(RuntimeError):
    pass


def _run_gh(args: list[str]) -> str:
    if shutil.which("gh") is None:
        raise ReadOnlyBackendError("gh is unavailable")
    completed = subprocess.run(
        ["gh", *args],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    if completed.returncode:
        raise ReadOnlyBackendError(completed.stderr.strip() or "gh read command failed")
    return completed.stdout


def _gh_json(args: list[str]) -> dict[str, Any]:
    value = json.loads(_run_gh(args))
    if not isinstance(value, dict):
        raise ReadOnlyBackendError("expected GitHub JSON object")
    return value


def _raw(repo: str, path: str) -> str:
    return _run_gh(["api", "-H", "Accept: application/vnd.github.raw+json", f"repos/{repo}/contents/{path}?ref=main"])


def observe_live(inputs: ReleaseGateInput) -> ReleaseSnapshot:
    """Gather public GitHub facts using GET-only gh commands.  No mutation verbs exist here."""
    successor = _gh_json(["pr", "view", str(inputs.successor_pr), "--repo", inputs.official_repo, "--json", "state,isDraft,headRefOid,files"])
    baseline = _gh_json(["pr", "view", str(inputs.baseline_pr), "--repo", inputs.official_repo, "--json", "state,mergedAt,reviews"])
    review_head: str | None = None
    trusted_score: float | None = None
    for review in baseline.get("reviews", []):
        body = str(review.get("body", ""))
        commit = review.get("commit") or {}
        match = re.search(r"Review Agent score\s+(\d+(?:\.\d+)?)/100", body)
        if match and commit.get("oid") == inputs.expected_baseline_head:
            review_head = str(commit["oid"])
            trusted_score = float(match.group(1))
            break
    workflow = _raw(inputs.official_repo, ".github/workflows/submission-validation.yml")
    queue = _raw(inputs.official_repo, "scripts/auto_review_queue.py")
    main = _gh_json(["api", f"repos/{inputs.official_repo}/commits/main"])
    lower_queue = queue.casefold()
    marker = any(token in lower_queue for token in ("historical_best", "high_water", "high-water", "score_guard"))
    return ReleaseSnapshot.from_dict({
        "freshness": "LIVE_GITHUB_READ_ONLY",
        "successor": {
            "exists": True,
            "state": successor.get("state"),
            "is_draft": successor.get("isDraft"),
            "head_sha": successor.get("headRefOid"),
            "changed_paths": [entry.get("path", "") for entry in successor.get("files", [])],
        },
        "baseline": {
            "exists": True,
            "merged": baseline.get("state") == "MERGED" or bool(baseline.get("mergedAt")),
            "review_head_sha": review_head,
            "trusted_score": trusted_score,
        },
        "policy": {
            "observed": True,
            "draft_validation_skipped": "draft == false" in workflow,
            "auto_review_threshold": 60.0 if "default=60.0" in queue else None,
            "high_water_guard_active": marker,
            "changed_paths": [],
            "current_main_sha": main.get("sha"),
        },
    })

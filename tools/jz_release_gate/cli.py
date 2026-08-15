"""CLI for the read-only Jing-Zhang release-safety gate."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from .github_backend import ReadOnlyBackendError, observe_live
from .model import ReleaseGateInput, ReleaseSnapshot
from .policy import evaluate_release_gate


def _read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"{path} must contain a JSON object")
    return value


def main() -> int:
    parser = argparse.ArgumentParser(description="Read-only Jing-Zhang release-safety gate")
    parser.add_argument("--config", required=True, type=Path, help="JSON config containing inputs and optional snapshot")
    parser.add_argument("--fixture", type=Path, help="optional offline snapshot JSON; overrides config snapshot")
    parser.add_argument("--live", action="store_true", help="refresh public GitHub observations through GET-only gh commands")
    parser.add_argument("--json-out", type=Path)
    args = parser.parse_args()
    config = _read_json(args.config)
    inputs = ReleaseGateInput.from_dict(config.get("inputs", config))
    try:
        snapshot = observe_live(inputs) if args.live else ReleaseSnapshot.from_dict(_read_json(args.fixture) if args.fixture else config.get("snapshot"))
    except ReadOnlyBackendError as exc:
        snapshot = ReleaseSnapshot.from_dict({"freshness": f"LIVE_READ_FAILED:{exc}"})
    decision = evaluate_release_gate(inputs, snapshot)
    result = decision.to_dict()
    result.update({
        "CURRENT_STATE": decision.current_state.value,
        "SAFE_TO_MARK_READY": decision.safe_to_mark_ready,
        "HISTORICAL_BEST": decision.historical_best,
        "HISTORICAL_BEST_PROVEN": decision.historical_best_proven,
        "SCORE_GUARD_ACTIVE": decision.score_guard_active,
        "TOOLING_DRIFT_CLASS": decision.tooling_drift_class.value,
        "BLOCKERS": list(decision.blockers),
    })
    text = json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(text + "\n", encoding="utf-8")
    print(text)
    return 0 if decision.current_state.value in {"SAFE_WAIT", "READY_FOR_TRUSTED_RESCORE"} else 2


if __name__ == "__main__":
    raise SystemExit(main())

"""Content hashes, visible-surface tests, and semantic-regression comparison."""
from __future__ import annotations

from dataclasses import dataclass
import json
from typing import Any

from .first_window import FirstWindowReport, first_window_report
from .invariants import InvariantReport, bilingual_parity, semantic_invariants
from .snapshot import PackageSnapshot


CORE_FIGURES = [
    f"assets/figures/{name}{suffix}.png"
    for name in ("site-overview", "land-use-structure", "key-areas", "mobility-bluegreen", "metrics-evidence")
    for suffix in ("", ".en")
]


@dataclass(frozen=True)
class CompareResult:
    added: tuple[str, ...]
    removed: tuple[str, ...]
    modified: tuple[str, ...]
    text_delta_bytes: int
    core_figure_hashes: dict[str, dict[str, str | None]]
    structured_evidence_delta: dict[str, str]
    baseline_invariants: InvariantReport
    candidate_invariants: InvariantReport
    baseline_bilingual: InvariantReport
    candidate_bilingual: InvariantReport
    baseline_first_window: FirstWindowReport
    candidate_first_window: FirstWindowReport
    semantic_regressions: tuple[str, ...]

    @property
    def ok(self) -> bool:
        return not self.semantic_regressions

    def to_dict(self) -> dict[str, Any]:
        return {
            "ok": self.ok,
            "file_delta": {"added": list(self.added), "removed": list(self.removed), "modified": list(self.modified), "text_delta_bytes": self.text_delta_bytes},
            "core_figure_hashes": self.core_figure_hashes,
            "structured_evidence_delta": self.structured_evidence_delta,
            "baseline_semantic_invariants": self.baseline_invariants.to_dict(),
            "candidate_semantic_invariants": self.candidate_invariants.to_dict(),
            "baseline_bilingual": self.baseline_bilingual.to_dict(),
            "candidate_bilingual": self.candidate_bilingual.to_dict(),
            "baseline_first_window": self.baseline_first_window.to_dict(),
            "candidate_first_window": self.candidate_first_window.to_dict(),
            "semantic_regressions": list(self.semantic_regressions),
        }


def compare_packages(baseline: PackageSnapshot, candidate: PackageSnapshot) -> CompareResult:
    base_paths, candidate_paths = set(baseline.files), set(candidate.files)
    added, removed = tuple(sorted(candidate_paths - base_paths)), tuple(sorted(base_paths - candidate_paths))
    common = base_paths & candidate_paths
    modified = tuple(sorted(path for path in common if baseline.files[path].sha256 != candidate.files[path].sha256))
    text_delta = sum(candidate.files[path].size for path in added if candidate.files[path].text is not None) - sum(baseline.files[path].size for path in removed if baseline.files[path].text is not None)
    text_delta += sum((candidate.files[path].size - baseline.files[path].size) for path in modified if candidate.files[path].text is not None)
    figure_hashes = {path: {"baseline": baseline.files.get(path).sha256 if path in baseline.files else None, "candidate": candidate.files.get(path).sha256 if path in candidate.files else None} for path in CORE_FIGURES}
    structured = {
        path: f"{baseline.files.get(path).sha256 if path in baseline.files else 'MISSING'} -> {candidate.files.get(path).sha256 if path in candidate.files else 'MISSING'}"
        for path in sorted(path for path in base_paths | candidate_paths if path.endswith((".json", ".geojson")))
        if (path not in common or baseline.files[path].sha256 != candidate.files[path].sha256)
    }
    base_invariants, candidate_invariants = semantic_invariants(baseline), semantic_invariants(candidate)
    base_bilingual, candidate_bilingual = bilingual_parity(baseline), bilingual_parity(candidate)
    base_window, candidate_window = first_window_report(baseline), first_window_report(candidate)
    regressions = [key for key, passed in base_invariants.checks.items() if passed and not candidate_invariants.checks.get(key, False)]
    regressions.extend(key for key, passed in candidate_invariants.checks.items() if not passed)
    regressions.extend(key for key, passed in candidate_bilingual.checks.items() if not passed)
    return CompareResult(added, removed, modified, text_delta, figure_hashes, structured, base_invariants, candidate_invariants, base_bilingual, candidate_bilingual, base_window, candidate_window, tuple(sorted(set(regressions))))


def render_markdown(result: CompareResult) -> str:
    data = result.to_dict()
    lines = ["# Review-packet regression comparison", "", f"RESULT={'PASS' if result.ok else 'SEMANTIC_REGRESSION'}", "", "## File delta", f"- Added: {len(result.added)}", f"- Removed: {len(result.removed)}", f"- Modified: {len(result.modified)}", f"- Text-byte delta: {result.text_delta_bytes}", "", "## Semantic invariants", f"- Baseline: {'PASS' if result.baseline_invariants.ok else 'DIAGNOSTIC_GAPS'}", f"- Candidate: {'PASS' if result.candidate_invariants.ok else 'FAIL'}", f"- Bilingual candidate: {'PASS' if result.candidate_bilingual.ok else 'FAIL'}", "", "## First-window packets", f"- Baseline inventory: {'PASS' if all(result.baseline_first_window.inventory.values()) else 'FAIL'}", f"- Candidate inventory: {'PASS' if all(result.candidate_first_window.inventory.values()) else 'FAIL'}", "", "## Stop-ship regressions"]
    lines.extend([f"- {item}" for item in result.semantic_regressions] or ["- none"])
    lines.extend(["", "## Machine summary", "```json", json.dumps(data["structured_evidence_delta"], ensure_ascii=False, indent=2), "```", ""])
    return "\n".join(lines)

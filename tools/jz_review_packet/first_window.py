"""Checks the actual first-window surface family selected by Review Agent tooling."""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any

from .snapshot import PackageSnapshot


OFFICIAL_PACKET_SURFACES = {
    "figures": [
        "assets/figures/site-overview.png",
        "assets/figures/land-use-structure.png",
        "assets/figures/key-areas.png",
        "assets/figures/mobility-bluegreen.png",
        "assets/figures/metrics-evidence.png",
    ],
    "pdfs": ["drawings/a3-booklet.pdf", "drawings/a0-boards.pdf"],
    "html": ["report/proposal.html", "visual/index.html"],
}

TERM_PATTERNS = {
    "STATUS_ACTION": r"STATUS\s*[×xX]\s*ACTION|状态\s*[—×xX]\s*行动",
    "TWELVE_TO_THREE": r"12\s*(?:→|->|to|到|至)\s*(?:3|three|三)|twelve[- ]to[- ]three",
    "DEEP_TASK_IDS": r"S01.{0,160}S04.{0,160}S07",
    "ORDINARY_SPACE_SUFFICIENCY": r"ordinary[ -]space sufficiency|普通.{0,12}(?:空间|场所).{0,12}(?:充分|足够)",
    "NO_BUILD": r"NO[ -]BUILD|不建设|不新建",
    "THREE_INTERFACES": r"three.{0,24}interfaces|3.{0,24}interfaces|三.{0,24}(?:接口|界面)",
    "HUNDRED_DAY_SIGNAL": r"100[ -]day|d0[_ -]d30.{0,160}d61[_ -]d100|100天",
    "STOP_RESET": r"STOP.{0,120}(?:RESET|reset)|停止.{0,120}(?:重置|恢复)",
}


@dataclass(frozen=True)
class FirstWindowReport:
    inventory: dict[str, bool]
    terms: dict[str, dict[str, bool]]
    artifact_checks: dict[str, bool]

    @property
    def ok(self) -> bool:
        reviewer_visible = ("proposal_zh", "proposal_en", "html_zh", "html_en")
        return all(self.inventory.values()) and all(any(hits[name] for name in reviewer_visible) for hits in self.terms.values()) and all(self.artifact_checks.values())

    def to_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "inventory": self.inventory, "terms": self.terms, "artifact_checks": self.artifact_checks}


def _is_png(record_bytes: bytes) -> bool:
    return len(record_bytes) >= 24 and record_bytes.startswith(b"\x89PNG\r\n\x1a\n") and record_bytes[12:16] == b"IHDR"


def _pdf_has_page(data: bytes) -> bool:
    return data.startswith(b"%PDF-") and b"/Type /Page" in data


def first_window_report(snapshot: PackageSnapshot) -> FirstWindowReport:
    inventory: dict[str, bool] = {}
    for category, primary_paths in OFFICIAL_PACKET_SURFACES.items():
        for primary in primary_paths:
            stem, suffix = primary.rsplit(".", 1)
            english = f"{stem}.en.{suffix}"
            inventory[primary] = primary in snapshot.files
            inventory[english] = english in snapshot.files
    surfaces = {
        "proposal_zh": snapshot.text("proposal.md"),
        "proposal_en": snapshot.text("proposal.en.md"),
        "html_zh": snapshot.text("report/proposal.html") + "\n" + snapshot.text("visual/index.html"),
        "html_en": snapshot.text("report/proposal.en.html") + "\n" + snapshot.text("visual/index.en.html"),
        "structured": snapshot.text("visual/assets/ai-spatial-admission.json"),
    }
    terms = {name: {surface: bool(re.search(pattern, text, flags=re.IGNORECASE | re.DOTALL)) for surface, text in surfaces.items()} for name, pattern in TERM_PATTERNS.items()}
    artifact_checks: dict[str, bool] = {}
    for relative, record in snapshot.files.items():
        if relative.startswith("assets/figures/") and relative.endswith(".png"):
            artifact_checks[f"PNG:{relative}"] = _is_png((snapshot.root / relative).read_bytes()) and record.size > 0
        if relative.startswith("drawings/") and relative.endswith(".pdf"):
            artifact_checks[f"PDF:{relative}"] = _pdf_has_page((snapshot.root / relative).read_bytes()) and record.size > 0
    return FirstWindowReport(inventory, terms, artifact_checks)

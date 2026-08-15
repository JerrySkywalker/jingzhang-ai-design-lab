"""Semantic and bilingual stop-ship checks for successor review packets."""
from __future__ import annotations

from dataclasses import asdict, dataclass
import re
from typing import Any

from .snapshot import PackageSnapshot


@dataclass(frozen=True)
class InvariantReport:
    checks: dict[str, bool]
    evidence: dict[str, str]

    @property
    def ok(self) -> bool:
        return all(self.checks.values())

    def to_dict(self) -> dict[str, Any]:
        return {"ok": self.ok, "checks": self.checks, "evidence": self.evidence}


def _admission(snapshot: PackageSnapshot) -> dict[str, Any]:
    value = snapshot.json("visual/assets/ai-spatial-admission.json")
    return value if isinstance(value, dict) else {}


def semantic_invariants(snapshot: PackageSnapshot) -> InvariantReport:
    admission = _admission(snapshot)
    tasks = admission.get("tasks") if isinstance(admission.get("tasks"), list) else []
    deep_ids = tuple(admission.get("deep_task_ids", ()))
    chain = " | ".join(str(item).casefold() for item in admission.get("admission_chain", ()))
    interfaces = admission.get("interfaces") if isinstance(admission.get("interfaces"), list) else []
    contracts = admission.get("delivery_contracts") if isinstance(admission.get("delivery_contracts"), list) else []
    task_ids = {item.get("task_id") for item in tasks if isinstance(item, dict)}
    deep_tasks = [item for item in tasks if isinstance(item, dict) and item.get("deep_task_packet") is True]
    no_build = [item for item in tasks if isinstance(item, dict) and item.get("no_build") is True]
    framework = str(admission.get("city_framework", "")).casefold()
    required_chain = (
        "ordinary city",
        "ordinary-space sufficiency",
        "special spatial condition",
        "evidence, rights and human authority",
        "minimum reversible spatial delta",
        "ttl, stop and degrade",
        "exit/reset",
        "ordinary city",
    )
    checks = {
        "STATUS_ACTION_PRESENT": "status" in framework and "action" in framework,
        "AI_OFF_CITY": admission.get("ai_off_city") == "PASS",
        "TASK_COUNT": admission.get("task_count") == 12 and len(tasks) == 12 and task_ids == {f"S{number:02d}" for number in range(1, 13)},
        "DEEP_TASK_COUNT": admission.get("deep_task_packet_count") == 3 and len(deep_tasks) == 3,
        "DEEP_TASK_IDS": deep_ids == ("S01", "S04", "S07") and {item.get("task_id") for item in deep_tasks} == {"S01", "S04", "S07"},
        "NO_BUILD_TASK_COUNT": admission.get("no_build_task_count") == 9 and len(no_build) == 9,
        "INTERFACE_COUNT": len(interfaces) == 3,
        "DELIVERY_CONTRACT_COUNT": len(contracts) == 3,
        "PUBLIC_RIGHTS_FLOOR_PRESENT": bool(str(admission.get("public_rights_floor", "")).strip()),
        "ADMISSION_CHAIN": all(needle in chain for needle in required_chain),
    }
    return InvariantReport(checks, {"admission_source": "visual/assets/ai-spatial-admission.json" if admission else "missing"})


def _tokens(text: str) -> set[str]:
    """Canonical task IDs and the three critical numbers across zh/en wording."""
    tokens = set(re.findall(r"S\d{2}", text, flags=re.IGNORECASE))
    aliases = {
        "12": r"\b12\b|十二",
        "3": r"\b3\b|\bthree\b|三",
        "100": r"\b100\b|one[- ]hundred|一百",
    }
    tokens.update(label for label, pattern in aliases.items() if re.search(pattern, text, flags=re.IGNORECASE))
    return tokens


def bilingual_parity(snapshot: PackageSnapshot) -> InvariantReport:
    pairs = (("proposal.md", "proposal.en.md"), ("report/proposal.html", "report/proposal.en.html"), ("visual/index.html", "visual/index.en.html"))
    checks: dict[str, bool] = {}
    evidence: dict[str, str] = {}
    for left, right in pairs:
        name = left.replace("/", "_").replace(".", "_")
        left_text, right_text = snapshot.text(left), snapshot.text(right)
        checks[f"PAIR_{name}"] = bool(left_text and right_text)
        if left_text and right_text:
            checks[f"TOKENS_{name}"] = _tokens(left_text) == _tokens(right_text)
        else:
            checks[f"TOKENS_{name}"] = False
        evidence[name] = f"{len(_tokens(left_text))}:{len(_tokens(right_text))} critical tokens"
    figure_pairs = [
        (f"assets/figures/{name}.png", f"assets/figures/{name}.en.png")
        for name in ("site-overview", "land-use-structure", "key-areas", "mobility-bluegreen", "metrics-evidence")
    ]
    pdf_pairs = (("drawings/a3-booklet.pdf", "drawings/a3-booklet.en.pdf"), ("drawings/a0-boards.pdf", "drawings/a0-boards.en.pdf"))
    checks["FIGURE_PAIRS"] = all(left in snapshot.files and right in snapshot.files for left, right in figure_pairs)
    checks["PDF_PAIRS"] = all(left in snapshot.files and right in snapshot.files for left, right in pdf_pairs)
    return InvariantReport(checks, evidence)

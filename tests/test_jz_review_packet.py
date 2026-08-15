from __future__ import annotations

import json
from pathlib import Path
import tempfile
import unittest

from tools.jz_review_packet.diff import compare_packages
from tools.jz_review_packet.invariants import bilingual_parity, semantic_invariants
from tools.jz_review_packet.snapshot import PackageSnapshot


PNG = b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + b"\x00" * 20
PDF = b"%PDF-1.4\n1 0 obj << /Type /Page >> endobj\n%%EOF"


def write_package(root: Path, *, missing_english_figure=False) -> None:
    root.mkdir(parents=True)
    admission = {
        "city_framework": "STATUS × ACTION",
        "ai_off_city": "PASS",
        "task_count": 12,
        "deep_task_packet_count": 3,
        "deep_task_ids": ["S01", "S04", "S07"],
        "no_build_task_count": 9,
        "admission_chain": ["ordinary city", "ordinary-space sufficiency", "special spatial condition", "evidence, rights and human authority", "minimum reversible spatial delta", "TTL, stop and degrade", "exit/reset", "ordinary city"],
        "public_rights_floor": "ordinary route survives",
        "tasks": [{"task_id": f"S{i:02d}", "deep_task_packet": i in (1, 4, 7), "no_build": i not in (1, 4, 7)} for i in range(1, 13)],
        "interfaces": [{}, {}, {}],
        "delivery_contracts": [{}, {}, {}],
    }
    (root / "visual/assets").mkdir(parents=True)
    (root / "visual/assets/ai-spatial-admission.json").write_text(json.dumps(admission), encoding="utf-8")
    text = "S01 S04 S07 12 3 100 STATUS × ACTION NO BUILD STOP RESET"
    for relative in ("proposal.md", "proposal.en.md", "report/proposal.html", "report/proposal.en.html", "visual/index.html", "visual/index.en.html"):
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    for stem in ("site-overview", "land-use-structure", "key-areas", "mobility-bluegreen", "metrics-evidence"):
        for suffix in ("", ".en"):
            if missing_english_figure and stem == "site-overview" and suffix == ".en":
                continue
            path = root / f"assets/figures/{stem}{suffix}.png"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(PNG)
    for stem in ("a3-booklet", "a0-boards"):
        for suffix in ("", ".en"):
            path = root / f"drawings/{stem}{suffix}.pdf"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(PDF)


class ReviewPacketTests(unittest.TestCase):
    def test_v04_semantic_fixture_passes(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "package"
            write_package(root)
            snapshot = PackageSnapshot.from_path(root)
            self.assertTrue(semantic_invariants(snapshot).ok)
            self.assertTrue(bilingual_parity(snapshot).ok)

    def test_lost_bilingual_figure_is_stop_ship_regression(self):
        with tempfile.TemporaryDirectory() as temp:
            baseline, candidate = Path(temp) / "baseline", Path(temp) / "candidate"
            write_package(baseline)
            write_package(candidate, missing_english_figure=True)
            result = compare_packages(PackageSnapshot.from_path(baseline), PackageSnapshot.from_path(candidate))
            self.assertFalse(result.ok)
            self.assertIn("FIGURE_PAIRS", result.semantic_regressions)

    def test_snapshot_can_find_nested_materialized_package(self):
        with tempfile.TemporaryDirectory() as temp:
            nested = Path(temp) / "submissions/JerrySkywalker/jingzhang-in-place"
            write_package(nested)
            self.assertEqual(nested.resolve(), PackageSnapshot.from_path(temp).root)

#!/usr/bin/env python3
"""Build the neutral, fixed packet used by Windows Sandbox reviewers."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path


CORE = [
    "proposal.md", "proposal.en.md", "manifest.json", "metrics.json", "assumptions.json",
    "sources.json", "self_check.json", "compliance_matrix.json", "standard_matrix.json",
    "design_depth_matrix.json", "agent.json", "simulation.json", "report/copyright_statement.md",
    "report/narrative.md", "visual/assets/ai-spatial-admission.json",
    "visual/assets/design-evidence-index.json", "visual/assets/renewal-project-portfolio.json",
    "visual/assets/status-action-register.json",
]
FIGURES = [
    "assets/figures/site-overview.png", "assets/figures/land-use-structure.png",
    "assets/figures/key-areas.png", "assets/figures/mobility-bluegreen.png",
    "assets/figures/metrics-evidence.png",
]
PDFS = ["drawings/a3-booklet.pdf", "drawings/a0-boards.pdf"]
HTML = ["report/proposal.html", "visual/index.html"]
FORBIDDEN = ("v0.4.1a", "candidate-a", "82 estimate", "77 baseline", "jz-v042-codex-subscription-score-loop-001")


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for part in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(part)
    return hasher.hexdigest()


def counterpart(path: str) -> str:
    value = Path(path)
    return value.with_name(f"{value.stem}.en{value.suffix}").as_posix()


def copy_file(source: Path, packet: Path, relative: str, role: str, records: list[dict]) -> None:
    origin = source / relative
    if not origin.is_file():
        raise SystemExit(f"missing required packet artifact: {relative}")
    target = packet / relative
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origin, target)
    records.append({"relative_path": relative, "size": target.stat().st_size, "sha256": digest(target), "role": role})


def render_pdf(source: Path, target: Path) -> None:
    tool = shutil.which("pdftoppm")
    if not tool:
        raise SystemExit("pdftoppm is required to create deterministic PDF page previews")
    result = subprocess.run([tool, "-png", "-f", "1", "-l", "1", "-singlefile", "-r", "144", str(source), str(target.with_suffix(""))], capture_output=True, text=True, check=False, timeout=60)
    if result.returncode or not target.is_file():
        raise SystemExit("could not rasterize " + source.name)


def browser() -> str:
    for candidate in (
        shutil.which("chrome"), shutil.which("msedge"),
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    ):
        if candidate and Path(candidate).is_file():
            return str(candidate)
    raise SystemExit("headless Chrome or Edge is required to create HTML first-window previews")


def render_html(source: Path, target: Path) -> None:
    result = subprocess.run([browser(), "--headless=new", "--disable-gpu", "--hide-scrollbars", "--window-size=1440,1600", f"--screenshot={target}", source.resolve().as_uri()], capture_output=True, text=True, check=False, timeout=60)
    if result.returncode or not target.is_file():
        raise SystemExit("could not screenshot " + source.name)


def record_generated(packet: Path, relative: str, role: str, records: list[dict]) -> None:
    path = packet / relative
    records.append({"relative_path": relative, "size": path.stat().st_size, "sha256": digest(path), "role": role})


def reject_contamination(packet: Path) -> None:
    for path in packet.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".json", ".html", ".txt"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace").casefold()
        found = [item for item in FORBIDDEN if item in text]
        if found:
            raise SystemExit(f"forbidden host-context marker in {path.relative_to(packet)}: {', '.join(found)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--rubric", required=True, type=Path)
    parser.add_argument("--schema", required=True, type=Path)
    parser.add_argument("--coordinator-receipt", required=True, type=Path)
    parser.add_argument("--source-head", required=True)
    args = parser.parse_args()
    source, packet = args.source.resolve(), args.out.resolve()
    if packet.exists():
        raise SystemExit(f"refusing to overwrite packet: {packet}")
    if not source.is_dir() or not args.rubric.is_file() or not args.schema.is_file():
        raise SystemExit("source, rubric, and schema must exist")
    packet.mkdir(parents=True)
    records: list[dict] = []
    for path in CORE:
        copy_file(source, packet, path, "structured_evidence" if path.endswith(".json") else "narrative_or_rights", records)
    for path in FIGURES:
        for localized in (path, counterpart(path)):
            copy_file(source, packet, localized, "core_figure", records)
    for path in PDFS:
        for localized in (path, counterpart(path)):
            copy_file(source, packet, localized, "drawing_pdf", records)
    for path in HTML:
        for localized in (path, counterpart(path)):
            copy_file(source, packet, localized, "review_visible_html", records)
    for source_path, target_name in ((args.rubric, "CURRENT_OFFICIAL_RUBRIC.md"), (args.schema, "SCORECARD_SCHEMA.json")):
        shutil.copy2(source_path, packet / target_name)
        record_generated(packet, target_name, "review_contract", records)
    (packet / "CANDIDATE_CONTEXT.md").write_text("CANDIDATE-X\n\nNeutral fixed packet. No baseline, target score, version history, or prior review is supplied.\n", encoding="utf-8")
    (packet / "REVIEWER_PROBE_PROMPT.md").write_text("Inspect only this packet and attached visual surfaces. Do not score. Report accessible filesystem roots, whether the named host paths exist, and whether this packet is readable. Do not use network, MCP, plugins, web search, or external documents. Return the confinement JSON only.\n", encoding="utf-8")
    (packet / "HARNESS_TEST_PROMPT.md").write_text("HARNESS_TEST_ONLY. Review only the supplied packet and attached visual surfaces. Return the supplied scorecard schema with run_classification=HARNESS_TEST_ONLY and discard_for_score_trajectory=true. Do not refer to any version, baseline, prior review, external context, web, MCP, plugin, or host path. This output is disposable and must never be used as a candidate score.\n", encoding="utf-8")
    record_generated(packet, "CANDIDATE_CONTEXT.md", "neutral_candidate_context", records)
    record_generated(packet, "REVIEWER_PROBE_PROMPT.md", "non_scoring_probe_prompt", records)
    record_generated(packet, "HARNESS_TEST_PROMPT.md", "disposable_harness_test_prompt", records)
    surfaces = packet / "visual-surfaces"
    surfaces.mkdir()
    for path in FIGURES:
        for localized in (path, counterpart(path)):
            target = surfaces / localized.replace("/", "__")
            shutil.copy2(packet / localized, target)
            record_generated(packet, target.relative_to(packet).as_posix(), "attached_core_figure", records)
    for path in PDFS:
        for localized in (path, counterpart(path)):
            target = surfaces / (localized.replace("/", "__").removesuffix(".pdf") + ".page-1.png")
            render_pdf(packet / localized, target)
            record_generated(packet, target.relative_to(packet).as_posix(), "attached_pdf_page_1", records)
    for path in HTML:
        for localized in (path, counterpart(path)):
            target = surfaces / (localized.replace("/", "__").removesuffix(".html") + ".first-window.png")
            render_html(packet / localized, target)
            record_generated(packet, target.relative_to(packet).as_posix(), "attached_html_first_window", records)
    reject_contamination(packet)
    records.sort(key=lambda entry: entry["relative_path"])
    content_hash = hashlib.sha256(json.dumps(records, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")).hexdigest()
    manifest = {"schema_version": "1.0.0", "candidate_id": "CANDIDATE-X", "packet_file_count": len(records), "packet_hash": content_hash, "manifest_envelope_excluded_from_its_own_hash": True, "files": records}
    (packet / "REVIEW_PACKET_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    receipt = {"source_head": args.source_head, "candidate_id": "CANDIDATE-X", "packet_hash": content_hash, "packet_file_count": len(records), "manifest_sha256": digest(packet / "REVIEW_PACKET_MANIFEST.json"), "host_packet_path": str(packet)}
    args.coordinator_receipt.parent.mkdir(parents=True, exist_ok=True)
    args.coordinator_receipt.write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"packet_hash": content_hash, "packet_file_count": len(records)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

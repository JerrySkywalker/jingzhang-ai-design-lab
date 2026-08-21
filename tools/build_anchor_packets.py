#!/usr/bin/env python3
"""Build a deterministic, bounded local review packet for trusted anchors."""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path
from typing import Any

FIGURE_FILES = (
    "assets/figures/site-overview.png",
    "assets/figures/land-use-structure.png",
    "assets/figures/key-areas.png",
    "assets/figures/mobility-bluegreen.png",
    "assets/figures/metrics-evidence.png",
)

PDF_FILES = (
    "drawings/a3-booklet.pdf",
    "drawings/a0-boards.pdf",
)

HTML_FILES = (
    "report/proposal.html",
    "visual/index.html",
)

FORBIDDEN_CONTEXT_TOKENS = (
    "v0.4.1a", "v0.4.2", "v0.4.3", "v0.4.4", "jz97", "score 77", "score 86", "score 90", "score 96",
    "official 77", "official 86", "official 90", "official 96", "host_preferred", "official96"
)


def sha256_file(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def counterpart(path_str: str) -> str:
    p = Path(path_str)
    return p.with_name(f"{p.stem}.en{p.suffix}").as_posix()


def render_pdf_page1(source: Path, target: Path) -> str | None:
    tool = shutil.which("pdftoppm")
    if not tool:
        return "pdftoppm is unavailable"
    try:
        result = subprocess.run(
            [tool, "-png", "-f", "1", "-l", "1", "-singlefile", "-r", "144", str(source), str(target.with_suffix(""))],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
            timeout=180,
        )
        if result.returncode == 0 and target.is_file():
            return None
        return f"Could not rasterize {source.name}"
    except Exception as exc:
        return f"Could not rasterize {source.name}: {exc}"


def extract_package_from_git(repo_dir: Path, commit_sha: str, sub_path: str, target_dir: Path) -> None:
    target_dir.mkdir(parents=True, exist_ok=True)
    cmd = ["git", "-C", str(repo_dir), "archive", commit_sha, sub_path]
    res = subprocess.run(cmd, capture_output=True, check=True)
    with tarfile.open(fileobj=io.BytesIO(res.stdout)) as tar:
        for member in tar.getmembers():
            if member.isfile():
                try:
                    rel = Path(member.name).relative_to(sub_path)
                except ValueError:
                    rel = Path(member.name)
                dest = target_dir / rel
                dest.parent.mkdir(parents=True, exist_ok=True)
                extracted = tar.extractfile(member)
                if extracted:
                    dest.write_bytes(extracted.read())


def build_anchor_packet(
    repo_dir: Path,
    source_head: str,
    sub_path: str,
    neutral_id: str,
    out_dir: Path,
    rubric_file: Path,
    schema_file: Path,
) -> dict[str, Any]:
    if out_dir.exists():
        shutil.rmtree(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    package_dir = out_dir / "package"
    extract_package_from_git(repo_dir, source_head, sub_path, package_dir)

    records: list[dict[str, Any]] = []
    warnings: list[dict[str, str]] = []

    def record_file(rel_path: str, file_path: Path, role: str) -> None:
        records.append({
            "relative_path": rel_path.replace("\\", "/"),
            "size": file_path.stat().st_size,
            "sha256": sha256_file(file_path),
            "role": role,
        })

    # Record package files
    for root, _, files in os.walk(package_dir):
        for f in sorted(files):
            full_p = Path(root) / f
            rel = full_p.relative_to(out_dir).as_posix()
            record_file(rel, full_p, "package_source")

    # Contract files
    shutil.copy2(rubric_file, out_dir / "CURRENT_OFFICIAL_RUBRIC.md")
    record_file("CURRENT_OFFICIAL_RUBRIC.md", out_dir / "CURRENT_OFFICIAL_RUBRIC.md", "review_contract")

    shutil.copy2(schema_file, out_dir / "SCORECARD_SCHEMA.json")
    record_file("SCORECARD_SCHEMA.json", out_dir / "SCORECARD_SCHEMA.json", "scorecard_schema")

    # Neutral candidate context
    cand_ctx = f"CANDIDATE {neutral_id}\n\nNeutral fixed evaluation packet. Review only the supplied structured deliverables and attached visual surfaces.\n"
    (out_dir / "CANDIDATE_CONTEXT.md").write_text(cand_ctx, encoding="utf-8")
    record_file("CANDIDATE_CONTEXT.md", out_dir / "CANDIDATE_CONTEXT.md", "neutral_candidate_context")

    (out_dir / "REVIEWER_PROBE_PROMPT.md").write_text(
        "Inspect only this packet and attached visual surfaces. Do not score. Report accessible filesystem roots, whether the named host paths exist, and whether this packet is readable. Do not use network, MCP, plugins, web search, or external documents. Return the confinement JSON only.\n",
        encoding="utf-8",
    )
    record_file("REVIEWER_PROBE_PROMPT.md", out_dir / "REVIEWER_PROBE_PROMPT.md", "non_scoring_probe_prompt")

    (out_dir / "HARNESS_TEST_PROMPT.md").write_text(
        "HARNESS_TEST_ONLY. Review only the supplied packet and attached visual surfaces. Return the supplied scorecard schema with run_classification=HARNESS_TEST_ONLY and discard_for_score_trajectory=true. Do not refer to any version, baseline, prior review, external context, web, MCP, plugin, or host path. This output is disposable and must never be used as a candidate score.\n",
        encoding="utf-8",
    )
    record_file("HARNESS_TEST_PROMPT.md", out_dir / "HARNESS_TEST_PROMPT.md", "disposable_harness_test_prompt")

    # Visual surfaces
    surfaces_dir = out_dir / "visual-surfaces"
    surfaces_dir.mkdir(parents=True, exist_ok=True)

    # Core figures
    for fig in FIGURE_FILES:
        for p in (fig, counterpart(fig)):
            src = package_dir / p
            if src.is_file():
                lbl = p.replace("/", "__")
                dest = surfaces_dir / lbl
                shutil.copy2(src, dest)
                record_file(dest.relative_to(out_dir).as_posix(), dest, "attached_core_figure")

    # PDF page 1 rasterization
    for pdf in PDF_FILES:
        for p in (pdf, counterpart(pdf)):
            src = package_dir / p
            if src.is_file():
                lbl = p.replace("/", "__").removesuffix(".pdf") + ".page-1.png"
                dest = surfaces_dir / lbl
                err = render_pdf_page1(src, dest)
                if err:
                    warnings.append({"source": p, "reason": err})
                else:
                    record_file(dest.relative_to(out_dir).as_posix(), dest, "attached_pdf_page_1")

    # HTML note (raw HTML deliverables are included in package/report and package/visual)
    for html in HTML_FILES:
        for p in (html, counterpart(html)):
            src = package_dir / p
            if src.is_file():
                warnings.append({"source": p, "note": "raw HTML supplied in package directory; screenshot omitted per headless policy"})

    # Contamination check on text files in packet root
    for path in (out_dir / "CANDIDATE_CONTEXT.md", out_dir / "REVIEWER_PROBE_PROMPT.md", out_dir / "HARNESS_TEST_PROMPT.md"):
        txt = path.read_text(encoding="utf-8").casefold()
        for tok in FORBIDDEN_CONTEXT_TOKENS:
            if tok in txt:
                raise RuntimeError(f"Forbidden token '{tok}' found in {path.name}")

    records.sort(key=lambda item: item["relative_path"])
    canonical_repr = json.dumps(records, ensure_ascii=False, separators=(",", ":"), sort_keys=True)
    packet_hash = hashlib.sha256(canonical_repr.encode("utf-8")).hexdigest()

    manifest = {
        "schema_version": "1.0.0",
        "neutral_id": neutral_id,
        "source_head": source_head,
        "source_package_path": sub_path,
        "packet_file_count": len(records),
        "packet_hash": packet_hash,
        "visual_surface_count": len([r for r in records if r["role"].startswith("attached_")]),
        "visual_warnings": warnings,
        "manifest_envelope_excluded_from_its_own_hash": True,
        "files": records,
    }

    (out_dir / "REVIEW_PACKET_MANIFEST.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    return manifest


def main():
    parser = argparse.ArgumentParser(description="Build anchor review packet")
    parser.add_argument("--repo", default="V:/src/haidian", type=Path)
    parser.add_argument("--head", required=True)
    parser.add_argument("--sub-path", required=True)
    parser.add_argument("--neutral-id", required=True)
    parser.add_argument("--out-dir", required=True, type=Path)
    parser.add_argument("--rubric", required=True, type=Path)
    parser.add_argument("--schema", required=True, type=Path)
    args = parser.parse_args()

    manifest = build_anchor_packet(
        repo_dir=args.repo.resolve(),
        source_head=args.head,
        sub_path=args.sub_path,
        neutral_id=args.neutral_id,
        out_dir=args.out_dir.resolve(),
        rubric_file=args.rubric.resolve(),
        schema_file=args.schema.resolve(),
    )
    print(json.dumps({
        "neutral_id": manifest["neutral_id"],
        "packet_file_count": manifest["packet_file_count"],
        "packet_hash": manifest["packet_hash"],
        "visual_surface_count": manifest["visual_surface_count"],
        "visual_warnings": manifest["visual_warnings"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()

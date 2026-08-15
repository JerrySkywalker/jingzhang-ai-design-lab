"""CLI for deterministic review-packet comparisons."""
from __future__ import annotations

import argparse
from io import BytesIO
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile

from .diff import compare_packages, render_markdown
from .snapshot import PackageSnapshot


def _materialize_ref(repo: Path, ref: str, submission_dir: str, destination: Path) -> Path:
    command = ["git", "-C", str(repo), "archive", "--format=tar", ref, submission_dir]
    completed = subprocess.run(command, capture_output=True, timeout=45, check=False)
    if completed.returncode:
        raise ValueError(completed.stderr.decode("utf-8", errors="replace").strip() or f"cannot archive {ref}")
    with tarfile.open(fileobj=BytesIO(completed.stdout), mode="r:") as archive:
        for member in archive.getmembers():
            target = (destination / member.name).resolve()
            if destination.resolve() not in target.parents and target != destination.resolve():
                raise ValueError("unsafe path in git archive")
        for member in archive.getmembers():
            archive.extract(member, destination)
    return destination


def _load(spec: str, repo: Path | None, submission_dir: str, temp: Path, label: str) -> PackageSnapshot:
    path = Path(spec)
    if path.exists():
        return PackageSnapshot.from_path(path)
    if repo is None:
        raise ValueError(f"{spec} is not a path; --repo is required for Git refs")
    return PackageSnapshot.from_path(_materialize_ref(repo, spec, submission_dir, temp / label))


def main() -> int:
    parser = argparse.ArgumentParser(description="Compare review-visible Jing-Zhang package snapshots")
    subparsers = parser.add_subparsers(dest="command", required=True)
    compare = subparsers.add_parser("compare")
    compare.add_argument("--baseline", required=True, help="package path or Git ref")
    compare.add_argument("--candidate", required=True, help="package path or Git ref")
    compare.add_argument("--repo", type=Path, help="Git repo required when a side is a ref")
    compare.add_argument("--submission-dir", default="submissions/JerrySkywalker/jingzhang-in-place")
    compare.add_argument("--json-out", type=Path)
    compare.add_argument("--markdown-out", type=Path)
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix="jz-review-packet-") as temp_name:
        temp = Path(temp_name)
        result = compare_packages(_load(args.baseline, args.repo, args.submission_dir, temp, "baseline"), _load(args.candidate, args.repo, args.submission_dir, temp, "candidate"))
    payload, markdown = json.dumps(result.to_dict(), ensure_ascii=False, indent=2, sort_keys=True), render_markdown(result)
    if args.json_out:
        args.json_out.parent.mkdir(parents=True, exist_ok=True)
        args.json_out.write_text(payload + "\n", encoding="utf-8")
    if args.markdown_out:
        args.markdown_out.parent.mkdir(parents=True, exist_ok=True)
        args.markdown_out.write_text(markdown + "\n", encoding="utf-8")
    print(payload)
    print(markdown)
    return 0 if result.ok else 3


if __name__ == "__main__":
    raise SystemExit(main())

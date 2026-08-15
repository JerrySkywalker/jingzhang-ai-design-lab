"""Path-safe package snapshots used by the local review-packet harness."""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Any


TEXT_SUFFIXES = {".md", ".html", ".json", ".geojson", ".txt", ".csv", ".svg"}


@dataclass(frozen=True)
class FileRecord:
    relative_path: str
    sha256: str
    size: int
    text: str | None


@dataclass(frozen=True)
class PackageSnapshot:
    root: Path
    files: dict[str, FileRecord]

    @classmethod
    def from_path(cls, source: str | Path) -> "PackageSnapshot":
        root = find_submission_root(Path(source))
        files: dict[str, FileRecord] = {}
        for path in sorted(root.rglob("*")):
            if not path.is_file() or path.is_symlink():
                continue
            resolved = path.resolve()
            if root not in resolved.parents and resolved != root:
                raise ValueError(f"file escapes package root: {path}")
            data = path.read_bytes()
            rel = path.relative_to(root).as_posix()
            text = data.decode("utf-8", errors="replace") if path.suffix.casefold() in TEXT_SUFFIXES else None
            files[rel] = FileRecord(rel, sha256(data).hexdigest(), len(data), text)
        return cls(root=root, files=files)

    def text(self, relative_path: str) -> str:
        record = self.files.get(relative_path)
        return record.text if record and record.text is not None else ""

    def json(self, relative_path: str) -> Any:
        content = self.text(relative_path)
        if not content:
            return None
        try:
            return json.loads(content)
        except json.JSONDecodeError:
            return None

    def all_text(self) -> str:
        return "\n".join(record.text for record in self.files.values() if record.text is not None)


def find_submission_root(source: Path) -> Path:
    """Accept a submission directory or a snapshot containing exactly one proposal."""
    source = source.resolve()
    if not source.exists() or not source.is_dir():
        raise ValueError(f"package path does not exist: {source}")
    if (source / "proposal.md").is_file():
        return source
    candidates = sorted(path.parent for path in source.rglob("proposal.md") if path.is_file())
    if len(candidates) != 1:
        raise ValueError(f"expected exactly one proposal.md beneath {source}, found {len(candidates)}")
    return candidates[0].resolve()

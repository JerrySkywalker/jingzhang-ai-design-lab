"""Deterministic review-packet comparison utilities."""

from .diff import compare_packages
from .snapshot import PackageSnapshot

__all__ = ["PackageSnapshot", "compare_packages"]

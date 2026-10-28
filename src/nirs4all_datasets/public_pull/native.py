"""Use the dataset extension's native nirs4all-formats readers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

from nirs4all_datasets import _n4ds


def open_records(path: str | Path) -> list[dict[str, Any]]:
    """Read an origin file with the embedded Rust format registry."""
    return cast(list[dict[str, Any]], json.loads(_n4ds.format_open_path(str(path))))


def open_bytes(name: str | Path, payload: bytes) -> list[dict[str, Any]]:
    """Read named origin bytes with the embedded Rust format registry."""
    return cast(list[dict[str, Any]], json.loads(_n4ds.format_open_bytes(str(name), payload)))

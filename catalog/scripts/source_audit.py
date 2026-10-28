#!/usr/bin/env python3
"""Inventory a local NIRS DB v2.0 snapshot without copying data or running scripts."""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from collections import Counter
from pathlib import Path
from typing import Any

from nirs4all_datasets.bootstrap import slugify

_CONVERTER = re.compile(r"\bconvert_[\w.-]+\.py\b")
_X_FILE = re.compile(r"X(?:\d+|_[A-Za-z0-9_]+)?\.csv")


def _file_info(path: Path, *, layout: bool = False) -> dict[str, Any]:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    info: dict[str, Any] = {"name": path.name, "size": path.stat().st_size, "sha256": digest.hexdigest()}
    if layout:
        with path.open(encoding="utf-8-sig", errors="replace", newline="") as stream:
            line = stream.readline()
        try:
            delimiter = csv.Sniffer().sniff(line, delimiters=";,\t").delimiter
        except csv.Error:
            delimiter = ";"
        header = next(csv.reader([line], delimiter=delimiter), [])
        info["layout"] = {
            "delimiter": {";": "semicolon", ",": "comma", "\t": "tab"}[delimiter],
            "column_count": len(header),
            "observation_id": "observation_id" in header,
            "sample_id": "sample_id" in header,
            "native_split": "split_original" in header,
        }
        if path.name == "Y.csv":
            with path.open(encoding="utf-8-sig", errors="replace", newline="") as stream:
                rows = csv.reader(stream, delimiter=delimiter)
                next(rows, None)
                info["layout"]["data_rows"] = sum(1 for row in rows if row)
    return info


def audit(source_tree: Path, baseline_ids: set[str], *, baseline: str = "unspecified") -> dict[str, Any]:
    """Return deterministic per-leaf fingerprints and converter dependency inventory."""
    v2 = source_tree / "v2.0"
    if not v2.is_dir():
        raise ValueError("source tree must contain v2.0/")
    leaves = sorted(p.parent for p in v2.glob("*/dataset_card.json"))
    available = {p.name for p in source_tree.rglob("convert_*.py") if p.is_file()}
    datasets = []
    counts: Counter[str] = Counter()
    for leaf in leaves:
        card_path = leaf / "dataset_card.json"
        card = json.loads(card_path.read_text(encoding="utf-8"))
        dataset_id = slugify(str(card.get("dataset_id") or leaf.name))
        script = leaf / "source_to_standard.py"
        references = sorted(set(_CONVERTER.findall(script.read_text(encoding="utf-8", errors="replace")))) if script.is_file() else []
        missing = [name for name in references if name not in available]
        counts.update(missing)
        tables = [_file_info(p, layout=True) for p in sorted(leaf.iterdir()) if p.is_file() and (p.name in {"Y.csv", "M.csv"} or _X_FILE.fullmatch(p.name))]
        datasets.append({
            "id": dataset_id,
            "source_leaf": f"v2.0/{leaf.name}",
            "new_vs_baseline": dataset_id not in baseline_ids,
            "card": _file_info(card_path),
            "script": _file_info(script) if script.is_file() else None,
            "shared_converters": references,
            "missing_shared_converters": missing,
            "standardized_tables": tables,
        })
    if len({d["id"] for d in datasets}) != len(datasets):
        raise ValueError("source snapshot has duplicate normalized dataset IDs")
    return {
        "schema": "nirs4all-datasets.source-audit.v1",
        "baseline": baseline,
        "summary": {
            "datasets": len(datasets),
            "new_vs_baseline": sum(d["new_vs_baseline"] for d in datasets),
            "with_script": sum(d["script"] is not None for d in datasets),
            "with_missing_shared_converters": sum(bool(d["missing_shared_converters"]) for d in datasets),
            "distinct_missing_shared_converters": len(counts),
            "missing_converter_usage": dict(sorted(counts.items())),
        },
        "datasets": datasets,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_tree", type=Path)
    parser.add_argument("--root", type=Path, default=Path("."), help="Git repository for HEAD baseline")
    parser.add_argument("--baseline", default="HEAD", help="Git revision for catalog comparison (default: HEAD)")
    parser.add_argument("--out", type=Path, default=Path("catalog/source_audit.json"))
    args = parser.parse_args()
    revision = subprocess.check_output(["git", "rev-parse", "--verify", f"{args.baseline}^{{commit}}"], cwd=args.root, text=True).strip()
    listing = subprocess.check_output(["git", "ls-tree", "-r", "--name-only", revision, "--", "catalog/datasets"], cwd=args.root, text=True)
    baseline = {Path(name).stem for name in listing.splitlines() if name.endswith(".yaml")}
    report = audit(args.source_tree, baseline, baseline=revision)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(report["summary"], sort_keys=True))


if __name__ == "__main__":
    main()

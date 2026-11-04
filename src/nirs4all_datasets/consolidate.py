"""Compose upstream per-target / per-instrument v2.0 leaves into one leaf per origin database.

A catalog dataset is one origin record: its samples with *all* their variables, and every spectral
block that shares those samples. Some upstream packages split a record into one leaf per target (the
same spectra, one ``y`` each) or one leaf per instrument (the same samples, one block each). The
committed ``consolidation.json`` declares, per database, which member leaves feed which spectral
block, and which leaves are superseded by an existing database. :func:`consolidate_tree` writes one
standardized leaf per database under ``<source_root>/consolidated/<id>/``; ``bootstrap`` then describes
it like any other leaf and skips the member leaves.

Within a block in ``union`` mode (the default), a member observation is the same observation as one
already composed only when its stored spectral values are identical and its sample identity, when both
declare one, agrees; their variables are then unioned. Two different non-empty values for one
variable abort the composition (two spellings of one number are one value; passport fields describing
how each member was exported keep the first member's value). Observations in ``stack`` mode, and
unmatched ones, stay distinct. A member's sample identity is its ``sample_id`` column unless the spec
names another one (``sample_columns``). No join is inferred from row position or row count, and no
sample identity is invented; members with different licences or release rights are never merged.
"""
from __future__ import annotations

import hashlib
import json
import shutil
from dataclasses import dataclass, field
from functools import lru_cache
from pathlib import Path
from typing import Any, cast

import numpy as np
import pandas as pd

SPEC_PATH = Path(__file__).with_name("consolidation.json")
CONSOLIDATED_DIR = "consolidated"
COMPOSER_VERSION = "1"
_OBS = "observation_id"
_SAMPLE = "sample_id"
# Per-task plumbing written by the upstream single-target exporter. A database has no single task,
# so these columns describe the retired view, not the samples.
_TASK_VIEW = frozenset({"dataset_id", "dataset_title", "dataset_slug", "trait_header", "trait_header_original", "task_type", "raw_label", "reference_value", "target_original_name", "class_index", "class_label", "label", "measurement_hint"})
_NA = ["", "NA", "N/A", "NaN", "nan", "null", "NULL", "<NA>"]
# Upstream bookkeeping that describes how a member leaf was produced, not the composed one.
_LEAF_BOOKKEEPING = {"Y.csv", "M.csv", "dataset_card.json", "datapackage.json", "source_to_standard.py", "raw_manifest.csv", "url_check.csv", "conversion_report.md", "consolidation.json"}


@lru_cache(maxsize=1)
def spec() -> dict[str, Any]:
    """The committed consolidation specification."""
    return cast(dict[str, Any], json.loads(SPEC_PATH.read_text(encoding="utf-8")))


def _member_ref(reference: str) -> tuple[str, str | None]:
    leaf_id, _, block = reference.partition(":")
    return leaf_id, block or None


def consumed_ids() -> dict[str, str]:
    """Every leaf id that does not become its own dataset, mapped to the database that replaces it."""
    consumed = dict(spec().get("superseded", {}))
    for database, entry in spec()["databases"].items():
        for block in entry["blocks"].values():
            for reference in block["members"]:
                consumed[_member_ref(reference)[0]] = database
    return consumed


@dataclass
class _Member:
    id: str
    card: dict[str, Any]
    metadata: pd.DataFrame
    targets: pd.DataFrame
    blocks: dict[str, Path]
    datapackage: dict[str, Any]


@dataclass
class _Observation:
    line: list[str]
    sample: str | None
    values: dict[str, str] = field(default_factory=dict)
    matched_by: set[str] = field(default_factory=set)


def _sep(path: Path) -> str:
    from nirs4all_datasets.canonical import _sniff_sep

    return _sniff_sep(path)


def _read_member(leaf: Path, member_id: str, renames: dict[str, str]) -> _Member:
    from nirs4all_datasets.canonical import _x_files

    blocks = _x_files(leaf)
    m_path, y_path = leaf / "M.csv", leaf / "Y.csv"
    metadata = pd.read_csv(m_path, sep=_sep(m_path), dtype=str, keep_default_na=False) if m_path.is_file() else pd.DataFrame(columns=[_OBS])
    targets = pd.read_csv(y_path, sep=_sep(y_path), dtype=str, keep_default_na=False) if y_path.is_file() else pd.DataFrame(columns=[_OBS])
    if _OBS not in metadata:
        raise ValueError(f"{member_id}: M.csv must declare {_OBS}")
    if _OBS not in targets:
        # Keyless Y is paired with M by row only when an X block confirms M's complete order.
        order = metadata[_OBS]
        confirmed = len(targets) == len(metadata) and order.is_unique and any(
            pd.read_csv(path, sep=_sep(path), usecols=[0], dtype=str, keep_default_na=False).iloc[:, 0].equals(order) for path in blocks.values()
        )
        if not confirmed:
            raise ValueError(f"{member_id}: Y.csv has no {_OBS} and its row pairing with M.csv cannot be verified")
        targets.insert(0, _OBS, order.to_numpy())
    for frame in (metadata, targets):
        frame.rename(columns=renames, inplace=True)
        if frame.columns.duplicated().any():
            raise ValueError(f"{member_id}: renames create duplicate columns")
        if not frame[_OBS].is_unique:
            raise ValueError(f"{member_id}: {_OBS} is not unique")
    card = json.loads((leaf / "dataset_card.json").read_text(encoding="utf-8"))
    package_path = leaf / "datapackage.json"
    package = json.loads(package_path.read_text(encoding="utf-8")) if package_path.is_file() else {}
    return _Member(member_id, card, metadata.drop(columns=[c for c in metadata if c in _TASK_VIEW]).set_index(_OBS), targets.set_index(_OBS), blocks, package)


def _spectral_keys(path: Path, header: list[str]) -> list[bytes]:
    """Content key of each stored spectrum: its float32 values, NaN canonicalized."""
    frame = pd.read_csv(path, sep=_sep(path), dtype=dict.fromkeys(header[1:], "float32") | {header[0]: str}, keep_default_na=False, na_values=dict.fromkeys(header[1:], _NA))
    values = frame[header[1:]].to_numpy(dtype=np.float32)
    values[np.isnan(values)] = np.float32("nan")
    return [hashlib.blake2b(row.tobytes(), digest_size=16).digest() for row in values]


def _read_lines(path: Path) -> tuple[list[str], list[list[str]]]:
    sep = _sep(path)
    with path.open(encoding="utf-8", newline="") as handle:
        rows = [line.rstrip("\r\n").split(sep) for line in handle if line.strip()]
    return rows[0], rows[1:]


def _sample_of(member: _Member, observation: str, column: str) -> str | None:
    if column not in member.metadata or observation not in member.metadata.index:
        return None
    value = str(member.metadata.at[observation, column]).strip()
    return value or None


def _values_of(member: _Member, observation: str, label: tuple[str, str] | None) -> dict[str, str]:
    values: dict[str, str] = {}
    for frame in (member.metadata, member.targets):
        if observation in frame.index:
            values.update({column: value for column, value in frame.loc[observation].items() if column != _SAMPLE and isinstance(value, str) and value.strip()})
    if label:
        values[label[0]] = label[1]
    return values


def _same_value(left: str, right: str) -> bool:
    """Equal text, or two spellings of one finite number (``19.360558981707516`` / ``19.36055898170752``)."""
    if left == right:
        return True
    try:
        a, b = float(left), float(right)
    except ValueError:
        return False
    return bool(np.isfinite(a) and np.isfinite(b) and np.isclose(a, b, rtol=1e-12, atol=0.0))


def _merge_values(target: _Observation, values: dict[str, str], member_id: str, conflicts: list[str]) -> None:
    from nirs4all_datasets.curation import _PASSPORT, canonical_name, is_provenance_column

    for column, value in values.items():
        current = target.values.get(column)
        if current is None:
            target.values[column] = value
        elif not _same_value(current, value) and not (is_provenance_column(column) or canonical_name(column) in _PASSPORT):
            # Passport fields describe how each member leaf was exported; the first member's are kept.
            conflicts.append(f"{member_id}: {column}={value!r} conflicts with {current!r}")


def _compose_block(block_id: str, block: dict[str, Any], members: dict[str, _Member], label_spec: dict[str, Any] | None, sample_columns: dict[str, str], report: dict[str, Any]) -> tuple[list[str], list[_Observation]]:
    mode = block.get("mode", "union")
    if mode not in {"union", "stack"}:
        raise ValueError(f"{block_id}: unknown mode {mode!r}")
    header: list[str] | None = None
    observations: list[_Observation] = []
    by_spectrum: dict[bytes, list[int]] = {}
    conflicts: list[str] = []
    for reference in block["members"]:
        member_id, member_block = _member_ref(reference)
        member = members[member_id]
        if member_block is None:
            if len(member.blocks) != 1:
                raise ValueError(f"{reference}: name the member block among {sorted(member.blocks)}")
            member_block = next(iter(member.blocks))
        path = member.blocks[member_block]
        member_header, rows = _read_lines(path)
        if header is None:
            header = member_header
        elif not _same_axis(member_header[1:], header[1:]):
            raise ValueError(f"{reference}: spectral axis differs from the first member of {block_id}")
        keys = _spectral_keys(path, member_header) if mode == "union" else [b""] * len(rows)
        label = (label_spec["column"], label_spec["values"][member_id]) if label_spec else None
        sample_column = sample_columns.get(member_id, _SAMPLE)
        matched = 0
        for row, key in zip(rows, keys, strict=True):
            observation = row[0]
            sample = _sample_of(member, observation, sample_column)
            values = _values_of(member, observation, label)
            target: _Observation | None = None
            if mode == "union":
                candidates = [i for i in by_spectrum.get(key, []) if member_id not in observations[i].matched_by and (sample is None or observations[i].sample in (None, sample))]
                if len(candidates) > 1:
                    candidates = [i for i in candidates if observations[i].sample == sample] or candidates
                # Stored duplicates (same sample, spectrum and variables) are indistinguishable; take them in order.
                if len(candidates) > 1 and all(observations[i].sample == observations[candidates[0]].sample and observations[i].values == observations[candidates[0]].values for i in candidates):
                    candidates = candidates[:1]
                if len(candidates) > 1:
                    raise ValueError(f"{reference}: observation {observation!r} matches {len(candidates)} identical spectra; declare an explicit identity")
                target = observations[candidates[0]] if candidates else None
            if target is None:
                target = _Observation(line=row[1:], sample=sample)
                observations.append(target)
                if mode == "union":
                    by_spectrum.setdefault(key, []).append(len(observations) - 1)
            else:
                matched += 1
                if target.sample is None:
                    target.sample = sample
            target.matched_by.add(member_id)
            _merge_values(target, values, member_id, conflicts)
        report[reference] = {"block": block_id, "observations": len(rows), "matched_existing": matched}
    if conflicts:
        raise ValueError(f"{block_id}: {len(conflicts)} conflicting variable values; add an explicit rename:\n  " + "\n  ".join(conflicts[:20]))
    assert header is not None
    return header, observations


def _same_axis(left: list[str], right: list[str]) -> bool:
    """Same spectral axis, allowing different decimal spellings of one header value."""
    if len(left) != len(right):
        return False
    try:
        return bool(np.allclose(np.asarray(left, dtype=float), np.asarray(right, dtype=float), rtol=1e-9, atol=0.0))
    except ValueError:
        return left == right


def _union(items: list[Any], key: Any) -> list[Any]:
    seen: dict[Any, Any] = {}
    for item in items:
        seen.setdefault(key(item), item)
    return list(seen.values())


def _compose_card(database: str, entry: dict[str, Any], members: dict[str, _Member], blocks: dict[str, tuple[dict[str, Any], int]], targets: list[str], metadata_columns: list[str], report: dict[str, Any]) -> dict[str, Any]:
    ordered = list(members.values())
    first = ordered[0].card
    licenses = {json.dumps([m.card.get("license_summary", {}).get("license_name"), (m.card.get("rights") or {}).get("public_release_allowed")]) for m in ordered}
    if len(licenses) != 1:
        raise ValueError(f"{database}: members carry different licenses or release rights: {sorted(licenses)}")
    renames = entry.get("renames", {})
    card: dict[str, Any] = json.loads(json.dumps(first))
    card["dataset_id"] = database
    card["dataset_name"] = entry.get("name") or first.get("dataset_name") or database
    card["spectral_blocks"] = [{**block, "block_id": block_id, "x_file": f"{block_id}.csv", "n_rows": n_rows} for block_id, (block, n_rows) in blocks.items()]
    organization = "single_block" if len(blocks) == 1 else "multi_block"
    card["spectral_data_summary"] = {**(first.get("spectral_data_summary") or {}), "organization_type": organization, "n_blocks": len(blocks)}
    card["spectral_organization"] = {**(first.get("spectral_organization") or {}), "organization_type": organization, "n_blocks": len(blocks), "notes": "Composed from upstream leaves of one origin record; blocks are aligned by sample identity, never by row position."}
    target_types: dict[str, Any] = {}
    target_details: dict[str, Any] = {}
    for member in ordered:
        summary = member.card.get("target_summary") or {}
        names = renames.get(member.id, {})
        for name, kind in (summary.get("target_types") or {}).items():
            target_types.setdefault(names.get(name, name), kind)
        for name, details in (summary.get("target_details") or {}).items():
            target_details.setdefault(names.get(name, name), details)
    card["target_summary"] = {"target_variables": targets, "target_types": {k: v for k, v in target_types.items() if k in targets}, "target_details": {k: v for k, v in target_details.items() if k in targets}}
    card["metadata_fields_summary"] = {"m_fields": metadata_columns}
    splits: list[dict[str, Any]] = [m.card["split_summary"] for m in ordered if isinstance(m.card.get("split_summary"), dict)]
    if splits:
        card["split_summary"] = {**splits[0], "original_split_available": any(s.get("original_split_available") for s in splits)}
    card["detected_sources"] = _union([s for m in ordered for s in m.card.get("detected_sources") or [] if isinstance(s, dict)], lambda s: s.get("url"))
    card["associated_publications"] = _union([p for m in ordered for p in m.card.get("associated_publications") or [] if isinstance(p, dict)], lambda p: p.get("doi") or p.get("title"))
    card["consolidation"] = {"composer_version": COMPOSER_VERSION, "members": report}
    return card


def _compose_datapackage(database: str, members: dict[str, _Member], renames: dict[str, dict[str, str]]) -> dict[str, Any]:
    resources = []
    for path in ("M.csv", "Y.csv"):
        fields: list[dict[str, Any]] = []
        schema_extra: dict[str, Any] = {}
        for member in members.values():
            for resource in member.datapackage.get("resources", []):
                if resource.get("path") != path or not isinstance(resource.get("schema"), dict):
                    continue
                schema = resource["schema"]
                schema_extra = schema_extra or {k: v for k, v in schema.items() if k != "fields"}
                names = renames.get(member.id, {})
                fields.extend({**f, "name": names.get(str(f.get("name")), f.get("name"))} for f in schema.get("fields", []) if isinstance(f, dict) and f.get("name") not in _TASK_VIEW - {"dataset_id"})
        if fields:
            resources.append({"name": Path(path).stem, "path": path, "profile": "tabular-data-resource", "schema": {**schema_extra, "fields": _union(fields, lambda f: f["name"])}})
    return {"profile": "data-package", "name": database, "title": database, "resources": resources}


def compose(database: str, leaves: dict[str, Path], out: Path) -> dict[str, Any]:
    """Write the composed leaf of ``database`` from its member ``leaves`` (id -> directory) into ``out``."""
    entry = spec()["databases"][database]
    renames = entry.get("renames", {})
    members = {member_id: _read_member(leaf, member_id, renames.get(member_id, {})) for member_id, leaf in leaves.items()}
    report: dict[str, Any] = {}
    composed: dict[str, tuple[list[str], list[_Observation]]] = {}
    for block_id, block in entry["blocks"].items():
        composed[block_id] = _compose_block(block_id, block, members, entry.get("label"), entry.get("sample_columns", {}), report)
    target_names = list(dict.fromkeys(c for m in members.values() for c in m.targets.columns))
    targets = [c for c in target_names if any(c in o.values for _, obs in composed.values() for o in obs)]
    metadata_names = list(dict.fromkeys([*(c for m in members.values() for c in m.metadata.columns if c != _SAMPLE), *([entry["label"]["column"]] if entry.get("label") else [])]))
    metadata_columns = [c for c in metadata_names if c not in targets and any(c in o.values for _, obs in composed.values() for o in obs)]
    has_sample = any(o.sample for _, obs in composed.values() for o in obs)

    if out.exists():
        shutil.rmtree(out)
    out.mkdir(parents=True)
    m_rows: list[dict[str, Any]] = []
    y_rows: list[dict[str, Any]] = []
    blocks_meta: dict[str, tuple[dict[str, Any], int]] = {}
    counter = 0
    for block_id, (header, observations) in composed.items():
        with (out / f"{block_id}.csv").open("w", encoding="utf-8", newline="") as handle:
            handle.write(";".join([_OBS, *header[1:]]) + "\n")
            for observation in observations:
                counter += 1
                observation_id = f"{database}_{counter:06d}"
                handle.write(";".join([observation_id, *observation.line]) + "\n")
                m_rows.append({"dataset_id": database, _OBS: observation_id, **({_SAMPLE: observation.sample or ""} if has_sample else {}), **{c: observation.values.get(c, "") for c in metadata_columns}})
                y_rows.append({_OBS: observation_id, **{c: observation.values.get(c, "") for c in targets}})
        block = entry["blocks"][block_id]
        first_id, first_block = _member_ref(block["members"][0])
        source_block: dict[str, Any] = next((b for b in members[first_id].card.get("spectral_blocks") or [] if b.get("block_id") == (first_block or b.get("block_id"))), {})
        blocks_meta[block_id] = ({**source_block, **({"signal_type": block["signal_type"]} if "signal_type" in block else {}), **({"block_name": block["name"]} if "name" in block else {})}, len(observations))
    pd.DataFrame(m_rows).to_csv(out / "M.csv", sep=";", index=False)
    if targets:
        pd.DataFrame(y_rows).to_csv(out / "Y.csv", sep=";", index=False)
    for leaf in leaves.values():
        for path in sorted(leaf.iterdir()):
            if path.is_file() and path.name not in _LEAF_BOOKKEEPING and not path.name.startswith("X") and not (out / path.name).exists():
                shutil.copy2(path, out / path.name)
    card = _compose_card(database, entry, members, blocks_meta, targets, ["dataset_id", _OBS, *([_SAMPLE] if has_sample else []), *metadata_columns], report)
    (out / "dataset_card.json").write_text(json.dumps(card, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    (out / "datapackage.json").write_text(json.dumps(_compose_datapackage(database, members, renames), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return report


def _input_fingerprint(database: str, leaves: dict[str, Path]) -> str:
    digest = hashlib.sha256(json.dumps({"composer": COMPOSER_VERSION, "entry": spec()["databases"][database]}, sort_keys=True).encode())
    digest.update(Path(__file__).read_bytes())
    for member_id, leaf in sorted(leaves.items()):
        for path in sorted(p for p in leaf.iterdir() if p.is_file()):
            stat = path.stat()
            digest.update(f"{member_id}/{path.name}:{stat.st_size}:{stat.st_mtime_ns}".encode())
    return digest.hexdigest()


def consolidate_tree(source_root: str | Path, *, only: set[str] | None = None) -> dict[str, Any]:
    """Compose every declared database whose member leaves exist under ``source_root``.

    Idempotent: a database is recomposed only when its spec entry, this composer, or a member file
    changed. A database with missing members is reported, not partially composed.
    """
    from nirs4all_datasets.bootstrap import base_leaves, slugify

    root = Path(source_root)
    available = {slugify(leaf.name): leaf for leaf in base_leaves(root)}
    report: dict[str, Any] = {"composed": [], "unchanged": [], "missing_members": {}, "errors": {}}
    for database, entry in spec()["databases"].items():
        if only and database not in only:
            continue
        member_ids = list(dict.fromkeys(_member_ref(ref)[0] for block in entry["blocks"].values() for ref in block["members"]))
        missing = [m for m in member_ids if m not in available]
        if missing:
            report["missing_members"][database] = missing
            continue
        leaves = {m: available[m] for m in member_ids}
        out = root / CONSOLIDATED_DIR / database
        marker = out / "consolidation.json"
        fingerprint = _input_fingerprint(database, leaves)
        if marker.is_file() and json.loads(marker.read_text(encoding="utf-8")).get("fingerprint") == fingerprint:
            report["unchanged"].append(database)
            continue
        try:
            members = compose(database, leaves, out)
        except (ValueError, KeyError, OSError) as exc:
            report["errors"][database] = f"{type(exc).__name__}: {exc}"
            continue
        marker.write_text(json.dumps({"fingerprint": fingerprint, "members": members}, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        report["composed"].append(database)
    return report

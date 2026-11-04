"""Recipes for fetching and assembling selected public EcoSIS resources.

Recipes name the exact origin resource, because a CKAN package can contain many
instruments or processing variants. Spectral columns retain the origin axis.
"""

from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

import pandas as pd

if TYPE_CHECKING:
    from nirs4all_datasets.schema import DatasetDescriptor


@lru_cache(maxsize=1)
def _recipes() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(Path(__file__).with_name("ecosis_recipes.json").read_text(encoding="utf-8")))


def supports(dataset_id: str) -> bool:
    """Return whether a verified origin recipe exists for this dataset."""
    return dataset_id in _recipes()


def build(descriptor: DatasetDescriptor, context: Any) -> Path:
    """Download the selected original tables and assemble a standardized leaf.

    A recipe names one spectral resource, or one per source under ``blocks`` when a package
    publishes several measurement modes of the same samples (e.g. reflectance and transmittance).
    """
    recipe = _recipes().get(descriptor.id)
    if recipe is None:
        raise ValueError(f"No verified EcoSIS assembly recipe for {descriptor.id!r}")
    parts = recipe.get("blocks") or {descriptor.sources[0].source_id: recipe}
    if set(parts) != {source.source_id for source in descriptor.sources}:
        raise ValueError(f"EcoSIS recipe for {descriptor.id} must name one resource per source")
    spectra: dict[str, pd.DataFrame] = {}
    targets, metadata = [], []
    start = 1
    for source in descriptor.sources:
        block, y, m = _assemble(descriptor, source, parts[source.source_id], context, start, partial_targets="blocks" in recipe)
        spectra[source.source_id] = block
        targets.append(y)
        metadata.append(m)
        start += len(block)
    return Path(context.write_tables(spectra, pd.concat(targets, ignore_index=True), pd.concat(metadata, ignore_index=True)))


def _assemble(descriptor: DatasetDescriptor, source: Any, recipe: dict[str, Any], context: Any, start: int, *, partial_targets: bool) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Join one spectral resource with its declared tables; observation ids continue from ``start``."""
    path = context.download(recipe["url"], recipe["filename"])
    raw = pd.read_csv(path, low_memory=False)
    for join in recipe.get("joins", [recipe["join"]] if "join" in recipe else []):
        extra_path = context.download(join["url"], join["filename"])
        extra = pd.read_csv(extra_path, low_memory=False, encoding=join.get("encoding", "utf-8"))
        for original, alias in join.get("rename", {}).items():
            if original not in extra:
                raise ValueError(f"EcoSIS join {join['url']} is missing expected column {original!r}")
            extra[alias] = extra[original]
        if join.get("duplicate_policy") == "first_with_records":
            key = join["on"]
            duplicates = extra.loc[extra.duplicated(key, keep=False)]
            if not duplicates.empty:
                records_name = f"raw_{Path(join['filename']).stem}_duplicate_records"
                records = pd.DataFrame(
                    [(value, rows.to_json(orient="records")) for value, rows in duplicates.groupby(key, dropna=False, sort=False)],
                    columns=[key, records_name],
                )
                extra = extra.drop_duplicates(key, keep="first").merge(records, on=key, how="left", validate="one_to_one")
        collisions = {column: f"raw_{Path(join['filename']).stem}_{column}" for column in extra if column != join["on"] and column in raw}
        extra = extra.rename(columns=collisions)
        raw = raw.merge(extra, on=join["on"], how="left", validate="many_to_one", indicator=True)
        if not join.get("allow_unmatched", False) and (raw["_merge"] != "both").any():
            raise ValueError(f"EcoSIS join {join['url']} is missing source sample IDs")
        raw = raw.drop(columns="_merge")
        for column in extra.columns:
            if column in raw and (pd.api.types.is_object_dtype(raw[column].dtype) or pd.api.types.is_string_dtype(raw[column].dtype)):
                raw[column] = raw[column].map(lambda value: value.strip() if isinstance(value, str) else value)
    if "axis_columns" in recipe:
        raw = raw.rename(columns={original: axis for axis, original in recipe["axis_columns"].items()})
    if "filter_notnull" in recipe:
        column = recipe["filter_notnull"]
        if column not in raw:
            raise ValueError(f"EcoSIS resource is missing filter column {column!r}")
        raw = raw.loc[raw[column].notna()].reset_index(drop=True)
    if source.axis_min is None or source.axis_max is None:
        raise ValueError(f"EcoSIS recipe for {descriptor.id} requires a declared axis range")
    axis = []
    for column in raw.columns:
        try:
            value = float(column)
        except ValueError:
            continue
        if source.axis_min <= value <= source.axis_max:
            axis.append(column)
    if recipe.get("drop_empty_spectra"):
        raw = raw.loc[raw[axis].notna().any(axis=1)].reset_index(drop=True)
    if len(axis) != source.n_variables:
        raise ValueError(f"EcoSIS resource {recipe['url']} has {len(axis)} axis columns; expected {source.n_variables}")
    targets = [v.name for v in descriptor.variables if v.role.value == "target"]
    # Each measurement-mode resource of a multi-source package carries its own subset of targets.
    target_columns = recipe.get("target_columns", {name: name for name in targets if not partial_targets or name in raw.columns})
    sample_column = recipe["sample_column"]
    required = [*([sample_column] if sample_column else []), *target_columns.values(), *recipe["metadata_columns"].values()]
    missing = [column for column in required if column not in raw.columns]
    if missing:
        raise ValueError(f"EcoSIS resource {recipe['url']} is missing expected columns: {missing}")
    ids = pd.Series([f"{descriptor.id}_{i:06d}" for i in range(start, start + len(raw))], name="observation_id")
    try:
        spectra = raw[axis].apply(pd.to_numeric, errors="raise")
    except (ValueError, TypeError) as exc:
        raise ValueError(f"EcoSIS resource {recipe['url']} has nonnumeric spectral values; retry the download") from exc
    spectra.insert(0, "observation_id", ids)
    y = pd.DataFrame({name: raw[column] for name, column in target_columns.items()})
    for name, mapping in recipe.get("target_maps", {}).items():
        mapped = y[name].map(mapping)
        if (mapped.isna() & y[name].notna()).any():
            raise ValueError(f"EcoSIS resource has unknown category in {name}")
        y[name] = mapped
    y.insert(0, "observation_id", ids)
    metadata = pd.DataFrame({"observation_id": ids, "sample_id": raw[sample_column].astype(str) if sample_column else ids})
    if sample_column and raw[sample_column].isna().any():
        raise ValueError(f"EcoSIS resource {recipe['url']} contains missing sample identities")
    for name, column in recipe["metadata_columns"].items():
        metadata[name] = raw[column]
    metadata["ecosis_resource_id"] = recipe["resource_id"]
    if recipe.get("child"):
        metadata["SpectralRep"] = 1
    # Preserve all original non-spectral columns; targets already appear in Y.
    extra_columns = {}
    for column in raw.columns.difference(axis, sort=False):
        if column in targets and column not in recipe.get("target_maps", {}):
            continue
        output_name = f"raw_{column}" if column in targets else column
        if column in metadata.columns or column in {"dataset_id", "observation_id", "sample_id"}:
            output_name = f"raw_{column}"
        extra_columns[output_name] = raw[column]
    if extra_columns:
        metadata = pd.concat([metadata, pd.DataFrame(extra_columns)], axis=1)
    return spectra, y, metadata

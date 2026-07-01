"""The consumer-facing :class:`NirsDataset` — a thin reader over a local canonical dataset.

A canonical dataset directory (``datasets/<id>/`` or a cache copy) holds the locked layout written by
:mod:`nirs4all_datasets.canonical`::

    canonical/dataset.json                  manifest of sources / variables / splits (relative paths)
    canonical/sources/<source_id>.parquet   observation_id, sample_id, <wavelength cols> (float32)
    canonical/variables.parquet             sample_id, <Y/metadata cols> (native dtype)   [optional]
    canonical/splits/<name>.parquet         sample_id, partition (str)                     [optional]

:class:`NirsDataset` reads those Parquet files (pandas/pyarrow) and exposes the spectra (``x``), the
per-sample targets/metadata (``y``/``metadata``), the native splits (``split``), and the identity
columns. It joins X sources to variables/splits **by sample identity** (``sample_id``), never by row
position — sources may differ in size (asymmetric repetitions), so a cross-source row-position merge
would be a correctness hazard and is refused.

The class never re-implements NIRS or IO logic: :meth:`to_io_spec` exposes the canonical files as a
``nirs4all-io`` ``DatasetSpec``, and :meth:`to_dataset_package` delegates assembly back to
``nirs4all-io``. :meth:`to_nirs4all` remains the direct core bridge for callers that want a
``SpectroDataset``.

The descriptor's tier governs what is exposed: an ``anonymized`` dataset masks metadata names and
normalizes targets on read (delegated to :mod:`nirs4all_datasets.qualify.anonymize`).
"""

from __future__ import annotations

import json
from functools import cached_property
from pathlib import Path
from typing import TYPE_CHECKING, Any

import numpy as np
import pandas as pd

from nirs4all_datasets.canonical import resolve_config
from nirs4all_datasets.schema import DatasetDescriptor, Tier, Variable, VariableRole

if TYPE_CHECKING:  # heavy / optional imports kept out of the runtime import path
    from nirs4all.data import SpectroDataset

_OBS_KEY = "observation_id"
_SAMPLE_KEY = "sample_id"
_ID_COLS = (_OBS_KEY, _SAMPLE_KEY)


def _parquet_columns(path: str | Path) -> list[str]:
    """Read a Parquet schema without loading the payload bytes."""
    import pyarrow.parquet as pq

    return [str(name) for name in pq.read_schema(path).names]


def _unique_same_values(left: np.ndarray, right: np.ndarray) -> bool:
    """Whether two arrays are unique-key sets with the same values."""
    left_values = [str(v) for v in left.tolist()]
    right_values = [str(v) for v in right.tolist()]
    return len(left_values) == len(set(left_values)) and len(right_values) == len(set(right_values)) and set(left_values) == set(right_values)


class NirsDataset:
    """A read-only view over one local canonical NIRS dataset.

    Wraps a dataset directory (``<root>/datasets/<id>`` or a download cache copy) holding the canonical
    layout, plus its :class:`~nirs4all_datasets.schema.DatasetDescriptor` and (optionally) its generated
    ``card.json``. All accessors read the Parquet files on demand and join by ``sample_id``.
    """

    def __init__(self, dataset_dir: str | Path, descriptor: DatasetDescriptor) -> None:
        """Bind a canonical dataset directory to its descriptor.

        Args:
            dataset_dir: The dataset directory containing ``canonical/dataset.json``.
            descriptor: The dataset descriptor (carries id, tier, variables, ids).

        Raises:
            FileNotFoundError: If ``<dataset_dir>/canonical/dataset.json`` is absent.
        """
        self._dir = Path(dataset_dir)
        self._descriptor = descriptor
        if not (self._dir / "canonical" / "dataset.json").exists():
            raise FileNotFoundError(f"no canonical data at {self._dir / 'canonical' / 'dataset.json'}")

    def __repr__(self) -> str:
        return f"NirsDataset(id={self.id!r}, tier={self.tier.value!r}, sources={self.sources()})"

    # -- identity ----------------------------------------------------------------------------------
    @property
    def id(self) -> str:
        """The dataset id (its permanent slug)."""
        return self._descriptor.id

    @property
    def descriptor(self) -> DatasetDescriptor:
        """The dataset's *public* descriptor — identical to the bound one for public/private tiers; for the
        anonymized tier a masked copy (``var_NNN`` variable names, no identifying free text) so the
        consumer API cannot leak an anonymized identity. Internal joins use the real descriptor."""
        return self._public_descriptor

    @cached_property
    def _public_descriptor(self) -> DatasetDescriptor:
        from nirs4all_datasets.qualify.anonymize import public_descriptor

        return public_descriptor(self._descriptor)

    @property
    def tier(self) -> Tier:
        """The dataset's visibility tier (``public`` / ``private`` / ``anonymized``)."""
        return self._descriptor.tier

    @cached_property
    def _config(self) -> dict[str, Any]:
        """The ``dataset.json`` manifest with every Parquet path absolutized."""
        return resolve_config(self._dir)

    def card(self) -> dict[str, Any] | None:
        """Return the generated identity ``card.json`` as a dict, or ``None`` if it has not been built.

        The qualify stage already writes an anonymized ``card.json`` for the anonymized tier; this also
        applies the public-card transform on read as a defence in depth (a stale/full card never leaks)."""
        path = self._dir / "card.json"
        if not path.exists():
            return None
        from nirs4all_datasets.qualify.anonymize import public_card

        card: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return public_card(card, self.tier)

    # -- structure ---------------------------------------------------------------------------------
    def sources(self) -> list[str]:
        """The X source ids, in canonical order (from ``dataset.json``)."""
        return [str(s["source_id"]) for s in self._config["sources"]]

    def variables(self) -> list[Variable]:
        """The declared :class:`Variable` list (targets + metadata) — masked (``var_NNN``) for the
        anonymized tier so variable names never leak through the public API."""
        return list(self._public_descriptor.variables)

    def _source_entry(self, source_id: str) -> dict[str, Any]:
        entry: dict[str, Any]
        for entry in self._config["sources"]:
            if str(entry["source_id"]) == source_id:
                return entry
        raise KeyError(f"unknown source {source_id!r}; available: {self.sources()}")

    def _read_source(self, source_id: str) -> pd.DataFrame:
        return pd.read_parquet(self._source_entry(source_id)["path"])

    # -- spectra -----------------------------------------------------------------------------------
    def x(self, source: str | None = None, *, concat: bool = True) -> np.ndarray | dict[str, np.ndarray]:
        """Return the spectral matrix/matrices (rows = observations, cols = wavelengths).

        The ``observation_id`` / ``sample_id`` columns are dropped; only the float32 spectral block is
        returned.

        Args:
            source: A single source id (returns its 2D array), or ``None`` for all sources.
            concat: When ``source is None``: if the alignment level is ``observation`` and every source
                has the same number of rows, the per-source matrices are horizontally concatenated into
                one 2D array (sources share the observation order). Otherwise — sample-aligned, or
                asymmetric row counts — a row-position concat would be wrong, so a ``{source_id: array}``
                dict is returned (``concat=False``) or a clear error is raised pointing at ``source=``
                (``concat=True``).

        Returns:
            One 2D ``np.ndarray`` (single source, or concatenable all-source), else a ``dict`` mapping
            each source id to its 2D array.

        Raises:
            KeyError: If ``source`` is not a known source id.
            ValueError: If ``concat=True`` but the sources cannot be safely row-aligned.
        """
        if source is not None:
            return self._spectra(source)

        ids = self.sources()
        arrays = {sid: self._spectra(sid) for sid in ids}
        if len(ids) == 1:
            return arrays[ids[0]]
        if not concat:
            return arrays

        level = str(self._config.get("alignment_level"))
        row_counts = {sid: arr.shape[0] for sid, arr in arrays.items()}
        if level == "observation" and len(set(row_counts.values())) == 1:
            return np.hstack([arrays[sid] for sid in ids])
        raise ValueError(
            f"cannot concatenate {len(ids)} sources of {self.id!r}: "
            f"alignment_level={level!r}, rows per source={row_counts}. "
            "Sources are linked by sample identity, never by row position. "
            "Pass source='<id>' to get one source, or concat=False for a {source_id: array} dict."
        )

    def _spectra(self, source_id: str) -> np.ndarray:
        """The float32 spectral block of one source (id columns dropped)."""
        df = self._read_source(source_id)
        spectral = df.drop(columns=[c for c in _ID_COLS if c in df.columns])
        return np.asarray(spectral.to_numpy(dtype="float32"))

    def wavelengths(self, source: str) -> np.ndarray:
        """The wavelength axis of a source as floats (its Parquet column headers; non-numeric -> NaN)."""
        df = self._read_source(source)
        cols = [c for c in df.columns if c not in _ID_COLS]
        return np.asarray(pd.to_numeric(pd.Series(cols), errors="coerce").to_numpy(), dtype=float)

    # -- ids ---------------------------------------------------------------------------------------
    def observation_ids(self, source: str) -> np.ndarray:
        """The per-spectrum ``observation_id`` values of a source (string array, in row order)."""
        return np.asarray(self._read_source(source)[_OBS_KEY].astype(str).to_numpy())

    def sample_ids(self, source: str | None = None) -> np.ndarray:
        """Per-sample ``sample_id`` values.

        With ``source=None`` returns the variables table's sample order when a variables table exists,
        else the unique sample ids across all sources (sorted, stable). With a ``source`` returns that
        source's per-observation ``sample_id`` column (one entry per spectrum).
        """
        if source is not None:
            return np.asarray(self._read_source(source)[_SAMPLE_KEY].astype(str).to_numpy())
        framed = self._variables_frame()
        if framed is not None:
            return np.asarray(framed[0][_SAMPLE_KEY].astype(str).to_numpy())
        seen: dict[str, None] = {}
        for sid in self.sources():
            for value in self._read_source(sid)[_SAMPLE_KEY].astype(str):
                seen.setdefault(value, None)
        return np.asarray(sorted(seen))

    # -- variables (Y / metadata) ------------------------------------------------------------------
    def _variables_frame(self) -> tuple[pd.DataFrame, dict[str, str]] | None:
        """The per-sample variables frame and a ``{descriptor_name: column_name}`` map, or ``None``.

        The map is identity for the public/private tiers; on the anonymized tier the columns are masked
        to ``var_NNN`` slots, so the map translates each original descriptor name to its masked column —
        accessors stay name-stable, the *frame* never reveals the original names.
        """
        variables = self._config.get("variables")
        if not variables or not variables.get("path"):
            return None
        df = pd.read_parquet(variables["path"])
        if self.tier is Tier.ANONYMIZED:
            return self._anonymize(df)
        identity = {c: c for c in df.columns if c != _SAMPLE_KEY}
        return df, identity

    def _anonymize(self, variables: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, str]]:
        """Mask metadata names + normalize targets for the ``anonymized`` tier (delegated to qualify)."""
        try:
            from nirs4all_datasets.qualify.anonymize import anonymize_variables
        except ImportError as exc:  # the qualify.anonymize step may not be installed/built yet
            raise RuntimeError(f"{self.id!r} is tier 'anonymized' but nirs4all_datasets.qualify.anonymize is unavailable; cannot serve anonymized variables.") from exc
        masked, name_map = anonymize_variables(variables, self._descriptor)
        return masked, name_map

    def _names_for(self, role: VariableRole) -> list[str]:
        return [v.name for v in self._descriptor.variables if v.role is role]

    def _select(self, role: VariableRole, name: str | None, *, kind: str) -> pd.DataFrame | None:
        framed = self._variables_frame()
        if framed is None:
            return None
        variables, name_map = framed
        if name is not None:
            column = name_map.get(name)
            if column is None or column not in variables.columns:
                # Report the columns actually present in the (possibly masked) frame, never the
                # name_map keys: on the anonymized tier those keys are the original names this tier
                # exists to hide, so listing them in an error would leak them.
                available = sorted(c for c in variables.columns if c != _SAMPLE_KEY)
                raise KeyError(f"{kind} {name!r} not in {self.id!r}; available: {available}")
            return variables[[_SAMPLE_KEY, column]]
        cols = [name_map[n] for n in self._names_for(role) if name_map.get(n) in variables.columns]
        if not cols:
            return None
        return variables[[_SAMPLE_KEY, *cols]]

    def y(self, name: str | None = None) -> pd.DataFrame | None:
        """Per-sample target values as a DataFrame (``sample_id`` + target columns), or ``None``.

        Args:
            name: A single target column name, or ``None`` for every ``role==target`` variable.

        Returns:
            A DataFrame keyed by ``sample_id``, or ``None`` if the dataset declares/holds no targets.

        Raises:
            KeyError: If ``name`` is not a column in the variables table.
        """
        return self._select(VariableRole.TARGET, name, kind="target")

    def metadata(self, name: str | None = None) -> pd.DataFrame | None:
        """Per-sample metadata values (``sample_id`` + metadata columns), or ``None``.

        Args:
            name: A single metadata column name, or ``None`` for every ``role==metadata`` variable.

        Returns:
            A DataFrame keyed by ``sample_id``, or ``None`` if there is no metadata.

        Raises:
            KeyError: If ``name`` is not a column in the variables table.
        """
        return self._select(VariableRole.METADATA, name, kind="metadata")

    # -- splits ------------------------------------------------------------------------------------
    def split(self, name: str = "original") -> pd.DataFrame | None:
        """Return a native split as a DataFrame (``sample_id`` + ``partition``), or ``None`` if absent.

        Splits are *documented, never auto-applied*: this returns the per-sample partition labels for
        the consumer to apply. ``name`` defaults to ``"original"`` (the only native split v2.0 emits).
        """
        for split in self._config.get("splits", []):
            if str(split["name"]) == name and split.get("path"):
                return pd.read_parquet(split["path"])
        return None

    # -- nirs4all-io bridge ------------------------------------------------------------------------
    def to_io_spec(self, *, source: str | None = None, split: str | None = "original") -> dict[str, Any]:
        """Return a ``nirs4all-io`` ``DatasetSpec`` over this dataset's canonical Parquet files.

        Datasets stays the catalog/access layer here: it only publishes paths, roles, units and join
        keys from the verified local canonical layout. ``nirs4all-io`` still owns loading, joins,
        partitioning and package materialization; ``nirs4all-formats`` remains behind IO for raw/vendor
        reads.

        Args:
            source: Optional single source id. When omitted, every source is included if they can be
                aligned without a many-to-many join. Asymmetric repeated sources raise a clear error;
                pass ``source=...`` to bridge one source.
            split: Native split name to expose as a metadata column. Splits are documented, not applied;
                IO receives the labels as metadata and does not create train/test partitions.

        Returns:
            A JSON-serializable spec dict accepted by ``nirs4all_io.load`` / ``to_dataset_package``.

        Raises:
            KeyError: If ``source`` is not known.
            ValueError: If multiple sources cannot be safely aligned for one IO package.
            RuntimeError: If an anonymized dataset has variables; writing a masked temporary copy would
                be a separate, explicit export step.
        """
        source_ids = self._bridge_source_ids(source)
        if self.tier is Tier.ANONYMIZED and self._config.get("variables"):
            raise RuntimeError(f"{self.id!r} is anonymized and has variables; refusing to expose the unmasked canonical variables.parquet through an IO spec.")

        primary = source_ids[0]
        sources: list[dict[str, Any]] = [self._io_source_spec(primary)]
        for sid in source_ids[1:]:
            spec = self._io_source_spec(sid)
            spec["join"] = self._io_feature_join(primary, sid)
            sources.append(spec)

        variables = self._io_variables_spec(primary)
        if variables is not None:
            sources.append(variables)

        split_spec = self._io_split_spec(primary, split)
        if split_spec is not None:
            sources.append(split_spec)

        return {
            "name": self.id,
            "sample_index": {"by": "id", "key": _SAMPLE_KEY, "observation_id": _OBS_KEY},
            "sources": sources,
        }

    def to_dataset_package(self, *, source: str | None = None, split: str | None = "original") -> Any:
        """Materialize this reference dataset as a ``nirs4all-io`` ``DatasetPackage``.

        This is the consumer-friendly bridge for pipelines that want IO's target-agnostic package.
        It delegates to ``nirs4all_io.to_dataset_package``; no parsing, joining or packaging is
        implemented in ``nirs4all-datasets``.
        """
        try:
            import nirs4all_io as nio
        except ImportError as exc:  # pragma: no cover - exercised only without the optional extra
            raise RuntimeError("to_dataset_package() needs the 'nirs4all-datasets[io]' extra (nirs4all-io).") from exc
        to_dataset_package = getattr(nio, "to_dataset_package", None)
        if not callable(to_dataset_package):
            raise RuntimeError(
                "to_dataset_package() needs a nirs4all_io build exposing DatasetPackage support. "
                "The installed nirs4all_io appears to expose only the pyo3 load/to_spec surface; "
                "install the Python MVP nirs4all-io build for DatasetPackage/canonical Parquet support."
            )
        return to_dataset_package(self.to_io_spec(source=source, split=split), name=self.id)

    def _bridge_source_ids(self, source: str | None) -> list[str]:
        ids = self.sources()
        if source is None:
            return ids
        if source not in ids:
            raise KeyError(f"unknown source {source!r} for {self.id!r}; available: {ids}")
        return [source]

    def _io_source_spec(self, source_id: str) -> dict[str, Any]:
        entry = self._source_entry(source_id)
        columns = _parquet_columns(entry["path"])
        feature_cols = [c for c in columns if c not in _ID_COLS]
        ignore_cols = [c for c in _ID_COLS if c in columns]
        column_roles: list[dict[str, Any]] = []
        if ignore_cols:
            column_roles.append({"role": "ignore", "select": ignore_cols})
        column_roles.append({"role": "features", "select": feature_cols})
        params: dict[str, Any] = {}
        if entry.get("axis_unit"):
            params["header_unit"] = entry["axis_unit"]
        source_model = next((s for s in self._descriptor.sources if s.source_id == source_id), None)
        if source_model is not None and source_model.signal_type.value != "auto":
            params["signal_type"] = source_model.signal_type.value
        return {
            "id": source_id,
            "role": "mixed",
            "modality": "spectroscopy",
            "input": entry["path"],
            "key": _SAMPLE_KEY,
            "columns": column_roles,
            **({"params": params} if params else {}),
        }

    def _io_feature_join(self, primary: str, source_id: str) -> dict[str, Any]:
        primary_obs = self.observation_ids(primary).astype(str)
        other_obs = self.observation_ids(source_id).astype(str)
        if len(primary_obs) == len(other_obs) and np.array_equal(primary_obs, other_obs):
            return {"to": primary, "how": "1:1"}
        if _unique_same_values(primary_obs, other_obs):
            return {"to": primary, "on": _OBS_KEY, "how": "1:1", "coverage": "complete"}
        primary_samples = self.sample_ids(primary).astype(str)
        other_samples = self.sample_ids(source_id).astype(str)
        if _unique_same_values(primary_samples, other_samples):
            return {"to": primary, "on": _SAMPLE_KEY, "how": "1:1", "coverage": "complete"}
        raise ValueError(
            f"cannot bridge sources {primary!r} and {source_id!r} of {self.id!r} into one IO package: "
            "their observations/samples are not uniquely alignable without a many-to-many join. "
            "Pass source='<id>' to bridge one source, or use x(concat=False) for source-separated arrays."
        )

    def _io_variables_spec(self, primary: str) -> dict[str, Any] | None:
        variables_entry = self._config.get("variables")
        if not variables_entry or not variables_entry.get("path"):
            return None
        framed = self._variables_frame()
        if framed is None:
            return None
        variables, name_map = framed
        target_cols = [name_map[n] for n in self._names_for(VariableRole.TARGET) if name_map.get(n) in variables.columns]
        metadata_cols = [name_map[n] for n in self._names_for(VariableRole.METADATA) if name_map.get(n) in variables.columns]
        selected = {_SAMPLE_KEY, *target_cols, *metadata_cols}
        ignored = [c for c in variables.columns if c not in selected]
        column_roles: list[dict[str, Any]] = []
        if ignored:
            column_roles.append({"role": "ignore", "select": ignored})
        if target_cols:
            column_roles.append({"role": "targets", "select": target_cols})
        if metadata_cols:
            column_roles.append({"role": "metadata", "select": metadata_cols})
        if not column_roles:
            return None
        return {
            "id": "variables",
            "role": "mixed",
            "input": variables_entry["path"],
            "key": _SAMPLE_KEY,
            "columns": column_roles,
            "join": {"to": primary, "on": _SAMPLE_KEY, "how": "m:1", "coverage": "warn"},
        }

    def _io_split_spec(self, primary: str, split: str | None) -> dict[str, Any] | None:
        if split is None:
            return None
        for split_entry in self._config.get("splits", []):
            if str(split_entry["name"]) != split or not split_entry.get("path"):
                continue
            split_id = "split_" + "".join(ch if ch.isalnum() else "_" for ch in split).strip("_")
            return {
                "id": split_id or "split",
                "role": "mixed",
                "input": split_entry["path"],
                "key": _SAMPLE_KEY,
                "columns": [{"role": "metadata", "select": ["partition"]}],
                "join": {"to": primary, "on": _SAMPLE_KEY, "how": "m:1", "coverage": "warn"},
            }
        return None

    # -- nirs4all bridge ---------------------------------------------------------------------------
    def to_nirs4all(self) -> SpectroDataset:
        """Assemble a nirs4all ``SpectroDataset`` from the canonical arrays (no NIRS/IO logic here).

        Each X source becomes one ``add_samples`` block (a list of arrays for multi-source, so the
        sources stay separate in nirs4all's data model), with the wavelength headers and axis unit
        carried through. Targets (``role==target``) and metadata (``role==metadata``) are attached
        per sample, aligned to the union sample order. The nirs4all dataset owns the result; this
        package only feeds it the already-materialized arrays.

        Returns:
            A nirs4all ``SpectroDataset`` populated with the dataset's sources, targets, and metadata.

        Note:
            Targets/metadata are joined to the spectra by ``sample_id`` order. This is a clean fit only
            when each source carries one spectrum per sample in a consistent order (the common
            observation-aligned case). For sample-aligned datasets with asymmetric repetitions, the
            per-sample variables are broadcast to the first source's observation order; inspect
            :meth:`sample_ids` / :meth:`observation_ids` if a different join is needed.
        """
        from nirs4all.data import SpectroDataset

        ids = self.sources()
        arrays = [self._spectra(sid) for sid in ids]
        headers = [[c for c in self._read_source(sid).columns if c not in _ID_COLS] for sid in ids]
        units = [self._source_entry(sid).get("axis_unit") for sid in ids]

        dataset = SpectroDataset(name=self.id)
        dataset.add_samples(arrays, {"partition": "train"}, headers=headers, header_unit=units)

        order = self.observation_ids(ids[0])
        framed = self._variables_frame()
        if framed is not None:
            variables, name_map = framed
            indexed = variables.set_index(_SAMPLE_KEY)
            sample_for_obs = self._read_source(ids[0]).set_index(_OBS_KEY)[_SAMPLE_KEY].astype(str)
            per_obs_samples = sample_for_obs.reindex(order)
            aligned = indexed.reindex(per_obs_samples)

            target_cols = [name_map[n] for n in self._names_for(VariableRole.TARGET) if name_map.get(n) in aligned.columns]
            if target_cols:
                dataset.add_targets(aligned[target_cols].to_numpy())
            meta_cols = [name_map[n] for n in self._names_for(VariableRole.METADATA) if name_map.get(n) in aligned.columns]
            if meta_cols:
                dataset.add_metadata(aligned[meta_cols].to_numpy(), headers=meta_cols)
        return dataset

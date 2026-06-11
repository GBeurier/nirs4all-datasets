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

The class never re-implements NIRS or IO logic: :meth:`to_nirs4all` assembles a nirs4all
``SpectroDataset`` from the already-materialized arrays (one ``add_samples`` block per source), so the
nirs4all data model — not this package — owns the resulting object.

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
        """The bound :class:`DatasetDescriptor`."""
        return self._descriptor

    @property
    def tier(self) -> Tier:
        """The dataset's visibility tier (``public`` / ``private`` / ``anonymized``)."""
        return self._descriptor.tier

    @cached_property
    def _config(self) -> dict[str, Any]:
        """The ``dataset.json`` manifest with every Parquet path absolutized."""
        return resolve_config(self._dir)

    def card(self) -> dict[str, Any] | None:
        """Return the generated identity ``card.json`` as a dict, or ``None`` if it has not been built."""
        path = self._dir / "card.json"
        if not path.exists():
            return None
        card: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
        return card

    # -- structure ---------------------------------------------------------------------------------
    def sources(self) -> list[str]:
        """The X source ids, in canonical order (from ``dataset.json``)."""
        return [str(s["source_id"]) for s in self._config["sources"]]

    def variables(self) -> list[Variable]:
        """The descriptor's declared :class:`Variable` list (targets + metadata)."""
        return list(self._descriptor.variables)

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
            raise RuntimeError(
                f"{self.id!r} is tier 'anonymized' but nirs4all_datasets.qualify.anonymize is unavailable; "
                "cannot serve anonymized variables."
            ) from exc
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

"""Tests for the access layer (local load real; remote fetch mocked, no network)."""
from __future__ import annotations

from pathlib import Path
from unittest.mock import MagicMock, patch

import numpy as np
import pytest

from nirs4all_datasets import schema as s
from nirs4all_datasets.access import canonical_file_ids, canonical_registry, fetch_private, fetch_public, load_local
from nirs4all_datasets.manifest import sha256_bytes

_HASH = "a" * 64


def _manifest() -> s.Manifest:
    files = [
        {"path": "raw/a.opus", "role": "raw", "sha256": "b" * 64, "size": 1},
        {"path": "canonical/X.parquet", "role": "canonical", "sha256": "c" * 64, "size": 2, "file_id": 11},
        {"path": "canonical/nirs4all_config.json", "role": "canonical", "sha256": "d" * 64, "size": 3, "file_id": 12},
    ]
    return s.Manifest(dataset_id="corn", descriptor_hash=_HASH, converter_name="c", converter_version="1", files=files)


def test_canonical_registry_and_file_ids() -> None:
    manifest = _manifest()
    assert canonical_registry(manifest) == {"X.parquet": "c" * 64, "nirs4all_config.json": "d" * 64}
    assert canonical_file_ids(manifest) == {"X.parquet": 11, "nirs4all_config.json": 12}


def test_fetch_public_uses_doi_and_sha256_registry(tmp_path: Path) -> None:
    pytest.importorskip("pooch")
    fake_pup = MagicMock()
    fake_pup.fetch.side_effect = lambda name: str(tmp_path / name)
    with patch("pooch.create", return_value=fake_pup) as create:
        out = fetch_public("doi:10.70112/ABC", {"X.parquet": "c" * 64}, tmp_path)  # doi: prefix is normalized
    kwargs = create.call_args.kwargs
    assert kwargs["base_url"] == "doi:10.70112/ABC/"
    assert kwargs["registry"] == {"X.parquet": "sha256:" + "c" * 64}
    assert out["X.parquet"] == tmp_path / "X.parquet"


def test_fetch_private_downloads_and_verifies(tmp_path: Path) -> None:
    content = b"parquet-bytes"
    registry = {"X.parquet": sha256_bytes(content)}
    session = MagicMock()
    resp = MagicMock()
    resp.ok = True
    resp.is_redirect = False
    resp.content = content
    session.get.return_value = resp

    out = fetch_private({"X.parquet": 11}, registry, tmp_path, instance="https://dv.example", token="TKN", session=session)

    args, kwargs = session.get.call_args
    assert args[0] == "https://dv.example/api/access/datafile/11"
    assert kwargs["headers"] == {"X-Dataverse-key": "TKN"}
    assert out["X.parquet"].read_bytes() == content


def test_fetch_private_rejects_checksum_mismatch(tmp_path: Path) -> None:
    session = MagicMock()
    resp = MagicMock()
    resp.ok = True
    resp.is_redirect = False
    resp.content = b"wrong-bytes"
    session.get.return_value = resp
    with pytest.raises(RuntimeError, match="checksum mismatch"):
        fetch_private({"X.parquet": 11}, {"X.parquet": _HASH}, tmp_path, instance="https://dv.example", token="TKN", session=session)


def test_load_local_round_trip(tmp_path: Path) -> None:
    pytest.importorskip("nirs4all")
    from nirs4all.data import SpectroDataset

    from nirs4all_datasets.ingest import write_canonical

    ds = SpectroDataset("tiny")
    ds.add_samples(np.random.RandomState(0).rand(15, 5).astype("float32"), headers=[str(1000 + i) for i in range(5)], header_unit="nm")
    ds.add_targets(np.linspace(0.0, 1.0, 15))
    write_canonical(ds, tmp_path)
    try:
        loaded = load_local(tmp_path).get_dataset_at(0)
    except Exception as exc:  # noqa: BLE001
        if "categorical_mode" in str(exc):
            pytest.skip("requires the nirs4all ParquetLoader fix")
        raise
    assert loaded.num_samples == 15

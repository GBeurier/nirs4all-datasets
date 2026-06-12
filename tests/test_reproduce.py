"""The opt-in 'reproduce from origin' path: origin resolution + the nirs4all-io delegation (no network)."""
from __future__ import annotations

from unittest.mock import MagicMock

import pytest

nio = pytest.importorskip("nirs4all_io")  # the [io] extra
pytest.importorskip("nirs4all")  # target="spectrodataset" builds a nirs4all SpectroDataset

from nirs4all_datasets.reproduce import _origin_files, assemble  # noqa: E402
from nirs4all_datasets.schema import OriginSource  # noqa: E402


def test_assemble_delegates_to_nirs4all_io(tmp_path) -> None:
    """A local X/Y folder is assembled by nirs4all-io (-> nirs4all-formats) — we re-implement nothing."""
    (tmp_path / "X.csv").write_text("observation_id;1100;1200;1300\no1;0.10;0.20;0.30\no2;0.20;0.30;0.40\n", encoding="utf-8")
    (tmp_path / "Y.csv").write_text("observation_id;protein\no1;5.0\no2;6.0\n", encoding="utf-8")
    ds = assemble(tmp_path, name="demo")
    assert ds is not None


def test_origin_files_resolves_zenodo_and_figshare() -> None:
    sess = MagicMock()
    sess.get.return_value.json.return_value = {"files": [{"key": "spectra.zip", "links": {"self": "https://zenodo.org/api/files/x/spectra.zip"}}]}
    zen = OriginSource(kind="zenodo", mode="raw", locator="10.5281/zenodo.42", access="open")
    assert _origin_files(zen, sess) == [("spectra.zip", "https://zenodo.org/api/files/x/spectra.zip")]

    sess.get.return_value.json.return_value = {"files": [{"name": "data.csv", "download_url": "https://figshare.com/ndownloader/files/9"}]}
    fig = OriginSource(kind="figshare", mode="raw", locator="10.6084/m9.figshare.987.v1", access="open")
    assert _origin_files(fig, sess) == [("data.csv", "https://figshare.com/ndownloader/files/9")]

    url = OriginSource(kind="url", mode="raw", locator="https://host.example/data/spectra.csv", access="open")
    assert _origin_files(url, MagicMock()) == [("spectra.csv", "https://host.example/data/spectra.csv")]

"""The public-origin readers are bundled with the dataset extension."""

from __future__ import annotations

import builtins
from pathlib import Path

import pytest

from nirs4all_datasets.public_pull import native


@pytest.fixture
def no_formats_python_import(monkeypatch):
    """Make an accidental separate Python formats dependency fail the test."""
    real_import = builtins.__import__

    def guarded(name, *args, **kwargs):
        if name == "nirs4all_formats" or name.startswith("nirs4all_formats."):
            raise AssertionError("the embedded reader must not import the Python formats package")
        return real_import(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", guarded)


def test_embedded_rod_path_and_bytes(tmp_path, no_formats_python_import):
    source = b"""data_synthetic
_chemical_name_mineral Syntheticite
_chemical_formula_sum 'X2 Y3'
loop_
_raman_spectrum.raman_shift
_raman_spectrum.intensity
100.0 2.5
101.0 3.5
"""
    path = tmp_path / "synthetic.rod"
    path.write_bytes(source)
    record = native.open_records(path)[0]
    by_bytes = native.open_bytes(path.name, source)[0]
    signal = record["signals"]["intensity"]
    assert signal["axis"]["values"] == [100.0, 101.0]
    assert signal["values"] == [2.5, 3.5]
    assert record["metadata"]["chemical_name_mineral"] == "Syntheticite"
    assert record["provenance"]["format"] == "raman-open-database"
    assert by_bytes["signals"] == record["signals"]


def test_invalid_file_raises_an_actionable_error(tmp_path, no_formats_python_import):
    path = tmp_path / "invalid.0"
    path.write_bytes(b"not an opus file")
    with pytest.raises(ValueError, match="unsupported format|invalid"):
        native.open_records(path)


@pytest.mark.network
def test_live_original_rod_and_opus(tmp_path, no_formats_python_import):
    from nirs4all_datasets.public_pull.common import PullContext

    ctx = PullContext("native_test", tmp_path / "work", tmp_path / "cache")
    rod = ctx.download("https://solsa.crystallography.net/rod/3500102.rod", "3500102.rod")
    record = native.open_records(rod)[0]
    assert record["provenance"]["format"] == "raman-open-database"
    assert record["signals"]["intensity"]["axis"]["values"][:3] == pytest.approx([50.50586, 51.47009, 52.43433])
    assert record["signals"]["intensity"]["values"][:3] == pytest.approx([265.264, 251.6975, 236.0346])

    files = ctx.provider_files("mendeley", "https://data.mendeley.com/datasets/d7sx7bf2hk/1")
    item = next(item for item in files if Path(item["name"]).name == "DE5_BP1_433.0")
    path = ctx.download(item["url"], "DE5_BP1_433.0", size=item.get("size"), sha256=item.get("sha256"))
    record = native.open_records(path)[0]
    by_bytes = native.open_bytes(path.name, path.read_bytes())[0]
    signal = record["signals"]["transmittance"]
    assert record["provenance"]["format"] == "bruker-opus"
    assert len(signal["values"]) == 3069
    assert signal["values"][:3] == pytest.approx([1.0017212629318237, 1.0008552074432373, 0.9998939037322998])
    assert by_bytes["signals"] == record["signals"]

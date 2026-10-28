"""Focused coverage for original-source tabular recipe mappings."""
from types import SimpleNamespace

import numpy as np
import pandas as pd

from nirs4all_datasets.public_pull import other


class Context:
    def __init__(self, path):
        self.path = path
        self.source_url = None
        self.result = None

    def download(self, url, filename=None):
        self.source_url = url
        return self.path

    def write_tables(self, sources, targets, metadata):
        self.result = (sources, targets, metadata)
        return self.path.parent


def test_twinspectra_retains_group_and_native_identifiers(tmp_path):
    path = tmp_path / "raw.csv"
    pd.DataFrame({"id": [101, 102], "sample": [1, 2], "group": ["A", "B"], "fold": [0, 1], "908.1": [0.5, 0.6]}).to_csv(path, index=False)
    context = Context(path)
    result = other.build(SimpleNamespace(id="zenodo_twinspectra_micronir_rdf_nir"), context)
    sources, y, m = context.result
    assert result == tmp_path
    assert context.source_url.startswith("https://zenodo.org/")
    assert sources["X"]["908.1"].tolist() == [0.5, 0.6]
    assert y["group"].tolist() == ["A", "B"]
    assert m["sample_id"].tolist() == ["1", "2"]
    assert m["fold"].tolist() == [0, 1]
    assert sources["X"]["observation_id"].equals(y["observation_id"])


def test_milk_uses_total_transmittance_and_all_targets(tmp_path):
    path = tmp_path / "raw.csv"
    metadata = {k: [1] for k in ("Cow_ID", "Fat", "Prot", "Lact", "SCC", "Urea", "Milk_yield", "Milk_Interv", "SET", "Time_Dark", "Time_Milk", "Time_PrevMilk", "Time_Sample", "Time_White")}
    fields = {f"Trans_{channel}_{i}": [float(i)] for channel in ("Tot", "Dark", "Sample", "White") for i in range(1, 257)}
    pd.DataFrame(metadata | fields).to_csv(path, index=False)
    context = Context(path)
    other.build(SimpleNamespace(id="zenodo_milk_composition_transmittance_nir"), context)
    sources, y, m = context.result
    assert np.allclose(sources["X"].iloc[0, 1:].astype(float), np.arange(1, 257))
    assert list(y.columns[1:]) == ["Fat", "Prot", "Lact", "SCC", "Urea", "Milk_yield"]
    assert m["Cow_ID"].tolist() == [1]


def test_chembl_preserves_native_peaks_and_distinct_frequency_axes(tmp_path, monkeypatch):
    import json
    import sqlite3
    import zlib

    path = tmp_path / "raw.db"
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE molecule (id INTEGER, SMILES TEXT, sdf_name TEXT, database_tag TEXT, Eg REAL, Homo REAL, Lumo REAL, Dtotal REAL, isotropic_pol REAL, electronic_ext REAL, heat_capacity REAL, Rx REAL, Ry REAL, Rz REAL, Dx REAL, Dy REAL, Dz REAL, xyz_name TEXT, blob_data BLOB)")
        for number, freq in [(1, [100.5, 200.5]), (2, [90.5])]:
            data = {"freq": freq, "IR Inten": [float(i + 1) for i in range(len(freq))], "Raman Activ": [float(i + 3) for i in range(len(freq))], "atoms": [6]}
            blob = zlib.compress(json.dumps(data).encode())
            db.execute("INSERT INTO molecule VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (number, "C", f"CHEMBL{number}.xyz.sdf", "ChEMBL", 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, "original.xyz", blob))

    class ChemblContext(Context):
        def provider_files(self, provider, locator):
            return [{"name": "Raman-ChEMBL-part1.db", "url": "https://origin.example/db", "size": path.stat().st_size}]

        def download(self, url, filename=None, **kwargs):
            return path

    monkeypatch.setattr(other, "_CHEMBL_LIMIT", 2)
    context = ChemblContext(path)
    other.build(SimpleNamespace(id="chembl_ir_raman_multiblock"), context)
    sources, y, m = context.result
    assert y["chembl_id"].tolist() == ["CHEMBL1", "CHEMBL2"]
    assert sources["X1"].iloc[0, 1:].tolist() == [1.0, 2.0]
    assert sources["X2"].iloc[0, 1:].tolist() == [3.0, 4.0]
    assert np.isnan(sources["X1"].iloc[1, 2])
    assert json.loads(m["mode_frequencies_cm1"].iloc[1]) == [90.5]
    assert m["Rx"].tolist() == [8.0, 8.0]
    with sqlite3.connect(path) as db:
        assert json.loads(zlib.decompress(db.execute("SELECT blob_data FROM molecule WHERE id = 1").fetchone()[0]))["freq"] == [100.5, 200.5]
    layout = json.loads((tmp_path / "pull-layout.json").read_text())
    assert layout["representation"] == "native_peak_lists"
    assert layout["sources"]["X1"]["axis_unit"] == "index"


def test_malaria_joins_publisher_sample_ids_and_keeps_stage_split(tmp_path, monkeypatch):
    import zipfile

    from nirs4all_datasets.public_pull import native

    calibration = tmp_path / "calibration.dta"
    validation = tmp_path / "validation.dta"
    pd.DataFrame({"sampleid": ["M214C001", "S214C002"], "Stage": [2, 1], "parasite_load": [12.0, 3.0], "age": [4, 5]}).to_stata(calibration, write_index=False)
    pd.DataFrame({"sampleid": ["M113G3"], "Stage": [2], "parasiteload": [22.0], "age": [6]}).to_stata(validation, write_index=False)
    archive = tmp_path / "spectra.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("Spectra training dataset oocyst infection/21C400001.spc", b"1")
        z.writestr("Spectra test dataset oocyst infection/113G00003.spc", b"3")

    class MalariaContext(Context):
        def dataverse_file(self, file_id, filename, *, guestbook_id):
            assert guestbook_id == 293
            return {3326596: archive, 3326589: calibration, 3330651: validation}[file_id]

    def parse(name, payload):
        value = int(payload.decode())
        return [{"signals": {"signal": {"axis": {"values": [1000, 1001]}, "values": [value, value + 1]}}}]

    monkeypatch.setattr(native, "open_bytes", parse)
    context = MalariaContext(archive)
    other.build(SimpleNamespace(id="malaria_anopheles_gambiae_oocyst_nir"), context)
    sources, targets, metadata = context.result
    assert sources["X"]["1000"].tolist() == [1, 3]
    assert targets["x"].tolist() == [12.0, 22.0]
    assert metadata["sample_id"].tolist() == ["M214C001", "M113G3"]
    assert metadata["split_original"].tolist() == ["train", "test"]
    assert metadata["age"].tolist() == [4, 6]


def test_malaria_does_not_submit_a_missing_guestbook_profile(tmp_path, monkeypatch):
    from nirs4all_datasets.public_pull.common import PullContext

    context = PullContext("malaria_anopheles_gambiae_oocyst_nir", tmp_path / "stage", tmp_path / "cache")
    monkeypatch.setattr(context, "get_json", lambda *_args, **_kwargs: {"data": {"nameRequired": True, "customQuestions": []}})
    monkeypatch.setattr(context.session, "post", lambda *_args, **_kwargs: (_ for _ in ()).throw(AssertionError("unexpected submission")))
    import pytest
    with pytest.raises(ValueError, match="guestbook_response.*name"):
        other.build(SimpleNamespace(id="malaria_anopheles_gambiae_oocyst_nir"), context)


def test_origin_metadata_uses_names_visible_after_canonical_conversion(tmp_path):
    context = Context(tmp_path / "source.csv")
    raw = pd.DataFrame({"target": [7], "source_file": ["raw.spc"], "source_split_index": [12]})
    other._write(context, "example", raw, {"X": pd.DataFrame({"1000": [0.4]})}, ["target"], None, "https://origin.example/raw.spc")
    metadata = context.result[2]
    assert metadata["origin_file"].tolist() == ["raw.spc"]
    assert metadata["origin_split_index"].tolist() == [12]
    assert metadata["origin_url"].tolist() == ["https://origin.example/raw.spc"]

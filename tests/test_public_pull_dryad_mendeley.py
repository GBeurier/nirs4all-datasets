"""Focused checks for origin recipes' axes, targets and identity joins."""
from pathlib import Path
from types import SimpleNamespace

import pandas as pd

from nirs4all_datasets.public_pull import dryad, mendeley


class TableContext:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.sources = None
        self.targets = None
        self.metadata = None

    def download(self, url: str, filename: str, **kwargs: object) -> Path:
        return self.root / filename

    def extract(self, path: Path) -> Path:
        return self.root

    def provider_files(self, provider: str, locator: str) -> list[dict[str, str]]:
        return [{"name": "Data-Parastar et al 2020 Food Control v2.csv", "url": "https://example.test/chicken.csv"}]

    def write_tables(self, sources: dict, targets: pd.DataFrame | None = None, metadata: pd.DataFrame | None = None) -> Path:
        self.sources, self.targets, self.metadata = sources, targets, metadata
        return self.root


def test_chicken_keeps_three_classes_and_wavelengths(tmp_path: Path) -> None:
    table = pd.DataFrame({"Sample_number": [42, 42], "Production_system": ["A", "B"], "Scan_type": ["OM", "OM"], "Freshness": ["FR", "NF"]})
    table = pd.concat([table, pd.DataFrame({f"X{i}": [i, i + 1] for i in range(125)})], axis=1)
    table.to_csv(tmp_path / "Data-Parastar et al 2020 Food Control v2.csv", sep=";", index=False)
    context = TableContext(tmp_path)
    mendeley.build(SimpleNamespace(id="mendeley_chicken_meat_authenticity_handheld_nir"), context)
    assert context.sources["X"].columns.tolist()[1:] == [str(i) for i in range(125)]
    assert context.targets[["Production_system", "Scan_type", "Freshness"]].values.tolist() == [["A", "OM", "FR"], ["B", "OM", "NF"]]
    assert context.metadata["original_sample_id"].tolist() == [42, 42]


def test_dryad_beetle_transposes_axis_and_preserves_labels(tmp_path: Path) -> None:
    pd.DataFrame({"wl": [400, 401], "one": [1.0, 2.0], "two": [3.0, 4.0]}).to_csv(tmp_path / "1_Reflectancedata.csv", index=False)
    context = TableContext(tmp_path)
    dryad.build(SimpleNamespace(id="dryad_beetle_reflectance_manual"), context)
    assert context.sources["X"].columns.tolist() == ["observation_id", "400", "401"]
    assert context.sources["X"].iloc[:, 1:].values.tolist() == [[1.0, 2.0], [3.0, 4.0]]
    assert context.metadata["original_sample_id"].tolist() == ["one", "two"]


def test_fairdata_joins_zero_padded_spectral_ids(tmp_path: Path) -> None:
    import io
    import zipfile

    from nirs4all_datasets.public_pull.common import PullContext
    from nirs4all_datasets.public_pull.fairdata import build

    spectral = io.BytesIO()
    with pd.ExcelWriter(spectral, engine="openpyxl") as writer:
        for sheet in ("AvaSpec-ULS2048L-USB2", "AvaSpec-NIR256-2.5-HSC"):
            pd.DataFrame({"id": ["M01_ACL", "M01_ACL"], "site": [1, 2], "1000": [0.2, 0.3]}).to_excel(writer, sheet_name=sheet, index=False)
    chemistry = io.BytesIO()
    with pd.ExcelWriter(chemistry, engine="openpyxl") as writer:
        pd.DataFrame({"Property": ["M1_ACL"], "Knee identifier": [1], "Ligament type": ["ACL"], "Starch": [12.5]}).to_excel(writer, index=False, startrow=10)
    archive = io.BytesIO()
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED) as z:
        z.writestr("folder/Data_biomechanics_and_biochemistry.xlsx", chemistry.getvalue())
        z.writestr("folder/Data_NIRS.xlsx", spectral.getvalue())

    class Response:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            return None

        def raise_for_status(self):
            return None

        def json(self):
            return {"url": "https://example.test/public-package"}

        def iter_content(self, size):
            yield archive.getvalue()

    class Session:
        def post(self, *args, **kwargs):
            return Response()

        def get(self, *args, **kwargs):
            return Response()

    output = TableContext(tmp_path)
    context = PullContext("fairdata_bovine_knee_ligament_nir_manual", tmp_path, tmp_path, timeout=1)
    context.session.close()
    context.session = Session()
    context.get_json = lambda *args, **kwargs: {"status": "SUCCESS", "package": "source.zip"}
    context.write_tables = output.write_tables
    build(SimpleNamespace(targets=[SimpleNamespace(name="Starch")]), context)
    assert context.downloaded_bytes == len(archive.getvalue())
    assert output.targets["Starch"].tolist() == [12.5, 12.5]
    assert output.metadata["original_sample_id"].tolist() == ["M01_ACL", "M01_ACL"]
    assert output.metadata["site"].tolist() == [1, 2]


def test_harvard_forage_refuses_new_required_guestbook_fields(tmp_path: Path) -> None:
    import pytest

    from nirs4all_datasets.public_pull.harvard_forage import build

    context = TableContext(tmp_path)
    context.get_json = lambda *args, **kwargs: {"data": {"emailRequired": True, "customQuestions": []}}
    with pytest.raises(ValueError, match="requires user information"):
        build(SimpleNamespace(), context)


def test_cucurbit_preserves_source_partitions(tmp_path: Path) -> None:
    filename = "Dataset_RAW_Vis-NIR_Spectra_for_Intact_Cucurbitaceae_Fruits.xlsx"
    path = tmp_path / filename
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        for sheet, sample in (("Calibration Set", "Zucchini 1"), ("Prediction Set", "Melon 2")):
            pd.DataFrame({"sample": [sample], "Water Content (%)": [91], "SSC (%)": [4], 381: [0.1], 384: [0.2]}).to_excel(writer, sheet_name=sheet, index=False)
    context = TableContext(tmp_path)
    context.provider_files = lambda *args: [{"name": filename, "url": "https://example.test/source"}]
    mendeley.build(SimpleNamespace(id="mendeley_cucurbitaceae_fruits_visnir"), context)
    assert context.metadata["split_original"].tolist() == ["calibration", "prediction"]
    assert context.metadata["sample_id"].tolist() == ["Zucchini 1", "Melon 2"]
    assert context.targets["Water_Content_pct"].tolist() == [91, 91]


def test_beetle_origin_labels_survive_canonical_export(tmp_path: Path, monkeypatch) -> None:
    import zipfile

    from nirs4all_datasets import public_pull
    from nirs4all_datasets.dataset import NirsDataset
    from nirs4all_datasets.public_pull.common import PullContext
    from nirs4all_datasets.schema import DatasetDescriptor

    archive = tmp_path / "origin.zip"
    with zipfile.ZipFile(archive, "w") as z:
        z.writestr("1_Reflectancedata.csv", "wl,one,two\n400,1,3\n401,2,4\n")
    monkeypatch.setattr(PullContext, "download", lambda *args, **kwargs: archive)
    descriptor = DatasetDescriptor(
        id="dryad_beetle_reflectance_manual", name="Beetle", description="Original source spectra", tier="public",
        sources=[{"source_id": "X", "axis_unit": "nm"}], provenance={"contributor": "Origin"},
        governance={"license": "CC0-1.0"}, origin_sources=[{"kind": "url", "mode": "raw", "access": "open", "locator": "https://datadryad.org/"}],
    )
    directory, runtime = public_pull.pull(descriptor, cache_dir=tmp_path / "cache")
    metadata = NirsDataset(directory, runtime).metadata()
    assert metadata["original_sample_id"].tolist() == ["one", "two"]


def test_coffee_retains_unlabelled_spectrum_and_source_dispersion(tmp_path: Path) -> None:
    with pd.ExcelWriter(tmp_path / "FTNIR_Data.xlsx", engine="openpyxl") as writer:
        pd.DataFrame({"Wavenumber": [12000, 11996], "M 1_1": [0.1, 0.2], "M 21_1": [0.3, 0.4]}).to_excel(writer, sheet_name="FTNIR_data ", index=False)
    with pd.ExcelWriter(tmp_path / "Moisture_values.xlsx", engine="openpyxl") as writer:
        pd.DataFrame({"Sample": ["M 1"], "Moisture W.B": [51.0], "Standard deviation": [0.95], "Coefficient of variation (%)": [1.83]}).to_excel(writer, sheet_name="Hoja1", index=False)
    context = TableContext(tmp_path)
    context.provider_files = lambda *args: [{"name": name, "url": "https://example.test/" + name} for name in ("FTNIR_Data.xlsx", "Moisture_values.xlsx")]
    mendeley.build(SimpleNamespace(id="mendeley_coffee_drying_ftnir_moisture"), context)
    assert len(context.sources["X"]) == 2
    assert context.targets["Moisture_WB"].iloc[0] == 51.0
    assert pd.isna(context.targets["Moisture_WB"].iloc[1])
    assert context.metadata["moisture_standard_deviation"].iloc[0] == 0.95
    assert context.metadata["moisture_coefficient_of_variation_pct"].iloc[0] == 1.83

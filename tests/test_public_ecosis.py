"""EcoSIS recipes operate on downloaded origin tables, not a source checkout."""

from types import SimpleNamespace

import pandas as pd
import pytest

from nirs4all_datasets.public_pull import ecosis

DATASET = "ecosis_2018_cedar_creek_pressed_leaves_reflectance_nirs"


class Context:
    def __init__(self, path):
        self.path = path
        self.frames = None

    def download(self, url, filename=None):
        assert url.startswith("https://data.ecosis.org/dataset/")
        return self.path

    def write_tables(self, sources, targets, metadata):
        self.frames = (sources, targets, metadata)
        return self.path.parent


def descriptor():
    return SimpleNamespace(
        id=DATASET,
        sources=[SimpleNamespace(source_id="X", axis_min=400, axis_max=401, n_variables=2)],
        variables=[SimpleNamespace(name="Species", role=SimpleNamespace(value="target"))],
    )


def test_assembly_preserves_axis_targets_and_source_metadata(tmp_path):
    path = tmp_path / "origin.csv"
    path.write_text("sample_name,Plot,Species,latitude,longitude,400,401\na,p,oak,42,-71,0.1,0.2\n", encoding="utf-8")
    context = Context(path)
    ecosis.build(descriptor(), context)
    sources, targets, metadata = context.frames
    assert sources["X"].columns.tolist() == ["observation_id", "400", "401"]
    assert sources["X"].iloc[0, 1:].tolist() == [0.1, 0.2]
    assert targets.Species.tolist() == ["oak"]
    assert metadata.sample_id.tolist() == ["a"]
    assert metadata.site.tolist() == ["p"]
    assert metadata.Plot.tolist() == ["p"]
    assert ecosis.supports(DATASET)
    assert not ecosis.supports("ecosis_unknown")


def test_missing_axis_fails_explicitly(tmp_path):
    path = tmp_path / "origin.csv"
    path.write_text("sample_name,Plot,Species,latitude,longitude,400\na,p,oak,42,-71,0.1\n", encoding="utf-8")
    with pytest.raises(ValueError, match="axis columns"):
        ecosis.build(descriptor(), Context(path))


@pytest.mark.network
@pytest.mark.parametrize("dataset_id", sorted(ecosis._recipes()))
def test_live_origin_cold_download(tmp_path, dataset_id):
    import json
    from pathlib import Path

    import requests

    from nirs4all_datasets.schema import DatasetDescriptor

    index = json.loads((Path(__file__).parents[1] / "catalog" / "index.json").read_text())
    desc = DatasetDescriptor.model_validate(index["datasets"][dataset_id]["descriptor"])
    class NetworkContext(Context):
        def download(self, url, filename=None):
            response = requests.get(url, timeout=120)
            response.raise_for_status()
            path = tmp_path / filename
            path.write_bytes(response.content)
            return path

    context = NetworkContext(tmp_path / "origin.csv")
    ecosis.build(desc, context)
    sources, targets, metadata = context.frames
    assert len(sources["X"]) == len(targets) == len(metadata) == desc.sources[0].n_observations
    assert len(sources["X"].columns) == desc.sources[0].n_variables + 1
    assert metadata["sample_id"].notna().all()
    if dataset_id == DATASET:
        assert targets.iloc[0]["Species"] == "PIBA"
        assert metadata.iloc[0]["sample_id"] == "101_PIBA_1A_OUTER"
        assert pd.to_numeric(sources["X"]["400"]).iloc[0] == pytest.approx(0.19396444)


def test_join_aligns_by_key_and_preserves_missing_trait_rows(tmp_path, monkeypatch):
    raw = tmp_path / "raw.csv"
    raw.write_text("sample_name,Plot,latitude,longitude,400,401\na,p,42,-71,0.1,0.2\nb,q,43,-72,0.3,0.4\n", encoding="utf-8")
    extra = tmp_path / "traits.csv"
    extra.write_text("sample_name,Species\na,oak\n", encoding="utf-8")
    recipe = {
        "url": "https://data.ecosis.org/dataset/raw",
        "filename": "raw.csv",
        "resource_id": "resource",
        "sample_column": "sample_name",
        "metadata_columns": {"site": "Plot", "latitude": "latitude", "longitude": "longitude"},
        "joins": [{"url": "https://data.ecosis.org/dataset/traits", "filename": "traits.csv", "on": "sample_name", "allow_unmatched": True}],
    }
    monkeypatch.setattr(ecosis, "_recipes", lambda: {DATASET: recipe})

    class JoinContext(Context):
        def download(self, url, filename=None):
            return tmp_path / filename

    context = JoinContext(raw)
    ecosis.build(descriptor(), context)
    sources, targets, metadata = context.frames
    assert len(sources["X"]) == len(targets) == len(metadata) == 2
    assert targets.Species.iloc[0] == "oak"
    assert pd.isna(targets.Species.iloc[1])
    assert metadata.sample_id.tolist() == ["a", "b"]


def test_duplicate_join_retains_original_rows_and_selects_first(tmp_path, monkeypatch):
    raw = tmp_path / "raw.csv"
    raw.write_text("sample_name,Plot,latitude,longitude,400,401\na,p,42,-71,0.1,0.2\n", encoding="utf-8")
    traits = tmp_path / "traits.csv"
    traits.write_text("sample_name,Species\na,oak\na,maple\n", encoding="utf-8")
    recipe = {
        "url": "https://data.ecosis.org/dataset/raw",
        "filename": "raw.csv",
        "resource_id": "resource",
        "sample_column": "sample_name",
        "metadata_columns": {"site": "Plot", "latitude": "latitude", "longitude": "longitude"},
        "joins": [{"url": "https://data.ecosis.org/dataset/traits", "filename": "traits.csv", "on": "sample_name", "duplicate_policy": "first_with_records"}],
    }
    monkeypatch.setattr(ecosis, "_recipes", lambda: {DATASET: recipe})

    class JoinContext(Context):
        def download(self, url, filename=None):
            return tmp_path / filename

    context = JoinContext(raw)
    ecosis.build(descriptor(), context)
    _, targets, metadata = context.frames
    assert targets.Species.tolist() == ["oak"]
    assert '"Species":"oak"' in metadata.raw_traits_duplicate_records.iloc[0]
    assert '"Species":"maple"' in metadata.raw_traits_duplicate_records.iloc[0]


def test_nonnumeric_spectrum_fails_instead_of_coercing_corruption(tmp_path):
    path = tmp_path / "origin.csv"
    path.write_text("sample_name,Plot,Species,latitude,longitude,400,401\na,p,oak,42,-71,proxy-error,0.2\n", encoding="utf-8")
    with pytest.raises(ValueError, match="nonnumeric spectral values"):
        ecosis.build(descriptor(), Context(path))

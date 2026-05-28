"""Tests for the interactive static-site generator (pure rendering; no nirs4all)."""
from __future__ import annotations

import json
from pathlib import Path

import yaml

from nirs4all_datasets.site import build_site


def _registry(tmp_path: Path, dataset_id: str = "corn_oil", name: str = "Corn — oil") -> Path:
    root = tmp_path
    (root / "catalog" / "datasets").mkdir(parents=True)
    catalog = {
        "schema_version": "1.0",
        "n_datasets": 1,
        "datasets": [{
            "id": dataset_id, "name": name, "version": "1.0.0", "domain": "corn", "task_type": "regression",
            "targets": ["oil"], "n_samples": 80, "n_features": 700, "signal_type": "absorbance",
            "license": "CC-BY-4.0", "visibility": "restricted", "has_card": True, "is_stale": False, "doi": None,
        }],
    }
    (root / "catalog" / "datasets.yaml").write_text(yaml.safe_dump(catalog), encoding="utf-8")
    (root / "catalog" / "datasets" / f"{dataset_id}.yaml").write_text(yaml.safe_dump({
        "schema_version": "1.0", "id": dataset_id, "name": name, "version": "0.1.0", "description": "desc",
        "domain": "corn", "keywords": ["corn", "nir"],
        "instrument": {"modality": "NIR", "axis_unit": "nm", "signal_type": "absorbance"},
        "targets": [{"name": "oil", "task_type": "regression"}],
        "provenance": {"contributor": "Lab"},
        "governance": {"license": "CC-BY-4.0", "visibility": "restricted", "confidentiality_class": "public"},
    }), encoding="utf-8")

    dd = root / "datasets" / dataset_id
    (dd / "assets").mkdir(parents=True)
    (dd / "assets" / "spectra_envelope.png").write_bytes(b"\x89PNG\r\n\x1a\n")  # stub
    (dd / "card.json").write_text(json.dumps({
        "identity": {"id": dataset_id, "name": name, "version": "1.0.0", "description": "desc", "doi": None},
        "inventory": {"n_samples": 80, "n_features": 700, "n_sources": 1, "n_folds": 0},
        "spectral": {"wavelength_unit": "nm", "wavelength_range": [1100.0, 2498.0], "signal_type": "absorbance"},
        "dimensionality": {"effective_rank": 3.2, "n_components_95": 4, "n_components_99": 9, "explained_variance_ratio": [0.99]},
        "shift": {"target": {"standardized_mean_diff": 0.3, "ks_statistic": 0.2, "ks_p": 0.4, "wasserstein": 0.1}, "covariate": {"pc_space_centroid_distance_std": 0.8, "pc1_ks_statistic": 0.2, "pc1_ks_p": 0.3}},
        "targets": {"task_type": "regression", "stats": {"mean": 3.5, "std": 0.2}, "partitions": {"train": {"mean": 3.4, "sd": 0.2, "nsample": 60}, "test": {"mean": 3.6, "sd": 0.1, "nsample": 20}}},
        "quality": {"has_nan": False, "spectral": {"noise_proxy_db": 40.0, "dynamic_range": 1.2}, "x_outliers": {"n_excluded": 5, "n_samples": 60, "exclusion_rate": 0.08, "method": "robust_mahalanobis"}},
        "assets": {"spectra_envelope": "assets/spectra_envelope.png"},
        "warnings": [],
    }), encoding="utf-8")
    (dd / "croissant.json").write_text("{}", encoding="utf-8")
    return root


def test_build_site_outputs(tmp_path: Path) -> None:
    root = _registry(tmp_path)
    out = build_site(root, tmp_path / "site")
    assert (out / "index.html").exists()
    assert (out / "style.css").exists() and (out / "app.js").exists()
    page = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "Corn — oil" in page
    assert "Effective rank" in page and "Train ↔ test shift" in page  # enriched sections rendered
    assert (out / "assets" / "corn_oil" / "spectra_envelope.png").exists()  # assets copied
    assert (out / "data" / "corn_oil.card.json").exists()  # downloadable card
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "const DATA =" in index and "corn_oil" in index


def test_index_json_escapes_script(tmp_path: Path) -> None:
    # A dataset name containing "</script>" must not break out of the inline data block.
    root = _registry(tmp_path, dataset_id="evil", name="Evil </script><b>x")
    out = build_site(root, tmp_path / "site")
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "</script><b>" not in index  # raw breakout neutralized
    assert "<\\/script>" in index  # escaped form present


def test_version_shown_in_index_and_card(tmp_path: Path) -> None:
    root = _registry(tmp_path)
    out = build_site(root, tmp_path / "site")
    index = (out / "index.html").read_text(encoding="utf-8")
    assert '"version": "1.0.0"' in index  # embedded in the index data
    assert ">Ver.<" in index  # version column header present
    card = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "1.0.0" in card and "Catalog version" in card


def test_skips_entries_without_card(tmp_path: Path) -> None:
    root = _registry(tmp_path)
    cat = yaml.safe_load((root / "catalog" / "datasets.yaml").read_text())
    cat["datasets"].append({"id": "nocard", "name": "No Card", "task_type": "regression", "has_card": False})
    (root / "catalog" / "datasets.yaml").write_text(yaml.safe_dump(cat), encoding="utf-8")
    out = build_site(root, tmp_path / "site")
    assert not (out / "dataset" / "nocard.html").exists()

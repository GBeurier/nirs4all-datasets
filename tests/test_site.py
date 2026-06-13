"""Tests for the schema-2.0 static-site generator (pure rendering; no nirs4all/pandas/matplotlib).

These build :func:`build_site` over a hand-written fixture catalog + cards (no qualify run needed) and
assert on the produced HTML: the index hero + KPIs + dataviz, the catalog listing + tier badges, one
detail page per dataset, the load-bearing tier gating (anonymized leaks no original name/description,
private serves no byte download, no dataset bytes written), and the cardless "card pending" state.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import yaml

from nirs4all_datasets.site import build_site, charts, pages
from nirs4all_datasets.site.model import DatasetView


# =============================================================================
# Fixture catalog builders (write artifacts directly — the site is pure render)
# =============================================================================
def _entry(dataset_id: str, *, tier: str = "public", domain: str = "corn", family: str = "NIR", n_targets: int = 1, n_sources: int = 1, has_card: bool = True, is_stale: bool = False, license: str = "CC-BY-4.0") -> dict[str, Any]:
    return {
        "id": dataset_id,
        "name": dataset_id.replace("_", " ").title(),
        "domain": domain,
        "tier": tier,
        "license": license,
        "content_version": "1.0.0",
        "schema_protocol": "2.0",
        "spectro_family": family,
        "modalities": [family],
        "n_sources": n_sources,
        "source_ids": [f"X{i + 1}" for i in range(n_sources)],
        "n_features_total": 700,
        "alignment_level": "sample",
        "n_targets": n_targets,
        "targets": [f"t{i}" for i in range(n_targets)],
        "n_metadata": 1,
        "has_split": True,
        "splits": ["cv"],
        "n_samples": 80,
        "doi": "10.5281/zenodo.1" if tier == "public" else None,
        "origin_kinds": ["zenodo"],
        "origin_access": ["open"],
        "n_publications": 1,
        "has_card": has_card,
        "is_stale": is_stale,
        "publishable": tier == "public",
        "health": {"degraded": False, "alive": True},
    }


def _card(dataset_id: str, *, name: str, description: str, target_name: str, family: str = "NIR", n_sources: int = 1) -> dict[str, Any]:
    sources = [
        {
            "source_id": f"X{i + 1}", "instrument_name": f"Spectro {i + 1}", "modality": family,
            "axis_unit": "nm", "axis_min": 1100.0, "axis_max": 2498.0, "n_observations": 80, "n_variables": 700,
            "spectral": {
                "value_min": 0.0, "value_max": 1.2, "mean_min": 0.1, "mean_max": 0.9, "n_outliers": 3,
                "pca": {"n_components": 3, "explained_variance_ratio": [0.8, 0.15, 0.05]},
                "quality": {"noise_proxy_db": 35.0, "smoothness": 0.01, "dynamic_range": 0.8, "saturation_fraction": 0.0},
                "spacing": {"mean": 2.0, "std": 0.0, "min": 2.0, "max": 2.0, "median": 2.0, "is_uniform": True},
                "dimensionality": {"effective_rank": 1.5, "n_components_95": 2, "n_components_99": 3, "cumulative_top10": 1.0},
                "profile": {
                    "integrity": {"nan_ratio": 0.0, "inf_count": 0, "finite_ratio": 1.0, "zero_ratio": 0.0, "zero_column_ratio": 0.0},
                    "amplitude": {"mean_reflectance": 0.4, "area_under_curve": 560.0, "peak_to_peak": 0.8, "variance": 0.04},
                    "noise": {"noise_rms": 0.002, "snr": 200.0, "snr_db": 46.0, "bandwise_snr_min": 80.0, "bandwise_snr_median": 150.0, "worst_band_index": 2, "worst_band_axis": 1500.0},
                    "artefacts": {"spike_count": 2, "spike_rate": 0.001, "jump_count": 1, "jump_rate": 0.0005, "clip_fraction": 0.0},
                    "shape": {"baseline_slope": 0.02, "curvature_rms": 0.001, "d1_rms": 0.01, "edge_noise_ratio": 1.2},
                    "outliers": {"pca_q_median": 0.1, "pca_q_p95": 0.7, "pca_q_max": 1.0, "pca_q_ratio": 7.0, "hotelling_t2_median": 1.0, "hotelling_t2_p95": 4.0, "hotelling_t2_max": 5.0, "hotelling_t2_ratio": 4.0, "mahalanobis_h_median": 1.0, "mahalanobis_h_p95": 2.0, "mahalanobis_h_max": 2.5, "mahalanobis_h_ratio": 2.0},
                    "reference": {"rms_to_mean_spectrum": 0.02, "rms_to_mean_spectrum_p95": 0.09, "sam_to_mean_spectrum": 0.01, "sam_to_mean_spectrum_p95": 0.06, "affine_offset_median": 0.0, "affine_offset_p95_abs": 0.02, "affine_gain_median": 1.0, "affine_gain_p95_abs_delta": 0.05, "affine_residual_rms_median": 0.01, "affine_residual_rms_p95": 0.03, "peak_position_std": 1.0, "xcorr_lag_p95_features": 2.0, "xcorr_lag_p95_axis": 4.0},
                    "repeatability": {"n_repeat_groups": 5, "rms_intra_id": 0.01, "sam_intra_id": 0.02, "cv_intra_id": 0.03, "distance_to_centroid_p95": 0.03},
                    "structure": {"pca_score_density": 4.0, "local_outlier_factor_p95": 1.4, "isolation_forest_score_p95": None, "density_cv": 0.2},
                    "profile_scores": {"integrity_risk": 0.0, "noise_risk": 0.1, "local_artefact_risk": 0.2, "shape_drift": 0.15, "outlier_pressure": 0.7, "reference_spread": 0.25, "repeatability_risk": 0.2, "structure_complexity": 0.25},
                    "diagnostics": [{"key": "splice", "label": "Splice / raccord détecteurs", "score": 0.62, "strength": "moyenne", "evidence": [{"signal": "PCA Q", "level": 0.7}], "interpretation": "Rupture aux jonctions de détecteurs."}],
                },
                "score_plot": {"explained_variance_ratio": [0.8, 0.15], "points": [{"x": -1.0, "y": 0.2}, {"x": 0.0, "y": -0.1}, {"x": 1.0, "y": 0.3}]},
                "xy": [{"target": target_name, "n": 80, "max_abs_corr": 0.82, "argmax_axis": 1300.0, "mean_abs_corr": 0.31, "frac_abs_corr_gt_0_5": 0.2, "curve": {"axis": [1100.0, 1300.0, 1500.0], "corr": [0.1, 0.82, -0.2], "abs_corr": [0.1, 0.82, 0.2]}}],
                "curve": {"axis": [1100.0, 1300.0, 1500.0], "q05": [0.1, 0.2, 0.15], "q25": [0.2, 0.3, 0.25], "median": [0.3, 0.4, 0.35], "q75": [0.4, 0.5, 0.45], "q95": [0.5, 0.6, 0.55], "mean": [0.3, 0.4, 0.35]},
            },
            "assets": [],
        }
        for i in range(n_sources)
    ]
    return {
        "schema_version": "2.0", "protocol_version": "1.0",
        "identity": {"id": dataset_id, "name": name, "domain": "corn", "tier": "public", "description": description, "keywords": ["corn", "nir-secret-keyword"]},
        "versions": {"content": "1.0.0", "schema_protocol": "2.0"},
        "alignment": {"level": "sample", "sample_id_available": True, "n_samples": 80, "n_observations_total": 160, "reps_per_sample": {"min": 2, "max": 2, "mean": 2.0}, "profile_scores": {"integrity_risk": 0.0, "noise_risk": 0.1, "local_artefact_risk": 0.2, "shape_drift": 0.15, "outlier_pressure": 0.7, "reference_spread": 0.25, "repeatability_risk": 0.2, "structure_complexity": 0.25}},
        "sources": sources,
        "variables": [
            {"name": target_name, "role": "target", "type": "numeric", "unit": "%", "stats": {"n": 80, "n_missing": 0, "min": 3.0, "max": 9.0, "mean": 6.1, "std": 1.2, "median": 6.0, "q1": 5.0, "q3": 7.0}, "histogram": {"edges": [3.0, 5.0, 7.0, 9.0], "counts": [20, 40, 20]}, "assets": []},
            {"name": "variety", "role": "metadata", "type": "categorical", "unit": None, "stats": {"n": 80, "n_missing": 0, "n_classes": 3, "top_classes": [{"name": "a", "count": 40}]}, "assets": []},
        ],
        "splits": [{"name": "cv", "applied": False, "partitions": {"train": 60, "test": 20}}],
        "provenance": {"contributor": "Secret Lab", "reference_method": "Kjeldahl", "conversion_status": "complete", "origin_sources": [{"kind": "zenodo", "locator": "10.5281/zenodo.1", "access": "open", "license": "CC-BY-4.0", "title": "Origin title"}], "publications": [{"doi": "10.1038/s41586-020-0", "title": "Paper", "year": 2020}], "warnings": []},
        "integrity": {"content_hash": "abc123def456789a", "processing_hash": "p" * 40, "metadata_hash": "m" * 40, "manifest": "manifest.json"},
        "governance": {"license": "CC-BY-4.0", "tier": "public", "permitted_use": "research", "access_policy": "open", "redistribution_rights": "open under CC-BY-4.0"},
        "assets": {"sources": {f"X{i + 1}": [f"assets/X{i + 1}/spectra_envelope.png"] for i in range(n_sources)}, "variables": [f"assets/variables/{target_name}.png", "assets/variables/variety.png"]},
        "warnings": [],
    }


def _write_dataset(root: Path, dataset_id: str, card: dict[str, Any] | None, *, anon: dict[str, Any] | None = None, n_sources: int = 1) -> None:
    dd = root / "datasets" / dataset_id
    (dd / "assets").mkdir(parents=True)
    png = b"\x89PNG\r\n\x1a\n"
    for i in range(n_sources):
        (dd / "assets" / f"X{i + 1}").mkdir()
        (dd / "assets" / f"X{i + 1}" / "spectra_envelope.png").write_bytes(png)
    (dd / "assets" / "variables").mkdir()
    if card:
        for v in card["variables"]:
            (dd / "assets" / "variables" / f"{v['name']}.png").write_bytes(png)
        (dd / "card.json").write_text(json.dumps(card), encoding="utf-8")
        (dd / "croissant.json").write_text("{}", encoding="utf-8")
        # a stray canonical parquet that must NEVER be copied into the site
        (dd / "canonical").mkdir()
        (dd / "canonical" / "X1.parquet").write_bytes(b"PARQUET-BYTES")
    if anon:
        (dd / "card.anon.json").write_text(json.dumps(anon), encoding="utf-8")


def _build_fixture(tmp_path: Path) -> Path:
    """A 4-dataset fixture: public, private, anonymized, and a cardless entry."""
    from nirs4all_datasets.qualify.anonymize import anonymize_card

    root = tmp_path
    (root / "catalog" / "datasets").mkdir(parents=True)

    pub = _card("corn_oil", name="Corn — oil", description="Public corn oil dataset.", target_name="oil")
    _write_dataset(root, "corn_oil", pub)

    prv = _card("wheat_protein", name="Wheat — protein", description="Private wheat protein dataset.", target_name="protein", n_sources=2)
    _write_dataset(root, "wheat_protein", prv, n_sources=2)

    # The qualify stage writes card.json ALREADY anonymized for the anonymized tier, so the fixture's
    # tracked card.json IS the anon card (no separate card.anon.json) -- the site reads card.json for all tiers.
    ano_full = _card("grass_secret", name="Grass — SECRETNAME", description="Top secret grass description.", target_name="MOISTURE_SECRET")
    _write_dataset(root, "grass_secret", anonymize_card(ano_full))

    entries = [
        _entry("corn_oil", tier="public"),
        _entry("wheat_protein", tier="private", domain="wheat", n_sources=2),
        _entry("grass_secret", tier="anonymized", domain="grass"),
        _entry("nocard", tier="public", domain="soil", has_card=False, license="LicenseRef-not-cleared"),
    ]
    summary = {
        "n_datasets": 4, "n_with_card": 3, "n_stale": 0, "n_publishable": 2, "n_multi_source": 1,
        "n_with_targets": 4, "n_metadata_only": 0, "n_with_split": 4, "n_degraded": 0,
        "by_tier": {"public": 2, "private": 1, "anonymized": 1},
        "by_spectro_family": {"NIR": 4}, "by_domain": {"corn": 1, "wheat": 1, "grass": 1, "soil": 1},
        "license_mix": {"CC-BY-4.0": 3, "LicenseRef-not-cleared": 1}, "origin_kinds": {"zenodo": 4},
        "samples": {"min": 80, "median": 80, "max": 80, "total": 320},
        "features": {"min": 700, "median": 700, "max": 700, "total": 2800},
        "total_sources": 5, "total_targets": 4, "total_publications": 4,
    }
    catalog = {"schema_version": "2.0", "n_datasets": 4, "summary": summary, "datasets": entries}
    (root / "catalog" / "datasets.yaml").write_text(yaml.safe_dump(catalog, sort_keys=False), encoding="utf-8")
    return root


# =============================================================================
# Tests
# =============================================================================
def test_index_has_hero_kpis_and_dataviz(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "hero-spectra" in index and "wave-dots" in index  # lifted spectral-wave hero
    assert "kpi-v" in index  # KPI strip rendered
    assert ">320<" in index or "320" in index  # total samples KPI value
    # multiple inline SVG charts, each accessible
    assert index.count('role="img"') >= 5
    for label in ("Datasets by domain", "Datasets by access tier", "Wavelength coverage by family", "Samples versus features"):
        assert f'aria-label="{label}"' in index
    assert "data-goatcounter-settings='{\"path\": \"/datasets\"}'" in index


def test_catalog_lists_all_datasets_with_tier_badges(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "catalog.html").read_text(encoding="utf-8")
    for did in ("corn_oil", "wheat_protein", "grass_secret", "nocard"):
        assert f"dataset/{did}.html" in page
    assert "tier-public" in page and "tier-private" in page and "tier-anonymized" in page
    assert 'id="cards"' in page and 'data-tier=' in page  # filter UI present


def test_dataset_page_per_dataset(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    for did in ("corn_oil", "wheat_protein", "grass_secret", "nocard"):
        assert (out / "dataset" / f"{did}.html").exists()
    public = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "Corn — oil" in public
    assert "Dataset property explorer" in public and "Spectral sources" in public and "Provenance" in public
    assert "Metric interpretation reference" in public and "PCA Q (SPE)" in public
    assert "Computed metric scores" in public and "Interprétation dataset" in public
    assert "count(isnan(X)) / X.size" in public
    assert "Bug-hunting / supervised audits" in public and "Label bugs" in public
    assert "X-Y spectral correlation" in public and "PCA score plot" in public
    assert "get(&quot;corn_oil&quot;)" in public  # load snippet (HTML-escaped quotes)


def test_chart_axes_use_nice_ticks_not_raw_bounds() -> None:
    svg = charts.xy_correlation_curve({
        "curve": {
            "axis": [0.1434751235423145, 0.171, 0.206, 0.25788421234],
            "corr": [0.1, 0.2, -0.1, 0.3],
            "abs_corr": [0.1, 0.2, 0.1, 0.3],
        }
    })
    assert "0.15" in svg and "0.20" in svg and "0.25" in svg
    assert "0.1434751235423145" not in svg


def test_singleton_categorical_variables_skip_useless_barplot() -> None:
    view = DatasetView(
        entry={"id": "d"},
        tier="public",
        card={},
        has_card=True,
        show_value_stats=True,
        show_variable_plots=True,
        show_byte_download=False,
        show_metadata_downloads=True,
        asset_dataset_id="d",
    )
    html = pages._variable_card(  # noqa: SLF001 - focused rendering regression
        view,
        {
            "name": "sample_code",
            "role": "metadata",
            "type": "categorical",
            "unit": None,
            "stats": {
                "n": 3,
                "n_missing": 0,
                "n_classes": 3,
                "top_classes": [{"name": "a", "count": 1}, {"name": "b", "count": 1}, {"name": "c", "count": 1}],
            },
            "balance": {"normalized_entropy": 1.0, "imbalance_ratio": 1.0},
        },
    )
    assert "sample_code" in html
    assert "var-chart" not in html


def test_public_full_with_downloads(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "card.json" in page and "croissant.json" in page  # metadata downloads offered
    assert (out / "data" / "corn_oil.card.json").exists()
    assert (out / "data" / "corn_oil.croissant.json").exists()
    # visuals are inline interactive SVG (no PNG assets are copied anymore)
    assert "chart-spectra" in page and "<svg" in page and "<polygon" in page  # spectra-with-quantiles chart
    assert "var-card" in page  # per-variable distribution cards
    assert not (out / "assets").exists()


def test_private_no_byte_download_but_full_metadata(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "wheat_protein.html").read_text(encoding="utf-8")
    assert "Wheat — protein" in page
    assert "token" in page.lower()  # export-requires-token note
    # no downloadable metadata files for a private dataset
    assert not (out / "data" / "wheat_protein.card.json").exists()
    assert not (out / "data" / "wheat_protein.croissant.json").exists()
    # but interactive charts + metrics are still shown (inline SVG)
    assert "chart-spectra" in page and "<svg" in page
    assert "Spectro 1" in page  # instrument metadata shown


def test_anonymized_leaks_no_original_name_or_description(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "grass_secret.html").read_text(encoding="utf-8")
    # the original variable name, description text, contributor, and keyword must never appear
    assert "MOISTURE_SECRET" not in page
    assert "Top secret grass description" not in page
    assert "Secret Lab" not in page
    assert "nir-secret-keyword" not in page
    # masked structure is shown instead
    assert "var_001" in page
    assert "Anonymized" in page
    # no per-variable PNG assets are served for the anonymized tier
    assert not (out / "assets" / "grass_secret").exists()


def test_cardless_renders_card_pending(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "nocard.html").read_text(encoding="utf-8")
    assert "card pending" in page.lower()
    assert "soil" in page  # descriptor metadata still rendered
    assert not (out / "data" / "nocard.card.json").exists()  # no fake download


def test_no_dataset_bytes_written(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    leaked = []
    for f in out.rglob("*"):
        if not f.is_file():
            continue
        if f.suffix.lower() in {".parquet", ".csv"}:
            leaked.append(str(f.relative_to(out)))
        elif f.suffix.lower() == ".json":
            # only public card/croissant metadata under data/ is permitted (no bytes)
            if not (f.parent.name == "data" and f.name.endswith((".card.json", ".croissant.json"))):
                leaked.append(str(f.relative_to(out)))
    assert not leaked, f"dataset bytes leaked into the site: {leaked}"


def test_stale_card_renders_as_pending(tmp_path: Path) -> None:
    root = _build_fixture(tmp_path)
    cat = yaml.safe_load((root / "catalog" / "datasets.yaml").read_text())
    for e in cat["datasets"]:
        if e["id"] == "corn_oil":
            e["is_stale"] = True
    (root / "catalog" / "datasets.yaml").write_text(yaml.safe_dump(cat, sort_keys=False), encoding="utf-8")
    out = build_site(root, tmp_path / "site")
    page = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "card pending" in page.lower()  # a stale card is treated as no card (never shows wrong stats)
    assert not (out / "data" / "corn_oil.card.json").exists()

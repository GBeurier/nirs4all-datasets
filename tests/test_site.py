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
from xml.etree import ElementTree

import yaml

from nirs4all_datasets.site import build_site, charts, pages
from nirs4all_datasets.site import components as C
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
    for label in ("Datasets by domain", "Datasets by access tier", "Datasets by wavelength coverage", "Samples versus features"):
        assert f'aria-label="{label}"' in index
    assert "data-goatcounter-settings='{\"path\": \"/datasets\"}'" in index
    assert '<link rel="canonical" href="https://datasets.nirs4all.org/">' in index
    assert '"@type":"DataCatalog"' in index


def test_index_provenance_follows_hero_before_bank_statistics(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    index = (out / "index.html").read_text(encoding="utf-8")
    assert index.count("Built to be <em>cited</em>") == 1
    assert index.index(C.HERO_MARKUP) < index.index("Built to be <em>cited</em>") < index.index("The bank at a glance")


def test_wavelength_coverage_uses_all_sources_and_declared_units() -> None:
    def view(*sources: dict[str, Any]) -> DatasetView:
        return DatasetView(_entry("example"), "public", {"sources": list(sources)}, True, True, True, False, True, "example")

    def source(lo: Any, hi: Any, unit: str, modality: str = "NIR") -> dict[str, Any]:
        return {"axis_min": lo, "axis_max": hi, "axis_unit": unit, "modality": modality}

    nir = source(1000, 2000, "nm")
    mir_wavenumber = source(400, 4000, "cm-1", "MIR")
    assert pages._wavelength_range_nm(mir_wavenumber) == (2500, 25000)
    assert pages._wavelength_range_nm(source(10000, 5000, "cm^-1")) == (1000, 2000)
    assert pages._wavelength_coverage([
        view(nir),
        view(mir_wavenumber),
        view(nir, mir_wavenumber),
        view(source(2499, 2501, "nm")),
        view(source(780, 2500, "nm")),
        view(source(400, 700, "nm")),
        view(source(1, 2, "none")),
        view(nir, source(1, 2, "index")),
        view(source(400, 4000, "cm-1", "Raman")),
        view(source(0, 1000, "cm-1")),
        view(source(float("nan"), 1000, "nm")),
        view(),
    ]) == {"NIR": 2, "MIR": 1, "Mixed": 2, "Other": 1, "Unclassified": 6}


def test_wavelength_coverage_has_visible_equivalent_data(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    index = (out / "index.html").read_text(encoding="utf-8")
    assert "View wavelength coverage data" in index
    assert '<th scope="row">NIR</th><td>3</td><td>75.0%</td>' in index
    assert '<th scope="row">Unclassified</th><td>1</td><td>25.0%</td>' in index
    assert "Wavenumbers are converted to nm" in index


def test_catalog_lists_all_datasets_with_tier_badges(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "catalog.html").read_text(encoding="utf-8")
    for did in ("corn_oil", "wheat_protein", "grass_secret", "nocard"):
        assert f"dataset/{did}.html" in page
    assert "tier-public" in page and "tier-private" in page and "tier-anonymized" in page
    assert 'id="cards"' in page and 'data-tier=' in page  # filter UI present
    assert '<link rel="canonical" href="https://datasets.nirs4all.org/catalog.html">' in page


def test_dataset_page_per_dataset(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    for did in ("corn_oil", "wheat_protein", "grass_secret", "nocard"):
        assert (out / "dataset" / f"{did}.html").exists()
    public = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "Corn — oil" in public
    assert "Dataset property explorer" in public and "Spectral sources" in public and "Provenance" in public
    assert "Metric interpretation reference" in public and "PCA Q (SPE)" in public
    assert "Computed metric scores" in public and "Descriptive interpretation" in public and "Possible causes to verify" in public
    assert "count(isnan(X)) / X.size" in public
    assert "Bug-hunting / supervised audits" in public and "Label bugs" in public
    assert "X-Y spectral correlation" in public and "PCA score plot" in public
    assert "get(&quot;corn_oil&quot;)" in public  # load snippet (HTML-escaped quotes)
    assert '<link rel="canonical" href="https://datasets.nirs4all.org/dataset/corn_oil.html">' in public
    assert '<meta property="og:url" content="https://datasets.nirs4all.org/dataset/corn_oil.html">' in public
    assert '"@type":"Dataset"' in public


def test_site_emits_crawl_discovery_files(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    robots = (out / "robots.txt").read_text(encoding="utf-8")
    sitemap = (out / "sitemap.xml").read_text(encoding="utf-8")
    assert "Sitemap: https://datasets.nirs4all.org/sitemap.xml" in robots
    assert "<loc>https://datasets.nirs4all.org/</loc>" in sitemap
    assert "<loc>https://datasets.nirs4all.org/catalog.html</loc>" in sitemap
    assert "<loc>https://datasets.nirs4all.org/dataset/corn_oil.html</loc>" in sitemap
    assert (out / "CNAME").read_text(encoding="utf-8").strip() == "datasets.nirs4all.org"
    assert (out / ".nojekyll").exists()


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


def test_partial_profile_from_computed_scores_is_rendered_with_values(tmp_path: Path) -> None:
    import numpy as np

    from nirs4all_datasets.qualify import metrics

    spectra = np.random.default_rng(4).normal(0.5, 0.1, (30, 20))
    profile = metrics.spectral_profile(spectra, sample_ids=[f"s{i}" for i in range(30)])
    scores = metrics.aggregate_profile_scores([profile])
    assert scores is not None and scores["repeatability_risk"] is None
    root = _build_fixture(tmp_path)
    card_path = root / "datasets" / "corn_oil" / "card.json"
    card = json.loads(card_path.read_text())
    card["alignment"]["profile_scores"] = scores
    card["sources"][0]["spectral"]["profile"] = profile
    card_path.write_text(json.dumps(card))
    out = build_site(root, tmp_path / "site")
    detail = (out / "dataset" / "corn_oil.html").read_text()
    bank = (out / "index.html").read_text()
    assert 'Corn — oil — integrity:' in detail
    assert 'Corn — oil — artefacts:' in detail
    assert 'Corn — oil — baseline:' in detail
    if scores["noise_risk"] is None:
        assert 'Corn — oil — noise:' not in detail
    else:
        assert 'Corn — oil — noise:' in detail
    assert 'Corn — oil profile</title>' not in detail
    assert 'unavailable</td>' in detail
    assert 'View profile values' in bank
    assert 'unavailable</td>' in bank


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
    assert page.index('<h2>Provenance &amp; citation</h2>') < page.index('<h2>Governance &amp; integrity</h2>') < page.index('<h2>Identity card pending</h2>')
    assert "https://doi.org/10.5281/zenodo.1" in page
    assert "LicenseRef-not-cleared" in page
    assert "Detailed origin and publication records are unavailable" in page
    assert "Detailed policies and integrity hashes are unavailable" in page
    assert not (out / "data" / "nocard.card.json").exists()  # no fake download


def test_panel_purposes_cover_overview_catalog_and_nested_detail_cards(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    index = (out / "index.html").read_text()
    assert '<h3 class="viz-h">Sample-size distribution</h3><p class="viz-sub">' in index
    assert "logarithmic bins" in index
    catalog = (out / "catalog.html").read_text()
    assert "Compare source, sample and target counts" in catalog
    assert '<h3>No matching datasets</h3><p>Reset the filters' in catalog
    for dataset_id in ("corn_oil", "wheat_protein", "grass_secret"):
        detail = (out / "dataset" / f"{dataset_id}.html").read_text()
        assert "Read the signal and variation summaries for this source." in detail
        assert "Dimensionless scores from 0 to 1 summarize each property" in detail
        assert "Look up each measured quantity" in detail
        assert "Find measurement-specific checks" in detail
        assert "Review suggested follow-up methods" in detail
        if dataset_id == "grass_secret":
            assert "Review observation and missing-value counts; numeric values are unavailable" in detail
        else:
            assert "Read the recorded value distribution and summary statistics" in detail
    assert "summary statistics in %." in (out / "dataset" / "corn_oil.html").read_text()
    assert "Review the catalog metadata below" in (out / "dataset" / "nocard.html").read_text()


def test_empty_source_and_variable_panels_keep_purpose_and_availability(tmp_path: Path) -> None:
    root = _build_fixture(tmp_path)
    card_path = root / "datasets" / "corn_oil" / "card.json"
    card = json.loads(card_path.read_text())
    card.update(sources=[{"source_id": "X1", "spectral": {}}], variables=[], alignment={}, splits=[], provenance={})
    card_path.write_text(json.dumps(card))
    out = build_site(root, tmp_path / "site")
    detail = (out / "dataset" / "corn_oil.html").read_text()
    for title in ("Sampling", "Signal &amp; quality", "Integrity &amp; artefacts", "Shape &amp; reference", "Outliers &amp; repeatability", "Dimensionality (PCA)"):
        assert f'<h4>{title}</h4><p class="panel-intro">' in detail
    assert detail.count("No values are available for this source") == 6
    assert "A spectral summary plot is unavailable" in detail
    assert "A usable two-component observation projection is unavailable" in detail
    assert "Per-component explained variance is unavailable" in detail
    assert "No target or metadata variable summaries are recorded" in detail
    assert "Observation-to-sample alignment is not recorded" in detail
    assert "No original partition summaries are recorded" in detail
    assert "Property scores and diagnostic evidence are unavailable" in detail
    assert "Origin and citation details are not recorded" in detail
    assert "metadata-only (no declared prediction targets)" not in detail


def test_empty_bank_and_missing_source_lists_keep_titled_explanations(tmp_path: Path) -> None:
    assert '<h3 class="viz-h">Bank statistics unavailable</h3><p class="viz-sub">' in pages._dataviz({}, [])
    root = _build_fixture(tmp_path)
    card_path = root / "datasets" / "corn_oil" / "card.json"
    card = json.loads(card_path.read_text())
    card["sources"] = []
    card_path.write_text(json.dumps(card))
    out = build_site(root, tmp_path / "site")
    detail = (out / "dataset" / "corn_oil.html").read_text()
    assert '<h2>Spectral sources</h2><div class="panel-body"><p class="panel-intro">' in detail
    assert "No spectral source summaries are recorded" in detail


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
    assert page.index('<h2>Provenance &amp; citation</h2>') < page.index('<h2>Governance &amp; integrity</h2>') < page.index('<h2>Identity card pending</h2>')
    assert "https://doi.org/10.5281/zenodo.1" in page
    assert "Secret Lab" not in page  # never use stale card provenance
    assert not (out / "data" / "corn_oil.card.json").exists()


def test_anonymized_pending_provenance_uses_no_identifying_card_details(tmp_path: Path) -> None:
    root = _build_fixture(tmp_path)
    catalog_path = root / "catalog" / "datasets.yaml"
    catalog = yaml.safe_load(catalog_path.read_text())
    for entry in catalog["datasets"]:
        if entry["id"] == "grass_secret":
            entry["is_stale"] = True
    catalog_path.write_text(yaml.safe_dump(catalog))
    card_path = root / "datasets" / "grass_secret" / "card.json"
    card_path.write_text(json.dumps(_card("grass_secret", name="SECRETNAME", description="Secret description", target_name="SECRET_TARGET")))
    out = build_site(root, tmp_path / "site")
    page = (out / "dataset" / "grass_secret.html").read_text()
    for text in ("SECRETNAME", "Secret description", "SECRET_TARGET", "Secret Lab", "Kjeldahl", "Origin title"):
        assert text not in page
    assert page.count('<h2>Provenance &amp; citation</h2>') == 1
    assert page.count('<h2>Governance &amp; integrity</h2>') == 1
    assert "Detailed origin and publication records are unavailable" in page
    assert not (out / "data" / "grass_secret.card.json").exists()


def test_intrinsic_profile_renders_external_checks_and_exact_provider_context():
    from nirs4all_datasets.qualify import metrics

    profile = {"diagnostics": metrics.diagnostic_hypotheses({}), "producer": {"name": "nirs4all-preflight", "engine_version": "0.1.0", "protocol_version": "1", "population_id": "development_real", "context_id": "intrinsic/masked/v1", "view_id": "native"}}
    view = DatasetView(entry={"id": "d"}, tier="public", card={"sources": [{"source_id": "X", "spectral": {"profile": profile}}]}, has_card=True, show_value_stats=True, show_variable_plots=False, show_byte_download=False, show_metadata_downloads=True, asset_dataset_id="d")
    html = pages._profile_panel(view)
    assert "white/black reference actually acquired" in html
    assert "intrinsic/masked/v1" in html and "development_real" in html and "nirs4all-preflight" in html
    assert "0.78 does not mean a 78%" in html


def test_diagnostic_chart_keeps_full_real_labels_separate_and_inside_canvas() -> None:
    from nirs4all_datasets.qualify import metrics

    diagnostics = metrics.diagnostic_hypotheses({}, domain_context="VERA25")
    for item in diagnostics:
        item["score"] = 0.62
    svg = ElementTree.fromstring(charts.diagnostic_bars(diagnostics, top_n=len(diagnostics)))
    height = float(svg.attrib["viewBox"].split()[3])
    labels = [text for text in svg.findall("text") if text.find("tspan") is not None]
    assert ["".join(text.itertext()) for text in labels] == [item["label"] for item in diagnostics]
    previous_bottom = 30.0
    for text in labels:
        positions = [float(span.attrib["y"]) for span in text.findall("tspan")]
        assert min(positions) - previous_bottom >= 17
        assert max(positions) < height - 8
        previous_bottom = max(positions)


def test_dataset_explanations_order_and_legacy_diagnostic_language(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    html = (out / "dataset" / "corn_oil.html").read_text()
    assert html.index('<h2>Provenance &amp; citation</h2>') < html.index('<h2>Governance &amp; integrity</h2>') < html.index('<h2>Dataset property explorer</h2>')
    assert 'aria-label="Explain PCA Q p95/median"' in html
    assert 'View plotted PCA coordinates' in html
    assert 'View explained variance values' in html
    assert 'Principal component analysis (PCA)' in html
    assert 'without using targets' in html
    # The fixture deliberately contains old French diagnostics; display must use current English.
    for text in ('raccord détecteurs', 'Rupture aux jonctions', 'moyenne', 'Interprétation', 'Famille'):
        assert text not in html
    assert 'different probe' in html
    assert 'class="diagnostic-scroll" role="region" aria-label="Diagnostic hypotheses chart, horizontally scrollable" tabindex="0"' in html
    assert 'On narrow screens, scroll the chart horizontally.' in html
    assert '<caption>Diagnostic hypotheses and supporting evidence</caption>' in html
    assert '<th>Signature compatible with a spectral splice<small>X1</small></th>' in html
    assert '.explorer-grid > div { min-width: 0; }' in html
    assert '.diagnostic-scroll { max-width: 100%; overflow-x: auto;' in html
    assert '.diagnostic-scroll .diag-chart { min-width: 520px; }' in html


def test_pca_score_panel_interprets_saved_variance_and_source_scope() -> None:
    source = _card("corn", name="Corn", description="Corn spectra", target_name="oil")["sources"][0]
    source["name"] = "Instrument <one>"
    # Adjacent scree values describe a separate projection and must not supply this summary.
    source["spectral"]["pca"]["explained_variance_ratio"] = [0.2, 0.1]
    html = pages._pca_score_panel(source)
    assert "Source Instrument &lt;one&gt;: 3 of 80 source observations are plotted." in html
    assert "PC1 captures 80.0% and PC2 15.0%" in html
    assert "95.0% together; 5.0% remains outside this view." in html
    assert "horizontal PC1 axis" in html and "vertical PC2" in html
    assert "not wavelengths or target values" in html
    assert "separate groups or isolated dots are leads to inspect" in html
    assert "cannot identify groups" in html
    assert "selection method are not supplied" in html
    assert "at most 800" not in html
    assert '<caption>Plotted observation positions (not original sample IDs)</caption>' in html
    assert '<td>1</td><td>-1</td><td>0.2</td>' in html


def test_pca_score_panel_handles_unavailable_variance_without_inventing_coverage() -> None:
    source = _card("corn", name="Corn", description="Corn spectra", target_name="oil")["sources"][0]
    source.pop("n_observations")
    for ev in ([], [0.8], [0.8, None], [float("nan"), 0.1], [-0.1, 0.2], [0.8, 0.5], [True, 0]):
        source["spectral"]["score_plot"]["explained_variance_ratio"] = ev
        html = pages._pca_score_panel(source)
        assert "Source X1: 3 plotted observations." in html
        assert "Explained variance is unavailable" in html
        assert "together;" not in html
        assert "PC1 (" not in html and "PC2 (" not in html
        assert "View plotted PCA coordinates" in html


def test_pca_score_panel_filters_invalid_coordinates_and_omits_unusable_clouds() -> None:
    source = _card("corn", name="Corn", description="Corn spectra", target_name="oil")["sources"][0]
    points = source["spectral"]["score_plot"]["points"]
    points.extend([None, {"x": float("nan"), "y": 0}, {"x": 1, "y": True}])
    html = pages._pca_score_panel(source)
    assert "3 of 80 source observations" in html
    assert html.count('<circle ') == 3
    points.pop(0)
    assert pages._pca_score_panel(source) == ""
    source["spectral"].pop("score_plot")
    assert pages._pca_score_panel(source) == ""


def test_guide_is_linked_and_documents_missing_scores_and_pca(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    guide = (out / 'guide.html').read_text()
    for anchor in ('access', 'pca', 'scores', 'glossary'):
        assert f'id="{anchor}"' in guide
    assert 'different row samples' in guide
    assert 'does not mean a 78% causal probability' in guide
    assert 'A dash or “unavailable”' in guide
    assert '<loc>https://datasets.nirs4all.org/guide.html</loc>' in (out / 'sitemap.xml').read_text()
    assert 'href="../guide.html"' in (out / 'dataset' / 'corn_oil.html').read_text()


def test_computed_metric_help_covers_every_row_and_preserves_native_disclosure() -> None:
    from nirs4all_datasets.qualify import metrics
    from nirs4all_datasets.site.explanations import COMPUTED_METRIC_HELP

    panel = ElementTree.fromstring(pages._metric_scores_panel({}))
    rows = panel.findall(".//tbody/tr")
    catalog = metrics.metric_catalog()
    assert len(rows) == len(catalog) > 0
    for row, metric in zip(rows, catalog, strict=True):
        key = metric.get("legacy_key") or metric["key"]
        assert key in COMPUTED_METRIC_HELP
        help_control = row.find("td[2]/details[@class='metric-help']")
        assert help_control is not None and "open" not in help_control.attrib
        trigger = help_control.find("summary")
        assert trigger is not None and trigger.text == "?"
        assert trigger.attrib["aria-label"] == f'Explain {metric["metric"]}'
        explanation = help_control.find("span")
        assert explanation is not None and explanation.text
        assert COMPUTED_METRIC_HELP[key] in explanation.text
        assert (metric["score_note"].rstrip(".") or "No alert mapping is defined") in explanation.text
        assert "not a fault probability" in explanation.text
        assert "A dash means unavailable" in explanation.text
        assert "aria-hidden" not in explanation.attrib


def test_computed_metric_help_escapes_content(monkeypatch: Any) -> None:
    from nirs4all_datasets.qualify import metrics

    row = metrics.metric_score_rows({})[0]
    row.update(metric='<img src=x onerror="alert(1)">', score_note='a "quoted" rule: X < 1 & X > 0')
    monkeypatch.setattr(metrics, "metric_score_rows", lambda _: [row])
    panel = ElementTree.fromstring(pages._metric_scores_panel({}))
    trigger = panel.find(".//details[@class='metric-help']/summary")
    assert trigger is not None and trigger.attrib["aria-label"] == f'Explain {row["metric"]}'
    assert panel.find(".//img") is None
    explanation = panel.find(".//details[@class='metric-help']/span")
    assert explanation is not None and 'X < 1 & X > 0' in (explanation.text or "")


def test_private_tier_with_open_source_uses_raw_retrieval_without_token(tmp_path: Path) -> None:
    root = _build_fixture(tmp_path)
    catalog_path = root / 'catalog' / 'datasets.yaml'
    catalog = yaml.safe_load(catalog_path.read_text())
    entry = next(e for e in catalog['datasets'] if e['id'] == 'wheat_protein')
    entry.update(retrieval_status='missing_delegate', retrieval_public_retrievable=True, retrieval_public_redistributable=False, retrieval_route_count=1)
    catalog_path.write_text(yaml.safe_dump(catalog))
    out = build_site(root, root / 'site')
    html = (out / 'dataset' / 'wheat_protein.html').read_text()
    assert 'Original source available without a Dataverse token' in html
    assert 'retrieve(&quot;wheat_protein&quot;, prepare=False)' in html
    assert 'get(&quot;wheat_protein&quot;, token=' not in html
    assert 'raw source available · assembly incomplete' in html
    assert 'data-access="open"' in (out / 'catalog.html').read_text()
    # Source availability must never publish restricted card downloads or change the recorded tier.
    assert not (out / 'data' / 'wheat_protein.card.json').exists()
    assert entry['tier'] == 'private'


def test_open_origin_without_raw_route_does_not_advertise_implemented_download() -> None:
    from nirs4all_datasets.site.components import load_snippet

    html = load_snippet('d', 'private', open_retrieval=True, retrieval_status='missing_delegate', raw_route_available=False)
    assert 'Automatic retrieval is not implemented' in html
    assert 'retrieve(' not in html and 'token=' not in html

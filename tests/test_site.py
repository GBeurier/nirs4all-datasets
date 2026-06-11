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

from nirs4all_datasets.site import build_site


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
            "spectral": {"value_min": 0.0, "value_max": 1.2, "mean_min": 0.1, "mean_max": 0.9, "n_outliers": 3, "pca": None},
            "assets": [f"assets/X{i + 1}/spectra_envelope.png"],
        }
        for i in range(n_sources)
    ]
    return {
        "schema_version": "2.0", "protocol_version": "1.0",
        "identity": {"id": dataset_id, "name": name, "domain": "corn", "tier": "public", "description": description, "keywords": ["corn", "nir-secret-keyword"]},
        "versions": {"content": "1.0.0", "schema_protocol": "2.0"},
        "alignment": {"level": "sample", "sample_id_available": True, "n_samples": 80, "n_observations_total": 160, "reps_per_sample": {"min": 2, "max": 2, "mean": 2.0}},
        "sources": sources,
        "variables": [
            {"name": target_name, "role": "target", "type": "numeric", "unit": "%", "stats": {"n": 80, "n_missing": 0, "min": 3.0, "max": 9.0, "mean": 6.1, "std": 1.2, "median": 6.0, "q1": 5.0, "q3": 7.0}, "assets": [f"assets/variables/{target_name}.png"]},
            {"name": "variety", "role": "metadata", "type": "categorical", "unit": None, "stats": {"n": 80, "n_missing": 0, "n_classes": 3, "top_classes": [{"name": "a", "count": 40}]}, "assets": ["assets/variables/variety.png"]},
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

    ano_full = _card("grass_secret", name="Grass — SECRETNAME", description="Top secret grass description.", target_name="MOISTURE_SECRET")
    ano = anonymize_card(ano_full)
    _write_dataset(root, "grass_secret", ano_full, anon=ano)

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
    for label in ("Datasets by domain", "Datasets by access tier", "Wavelength coverage by dataset"):
        assert f'aria-label="{label}"' in index


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
    assert "Spectral sources" in public and "Provenance" in public
    assert "get(&quot;corn_oil&quot;)" in public  # load snippet (HTML-escaped quotes)


def test_public_full_with_downloads(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "corn_oil.html").read_text(encoding="utf-8")
    assert "card.json" in page and "croissant.json" in page  # metadata downloads offered
    assert (out / "data" / "corn_oil.card.json").exists()
    assert (out / "data" / "corn_oil.croissant.json").exists()
    assert (out / "assets" / "corn_oil" / "X1" / "spectra_envelope.png").exists()  # spectra plot copied


def test_private_no_byte_download_but_full_metadata(tmp_path: Path) -> None:
    out = build_site(_build_fixture(tmp_path), tmp_path / "site")
    page = (out / "dataset" / "wheat_protein.html").read_text(encoding="utf-8")
    assert "Wheat — protein" in page
    assert "token" in page.lower()  # export-requires-token note
    # no downloadable metadata files for a private dataset
    assert not (out / "data" / "wheat_protein.card.json").exists()
    assert not (out / "data" / "wheat_protein.croissant.json").exists()
    # but plots + metrics are still shown
    assert (out / "assets" / "wheat_protein" / "X1" / "spectra_envelope.png").exists()
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

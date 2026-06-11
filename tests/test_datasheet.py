"""Tests for the Datasheets-for-Datasets renderer (pure card+descriptor -> Markdown, no nirs4all in the asserts)."""
from __future__ import annotations

from typing import Any

from nirs4all_datasets.qualify.datasheet import render_datasheet
from nirs4all_datasets.qualify.profile import qualify

_SECTIONS = [
    "## Motivation",
    "## Composition",
    "## Collection process",
    "## Preprocessing",
    "## Uses",
    "## Distribution",
    "## Maintenance",
]


def test_render_datasheet_has_sections_variables_and_tier(canonical_dataset: Any) -> None:
    """The datasheet has the Gebru sections, a Sources table, the variables, and the tier wording."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1", "X2"), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    md = render_datasheet(card, desc)
    assert md.strip()  # non-empty

    for section in _SECTIONS:
        assert section in md
    assert "### Sources (X)" in md
    for source in desc.sources:
        assert source.source_id in md  # each source row appears
    for var in desc.variables:
        assert var.name in md  # Moisture, variety
    # Tier wording: the visibility tier and its one-line distribution policy.
    assert desc.tier.value in md
    assert "redistributable" in md  # from the tier-wording line


def test_render_datasheet_links_publications(canonical_dataset: Any) -> None:
    """Related publications are rendered as resolvable DOI links."""
    dataset_dir, desc = canonical_dataset("corn", blocks=("X1",), sample_of={"o1": "s1", "o2": "s2"})
    card = qualify(dataset_dir, desc, compute_assets=False, compute_pca=False)

    md = render_datasheet(card, desc)
    assert "### Related publications" in md
    for pub in desc.publications:
        assert pub.doi and f"https://doi.org/{pub.doi}" in md

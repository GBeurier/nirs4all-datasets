"""Focused guards for residual public-source raw retrieval routes."""
from __future__ import annotations

from pathlib import Path

import yaml

from nirs4all_datasets.schema import DatasetDescriptor, RetrievalMethod, RetrievalProvider, RetrievalStatus

ROOT = Path(__file__).resolve().parents[1]


def _descriptor(dataset_id: str) -> DatasetDescriptor:
    path = ROOT / "catalog" / "datasets" / f"{dataset_id}.yaml"
    return DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))


def test_openspecy_raw_routes_are_machine_retrievable() -> None:
    for dataset_id, modality in [("openspecy_ftir", "FTIR"), ("openspecy_raman", "RAMAN")]:
        descriptor = _descriptor(dataset_id)
        route = descriptor.retrieval.routes[0]
        resource = route.resources[0]

        assert descriptor.retrieval.status is RetrievalStatus.RAW_REPRODUCIBLE
        assert descriptor.retrieval.public_retrievable is True
        assert descriptor.retrieval.blockers == []
        assert route.method is RetrievalMethod.RAW_RETRIEVE
        assert route.provider is RetrievalProvider.URL
        assert route.redistribution_allowed is False
        assert route.canonicalization is not None
        assert route.canonicalization.engine.value == "nirs4all_formats"
        assert route.canonicalization.delegate == "source_to_standard.py"
        assert modality in (route.canonicalization.notes or "")
        assert resource.file_name == "nobaseline.rds"
        assert resource.format.value == "openspecy_rds"
        assert resource.selector.value == "https://d2jrxerjcsjhs7.cloudfront.net/nobaseline.rds"
        assert resource.sha256 == "aa6d66a3cf2a977a5349ed5398d8025df80003fb1d7356ff4aca9f7ebc529cdf"
        assert resource.size == 25865439


def test_pnnl_quant_ir_declares_the_selected_jcamp_sources() -> None:
    descriptor = _descriptor("pnnl_quant_ir")
    route = descriptor.retrieval.routes[0]

    assert descriptor.retrieval.status is RetrievalStatus.RAW_REPRODUCIBLE
    assert descriptor.retrieval.public_retrievable is True
    assert descriptor.retrieval.public_redistributable is False
    assert descriptor.retrieval.blockers == []
    assert route.method is RetrievalMethod.RAW_RETRIEVE
    assert route.provider is RetrievalProvider.URL
    assert route.redistribution_allowed is False
    assert route.max_total_bytes == 5_000_000
    assert route.canonicalization is not None
    assert route.canonicalization.engine.value == "nirs4all_formats"
    assert route.canonicalization.delegate == "source_to_standard.py"

    resources = route.resources
    assert len(resources) == 20
    assert resources[0].file_name == "001_74_85_1_quant_ir.jdx"
    assert resources[0].selector.value == "https://webbook.nist.gov/cgi/cbook.cgi?JCAMP=C74851&Index=1&Type=IR"
    assert resources[0].sha256 == "99a38318e014ed08e19bd365f2d02744697ba6543c5d44e0695bd854cba78b26"
    assert resources[0].size == 31267
    assert resources[-1].file_name == "020_7446_09_5_quant_ir.jdx"
    assert resources[-1].selector.value == "https://webbook.nist.gov/cgi/cbook.cgi?JCAMP=C7446095&Index=2&Type=IR"
    assert resources[-1].sha256 == "b6bb057031fd45549c3912ade1c36a42fc703d6271bb6d08883549efd8c298b6"
    assert resources[-1].size == 30600

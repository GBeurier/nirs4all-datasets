"""Reproduce the public Harvard Dataverse forage spectral dataset."""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import DatasetDescriptor

_ID = "harvard_dataverse_forage_quality_visnir_manual"
_ORIGIN = "https://dataverse.harvard.edu/api/access/dataset/:persistentId"
_DOI = "doi:10.7910/DVN/XPNIQY"


def supports(dataset_id: str) -> bool:
    return dataset_id == _ID


def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    """Submit the source's optional guestbook and download its original CSV."""
    del descriptor
    guestbook = context.get_json("https://dataverse.harvard.edu/api/guestbooks/306")["data"]
    if any(guestbook.get(k) for k in ("nameRequired", "emailRequired", "institutionRequired", "positionRequired")) or any(q.get("required") for q in guestbook.get("customQuestions", [])):
        raise ValueError("Harvard Dataverse guestbook now requires user information; an anonymous download is unavailable")
    response = context.session.post(_ORIGIN, params={"persistentId": _DOI, "signed": "true", "format": "original"}, json={"guestbookResponse": {"answers": []}}, timeout=context.timeout)
    response.raise_for_status()
    signed_url = response.json()["data"]["signedUrl"]
    try:
        archive = context.download(signed_url, "harvard_forage.zip")
    except Exception:
        raise RuntimeError("Could not download the Harvard Dataverse forage source archive") from None
    context.downloads[-1]["url"] = f"{_ORIGIN}?persistentId={_DOI}"
    root = context.extract(archive)
    matches = list(root.rglob("02a. Fulldata.csv"))
    if len(matches) != 1:
        raise ValueError("Harvard Dataverse archive does not contain the expected original full-data CSV")
    table = pd.read_csv(matches[0], encoding="latin1", low_memory=False)
    target_names = ["FDN", "FDA", "DIVMS", "PC"]
    expected = ["Country", "Location", "Harvest date", *target_names]
    if table.columns[:7].tolist() != expected:
        raise ValueError("Unexpected columns in the Harvard forage full-data table")
    ids = [f"forage_{i:04d}" for i in range(1, len(table) + 1)]
    x = table.iloc[:, 7:].copy()
    x.insert(0, "observation_id", ids)
    targets = table[target_names].apply(pd.to_numeric, errors="coerce")
    targets.insert(0, "observation_id", ids)
    metadata = table.iloc[:, :3].rename(columns={"Country": "country", "Location": "location", "Harvest date": "harvest_date"})
    metadata.insert(0, "observation_id", ids)
    return context.write_tables({"X": x}, targets=targets, metadata=metadata)

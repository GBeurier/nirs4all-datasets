"""Reproduce the open Fairdata bovine ligament spectral dataset."""
from __future__ import annotations

import re
from pathlib import Path

import pandas as pd
from stream_unzip import stream_unzip

from nirs4all_datasets.public_pull.common import PullContext
from nirs4all_datasets.schema import DatasetDescriptor

_DATASET = "fairdata_bovine_knee_ligament_nir_manual"
_ID = "925999ad-8127-4428-b7cc-c03c12e62d3c"
_API = "https://etsin.fairdata.fi/api/v3/download"
_FILES = {"Data_NIRS.xlsx", "Data_biomechanics_and_biochemistry.xlsx"}


def supports(dataset_id: str) -> bool:
    return dataset_id == _DATASET


def build(descriptor: DatasetDescriptor, context: PullContext) -> Path:
    """Read the two published workbooks and join chemistry by tissue identity."""
    status = context.get_json(f"{_API}/requests", cr_id=_ID)
    if status.get("status") != "SUCCESS" or not status.get("package"):
        raise ValueError("Fairdata full archive is not yet available")
    response = context.session.post(f"{_API}/authorize", json={"cr_id": _ID, "package": status["package"]}, timeout=context.timeout)
    response.raise_for_status()
    url = response.json()["url"]
    paths: dict[str, Path] = {}
    # The source ZIP is 1.85 GB, but both required workbooks are its first
    # members. The streaming ZIP reader checks each consumed member's CRC.
    with context.session.get(url, stream=True, timeout=context.timeout) as response:
        response.raise_for_status()
        for raw_name, _size, chunks in stream_unzip(context.iter_bytes(response)):
            name = Path(raw_name.decode("utf-8")).name
            if name in _FILES:
                target = context.directory / name
                with target.open("wb") as out:
                    for chunk in chunks:
                        out.write(chunk)
                paths[name] = target
            else:
                for _ in chunks:
                    pass
            if paths.keys() >= _FILES:
                break
    if paths.keys() != _FILES:
        raise ValueError(f"Fairdata archive missing original workbooks: {sorted(_FILES - paths.keys())}")
    context.downloads.append({"url": f"{_API}/requests?cr_id={_ID}", "name": status["package"], "members": sorted(_FILES), "archive_sha256": status.get("checksum")})
    source = paths["Data_NIRS.xlsx"]
    tables = [pd.read_excel(source, sheet_name=s) for s in ("AvaSpec-ULS2048L-USB2", "AvaSpec-NIR256-2.5-HSC")]
    identities = tables[0][["id", "site"]]
    if not identities.equals(tables[1][["id", "site"]]) or identities.duplicated().any():
        raise ValueError("Fairdata instrument sources do not share unique tissue/site identities")
    ids = [f"{sample}_site{site}" for sample, site in identities.itertuples(index=False, name=None)]
    spectra = {}
    for key, table in zip(("X_AvaSpec_ULS2048L_USB2", "X_AvaSpec_NIR256_2_5_HSC"), tables, strict=True):
        x = table.iloc[:, 2:].copy()
        x.columns = [str(v) for v in x.columns]
        x.insert(0, "observation_id", ids)
        spectra[key] = x
    chemistry = pd.read_excel(paths["Data_biomechanics_and_biochemistry.xlsx"], header=10)
    chemistry = chemistry[chemistry["Property"].astype(str).str.match(r"^M\d+_")].copy()
    chemistry["key"] = chemistry["Property"].astype(str).str.strip()
    if chemistry["key"].duplicated().any():
        raise ValueError("Fairdata chemistry has duplicate tissue IDs")
    chemistry = chemistry.set_index("key")
    keys = [re.sub(r"^M0+(\d+)_", r"M\1_", str(s)) for s in identities["id"]]
    if not all(key in chemistry.index for key in keys):
        raise ValueError("Fairdata spectral tissue IDs do not match chemistry")
    target_names = [v.name for v in descriptor.targets]
    targets = chemistry.loc[keys, target_names].reset_index(drop=True)
    targets.insert(0, "observation_id", ids)
    joined = chemistry.loc[keys].reset_index(drop=True)
    metadata = pd.DataFrame({"observation_id": ids, "original_sample_id": identities["id"], "site": identities["site"], "knee_identifier": joined["Knee identifier"], "ligament_type": joined["Ligament type"]})
    return context.write_tables(spectra, targets=targets, metadata=metadata)

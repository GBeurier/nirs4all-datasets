# Datasheet — Herbarium resurvey NIRS spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Herbarium resurvey NIRS spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD herbarium

## Composition

- **Alignment:** sample level; 1229 sample(s), 2718 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 2–3 (mean 2.212).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 350–2500 nm | 2718 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=1229, missing=0, classes=1, top True (×1229) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=1229, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\herbarium (×1229) |
| manual_download_file | metadata | categorical | *Not specified.* | n=1229, missing=0, classes=1, top doi_10_5061_dryad_z34tmpgpw__v20241216.zip::Kuehn_et_al._Resurvey_-_JEcol_Open_Data.zip::*dpt (×1229) |
| official_source_url | metadata | categorical | *Not specified.* | n=1229, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.z34tmpgpw (×1229) |
| standardization_batch | metadata | categorical | *Not specified.* | n=1229, missing=0, classes=1, top v0.8.60 (×1229) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.z34tmpgpw`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: 1229 source identifiers and 1229 distinct spectral vectors for 2718 rows: each spectrum is copied into 2–3 calibration/prediction folders. The 1489 additional rows do not demonstrate repeated acquisitions.
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 8 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `67813c88bcbc4611f39cfa50697bd1f2263a266e7ac6fba94052abdcab7130ab`
- **Processing hash:** `b9700900997687889de09c317fc59420c0a4166c6e0e92e0f22f57786bebf31f` | **metadata hash:** `5bf3fa69ecad1caead0b281dfd3b8baf8f6b5f650f995069f91f18564971e28f`

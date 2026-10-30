# Datasheet — Beetle ventral transmittance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Beetle ventral transmittance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 0 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD beetle

## Composition

- **Alignment:** sample level; 56 sample(s), 56 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–1700 nm | 56 | 701 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| manual_download | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top True (×56) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\beetle (×56) |
| manual_download_file | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top doi_10_5061_dryad_7wm37pvx4__v20220916.zip::3_Transmittanceventraldata.csv (×56) |
| official_source_url | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.7wm37pvx4 (×56) |
| standardization_batch | metadata | categorical | *Not specified.* | n=56, missing=0, classes=1, top v0.8.57 (×56) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.7wm37pvx4`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Original sample identifier retained under a prefixed/equivalent name
- **Curated views:** M: 0 fields, Y: 0 fields, measurements: 0 fields, passport: 6 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `423437437956c3883324bc10d824741020a92b381aafdfa3968e36eb02ec2217`
- **Processing hash:** `67fad23096f8ceeb66d695ba811363dccf31e89e16690218ed2e0ddf39863217` | **metadata hash:** `a9f30efdcf3a0738a6d779512857709cf85c18d4fe136b901a1f7b936e2b17b5`

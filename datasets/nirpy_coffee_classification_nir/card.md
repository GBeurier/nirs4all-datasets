# Datasheet — Coffee — NIR (Nirpy)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research coffee classification NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 70 sample(s), 70 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research coffee classification NIR | *Not specified.* | NIR | 1100–2300 nm | 70 | 601 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Coffee Type | target | categorical | *Not specified.* | n=70, missing=0, classes=7, top Tauro (×10) |
| repository_url | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×70) |
| license | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top MIT License (×70) |
| license_url | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×70) |
| rights_status | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top explicit_open (×70) |
| usage_scope | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top public_reuse_possible (×70) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top True (×70) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top NIR (×70) |
| axis_unit | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top index (×70) |
| axis_min | metadata | numeric | *Not specified.* | n=70, missing=0, range 1–1, mean 1 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=70, missing=0, range 601–601, mean 601 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=70, missing=0, range 601–601, mean 601 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=70, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×70) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/coffee_classification.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; Spectral declaration for X: The dataset author's analysis specifies 1100 to 2300 nm in 2 nm steps for these 601 ordered channels. All canonical feature values match the pinned original source at float32 precision. Restore wavelength labels only for the verified standardized raw SHA-256; preserve raw indices, measured values, identities, targets and partitions. Evidence: https://nirpyresearch.com/analysis-ground-coffee-nir-spectroscopy/, https://raw.githubusercontent.com/nevernervous78/nirpyresearch/97a5d7dd1fe72472d9b3a070c53c712f16fc1e2f/data/coffee_classification.csv
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 16 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.1 | **schema/protocol:** 2.0
- **Content hash:** `7e40e9b05a9ea4b37d973eaf2ff9872f6215da347f06474feb52ea9f99a978e0`
- **Processing hash:** `025186d7153730b4e47a1acb9bb715da08ffaf2631ec3a3f4e1c744ff7ac610f` | **metadata hash:** `4998b14dc3e5f7df005e034b6ddaccaf6c596e9fa3465441b5bee95683808b55`

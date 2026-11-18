# Datasheet — Plums — Brix and firmness, NIR (Nirpy)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research plums Brix and firmness NIR. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 40 sample(s), 40 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research plums Brix and firmness NIR | *Not specified.* | NIR | 1102–2300 nm | 40 | 600 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Brix | target | numeric | *Not specified.* | n=40, missing=0, range 19.65–23.5, mean 21.86 ± 0.9559 |
| Firmness | target | numeric | *Not specified.* | n=40, missing=0, range 2.85–4.85, mean 3.924 ± 0.4442 |
| repository_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×40) |
| license | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top MIT License (×40) |
| license_url | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×40) |
| rights_status | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top explicit_open (×40) |
| usage_scope | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top public_reuse_possible (×40) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top True (×40) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top NIR (×40) |
| axis_unit | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top index (×40) |
| axis_min | metadata | numeric | *Not specified.* | n=40, missing=0, range 0–0, mean 0 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=40, missing=0, range 599–599, mean 599 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=40, missing=0, range 600–600, mean 600 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=40, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×40) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/NIRplums_brix_firmness.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; Spectral declaration for X: The dataset author's analysis specifies 1102 to 2300 nm in 2 nm steps for these 600 ordered channels. All canonical feature values match the pinned original source at float32 precision. Restore wavelength labels only for the verified standardized raw SHA-256; preserve raw indices, measured values, identities, targets and partitions. Evidence: https://nirpyresearch.com/wavelength-band-selection-with-simulated-annealing/, https://raw.githubusercontent.com/nevernervous78/nirpyresearch/97a5d7dd1fe72472d9b3a070c53c712f16fc1e2f/data/NIRplums_brix_firmness.csv
- **Curated views:** M: 0 fields, Y: 2 fields, passport: 16 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `1208f6a924115405d4cd63b28ebe3693306f6ecd3a11baa1c94fe0dd331af8b0`
- **Processing hash:** `4fac2a1cb77d2a8e71cda013194f10637f3a02fac70568bb63880dd08d1ecd82` | **metadata hash:** `157915a8c4226226a75465ced48b9967d33f556a15e0ba93ca644e2c4a21d190`

# Datasheet — CGL_NIR grain protein Eigenvector

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** cgl
- **Description:** CGL_NIR grain protein Eigenvector. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, cgl
- **Contributor:** Eigenvector data sets

## Composition

- **Alignment:** sample level; 231 sample(s), 231 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra | unknown | NIR | 1104–2496 nm | 231 | 117 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Casein_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–88.83, mean 29.61 ± 22.49 |
| Glucose_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–91.5, mean 30.5 ± 23.17 |
| Lactate_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 0–75.71, mean 25.24 ± 19.17 |
| Moisture_wt_pct | target | numeric | *Not specified.* | n=231, missing=0, range 5.3–24.29, mean 12.7 ± 4.459 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): calibration: 153, test: 78

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://eigenvector.com/wp-content/uploads/2021/04/CGL_nir.mat_.zip`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 4 fields, passport: 5 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** license unknown, redistribution not cleared
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `4f57a59a4b1af946366f9a1cc5dec22cdce9ebdcb022bbdbe8c057ca2b17aa95`
- **Processing hash:** `7526b8eab443d67866f1d3ec64c89bd6d4b1a46983f537ae9cd843e3af7c0c9a` | **metadata hash:** `0a72cfb33c599ec0b2786e76cf16540ec911aede764c313a8e9b5e30ddd1ca19`

# Datasheet — EcoSIS Varietal Discrimination and Detection of PVY in Solanum tuberosum: Hawaii 2014 (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Varietal Discrimination and Detection of PVY in Solanum tuberosum: Hawaii 2014 (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Varietal Discrimination and Detection of PVY in Solanum tuberosum: Hawaii 2014

## Composition

- **Alignment:** observation level; 761 sample(s), 761 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Hawaii_ecosis_spectra.csv | Spectra Vista Corp HR-1024i | NIR | 350–2500 nm | 761 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| row_id | target | categorical | *Not specified.* | n=761, missing=0, classes=226, top 388 (×13) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top 1d5f5b6f-9d0e-4719-a655-587f681bcc18 (×761) |
| site | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top source-provided coordinates when available (×761) |
| year | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| date | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top Leaf (×761) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top Spectra Vista Corp HR-1024i (×761) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top Contact (×761) |
| signal_type | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top reflectance (×761) |
| axis_unit | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top nm (×761) |
| axis_min | metadata | numeric | *Not specified.* | n=761, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=761, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=761, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=761, missing=761, classes=0, — |
| license | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top not specified (×761) |
| rights_status | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top manual_review_needed (×761) |
| usage_scope | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top private_use_only (×761) |
| notes | metadata | categorical | *Not specified.* | n=761, missing=0, classes=1, top EcoSIS package varietal-discrimination-and-detection-of-pvy-in-solanum-tuberosum--hawaii-2014, no interpolation applied by project. (×761) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/varietal-discrimination-and-detection-of-pvy-in-solanum-tuberosum--hawaii-2014`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS license is missing or unclear; private/internal conversion only by v0.5 policy.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `a08c61a3994dbd4860a74dc00b97760125fd2787d1624d6ca057f24c40f75f02`
- **Processing hash:** `549b868fa63cb11db22d32b7fb179104cfb609899a7bf26ceb397fcf7a623d7c` | **metadata hash:** `cc863cec0b259b8b204a6688b33a0511aca1c887c188f00d099a773d2cc10ff5`

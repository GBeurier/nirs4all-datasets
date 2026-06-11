# Datasheet — EcoSIS Spectra from in situ deciduous leaves and leaves collected for nitrogen analysis throughout autumn (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Spectra from in situ deciduous leaves and leaves collected for nitrogen analysis throughout autumn (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 11 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Spectra from in situ deciduous leaves and leaves collected for nitrogen analysis throughout autumn

## Composition

- **Alignment:** observation level; 1 sample(s), 1013 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1013–1013 (mean 1013).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | CollectedDryAutumnSpectra2016.csv | Spectral Evolution PSP1100 | NIR | 320–1100 nm | 1013 | 781 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LeafNumber | target | numeric | *Not specified.* | n=1, missing=0, range 1–1, mean 1 ± 0 |
| Species | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top Beech (×1) |
| Count | target | numeric | *Not specified.* | n=1, missing=0, range 15–15, mean 15 ± 0 |
| LeafArea_cm_2 | target | numeric | *Not specified.* | n=1, missing=0, range 591.6–591.6, mean 591.6 ± 0 |
| wetWeight_g | target | numeric | *Not specified.* | n=1, missing=0, range 3–3, mean 3 ± 0 |
| dryWeight_g | target | numeric | *Not specified.* | n=1, missing=0, range 1.39–1.39, mean 1.39 ± 0 |
| N | target | numeric | *Not specified.* | n=1, missing=0, range 2.68–2.68, mean 2.68 ± 0 |
| C | target | numeric | *Not specified.* | n=1, missing=0, range 49.03–49.03, mean 49.03 ± 0 |
| H | target | numeric | *Not specified.* | n=1, missing=0, range 6.827–6.827, mean 6.827 ± 0 |
| C/N | target | numeric | *Not specified.* | n=1, missing=0, range 18.32–18.32, mean 18.32 ± 0 |
| C/H | target | numeric | *Not specified.* | n=1, missing=0, range 7.183–7.183, mean 7.183 ± 0 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 7138fe3b-a9e2-4f45-90e2-bd4fe7340544 (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Fair Hill Natural Resource Management Area, Elkton, MD (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2016–2016, mean 2016 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Beech (×1) |
| genus | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Leaf (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Spectral Evolution PSP1100 (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Contact (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 320–320, mean 320 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 1100–1100, mean 1100 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 781–781, mean 781 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Kathryn I. Wheeler, Delphis F. Levia and Rodrigo Vargas. 2016. Spectra from in situ deciduous leaves and leaves collected for nitrogen analysis throughout autumn. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top not specified (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top manual_review_needed (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top private_use_only (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package spectra-from-in-situ-deciduous-leaves-and-leaves-collected-for-nitrogen-analysis-throughout-autumn, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/spectra-from-in-situ-deciduous-leaves-and-leaves-collected-for-nitrogen-analysis-throughout-autumn`
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
- **Content hash:** `c6cb3cb50e2bc7934dc2d62974759514fd6a28d758adcbac0ae0ee089b4b5a76`
- **Processing hash:** `768501ae7375e08d2f307d59777159b7c46be731dc82b0242950c2130b725acb` | **metadata hash:** `48bfb7b7214160be8eb1367138c6efcf2424efdba0c5e3d7e97987c11ea0ce9e`

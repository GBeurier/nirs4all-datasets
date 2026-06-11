# Datasheet — EcoSIS Common Milkweed Leaf Responses to Water Stress and Elevated Temperature (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Common Milkweed Leaf Responses to Water Stress and Elevated Temperature (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 19 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Common Milkweed Leaf Responses to Water Stress and Elevated Temperature

## Composition

- **Alignment:** observation level; 735 sample(s), 735 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Couture et al. 2015_APIS_spectra.csv | Analytical Spectral Devices Inc. FieldSpec 3 | NIR | 350–2500 nm | 735 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| N___dm | target | numeric | *Not specified.* | n=735, missing=0, range 2–5.27, mean 3.422 ± 0.5485 |
| C | target | numeric | *Not specified.* | n=735, missing=0, range 43.5–48.8, mean 45.93 ± 0.903 |
| C_N | target | numeric | *Not specified.* | n=735, missing=0, range 8.93–23.01, mean 13.78 ± 2.277 |
| Fiber___dm | target | numeric | *Not specified.* | n=735, missing=0, range 15.94–46.39, mean 31.89 ± 4.501 |
| Lignin___dm | target | numeric | *Not specified.* | n=735, missing=0, range -0.43–31.37, mean 15.75 ± 4.068 |
| LMA | target | numeric | *Not specified.* | n=735, missing=0, range 8.44–115.2, mean 55.49 ± 20.49 |
| CG___dm | target | numeric | *Not specified.* | n=735, missing=4, range 0.26–3.77, mean 1.91 ± 0.5247 |
| Vcmax | target | numeric | *Not specified.* | n=735, missing=0, range 0–183, mean 107.5 ± 33.74 |
| Trichomes__mm2 | target | numeric | *Not specified.* | n=735, missing=534, range 2.5–29.5, mean 13.24 ± 5.367 |
| L_mass__g | target | numeric | *Not specified.* | n=735, missing=464, range 0.14–7.55, mean 2.003 ± 1.484 |
| R_mass__g | target | numeric | *Not specified.* | n=735, missing=464, range 0.17–26.76, mean 4.95 ± 4.684 |
| S_mass__g | target | numeric | *Not specified.* | n=735, missing=464, range 0.07–10.7, mean 1.362 ± 1.373 |
| Total_growth__g | target | numeric | *Not specified.* | n=735, missing=464, range 0.51–38.01, mean 8.313 ± 7.137 |
| NDWI | target | numeric | *Not specified.* | n=735, missing=0, range 0–0.074, mean 0.03499 ± 0.01202 |
| ABG__g | target | numeric | *Not specified.* | n=735, missing=464, range 0.2–16.6, mean 3.365 ± 2.762 |
| Water_treatment | target | categorical | *Not specified.* | n=735, missing=0, classes=2, top ww (×384) |
| Room | target | numeric | *Not specified.* | n=735, missing=0, range 1–4, mean 2.472 ± 1.117 |
| Temperature | target | numeric | *Not specified.* | n=735, missing=0, range 23–30, mean 26.61 ± 3.501 |
| Time | target | numeric | *Not specified.* | n=735, missing=0, range 4–8, mean 5.535 ± 1.946 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top b50d44e3-f995-4b37-9f42-a88854decd44 (×735) |
| site | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top UW-Madison Biotron Laboratory (×735) |
| country | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top source-provided coordinates when available (×735) |
| year | metadata | numeric | *Not specified.* | n=735, missing=0, range 2015–2015, mean 2015 ± 0 |
| date | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=735, missing=735, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top Leaf (×735) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top leaf (×735) |
| instrument | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top Analytical Spectral Devices Inc. FieldSpec 3 (×735) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top Contact (×735) |
| signal_type | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top reflectance (×735) |
| axis_unit | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top nm (×735) |
| axis_min | metadata | numeric | *Not specified.* | n=735, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=735, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=735, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top 10.1007/s11829-015-9367-y \| 10.21232/dep7jvyq (×735) |
| citation | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top John Couture. 2015. Common Milkweed Leaf Responses to Water Stress and Elevated Temperature. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.1007/s11829-015-9367-y (×735) |
| license | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top Other (Open) (×735) |
| rights_status | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top explicit_open (×735) |
| usage_scope | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top public_reuse_possible (×735) |
| notes | metadata | categorical | *Not specified.* | n=735, missing=0, classes=1, top EcoSIS package common-milkweed-leaf-responses-to-water-stress-and-elevated-temperature, no interpolation applied by project. (×735) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/common-milkweed-leaf-responses-to-water-stress-and-elevated-temperature`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Published Paper — [10.1007/s11829-015-9367-y](https://doi.org/10.1007/s11829-015-9367-y)
- *Not specified.* — [10.21232/dep7jvyq](https://doi.org/10.21232/dep7jvyq)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `fd2c5afcbc9db88d8c4070a270c116c2642007b0769d916a87e92bbe9478902c`
- **Processing hash:** `06ceaf0b284161afd240cac7f69b1a895c99621be605a66b4944412f0863cc3b` | **metadata hash:** `71c35b7da812492b42b2689fe2ff183247dd3a7526b843886eb3a5cfc7376a87`

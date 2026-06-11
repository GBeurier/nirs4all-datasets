# Datasheet — EcoSIS FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER

## Composition

- **Alignment:** observation level; 1 sample(s), 138 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 138–138 (mean 138).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | spectra.csv | Spectral Evolution PSR+ 3500 | NIR | 350–2500 nm | 138 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| SpeciesCode | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top QUMA (×1) |
| Genus | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top Quercus (×1) |
| Species | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top macrocarpa (×1) |
| Treatment | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top Monoculture (×1) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top a3b4c504-c975-423c-9abb-0a8075cefc85 (×1) |
| site | metadata | numeric | *Not specified.* | n=1, missing=0, range 7–7, mean 7 ± 0 |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Cedar Creek LTER (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2018–2018, mean 2018 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top macrocarpa (×1) |
| genus | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Quercus (×1) |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Leaf (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top leaf (×1) |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Contact (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.1101/845701 \| 10.21232/FR7US97g (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Shan Kothari, Rebecca Montgomery and Jeannine Cavender-Bares. 2018. FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/FR7US97g (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Creative Commons Attribution (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top explicit_open (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top public_reuse_possible (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package fab-leaf-spectra-across-a-light-gradient-at-cedar-creek-lter, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fab-leaf-spectra-across-a-light-gradient-at-cedar-creek-lter`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Physiological responses to light explain competition and facilitation in a tree diversity experiment — [10.1101/845701](https://doi.org/10.1101/845701)
- FAB Leaf Spectra Across a Light Gradient at Cedar Creek LTER — [10.21232/FR7US97g](https://doi.org/10.21232/FR7US97g)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `7459f8be50df761a924bc34c4da2d28337e83bc0759a0f29009877840a94ea9a`
- **Processing hash:** `466d229d0dafaacbae817442886bcf3f5872558ca7985cb003710419a6e189d6` | **metadata hash:** `908db3924f866ba8b559a187a412e0afcc38d7b69023d53100483a355493c0b3`

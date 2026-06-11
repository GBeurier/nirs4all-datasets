# Datasheet — EcoSIS Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan

## Composition

- **Alignment:** observation level; 2399 sample(s), 2399 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | coastal grassland Belgium and Japan ITV spectra and traits.csv | spectra vista corporation, sv SVC HR-1024TM | NIR | 400–2450 nm | 2399 | 2051 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| latin_genus | target | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosa (×729) |
| latin_species | target | categorical | *Not specified.* | n=2399, missing=0, classes=4, top rugosa (×729) |
| LMA__mg/cm2 | target | numeric | *Not specified.* | n=2399, missing=0, range 1.525–13.89, mean 6.221 ± 2.649 |
| LDMC__mg/mg | target | numeric | *Not specified.* | n=2399, missing=0, range 0.0704–0.5409, mean 0.2664 ± 0.1081 |
| EWT__mg/cm2 | target | numeric | *Not specified.* | n=2399, missing=0, range 5.474–42.72, mean 18.44 ± 7.05 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top ee8fe8de-aab0-4d69-834d-bf9178e16c2a (×2399) |
| site | metadata | categorical | *Not specified.* | n=2399, missing=2399, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Oostende, Ishikari (×2399) |
| country | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=2, top Belgium (×2041) |
| latitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 43.15–51.36, mean 50.05 ± 2.858 |
| longitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2.644–141.4, mean 23.61 ± 49.31 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top source-provided coordinates when available (×2399) |
| year | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2019–2019, mean 2019 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2399, missing=2399, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top rugosa (×729) |
| genus | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosa (×729) |
| family | metadata | categorical | *Not specified.* | n=2399, missing=2399, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Leaf (×2399) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top leaf (×2399) |
| instrument | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top spectra vista corporation, sv SVC HR-1024TM (×2399) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Contact (×2399) |
| signal_type | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top reflectance (×2399) |
| axis_unit | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top nm (×2399) |
| axis_min | metadata | numeric | *Not specified.* | n=2399, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2450–2450, mean 2450 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2051–2051, mean 2051 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top 10.1016/j.ecolind.2021.108111 (×2399) |
| citation | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Kenny Helsen Leonardo Bassi Hannes Feilhauer Teja Kattenborn Hajime Matsushima Elisa Van Cleemput Ben Somers Olivier Honnay. 2019. Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×2399) |
| license | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Open Data Commons Open Database License (ODbL) (×2399) |
| rights_status | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top explicit_open (×2399) |
| usage_scope | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top public_reuse_possible (×2399) |
| notes | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top EcoSIS package leaf-spectra-of-4-plant-species-from-belgian-dune-grasslands---rosa-rugosa-from-the-northern-japan, no interpolation applied by project. (×2399) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-spectra-of-4-plant-species-from-belgian-dune-grasslands---rosa-rugosa-from-the-northern-japan`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Paper: Evaluating different methods for retrieving intraspecific leaf trait variation from hyperspectral leaf reflectance — [10.1016/j.ecolind.2021.108111](https://doi.org/10.1016/j.ecolind.2021.108111)

## Distribution

- **License:** ODbL-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `1c2e09229d87946cfb262cbf9141bd2626818fce81084704448a5b33de36775a`
- **Processing hash:** `f52f4d2fb0fda1300b2394d458db3860f5ffb7274826e895e0cf2238ce4e41ab` | **metadata hash:** `90c8aa842c7959a8f36c3246de733eea182e058af131caaaf0bc50e798178954`

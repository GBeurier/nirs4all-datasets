# Datasheet — EcoSIS Intact- and ground-leaf litter spectra from Cedar Creek and Minneapolis (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Intact- and ground-leaf litter spectra from Cedar Creek and Minneapolis (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 12 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Intact- and ground-leaf litter spectra from Cedar Creek and Minneapolis

## Composition

- **Alignment:** observation level; 322 sample(s), 322 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | intact_spec.csv | Spectral Evolution PSR+ 3500 | NIR | 400–2400 nm | 322 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| species | target | categorical | *Not specified.* | n=322, missing=0, classes=11, top QUAL (×37) |
| number | target | numeric | *Not specified.* | n=322, missing=0, range 1–30, mean 6.137 ± 6.782 |
| latin_genus | target | categorical | *Not specified.* | n=322, missing=0, classes=5, top Quercus (×137) |
| latin_species | target | categorical | *Not specified.* | n=322, missing=0, classes=11, top alba (×37) |
| solubles | target | numeric | *Not specified.* | n=322, missing=6, range 27.56–71.41, mean 51.25 ± 9.844 |
| hemicellulose | target | numeric | *Not specified.* | n=322, missing=6, range 5.723–25.97, mean 14 ± 4.001 |
| recalcitrant | target | numeric | *Not specified.* | n=322, missing=6, range 20.71–58.66, mean 34.75 ± 8.759 |
| Cmass | target | numeric | *Not specified.* | n=322, missing=0, range 40.92–61.39, mean 52.3 ± 4.017 |
| Nmass | target | numeric | *Not specified.* | n=322, missing=0, range 0.24–2.57, mean 0.9215 ± 0.4703 |
| LMA | target | numeric | *Not specified.* | n=322, missing=3, range 39.47–282, mean 115.6 ± 62.91 |
| Carea | target | numeric | *Not specified.* | n=322, missing=3, range 16.15–172.2, mean 62.18 ± 38.01 |
| Narea | target | numeric | *Not specified.* | n=322, missing=3, range 0.2723–2.431, mean 0.8684 ± 0.347 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top de3d9519-dbde-462d-bf44-433ba2c1907b (×322) |
| site | metadata | numeric | *Not specified.* | n=322, missing=205, range 4–147, mean 72.45 ± 43.4 |
| location | metadata | categorical | *Not specified.* | n=322, missing=322, classes=0, — |
| country | metadata | categorical | *Not specified.* | n=322, missing=322, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=322, missing=0, range 44.95–45.4, mean 45.38 ± 0.08537 |
| longitude | metadata | numeric | *Not specified.* | n=322, missing=0, range -93.21–-93.19, mean -93.19 ± 0.003794 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top source-provided coordinates when available (×322) |
| year | metadata | numeric | *Not specified.* | n=322, missing=0, range 2024–2024, mean 2024 ± 0 |
| date | metadata | categorical | *Not specified.* | n=322, missing=322, classes=0, — |
| genus | metadata | categorical | *Not specified.* | n=322, missing=322, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=322, missing=322, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top Leaf, Other (×322) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top leaf (×322) |
| instrument | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top Spectral Evolution PSR+ 3500 (×322) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top Contact (×322) |
| signal_type | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top reflectance (×322) |
| axis_unit | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top nm (×322) |
| axis_min | metadata | numeric | *Not specified.* | n=322, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=322, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=322, missing=0, range 2001–2001, mean 2001 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top 10.1101/2023.11.27.568939 \| 10.5061/dryad.hdr7sqvrk (×322) |
| citation | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top Shan Kothari, Sarah Hobbie and Jeannine Cavender-Bares. 2024. Intact- and ground-leaf litter spectra from Cedar Creek and Minneapolis. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). https://doi.org/10.5061/dryad.hdr7sqvrk (×322) |
| license | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top Creative Commons Attribution (×322) |
| rights_status | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top explicit_open (×322) |
| usage_scope | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top public_reuse_possible (×322) |
| notes | metadata | categorical | *Not specified.* | n=322, missing=0, classes=1, top EcoSIS package intact--and-ground-leaf-litter-spectra-from-cedar-creek-and-minneapolis, no interpolation applied by project. (×322) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/intact--and-ground-leaf-litter-spectra-from-cedar-creek-and-minneapolis`
- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.hdr7sqvrk`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- bioRxiv preprint — [10.1101/2023.11.27.568939](https://doi.org/10.1101/2023.11.27.568939)

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `e22610e570b6e676d4a2943ecbaaec9aea409cd30785af73977d0390a490fb53`
- **Processing hash:** `f178a369f9944a30499af8e256d5939608613eef9eebf8949273b02da0fa13ce` | **metadata hash:** `09e66ad9c168d356630dff8f0ceb5f616fc7cde1b43ec703b1bf56ab1f62ed3f`

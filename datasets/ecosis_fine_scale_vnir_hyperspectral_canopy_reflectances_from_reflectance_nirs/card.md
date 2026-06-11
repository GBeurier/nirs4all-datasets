# Datasheet — EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests

## Composition

- **Alignment:** observation level; 1 sample(s), 2850 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 2850–2850 (mean 2850).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra and Metadata.csv | Headwall Photonics Nano-Hyperspec | NIR | 449.7–949.7 nm | 2850 | 226 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Row_No | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top 1 (×1) |
| Individual | target | numeric | *Not specified.* | n=1, missing=0, range 1–1, mean 1 ± 0 |
| DOY | target | numeric | *Not specified.* | n=1, missing=0, range 134–134, mean 134 ± 0 |
| Reading | target | numeric | *Not specified.* | n=1, missing=0, range 1–1, mean 1 ± 0 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 54647cde-1d77-44b4-83fc-af21f2d0304f (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Blandy Experimental Farm (×1) |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Blandy Experimental Farm, Virginia (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 39°03'52.2" N (×1) |
| longitude | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 78°03'28.9" W (×1) |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | numeric | *Not specified.* | n=1, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top umbellata, davurica, maackii, altissima, triacanthos, pomifera, nigra, virginiana (×1) |
| genus | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Elaeagnus, Rhamnus, Lonicera, Ailanthus, Gleditsia, Maclura, Juglans, Juniperus (×1) |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Canopy (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top canopy (×1) |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Headwall Photonics Nano-Hyperspec (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Pixel (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 449.7–449.7, mean 449.7 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 949.7–949.7, mean 949.7 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 226–226, mean 226 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Kelsey Huelsman Howard Epstein Xi Yang. 2020. Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Creative Commons Non-Commercial (Any) (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top explicit_restricted (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top private_use_only (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package fine-scale-vnir-hyperspectral-canopy-reflectances-from-virginia-successional-forests, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fine-scale-vnir-hyperspectral-canopy-reflectances-from-virginia-successional-forests`
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
- **Redistribution rights:** EcoSIS license is restricted or non-commercial; public redistribution of derived X/Y/M is not cleared in this pass.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `da6275280b8e6b411082af16a5d1868a73206d02430cd4c4c2639ea554b22b1a`
- **Processing hash:** `d3491503171e0416b83a268284fc64b620f3430022fb12dca8b7bb4915a1b241` | **metadata hash:** `c3cefaca9253ed87e7b06829bbe4ad6afe7431d3037085167023f947df9ac6d1`

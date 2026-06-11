# Datasheet — EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests

## Composition

- **Alignment:** observation level; 2850 sample(s), 2850 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra and Metadata.csv | Headwall Photonics Nano-Hyperspec | NIR | 449.7–949.7 nm | 2850 | 226 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Row_No | target | categorical | *Not specified.* | n=2850, missing=0, classes=2850, top 1 (×1) |
| Individual | target | numeric | *Not specified.* | n=2850, missing=0, range 1–65, mean 26.22 ± 17.93 |
| DOY | target | numeric | *Not specified.* | n=2850, missing=0, range 134–249, mean 189.9 ± 45.69 |
| Reading | target | numeric | *Not specified.* | n=2850, missing=0, range 1–15, mean 8 ± 4.321 |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 54647cde-1d77-44b4-83fc-af21f2d0304f (×2850) |
| site | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm (×2850) |
| location | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Blandy Experimental Farm, Virginia (×2850) |
| country | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 39°03'52.2" N (×2850) |
| longitude | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top 78°03'28.9" W (×2850) |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top source-provided coordinates when available (×2850) |
| year | metadata | numeric | *Not specified.* | n=2850, missing=0, range 2020–2020, mean 2020 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top umbellata, davurica, maackii, altissima, triacanthos, pomifera, nigra, virginiana (×2850) |
| genus | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Elaeagnus, Rhamnus, Lonicera, Ailanthus, Gleditsia, Maclura, Juglans, Juniperus (×2850) |
| family | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Canopy (×2850) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top canopy (×2850) |
| instrument | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Headwall Photonics Nano-Hyperspec (×2850) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Pixel (×2850) |
| signal_type | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top reflectance (×2850) |
| axis_unit | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top nm (×2850) |
| axis_min | metadata | numeric | *Not specified.* | n=2850, missing=0, range 449.7–449.7, mean 449.7 ± 1.706e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=2850, missing=0, range 949.7–949.7, mean 949.7 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2850, missing=0, range 226–226, mean 226 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2850, missing=2850, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Kelsey Huelsman Howard Epstein Xi Yang. 2020. Fine-scale VNIR hyperspectral canopy reflectances from Virginia successional forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS) (×2850) |
| license | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top Creative Commons Non-Commercial (Any) (×2850) |
| rights_status | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top explicit_restricted (×2850) |
| usage_scope | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top private_use_only (×2850) |
| notes | metadata | categorical | *Not specified.* | n=2850, missing=0, classes=1, top EcoSIS package fine-scale-vnir-hyperspectral-canopy-reflectances-from-virginia-successional-forests, no interpolation applied by project. (×2850) |

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
- **Content hash:** `bbbe77ea6301a7062253c1c0c918fdce9496d38e433e6de34dd71a95a03e68c6`
- **Processing hash:** `d3491503171e0416b83a268284fc64b620f3430022fb12dca8b7bb4915a1b241` | **metadata hash:** `c3cefaca9253ed87e7b06829bbe4ad6afe7431d3037085167023f947df9ac6d1`

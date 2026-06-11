# Datasheet — EcoSIS Greater Cape Floristic Region Leaf Spectral Library (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Greater Cape Floristic Region Leaf Spectral Library (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Greater Cape Floristic Region Leaf Spectral Library

## Composition

- **Alignment:** observation level; 1 sample(s), 3205 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 3205–3205 (mean 3205).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | GCFRSpectralLibraryEcoSisV3.csv | OceanOptics USB-4000 | NIR | 450–949 nm | 3205 | 500 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Unnamed__0 | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top 1 (×1) |
| Genus | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top Bobartia (×1) |
| Species | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top indica (×1) |
| FamilyManningGoldblatt | target | categorical | *Not specified.* | n=1, missing=0, classes=1, top IRIDACEAE (×1) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top cb7a912b-174c-48a7-8846-d028947b422d (×1) |
| site | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Western Cape (×1) |
| country | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=1, missing=0, range -34.29–-34.29, mean -34.29 ± 0 |
| longitude | metadata | numeric | *Not specified.* | n=1, missing=0, range 18.44–18.44, mean 18.44 ± 0 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top source-provided coordinates when available (×1) |
| year | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 2010, 2020 (×1) |
| date | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top indica (×1) |
| genus | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Bobartia (×1) |
| family | metadata | categorical | *Not specified.* | n=1, missing=1, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Leaf (×1) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top leaf (×1) |
| instrument | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top OceanOptics USB-4000 (×1) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Proximal (×1) |
| signal_type | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top reflectance (×1) |
| axis_unit | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top nm (×1) |
| axis_min | metadata | numeric | *Not specified.* | n=1, missing=0, range 450–450, mean 450 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=1, missing=0, range 949–949, mean 949 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=1, missing=0, range 500–500, mean 500 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top 10.1111/geb.13306 \| 10.21232/VKxouiyN \| 10.21232/vkxouiyn (×1) |
| citation | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Frye H. Aeillo-Lammens M. E. Euston-Brown D. Jones C. S. Kilroy Mollmann H. Merow C. Slingsby J. A. van der Merwe H. Wilson A. M. & Silander J. A.. 2010, 2020. Greater Cape Floristic Region Leaf Spectral Library. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/VKxouiyN (×1) |
| license | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×1) |
| rights_status | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top explicit_open (×1) |
| usage_scope | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top public_reuse_possible (×1) |
| notes | metadata | categorical | *Not specified.* | n=1, missing=0, classes=1, top EcoSIS package greater-cape-floristic-region-leaf-spectral-library, no interpolation applied by project. (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/greater-cape-floristic-region-leaf-spectral-library`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- Plant spectral diversity as a surrogate for species,  functional and phylogenetic diversity across a hyper- diverse  biogeographic region — [10.1111/geb.13306](https://doi.org/10.1111/geb.13306)
- Greater Cape Floristic Region Leaf Spectral Library — [10.21232/VKxouiyN](https://doi.org/10.21232/VKxouiyN)
- *Not specified.* — [10.21232/vkxouiyn](https://doi.org/10.21232/vkxouiyn)

## Distribution

- **License:** CC-BY-SA-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `cfae1c9d3ce2167b79b29204b5efa644597ab6d7c51c27476fd3c876901623cd`
- **Processing hash:** `d22dcde77998ee3eaaa4b11b748db1a5be87ee61954b442b66d43d1e9415e682` | **metadata hash:** `7e0012d9c6f31494b1d31d3db614a051cc9e3e006946180df2a2d2228137ea3f`

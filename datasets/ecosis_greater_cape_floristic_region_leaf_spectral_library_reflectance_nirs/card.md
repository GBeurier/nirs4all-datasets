# Datasheet — Greater Cape Floristic Region — leaf reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Greater Cape Floristic Region Leaf Spectral Library (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Greater Cape Floristic Region Leaf Spectral Library

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 3205 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | GCFRSpectralLibraryEcoSisV3.csv | OceanOptics USB-4000 | NIR | 450–949 nm | 3205 | 500 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Unnamed__0 | target | categorical | *Not specified.* | n=3205, missing=0, classes=3205, top 1 (×1) |
| Genus | target | categorical | *Not specified.* | n=3205, missing=0, classes=378, top Protea (×153) |
| Species | target | categorical | *Not specified.* | n=3205, missing=0, classes=894, top capensis (×93) |
| FamilyManningGoldblatt | target | categorical | *Not specified.* | n=3205, missing=0, classes=102, top ASTERACEAE (×505) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top cb7a912b-174c-48a7-8846-d028947b422d (×3205) |
| site | metadata | categorical | *Not specified.* | n=3205, missing=3205, classes=0, — |
| location | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top Western Cape (×3205) |
| country | metadata | categorical | *Not specified.* | n=3205, missing=3205, classes=0, — |
| latitude | metadata | numeric | *Not specified.* | n=3205, missing=0, range -34.37–-31.27, mean -33.42 ± 0.9497 |
| longitude | metadata | numeric | *Not specified.* | n=3205, missing=0, range 18.38–24.35, mean 21.26 ± 2.486 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top source-provided coordinates when available (×3205) |
| year | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top 2010, 2020 (×3205) |
| date | metadata | categorical | *Not specified.* | n=3205, missing=3205, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=894, top capensis (×93) |
| genus | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=378, top Protea (×153) |
| family | metadata | categorical | *Not specified.* | n=3205, missing=3205, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top Leaf (×3205) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top leaf (×3205) |
| instrument | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top OceanOptics USB-4000 (×3205) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top Proximal (×3205) |
| signal_type | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top reflectance (×3205) |
| axis_unit | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top nm (×3205) |
| axis_min | metadata | numeric | *Not specified.* | n=3205, missing=0, range 450–450, mean 450 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=3205, missing=0, range 949–949, mean 949 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=3205, missing=0, range 500–500, mean 500 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top 10.1111/geb.13306 \| 10.21232/VKxouiyN \| 10.21232/vkxouiyn (×3205) |
| citation | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top Frye H. Aeillo-Lammens M. E. Euston-Brown D. Jones C. S. Kilroy Mollmann H. Merow C. Slingsby J. A. van der Merwe H. Wilson A. M. & Silander J. A.. 2010, 2020. Greater Cape Floristic Region Leaf Spectral Library. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). 10.21232/VKxouiyN (×3205) |
| license | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top Creative Commons Attribution Share-Alike (×3205) |
| rights_status | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top explicit_open (×3205) |
| usage_scope | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top public_reuse_possible (×3205) |
| notes | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1, top EcoSIS package greater-cape-floristic-region-leaf-spectral-library, no interpolation applied by project. (×3205) |
| source_NewUID | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1981, top 703_7_BK (×16) |
| source_finalname | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=1187, top Leucadendron salignum (×24) |
| source_Latitude | metadata | numeric | *Not specified.* | n=3205, missing=0, range -34.37–-31.27, mean -33.42 ± 0.9497 |
| source_Longitude | metadata | numeric | *Not specified.* | n=3205, missing=0, range 18.38–24.35, mean 21.26 ± 2.486 |
| source_Subregion | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=6, top Baviaanksloof (×1284) |
| source_DateMonthDay | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=57, top 703 (×192) |
| source_Sample | metadata | numeric | *Not specified.* | n=3205, missing=0, range 1–94, mean 17.37 ± 13.61 |
| source_SubregAbbr | metadata | categorical | *Not specified.* | n=3205, missing=0, classes=6, top BK (×1284) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/greater-cape-floristic-region-leaf-spectral-library`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 5 fields, Y: 3 fields, measurements: 0 fields, passport: 33 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `8529de6c2591ff8c45947621efd6c910c0c07a3483dd43eca4ccee3cba865a44`
- **Processing hash:** `1c7288b7c32c02bc0aa2f8ba847ec2c2f2ac1cf86fd5ad849c7a2038b45f4c25` | **metadata hash:** `c7f4b171359152998ec348a032b6c7c2475dbebcc7175db133ddc4f0f40dadf3`

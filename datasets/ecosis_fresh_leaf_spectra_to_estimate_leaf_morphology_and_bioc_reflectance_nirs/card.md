# Datasheet — EcoSIS Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests

## Composition

- **Alignment:** sample level; 2363 sample(s), 2379 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1.007).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | FFT_Fresh_Spectra_v2.csv | Analytical Spectral Devices FieldSpec2, FieldSpec3 | NIR | 350–2500 nm | 2379 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Species | target | categorical | *Not specified.* | n=2379, missing=0, classes=2, top ACRU (×2222) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top 1f0c7ae2-5fa4-49c3-b259-1f90ed8140f4 (×2379) |
| site | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=3, top BH (×1668) |
| location | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top North Central and Northeastern United States (×2379) |
| country | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| latitude | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| longitude | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top source-provided coordinates when available (×2379) |
| year | metadata | numeric | *Not specified.* | n=2379, missing=0, range 2014–2014, mean 2014 ± 0 |
| date | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| species | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=2, top ACRU (×2222) |
| genus | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| family | metadata | categorical | *Not specified.* | n=2379, missing=2379, classes=0, — |
| plant_part | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top Leaf (×2379) |
| canopy_or_leaf | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top leaf (×2379) |
| instrument | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top Analytical Spectral Devices FieldSpec2, FieldSpec3 (×2379) |
| acquisition_mode | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top Contact (×2379) |
| signal_type | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top reflectance (×2379) |
| axis_unit | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top nm (×2379) |
| axis_min | metadata | numeric | *Not specified.* | n=2379, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2379, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2379, missing=0, range 2151–2151, mean 2151 ± 0 |
| publication_doi | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top 10.1890/13-2110.1/abstract \| 10.21232/C2WC75 \| 10.21232/c2wc75 (×2379) |
| citation | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top Shawn Serbin. 2014. Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests. Data set. Available on-line [http://ecosis.org] from the Ecological Spectral Information System (EcoSIS). doi:10.21232/C2WC75 (×2379) |
| license | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top Other (Open) (×2379) |
| rights_status | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top explicit_open (×2379) |
| usage_scope | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top public_reuse_possible (×2379) |
| notes | metadata | categorical | *Not specified.* | n=2379, missing=0, classes=1, top EcoSIS package fresh-leaf-spectra-to-estimate-leaf-morphology-and-biochemistry-for-northern-temperate-forests, no interpolation applied by project. (×2379) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-leaf-spectra-to-estimate-leaf-morphology-and-biochemistry-for-northern-temperate-forests`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques.
- **Curated views:** M: 6 fields, Y: 1 fields, passport: 40 fields, measurements: 3 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- Link to Cited Paper — [10.1890/13-2110.1/abstract](https://doi.org/10.1890/13-2110.1/abstract)
- Fresh Leaf Spectra to Estimate Leaf Morphology and Biochemistry for Northern Temperate Forests — [10.21232/C2WC75](https://doi.org/10.21232/C2WC75)
- *Not specified.* — [10.21232/c2wc75](https://doi.org/10.21232/c2wc75)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** EcoSIS CKAN metadata exposes an open license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `faf2e7f8a63cfb57af6f3e7b77fdbef10286d16147a61333103bdbcc6ee47f5e`
- **Processing hash:** `8b62c524418f5b2a2e01d94e610184eb52a5d765579bdaabebe0337320183eb9` | **metadata hash:** `2b1232895abe199dd78edff5912a7478efadf085c0ce728820654ec2506d4b71`

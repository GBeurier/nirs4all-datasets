# Datasheet — Belgian dune plants + Japanese Rosa rugosa — leaf reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan (reflectance). Origin database composed from 4 standardized v2.0 leaves: 1 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Leaf spectra of 4 plant species from Belgian dune grasslands + Rosa rugosa from the Northern Japan

## Composition

- **Alignment:** sample level; 2399 sample(s), 2399 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

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
| location | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top Oostende, Ishikari (×2399) |
| country | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=2, top Belgium (×2041) |
| latitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 43.15–51.36, mean 50.05 ± 2.858 |
| longitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2.644–141.4, mean 23.61 ± 49.31 |
| coordinate_precision_notes | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top source-provided coordinates when available (×2399) |
| year | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2019–2019, mean 2019 ± 0 |
| species | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top rugosa (×729) |
| genus | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosa (×729) |
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
| source_ids | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=2399, top BPR1 Rosrug 1 (×1) |
| source_plot_code | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=75, top PR1 (×60) |
| source_Latitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 43.15–51.36, mean 50.05 ± 2.858 |
| source_Longitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2.644–141.4, mean 23.61 ± 49.31 |
| source_country | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=2, top Belgium (×2041) |
| source_Spcode | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosrug (×729) |
| SpectralRep | metadata | numeric | *Not specified.* | n=2399, missing=0, range 1–1, mean 1 ± 0 |
| ids | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=2399, top BPR1 Rosrug 1 (×1) |
| plot code | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=75, top PR1 (×60) |
| Latitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 43.15–51.36, mean 50.05 ± 2.858 |
| Longitude | metadata | numeric | *Not specified.* | n=2399, missing=0, range 2.644–141.4, mean 23.61 ± 49.31 |
| latin genus | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosa (×729) |
| latin species | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top rugosa (×729) |
| Spcode | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=4, top Rosrug (×729) |
| LMA (mg/cm2) | metadata | numeric | *Not specified.* | n=2399, missing=0, range 1.525–13.89, mean 6.221 ± 2.649 |
| LDMC (mg/mg) | metadata | numeric | *Not specified.* | n=2399, missing=0, range 0.0704–0.5409, mean 0.2664 ± 0.1081 |
| EWT (mg/cm2) | metadata | numeric | *Not specified.* | n=2399, missing=0, range 5.474–42.72, mean 18.44 ± 7.05 |
| dataset | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top EcoSIS (×2399) |
| dimensions | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top 1D (×2399) |
| axis_note | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×2399) |
| official_data_url | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top https://data.ecosis.org/dataset/leaf-spectra-of-4-plant-species-from-belgian-dune-grasslands---rosa-rugosa-from-the-northern-japan (×2399) |
| official_package_url | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top https://ecosis.org/package/leaf-spectra-of-4-plant-species-from-belgian-dune-grasslands---rosa-rugosa-from-the-northern-japan (×2399) |
| license_url | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top http://www.opendefinition.org/licenses/odc-odbl (×2399) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top True (×2399) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=2399, missing=0, classes=1, top ecosis_leaf_spectra_of_4_plant_species_from_belgian_dune_grass_reflectance_nirs (×2399) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** ok

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-spectra-of-4-plant-species-from-belgian-dune-grasslands---rosa-rugosa-from-the-northern-japan`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 5 fields, Y: 5 fields, measurements: 0 fields, passport: 40 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.3.0 | **schema/protocol:** 2.0
- **Content hash:** `3974179f57e4dba7d11cfb521b10c5ec0776f3a57d04b8380fe462cfaeca78ac`
- **Processing hash:** `dd38f17883891a65802513640878c8aa2e65221dea0b75e5e5c12edea2e079f6` | **metadata hash:** `c89fd27353e0fa7a54bf349aeb9b9c6c12f17fbeeb39957dd9f4fc40437d4473`

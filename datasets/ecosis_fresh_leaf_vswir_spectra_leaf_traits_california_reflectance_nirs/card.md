# Datasheet — EcoSIS Fresh Leaf VSWIR Spectra to Estimate Leaf Traits for California Ecosystems (reflectance)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Fresh Leaf VSWIR Spectra to Estimate Leaf Traits for California Ecosystems (reflectance). v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Fresh Leaf Spectra to Estimate Leaf Traits for California Ecosystems

## Composition

- **Alignment:** sample level; 285 sample(s), 285 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Spectra | ASD FieldSpec / FieldSpec 3 | NIR | 350–2500 nm | 285 | 2151 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Nitrogen | target | numeric | *Not specified.* | n=285, missing=1, range 0.454–3.805, mean 1.444 ± 0.6273 |
| Cellulose | target | numeric | *Not specified.* | n=285, missing=1, range 4.195–27.33, mean 11.82 ± 4.811 |
| Lignin | target | numeric | *Not specified.* | n=285, missing=1, range 2.586–22.51, mean 10.28 ± 3.373 |
| Water_Content | target | numeric | *Not specified.* | n=285, missing=1, range 20.22–76.85, mean 51 ± 9.325 |
| LMA | target | numeric | *Not specified.* | n=285, missing=20, range 34.7–388.9, mean 173.5 ± 80.35 |
| ecosis_package_name | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top fresh-leaf-spectra-to-estimate-leaf-traits-for-california-ecosystems (×285) |
| ecosis_resource_id | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top 396fc5a4-f6a8-4f4b-9bdb-2970223245c0 (×285) |
| site_code | metadata | categorical | *Not specified.* | n=285, missing=0, classes=3, top SB (×144) |
| site_name | metadata | categorical | *Not specified.* | n=285, missing=0, classes=3, top Santa Barbara (×144) |
| state | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top California (×285) |
| species | metadata | categorical | *Not specified.* | n=285, missing=0, classes=16, top BAPI (×18) |
| latin_genus | metadata | categorical | *Not specified.* | n=285, missing=0, classes=11, top Ceanothus (×54) |
| latin_species | metadata | categorical | *Not specified.* | n=285, missing=0, classes=16, top pilularis (×18) |
| age | metadata | categorical | *Not specified.* | n=285, missing=0, classes=5, top Old (×135) |
| replicate | metadata | numeric | *Not specified.* | n=285, missing=0, range 1–3, mean 2 ± 0.8179 |
| measurement_type | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Bare_Fiber (×285) |
| measurement | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top REFL (×285) |
| sample_name | metadata | categorical | *Not specified.* | n=285, missing=0, classes=111, top BAPI_1_Old (×3) |
| year_sampled | metadata | numeric | *Not specified.* | n=285, missing=0, range 2013–2013, mean 2013 ± 0 |
| sample_date | metadata | categorical | *Not specified.* | n=285, missing=0, classes=8, top 2013-04-01 00:00:00 (×48) |
| latitude | metadata | numeric | *Not specified.* | n=285, missing=0, range 34.42–37.04, mean 35 ± 1.057 |
| longitude | metadata | numeric | *Not specified.* | n=285, missing=0, range -119.8–-119.3, mean -119.7 ± 0.2106 |
| sample_type | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Vegetation (×285) |
| instrumentation | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top ASD FieldSpec (×285) |
| calibration | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Spectralon Ratio (×285) |
| wavelengths | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Nanometers (×285) |
| spectra_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Percent (×285) |
| nitrogen_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top percent (×285) |
| cellulose_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top percent (×285) |
| lignin_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top percent (×285) |
| water_content_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top percent (×285) |
| lma_units | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top grams per square meter (×285) |
| project | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top NASA HyspIRI Airborne Campaign (×285) |
| pi | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Dar Roberts (×285) |
| affiliation | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top VIPER - University of California Santa Barbara (×285) |
| signal_type | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top reflectance (×285) |
| axis_unit | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top nm (×285) |
| axis_min | metadata | numeric | *Not specified.* | n=285, missing=0, range 350–350, mean 350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=285, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=285, missing=0, range 2151–2151, mean 2151 ± 0 |
| rights_status | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top not_cleared (×285) |
| usage_scope | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top private_use_only (×285) |
| notes | metadata | categorical | *Not specified.* | n=285, missing=0, classes=1, top Converted from true EcoSIS XLSX workbook without project interpolation or resampling. (×285) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/fresh-leaf-spectra-to-estimate-leaf-traits-for-california-ecosystems`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: 285 spectral identifiers and 285 (sample_name, sample_date) pairs. The 111 labels are reused on 1–3 distinct dates; replicate is constant within each label, so these are not 1–3 reacquisitions of the same dated sample. Technical replicate status is undocumented.
- **Curated views:** M: 9 fields, Y: 5 fields, measurements: 2 fields, passport: 31 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Private/internal use only until EcoSIS license and redistribution terms are manually confirmed.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `d6b6a803fdaa04ac6bd136bf0884cae464aec2a9041fd499e1271ad1c976a1d3`
- **Processing hash:** `c8ea909c2cb05061bded51974044de18087a080dfae1c319b5fee79c34352308` | **metadata hash:** `1850fcf13bd84c0d3452c8ced2bef2afef75f7fb80b75c6078cb8229a450aa15`

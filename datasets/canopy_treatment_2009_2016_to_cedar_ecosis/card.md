# Datasheet — EcoSIS 2009 to 2016 Cedar Creek Enemy Removal Experiment Canopy Reflectance (MSR) (Treatment)

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** canopy
- **Description:** EcoSIS 2009 to 2016 Cedar Creek Enemy Removal Experiment Canopy Reflectance (MSR) (Treatment). v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, canopy
- **Contributor:** 2009 to 2016 Cedar Creek Enemy Removal Experiment Canopy Reflectance (MSR)

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 25414 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | e244_multispec_raw_data | *Not specified.* | NIR | 485–1650 nm | 25414 | 5 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Treatment | target | numeric | *Not specified.* | n=25414, missing=0, range 0–4, mean 2 ± 1.414 |
| SpectralRep | metadata | numeric | *Not specified.* | n=25414, missing=0, range 1–1, mean 1 ± 0 |
| Experiment | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top e244 (×25414) |
| Year | metadata | numeric | *Not specified.* | n=25414, missing=0, range 2008–2016, mean 2013 ± 2.226 |
| Month | metadata | numeric | *Not specified.* | n=25414, missing=0, range 4–11, mean 6.973 ± 1.556 |
| Day | metadata | numeric | *Not specified.* | n=25414, missing=0, range 1–31, mean 15.8 ± 8.995 |
| TIME | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=11717, top 11:22:57 (×11) |
| PLOT | metadata | numeric | *Not specified.* | n=25414, missing=0, range 1–205, mean 102.5 ± 59.12 |
| metadata_Treatment | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=5, top Control (×5086) |
| ANG | metadata | numeric | *Not specified.* | n=25414, missing=0, range 22–67.1, mean 37.78 ± 9.044 |
| IRR | metadata | numeric | *Not specified.* | n=25414, missing=0, range 10–1309, mean 735.7 ± 126.6 |
| Note | metadata | categorical | *Not specified.* | n=25414, missing=25384, classes=3, top Reflectance at less than zero in 1650 wavelength (×13) |
| dataset | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top EcoSIS (×25414) |
| dataset_slug | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top 2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr- (×25414) |
| task_type | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top classification (×25414) |
| trait_header | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top Treatment (×25414) |
| target_original_name | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top Treatment (×25414) |
| measurement_hint | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top e244_multispec_raw_data (×25414) |
| raw_label | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=5, top Control (×5086) |
| reference_value | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=5, top Control (×5086) |
| class_index | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=5, top 1 (×5086) |
| class_label | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=5, top Control (×5086) |
| n_points_original | metadata | numeric | *Not specified.* | n=25414, missing=0, range 5–5, mean 5 ± 0 |
| dimensions | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top 1D (×25414) |
| axis_note | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top wavelengths_as_provided_by_EcoSIS_resource (×25414) |
| official_data_url | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top https://data.ecosis.org/dataset/2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr- (×25414) |
| official_package_url | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top https://ecosis.org/package/2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr- (×25414) |
| license | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top Creative Commons Attribution (×25414) |
| license_url | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top http://www.opendefinition.org/licenses/cc-by (×25414) |
| rights_status | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top explicit_open (×25414) |
| usage_scope | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top public_reuse_possible (×25414) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top True (×25414) |
| parent_standardized_dataset_id | metadata | categorical | *Not specified.* | n=25414, missing=25414, classes=0, — |
| notes | metadata | categorical | *Not specified.* | n=25414, missing=0, classes=1, top Task-specific EcoSIS target not present in active parent Y table, wavelengths kept as provided by EcoSIS resource, no project interpolation. (×25414) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr-`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/api/3/action/package_show?id=2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr-`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ecosis.org/package/2009-to-2016-cedar-creek-enemy-removal-experiment-canopy-reflectance--msr-`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Le convertisseur amont a choisi Experiment=e244, code constant d’expérience. Les 205 parcelles, dates et heures décrivent plusieurs unités ; aucun identifiant de spécimen/répétition technique n’est établi.
- **Curated views:** M: 7 fields, Y: 1 fields, passport: 31 fields, measurements: 1 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** EcoSIS CKAN API package_show verified open license: Creative Commons Attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `13e7624d2fb9e1ca873e40aa1f8469d59bac9e8946e1cc1fe9c0e59d120dce39`
- **Processing hash:** `171f2c17db5d89d2cc79b3c9638c4720f480c0876d52e78b1a137d6c468cda53` | **metadata hash:** `c8b11cc87650d3275f6d62ccad3bf22b9ae58fc490d50164061006b9bff1c4ee`

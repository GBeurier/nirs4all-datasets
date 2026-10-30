# Datasheet — ROD Raman native-axis 3528-point mineral subset 0d479baa

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 3528-point mineral subset 0d479baa. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 17 sample(s), 17 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 99.17–3500 cm-1 | 17 | 3528 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top Otavite (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top C Cd O3 (×1) |
| compound_source | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top commercial powder Alfa aesar 97% A15812 (×1) |
| rod_database_code | target | categorical | *Not specified.* | n=17, missing=0, classes=17, top 3500081 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top 0d479baab4cbc2fc (×17) |
| axis_unit | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top cm^-1 (×17) |
| axis_min | metadata | numeric | *Not specified.* | n=17, missing=0, range 99.17–99.17, mean 99.17 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=17, missing=0, range 3500–3500, mean 3500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=17, missing=0, range 3528–3528, mean 3528 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top Raman (×17) |
| axis_status | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top real_common_axis_subset (×17) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=17, missing=0, classes=1, top false (×17) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top Otavite (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top Otavite (×1) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top C Cd O3 (×1) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top commercial powder Alfa aesar 97% A15812 (×1) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=17, missing=0, classes=17, top Raman spectrum of commercial Otavite (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=17, missing=17, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=17, missing=0, range 2017–2017, mean 2017 ± 0 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://solsa.crystallography.net/rod/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 3 fields, Y: 2 fields, measurements: 0 fields, passport: 25 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** ROD states that all data and the database are CC0/public domain. Users should acknowledge the original authors of the structural data.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f966c36154457ff0048635a0c6e15f08dfc79a9b6632130753bbb737b1ef67e9`
- **Processing hash:** `df11af9e94c549830c650fdf10e8e36f84ef92ba88d8bb9b5eed706c084ff8e8` | **metadata hash:** `e15b32b1f6f1149069c0fea84c4f8e82fdd262038047a1c83d2f640cccea5d6c`

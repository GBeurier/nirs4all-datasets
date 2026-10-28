# Datasheet — ROD Raman native-axis 972-point mineral subset 70adf657

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 972-point mineral subset 70adf657. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** observation level; 13 sample(s), 13 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 102.3–2000 cm-1 | 13 | 972 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=13, missing=0, classes=13, top BaO2 (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=13, missing=0, classes=13, top Ba O2 (×1) |
| compound_source | target | categorical | *Not specified.* | n=13, missing=0, classes=11, top commercial powder Alfa Aesar 99% (×2) |
| rod_database_code | target | categorical | *Not specified.* | n=13, missing=0, classes=13, top 3500160 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top 70adf657ab5cfea1 (×13) |
| axis_unit | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top cm^-1 (×13) |
| axis_min | metadata | numeric | *Not specified.* | n=13, missing=0, range 102.3–102.3, mean 102.3 ± 2.958e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=13, missing=0, range 2000–2000, mean 2000 ± 4.733e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=13, missing=0, range 972–972, mean 972 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top Raman (×13) |
| axis_status | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top real_common_axis_subset (×13) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=13, missing=0, classes=1, top false (×13) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=13, missing=1, classes=12, top BaO2 (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top Ba O2 (×1) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top Ba O2 (×1) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=13, missing=0, classes=11, top commercial powder Alfa Aesar 99% (×2) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=13, missing=0, classes=13, top Raman spectrum of commercial BaO2 (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=13, missing=13, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=13, missing=0, range 2018–2019, mean 2018 ± 0.2774 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://solsa.crystallography.net/rod/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `15eb7fdd8ab30dbff08696ada0bbbb8a6448b57f4a869748876f05d91b13ac94`
- **Processing hash:** `6299594cdc9bcc11f7d9fcc05c69bd0bc4f19033bba4b64c09fbe51679f48092` | **metadata hash:** `98fd70d2a84d13eb783e5a2d28c2798644232423130ef7610de885e3e5c5a47f`

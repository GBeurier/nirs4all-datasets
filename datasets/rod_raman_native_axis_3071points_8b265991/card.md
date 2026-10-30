# Datasheet — ROD Raman native-axis 3071-point mineral subset 8b265991

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 3071-point mineral subset 8b265991. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 10 sample(s), 10 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 39.57–3000 cm-1 | 10 | 3071 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=10, missing=0, classes=10, top Nitrobarite (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=10, missing=0, classes=10, top Ba N2 O6 (×1) |
| compound_source | target | categorical | *Not specified.* | n=10, missing=0, classes=9, top commercial powder Alfa Aesar 99% (×2) |
| rod_database_code | target | categorical | *Not specified.* | n=10, missing=0, classes=10, top 3500035 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top 8b2659916ff2178e (×10) |
| axis_unit | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top cm^-1 (×10) |
| axis_min | metadata | numeric | *Not specified.* | n=10, missing=0, range 39.57–39.57, mean 39.57 ± 7.49e-15 |
| axis_max | metadata | numeric | *Not specified.* | n=10, missing=0, range 3000–3000, mean 3000 ± 4.793e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=10, missing=0, range 3071–3071, mean 3071 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top Raman (×10) |
| axis_status | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top real_common_axis_subset (×10) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=10, missing=0, classes=1, top false (×10) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Nitrobarite (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Ba(NO3)2 (×1) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Ba N2 O6 (×1) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=10, missing=0, classes=9, top commercial powder Alfa Aesar 99% (×2) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=10, missing=0, classes=10, top Raman spectrum of commercial Ba(NO3)2 (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=10, missing=10, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=10, missing=0, range 2017–2017, mean 2017 ± 0 |

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
- **Content hash:** `09cb394b70c28c7b2a08d59224d17a4c0926f905563e5476c1fb16b574661291`
- **Processing hash:** `3b07b242a52ec6a7bd805b456a87df514abcb7651b4ab0b82429917fde0ed14b` | **metadata hash:** `3893b258b038ca908f5a3c9edd18e7e1e56fe16836cfc933169811745b3108c8`

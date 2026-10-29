# Datasheet — ROD Raman native-axis 977-point mineral subset 4244c525

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 977-point mineral subset 4244c525. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 31 sample(s), 31 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 150–1299 cm-1 | 31 | 977 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=31, missing=0, classes=31, top Corundum (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=31, missing=0, classes=30, top O2 Ti (×2) |
| compound_source | target | categorical | *Not specified.* | n=31, missing=0, classes=23, top commercial powder Alfa Aesar 99% (×5) |
| rod_database_code | target | categorical | *Not specified.* | n=31, missing=0, classes=31, top 3500216 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top 4244c5254fe8c103 (×31) |
| axis_unit | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top cm^-1 (×31) |
| axis_min | metadata | numeric | *Not specified.* | n=31, missing=0, range 150–150, mean 150 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=31, missing=0, range 1299–1299, mean 1299 ± 4.623e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=31, missing=0, range 977–977, mean 977 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top Raman (×31) |
| axis_status | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top real_common_axis_subset (×31) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=31, missing=0, classes=1, top false (×31) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=31, missing=0, classes=31, top Corundum (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=31, missing=1, classes=30, top Aluminium oxide (×1) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=31, missing=0, classes=30, top O2 Ti (×2) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=31, missing=0, classes=23, top commercial powder Alfa Aesar 99% (×5) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=31, missing=0, classes=31, top Raman spectrum of commercial Al2O3 (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=31, missing=31, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=31, missing=0, range 2018–2018, mean 2018 ± 0 |

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

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 3 fields, Y: 2 fields, passport: 25 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `3181b1b30dbfdc5debaabe094e59f5a86f46fd346d27a79a331a4d3d11a561aa`
- **Processing hash:** `c1b0f32356bb25de8f6e6e7db324de3e89272c87a2e446c27d8266b68d5cae6d` | **metadata hash:** `33c3f8154121c6a628464916ce6a72651d75c62729a455e05a282ba2b2015460`

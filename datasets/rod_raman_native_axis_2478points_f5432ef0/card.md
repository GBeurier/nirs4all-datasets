# Datasheet — ROD Raman native-axis 2478-point mineral subset f5432ef0

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 2478-point mineral subset f5432ef0. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 11 sample(s), 11 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 91.53–1286 cm-1 | 11 | 2478 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=11, missing=0, classes=10, top Armangite (×2) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=11, missing=0, classes=10, top C As18 Mn26 O57 (×2) |
| compound_source | target | categorical | *Not specified.* | n=11, missing=0, classes=11, top R060269 (×1) |
| rod_database_code | target | categorical | *Not specified.* | n=11, missing=0, classes=11, top 1000049 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top f5432ef05bf368f1 (×11) |
| axis_unit | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top cm^-1 (×11) |
| axis_min | metadata | numeric | *Not specified.* | n=11, missing=0, range 91.53–91.53, mean 91.53 ± 1.49e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=11, missing=0, range 1286–1286, mean 1286 ± 2.385e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=11, missing=0, range 2478–2478, mean 2478 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top Raman (×11) |
| axis_status | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top real_common_axis_subset (×11) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=11, missing=0, classes=1, top false (×11) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=11, missing=0, classes=10, top Armangite (×2) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=11, missing=0, classes=11, top R060269 (×1) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=11, missing=11, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=11, missing=0, classes=10, top Armangite, Mn26[As6(OH)4O14][As6O18]2[CO3], a fluorite derivative structure (×2) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=11, missing=5, classes=6, top 10.2113/gscanmin.38.4.847 (×1) |
| journal_year | metadata | numeric | *Not specified.* | n=11, missing=0, range 1971–2011, mean 1993 ± 12.52 |

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
- **Curated views:** M: 1 fields, Y: 2 fields, measurements: 0 fields, passport: 27 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `9f13c4b04bc6322d41bad321fdf0b306ab394c187a2e8e497c62a2036032db38`
- **Processing hash:** `6596db8b1d7c6a7514e410940fa201f32c1a1805bc4384dd6b83b85f262e5f89` | **metadata hash:** `926f2b9776294340aa586178d614002065de7f62689f91ffc7a4117bd60dcfdf`

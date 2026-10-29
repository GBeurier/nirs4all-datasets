# Datasheet — ROD Raman native-axis 2542-point mineral subset f4e30a51

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 2542-point mineral subset f4e30a51. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 27 sample(s), 27 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 50.17–2500 cm-1 | 27 | 2542 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=27, missing=0, classes=27, top aluminium(III) oxide (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=27, missing=0, classes=26, top O2 Ti (×2) |
| compound_source | target | categorical | *Not specified.* | n=27, missing=0, classes=20, top commercial powder Alfa Aesar 99.9% (×5) |
| rod_database_code | target | categorical | *Not specified.* | n=27, missing=0, classes=27, top 3500000 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top f4e30a51825ab03c (×27) |
| axis_unit | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top cm^-1 (×27) |
| axis_min | metadata | numeric | *Not specified.* | n=27, missing=0, range 50.17–50.17, mean 50.17 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=27, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=27, missing=0, range 2542–2542, mean 2542 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top Raman (×27) |
| axis_status | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top real_common_axis_subset (×27) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=27, missing=0, classes=1, top false (×27) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=27, missing=0, classes=27, top aluminium(III) oxide (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=27, missing=0, classes=26, top titanium(IV) oxide (×2) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=27, missing=0, classes=26, top O2 Ti (×2) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=27, missing=0, classes=20, top commercial powder Alfa Aesar 99.9% (×5) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=27, missing=0, classes=27, top Raman spectrum of commercial aluminium(III) oxide (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=27, missing=27, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=27, missing=0, range 2017–2019, mean 2017 ± 0.456 |

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
- **Content hash:** `9b57d17e211e6f4698b61b2356852ee8cbd41f2eaee3d992e65988d242cbe8a2`
- **Processing hash:** `f69753c5a696d9f7ad90e77b017d94bf54ea4a1aca33acdd74c5af2ec08b602d` | **metadata hash:** `7312f5d77d538b80ceb015e1cfaac2b0c9068e19a7fe3da3da7cc70938e026c5`

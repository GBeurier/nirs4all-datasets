# Datasheet — ROD Raman native-axis 2515-point mineral subset 4efbe55b

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 2515-point mineral subset 4efbe55b. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 15 sample(s), 15 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 89.78–1302 cm-1 | 15 | 2515 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=15, missing=0, classes=15, top Dugganite (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=15, missing=0, classes=15, top As6 O18 Pb3 Te Zn3 (×1) |
| compound_source | target | categorical | *Not specified.* | n=15, missing=0, classes=15, top R060498 (×1) |
| rod_database_code | target | categorical | *Not specified.* | n=15, missing=0, classes=15, top 1000241 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top 4efbe55b7913edc6 (×15) |
| axis_unit | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top cm^-1 (×15) |
| axis_min | metadata | numeric | *Not specified.* | n=15, missing=0, range 89.78–89.78, mean 89.78 ± 1.471e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=15, missing=0, range 1302–1302, mean 1302 ± 2.354e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=15, missing=0, range 2515–2515, mean 2515 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top Raman (×15) |
| axis_status | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top real_common_axis_subset (×15) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=15, missing=0, classes=1, top false (×15) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=15, missing=0, classes=15, top Dugganite (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=15, missing=14, classes=1, top Ca(CO3) (×1) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=15, missing=0, classes=15, top R060498 (×1) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=15, missing=15, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=15, missing=0, classes=15, top The crystal structure of dugganite, Pb3Zn3TeAs2O14 (×1) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=15, missing=9, classes=6, top 10.3749/canmin.49.3.865 (×1) |
| journal_year | metadata | numeric | *Not specified.* | n=15, missing=0, range 1964–2012, mean 1990 ± 16.28 |

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
- **Content hash:** `4118f44a14c50c6b249598cd1df1f73c92cb055018dc16faad839bdb9b809632`
- **Processing hash:** `5bbc221c5a712810ce3a8c387fe305c00ca7b9ce0110877a986f2b1781f17ac9` | **metadata hash:** `f4da9caae3cd6c135a842df0d9da8ebd21ba56c42ea1a36bfc57cdaa95056d91`

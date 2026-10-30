# Datasheet — ROD Raman native-axis 2023-point mineral subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rod
- **Description:** ROD Raman native-axis 2023-point mineral subset. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rod
- **Contributor:** Raman Open Database

## Composition

- **Alignment:** sample level; 48 sample(s), 48 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ROD native Raman axis group | ROD source metadata, not consistently specified | Raman | 50.51–2000 cm-1 | 48 | 2023 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=48, missing=0, classes=48, top Corundum (×1) |
| chemical_formula_sum | target | categorical | *Not specified.* | n=48, missing=0, classes=48, top Al2 O3 (×1) |
| compound_source | target | categorical | *Not specified.* | n=48, missing=0, classes=31, top commercial powder Alfa Aesar 99.9% (×6) |
| rod_database_code | target | categorical | *Not specified.* | n=48, missing=0, classes=48, top 3500102 (×1) |
| axis_digest | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top 8dc604ea4b2c277f (×48) |
| axis_unit | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top cm^-1 (×48) |
| axis_min | metadata | numeric | *Not specified.* | n=48, missing=0, range 50.51–50.51, mean 50.51 ± 7.181e-15 |
| axis_max | metadata | numeric | *Not specified.* | n=48, missing=0, range 2000–2000, mean 2000 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=48, missing=0, range 2023–2023, mean 2023 ± 0 |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top Raman (×48) |
| axis_status | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top real_common_axis_subset (×48) |
| interpolation_applied | metadata | categorical | *Not specified.* | n=48, missing=0, classes=1, top false (×48) |
| chemical_name_mineral | metadata | categorical | *Not specified.* | n=48, missing=0, classes=48, top Corundum (×1) |
| chemical_name_common | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| chemical_name_systematic | metadata | categorical | *Not specified.* | n=48, missing=0, classes=48, top aluminium(III) oxide (×1) |
| chemical_formula_structural | metadata | categorical | *Not specified.* | n=48, missing=0, classes=48, top Al2 O3 (×1) |
| chemical_compound_source | metadata | categorical | *Not specified.* | n=48, missing=0, classes=31, top commercial powder Alfa Aesar 99.9% (×6) |
| raman_measurement_device_model | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| raman_measurement_device_company | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| raman_measurement_device_excitation_laser_wavelength | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| raman_measurement_range_min | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| raman_measurement_range_max | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| publ_section_title | metadata | categorical | *Not specified.* | n=48, missing=0, classes=47, top Raman spectrum of commercial boron trioxide (×2) |
| journal_paper_doi | metadata | categorical | *Not specified.* | n=48, missing=48, classes=0, — |
| journal_year | metadata | numeric | *Not specified.* | n=48, missing=0, range 2017–2019, mean 2017 ± 0.3713 |

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
- **Content hash:** `1cb1639ce8fd58105dfbe84d8f7e26a52004ddcb73758e27a6227ab87153f5b8`
- **Processing hash:** `45978202dd1f2596ea91970b40db1ca89523a1464c0679128183dedffa4d9db3` | **metadata hash:** `db729b4cfa372a0747f35d7d41047f99975952055c56c84d7a3a4191af2a3a41`

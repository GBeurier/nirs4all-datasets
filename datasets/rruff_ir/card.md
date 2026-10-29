# Datasheet — RRUFF IR mineral spectral library common-axis subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rruff
- **Description:** RRUFF IR mineral spectral library common-axis subset. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rruff
- **Contributor:** RRUFF

## Composition

- **Alignment:** sample level; 347 sample(s), 347 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | RRUFF IR | not consistently available in selected text files | MIR | 399.2–4000 cm-1 | 347 | 1868 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=347, missing=0, classes=246, top Fluorapatite (×5) |
| chemistry | target | categorical | *Not specified.* | n=347, missing=1, classes=239, top TiO_2_ (×5) |
| class_label | target | categorical | *Not specified.* | n=347, missing=0, classes=246, top Fluorapatite (×5) |
| rruff_id | target | categorical | *Not specified.* | n=347, missing=0, classes=347, top R040130 (×1) |
| sample_name | target | categorical | *Not specified.* | n=347, missing=0, classes=347, top R040130-1 (×1) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top IR (×347) |
| axis_unit | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top cm^-1 (×347) |
| axis_min | metadata | numeric | *Not specified.* | n=347, missing=0, range 399.2–399.2, mean 399.2 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=347, missing=0, range 4000–4000, mean 4000 ± 4.554e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=347, missing=0, range 1868–1868, mean 1868 ± 0 |
| sample_description | metadata | categorical | *Not specified.* | n=347, missing=0, classes=321, top White massive (×4) |
| metadata_chemistry | metadata | categorical | *Not specified.* | n=347, missing=0, classes=342, top Ca_1.000_ F_2.000_ (×2) |
| locality | metadata | categorical | *Not specified.* | n=347, missing=0, classes=288, top unknown (×8) |
| laser_wavelength | metadata | categorical | *Not specified.* | n=347, missing=347, classes=0, — |
| instrument | metadata | categorical | *Not specified.* | n=347, missing=347, classes=0, — |
| acquisition_metadata | metadata | categorical | *Not specified.* | n=347, missing=0, classes=343, top Powder (×5) |
| quality_flags | metadata | categorical | *Not specified.* | n=347, missing=0, classes=8, top The identification of this mineral has been confirmed by X-ray diffraction and chemical analysis (×319) |
| citation | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top Lafuente, B., Downs, R. T., Yang, H., Stone, N. The Power of Databases: The RRUFF Project. Highlights in Mineralogical Crystallography, T Armbruster and R M Danisi, eds., Berlin, Germany, W. De Gruyter 2015, 1-30. (×347) |
| license_or_terms | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top manual_review_needed, redistribution not cleared (×347) |
| notes | metadata | categorical | *Not specified.* | n=347, missing=0, classes=1, top Infrared RAW, common-axis subset, no interpolation (×347) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/zipped_data_files/infrared/RAW.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/about/download-data/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: 347 spécimens RRUFF distincts, chacun avec un seul spectre IR exporté.
- **Curated views:** M: 1 fields, Y: 3 fields, measurements: 0 fields, passport: 20 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Redistribution not cleared; verify source terms before release.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `64b14476975997931a990e85177d00e9b85604e7df5a264b8f38b1696ab5d461`
- **Processing hash:** `e85f9240cd572685df6d384f5022099e572f41776cef4b7ce97d794530db2bc8` | **metadata hash:** `49424639ade54aa280fd13cd72d57c71f8b96cc8234241d57a230fcfd5274883`

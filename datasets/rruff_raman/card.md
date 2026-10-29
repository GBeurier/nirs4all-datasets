# Datasheet — RRUFF RAMAN mineral spectral library common-axis subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** rruff
- **Description:** RRUFF RAMAN mineral spectral library common-axis subset. v2.0 standardized NIRS package: 1 spectral source(s), 5 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, rruff
- **Contributor:** RRUFF

## Composition

- **Alignment:** sample level; 12 sample(s), 85 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 3–9 (mean 7.083).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | RRUFF RAMAN | not consistently available in selected text files | Raman | 51.43–1570 cm-1 | 85 | 1340 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| mineral_name | target | categorical | *Not specified.* | n=85, missing=0, classes=8, top Cerussite (×27) |
| chemistry | target | categorical | *Not specified.* | n=85, missing=0, classes=8, top Pb(CO_3_) (×27) |
| class_label | target | categorical | *Not specified.* | n=85, missing=0, classes=8, top Cerussite (×27) |
| rruff_id | target | categorical | *Not specified.* | n=85, missing=0, classes=12, top R050408 (×9) |
| sample_name | target | categorical | *Not specified.* | n=85, missing=0, classes=30, top R060358-3 (×3) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top RAMAN (×85) |
| axis_unit | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top cm^-1 (×85) |
| axis_min | metadata | numeric | *Not specified.* | n=85, missing=0, range 51.43–51.43, mean 51.43 ± 2.859e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=85, missing=0, range 1570–1570, mean 1570 ± 2.287e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=85, missing=0, range 1340–1340, mean 1340 ± 0 |
| sample_description | metadata | categorical | *Not specified.* | n=85, missing=0, classes=12, top Pale yellow fragment (×9) |
| metadata_chemistry | metadata | categorical | *Not specified.* | n=85, missing=0, classes=12, top Pb_1.00_S_1.00_O_4_ (×9) |
| locality | metadata | categorical | *Not specified.* | n=85, missing=0, classes=11, top Tsumeb mine, Tsumeb, Otavi District, Oshikoto, Namibia (×18) |
| laser_wavelength | metadata | numeric | *Not specified.* | n=85, missing=0, range 514–514, mean 514 ± 0 |
| instrument | metadata | categorical | *Not specified.* | n=85, missing=85, classes=0, — |
| acquisition_metadata | metadata | categorical | *Not specified.* | n=85, missing=0, classes=30, top Laser parallel to -b* (0 -1 0). Fiducial mark perpendicular to laser is parallel to c [0 0 1] \| Powder \| a: 12.0587 b: 12.0587 c: 12.0587 alpha: 90 beta: 90 gamma: 90 volume: 1753.49 crystal system: cubic (×3) |
| quality_flags | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top The identification of this mineral has been confirmed by X-ray diffraction and chemical analysis (×85) |
| citation | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top Lafuente, B., Downs, R. T., Yang, H., Stone, N. The Power of Databases: The RRUFF Project. Highlights in Mineralogical Crystallography, T Armbruster and R M Danisi, eds., Berlin, Germany, W. De Gruyter 2015, 1-30. (×85) |
| license_or_terms | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top manual_review_needed, redistribution not cleared (×85) |
| notes | metadata | categorical | *Not specified.* | n=85, missing=0, classes=1, top Raman Processed, common-axis subset, no interpolation (×85) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/zipped_data_files/raman/excellent_oriented.zip`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.rruff.net/about/download-data/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Le RRUFFID identifie le spécimen ; le suffixe de sample_name distingue des configurations. En Raman : 12 spécimens, 30 libellés/configurations et 85 acquisitions avec orientations variées. Ne pas transformer ces orientations en répétitions techniques identiques.
- **Curated views:** M: 1 fields, Y: 3 fields, passport: 20 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `fca1c66c300ed137e7d3b12e281a2defbb24179dea61c4dc01a2b0d04d352892`
- **Processing hash:** `1179462b7342e924a5e83f6198436ab36ccec8fe2520bfc0b15cb5ec2e9e9382` | **metadata hash:** `8df3df737f8ba6abecb1d8e1d8e25d6eefacbd28c51249da9e82b2f9e0c9ded1`

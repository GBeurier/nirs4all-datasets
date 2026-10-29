# Datasheet — Mendeley specialty coffee green roasted FT-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** mendeley
- **Description:** Mendeley specialty coffee green roasted FT-NIR. v2.0 standardized NIRS package: 2 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, mendeley
- **Contributor:** Fourier Transform Near Infrared (FT-NIR) spectra and sensory scores in green and roasted specialty coffee for machine learning-based quality monitoring

## Composition

- **Alignment:** sample level; 64 sample(s), 384 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 3–3 (mean 3).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X1 | green coffee raw FT-NIR | FT-NIR spectrometer | NIR | 4000–1.2e+04 cm-1 | 192 | 2001 |
| X2 | roasted coffee raw FT-NIR | FT-NIR spectrometer | NIR | 4000–1.2e+04 cm-1 | 192 | 2001 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Cup_quality_points | target | numeric | *Not specified.* | n=192, missing=0, range 80–88, mean 84.44 ± 1.849 |
| replicate | metadata | numeric | *Not specified.* | n=192, missing=0, range 1–3, mean 2 ± 0.8186 |
| api_url | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/nz2fr76trm/snapshot/3 (×192) |
| files_api_url | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top https://data.mendeley.com/public-api/datasets/nz2fr76trm/files?folder_id=root&version=3&$start=0&$limit=1000 (×192) |
| article_url | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340925003415 (×192) |
| doi_dataset | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top 10.17632/nz2fr76trm.3 (×192) |
| license | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×192) |
| license_id | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top cc-by-4.0 (×192) |
| license_url | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×192) |
| rights_status | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top explicit_open (×192) |
| usage_scope | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top public_reuse_possible (×192) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top True (×192) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top FT-NIR (×192) |
| axis_unit | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top cm^-1 (×192) |
| axis_min | metadata | numeric | *Not specified.* | n=192, missing=0, range 1.2e+04–1.2e+04, mean 1.2e+04 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=192, missing=0, range 4000–4000, mean 4000 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=192, missing=0, range 2001–2001, mean 2001 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=192, missing=0, classes=1, top Aligned raw FT-NIR spectra for green and roasted coffee with roasted coffee sensory cup quality. (×192) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/datasets/nz2fr76trm/3`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/nz2fr76trm/snapshot/3`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.mendeley.com/public-api/datasets/nz2fr76trm/files?folder_id=root&version=3&$start=0&$limit=1000`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M ; les fréquences de cet identifiant décrivent les lignes exportées, sans établir des répétitions techniques. Champs d’index examinés : replicate. Le nombre de niveaux d’un facteur Rep n’est pas utilisé comme nombre de spectres par échantillon.
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 23 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Mendeley Data record is licensed CC BY 4.0; redistribution/publication reuse allowed with attribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `504b712bebe2516ce86b721f73995526e9a2adaf51d4eba7be28436f6907bb2a`
- **Processing hash:** `5b5316a167f51ac059aed1216df98be9f8a6a357ebbb72ce4fd8224fce3792ab` | **metadata hash:** `0061d2ada9c72f53133c9df327f45304cc19061c4f9c30f86c861e9605182dea`

# Datasheet — Recherche Data Gouv fresh dried poultry cattle manure NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv fresh dried poultry cattle manure NIR. v2.0 standardized NIRS package: 2 spectral source(s), 8 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Dataset of chemical and Near-Infrared spectroscopy measurements of fresh and dried poultry and cattle manure

## Composition

- **Alignment:** sample level; 332 sample(s), 664 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_DG | DG standardized NIR absorbance | XDS Foss DG standardized by PDS | NIR | 1100–2498 nm | 332 | 700 |
| X_FH | FH standardized NIR absorbance | XDS Foss FH standardized by PDS | NIR | 1100–2498 nm | 332 | 700 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| type_manure | target | categorical | *Not specified.* | n=332, missing=0, classes=2, top cattle manure (×196) |
| DM | target | numeric | *Not specified.* | n=332, missing=0, range 11.26–82.48, mean 37.29 ± 20.06 |
| NH4 | target | numeric | *Not specified.* | n=332, missing=0, range 0.001–1.086, mean 0.2624 ± 0.2765 |
| N | target | numeric | *Not specified.* | n=332, missing=0, range 0.255–4.152, mean 1.369 ± 1.093 |
| CaO | target | numeric | *Not specified.* | n=332, missing=174, range 0.094–3.108, mean 0.5749 ± 0.5563 |
| K2O | target | numeric | *Not specified.* | n=332, missing=174, range 0.187–3.845, mean 1.022 ± 0.6479 |
| MgO | target | numeric | *Not specified.* | n=332, missing=174, range 0.062–1.054, mean 0.2266 ± 0.1862 |
| P2O5 | target | numeric | *Not specified.* | n=332, missing=174, range 0.091–3.02, mean 0.4767 ± 0.5851 |
| standard_cells_file | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top spectra_standard_cells.tab (×332) |
| api_url | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.15454/JIGO8R (×332) |
| article_url | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340920315274 (×332) |
| doi_dataset | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top 10.15454/JIGO8R (×332) |
| doi_publication | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top 10.1016/j.dib.2020.106647 (×332) |
| license | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Creative Commons Zero v1.0 Universal (×332) |
| license_id | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top cc0-1.0 (×332) |
| license_url | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top https://creativecommons.org/publicdomain/zero/1.0/ (×332) |
| rights_status | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top explicit_open (×332) |
| usage_scope | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top public_domain (×332) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top True (×332) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top NIR (×332) |
| axis_unit | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top nm (×332) |
| axis_min | metadata | numeric | *Not specified.* | n=332, missing=0, range 1100–1100, mean 1100 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=332, missing=0, range 2498–2498, mean 2498 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=332, missing=0, range 700–700, mean 700 ± 0 |
| signal_type | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top absorbance standardized by PDS (×332) |
| decoder | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top pandas.read_excel/openpyxl (×332) |
| notes | metadata | categorical | *Not specified.* | n=332, missing=0, classes=1, top Three main original-format Dataverse files are OOXML Excel workbooks despite .tab extensions, standard cells retained in raw manifest only. (×332) |
| spectrometer | metadata | categorical | *Not specified.* | n=332, missing=0, classes=3, top NIRFlex LDAR (×156) |
| township | metadata | categorical | *Not specified.* | n=332, missing=0, classes=114, top SAINT PAUL (×23) |
| country | metadata | categorical | *Not specified.* | n=332, missing=0, classes=2, top mainland France (×252) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Portail Data INRAE — kind `dataverse`, access `open`, license *Not specified.*: `10.15454/JIGO8R`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/publicdomain/zero/1.0/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.sciencedirect.com/science/article/pii/S2352340920315274`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Dataverse API terms report Creative Commons CC0 license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `821448bc77e70f69c886e7e030723be0d7de58b32f9c4a0e81f50ffede8d26a2`
- **Processing hash:** `30ebf048011538c7f843b22c10320f87e3cd76ba7ecd38d08eae882c27aee8aa` | **metadata hash:** `4ab8cd68f1c29b86c8961f064cad042c79e3618a5ef63956d6eb564e90486208`

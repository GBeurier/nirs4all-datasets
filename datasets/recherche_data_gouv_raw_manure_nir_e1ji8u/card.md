# Datasheet — Recherche Data Gouv raw cattle poultry pig manure NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv raw cattle poultry pig manure NIR. v2.0 standardized NIRS package: 1 spectral source(s), 9 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** A dataset of the chemical composition and near-infrared spectroscopy measurements of raw cattle, poultry and pig manure

## Composition

- **Alignment:** sample level; 490 sample(s), 490 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Q-interline AgriQuant B8 NIR absorbance | Q-interline AgriQuant B8 | NIR | 852.8–2502 nm | 490 | 1003 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Manure_type | target | categorical | *Not specified.* | n=490, missing=0, classes=6, top Cattle manure (×276) |
| DM | target | numeric | *Not specified.* | n=490, missing=0, range 12.2–90.8, mean 28.94 ± 15.94 |
| OM | target | numeric | *Not specified.* | n=490, missing=0, range 83.3–765.2, mean 215.1 ± 121 |
| AN | target | numeric | *Not specified.* | n=490, missing=0, range 0.01–12.99, mean 2.319 ± 2.758 |
| Total_N | target | numeric | *Not specified.* | n=490, missing=0, range 2.07–40.48, mean 9.575 ± 7.459 |
| P2O5 | target | numeric | *Not specified.* | n=490, missing=0, range 0.84–43.72, mean 7.976 ± 8.373 |
| K2O | target | numeric | *Not specified.* | n=490, missing=0, range 0.66–47.72, mean 10.55 ± 6.976 |
| CaO | target | numeric | *Not specified.* | n=490, missing=0, range 1.53–145.5, mean 13.33 ± 20.09 |
| MgO | target | numeric | *Not specified.* | n=490, missing=0, range 0.52–18.76, mean 3.386 ± 2.661 |
| api_url | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.15454/E1JI8U (×490) |
| article_url | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340921007563 (×490) |
| doi_dataset | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top 10.15454/E1JI8U (×490) |
| doi_publication | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top 10.1016/j.dib.2021.107304 (×490) |
| license | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top Etalab Open License 2.0 (×490) |
| license_id | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top etalab-2.0 (×490) |
| license_url | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×490) |
| rights_status | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top explicit_open (×490) |
| usage_scope | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top public_reuse_possible (×490) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top True (×490) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top NIR (×490) |
| axis_unit | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top nm (×490) |
| axis_min | metadata | numeric | *Not specified.* | n=490, missing=0, range 852.8–852.8, mean 852.8 ± 1.138e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=490, missing=0, range 2502–2502, mean 2502 ± 4.552e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=490, missing=0, range 1003–1003, mean 1003 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top Q-interline AgriQuant B8 (×490) |
| signal_type | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top absorbance (×490) |
| decoder | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top pandas.read_csv + pandas.read_excel/openpyxl (×490) |
| notes | metadata | categorical | *Not specified.* | n=490, missing=0, classes=1, top Spectra original-format file is comma-separated with decimal comma, chemical original-format file is OOXML Excel under a .tab extension. (×490) |
| LAT_WGS84 | metadata | numeric | *Not specified.* | n=490, missing=11, range 47.38–48.97, mean 48.03 ± 0.4279 |
| LONG_WGS84 | metadata | numeric | *Not specified.* | n=490, missing=11, range -4.826–-1.129, mean -2.586 ± 0.8685 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Portail Data INRAE — kind `dataverse`, access `open`, license *Not specified.*: `10.15454/E1JI8U`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://spdx.org/licenses/etalab-2.0.html`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.sciencedirect.com/science/article/pii/S2352340921007563`
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
- **Redistribution rights:** Official Recherche Data Gouv page reports Etalab Open License 2.0, compatible CC-BY 2.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `e484dd522ac40d18e7f0491921d36ae266d0b76de02df52db06d07af7be7bfc9`
- **Processing hash:** `7e09af8f14f3a2bde4807a0a26f0dfbf76d979db18b437e5aa13d569d63029e6` | **metadata hash:** `aa75c639fdcb5cb922840c83e1f9c07038a98a89da87cda85cf5f112723df6b7`

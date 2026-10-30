# Datasheet — Recherche Data Gouv oilseed rape tissue FT-NIR nitrogen carbon

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv oilseed rape tissue FT-NIR nitrogen carbon. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Dataset of near-infrared spectroscopy measurements of rapeseed ground organs to predict nitrogen and carbon content

## Composition

- **Alignment:** sample level; 2427 sample(s), 2427 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Bruker MPA FT-NIR absorbance | Bruker MPA FT-NIR | NIR | 3595–1.249e+04 cm-1 | 2427 | 1154 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| N content (%DM) | target | numeric | *Not specified.* | n=2427, missing=0, range 0.19–5.95, mean 2.199 ± 1.465 |
| C content (%DM) | target | numeric | *Not specified.* | n=2427, missing=0, range 4.83–60.26, mean 42.41 ± 3.277 |
| Tissue | target | categorical | *Not specified.* | n=2427, missing=0, classes=5, top Leaves (×771) |
| N regime | target | categorical | *Not specified.* | n=2427, missing=0, classes=2, top N+ (×1434) |
| W regime | target | categorical | *Not specified.* | n=2427, missing=0, classes=2, top W+ (×2187) |
| Growth condition | target | categorical | *Not specified.* | n=2427, missing=0, classes=2, top Tunnel (×1585) |
| api_url | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.57745/6VYUQN (×2427) |
| article_url | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top https://www.sciencedirect.com/science/article/pii/S2352340924011259 (×2427) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top 10.57745/6VYUQN (×2427) |
| doi_publication | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top 10.1016/j.dib.2024.110936 (×2427) |
| license | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top Etalab Open License 2.0 (×2427) |
| license_id | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top etalab-2.0 (×2427) |
| license_url | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×2427) |
| rights_status | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top explicit_open (×2427) |
| usage_scope | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top public_reuse_possible (×2427) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top True (×2427) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top FT-NIR (×2427) |
| axis_unit | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top cm^-1 (×2427) |
| axis_min | metadata | numeric | *Not specified.* | n=2427, missing=0, range 3595–3595, mean 3595 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2427, missing=0, range 1.249e+04–1.249e+04, mean 1.249e+04 ± 1.819e-12 |
| n_points_original | metadata | numeric | *Not specified.* | n=2427, missing=0, range 1154–1154, mean 1154 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top Bruker MPA FT-NIR (×2427) |
| signal_type | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top absorbance (×2427) |
| decoder | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top pandas.read_csv(sep=',', decimal=',') (×2427) |
| notes | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=1, top Spectral axis is descending wavenumber from source headers. (×2427) |
| Sample_ID | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=2427, top 15_N1S1_03-19_Res_1 (×1) |
| Accession | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=63, top Aviso (×445) |
| Growth season | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=3, top 2014-2015 (×1984) |
| BBCH dev. stage | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=7, top 31-35 (×964) |
| N_model_set-type | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=3, top Val (×1207) |
| C_model_set-type | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=3, top Cal (×1210) |
| Spectra_acquisition_year | metadata | numeric | *Not specified.* | n=2427, missing=0, range 2017–2017, mean 2017 ± 0 |
| Cup_type | metadata | categorical | *Not specified.* | n=2427, missing=0, classes=2, top Fix (×2236) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Recherche Data Gouv — kind `dataverse`, access `open`, license *Not specified.*: `10.57745/6VYUQN`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://spdx.org/licenses/etalab-2.0.html`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 3 fields, Y: 6 fields, measurements: 0 fields, passport: 27 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Dataverse API reports Etalab Open License 2.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `dcd44de74d833a45b34883aaec4a476ee1e31d28014f2f6b78738c7fe97cf977`
- **Processing hash:** `366b8c5db8addafcf9d8df5696675d681461edb72a93c90a6c90e4bdc7cdd907` | **metadata hash:** `dd4c9581c2958fc18c45e0c00ed67680e7cded33864b27d9f34bd4a73cb6aea6`

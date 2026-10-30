# Datasheet — Recherche Data Gouv grapevine leaf MicroNIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv grapevine leaf MicroNIR. v2.0 standardized NIRS package: 1 spectral source(s), 7 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Robustness of high-throughput prediction of leaf ecophysiological traits using NIRS and poro-fluorometry

## Composition

- **Alignment:** sample level; 2408 sample(s), 2408 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | MicroNIR leaf spectra | MicroNIR | NIR | 908.1–1676 nm | 2408 | 125 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=2408, missing=22, range 1.429–7.974, mean 4.597 ± 0.9574 |
| WCf | target | numeric | *Not specified.* | n=2408, missing=965, range 0.6061–0.8584, mean 0.7293 ± 0.0317 |
| WQ | target | numeric | *Not specified.* | n=2408, missing=965, range 41.1–189.5, mean 86.41 ± 17.04 |
| An | target | numeric | *Not specified.* | n=2408, missing=2292, range 0.05647–18.62, mean 6.71 ± 3.915 |
| PSI | target | numeric | *Not specified.* | n=2408, missing=2295, range -1.966–-0.26, mean -0.9737 ± 0.3884 |
| WUEintr | target | numeric | *Not specified.* | n=2408, missing=2295, range 14.13–187.6, mean 90.15 ± 36.92 |
| WUEinst | target | numeric | *Not specified.* | n=2408, missing=2295, range 0.8329–12.39, mean 4.321 ± 1.991 |
| api_url | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.57745/WVAPOL (×2408) |
| article_url | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top https://doi.org/10.1002/ppj2.70059 (×2408) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top 10.57745/WVAPOL (×2408) |
| doi_publication | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top 10.1002/ppj2.70059 (×2408) |
| license | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top Etalab Open License 2.0 (×2408) |
| license_id | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top etalab-2.0 (×2408) |
| license_url | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×2408) |
| rights_status | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top explicit_open (×2408) |
| usage_scope | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top public_reuse_possible (×2408) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top True (×2408) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top NIR (×2408) |
| axis_unit | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top nm (×2408) |
| axis_min | metadata | numeric | *Not specified.* | n=2408, missing=0, range 908.1–908.1, mean 908.1 ± 1.137e-13 |
| axis_max | metadata | numeric | *Not specified.* | n=2408, missing=0, range 1676–1676, mean 1676 ± 4.548e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=2408, missing=0, range 125–125, mean 125 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top MicroNIR (×2408) |
| signal_type | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top source NIRS value (×2408) |
| decoder | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top pandas.read_csv(sep=',', decimal=',') (×2408) |
| notes | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=1, top Traits/design/covariates joined by Leaf_ID when present. ASD source contains one duplicated Leaf_ID retained as separate observations. (×2408) |
| Experiment | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=2, top Greenhouse (×1560) |
| Phenotyping_type | metadata | categorical | *Not specified.* | n=2408, missing=0, classes=2, top HT (×2292) |
| IDVar | metadata | categorical | *Not specified.* | n=2408, missing=849, classes=246, top V1576 (×13) |
| Water_treatment | metadata | categorical | *Not specified.* | n=2408, missing=849, classes=3, top WW (×525) |
| Date_leaf_measurement | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=23, top 03/06/2022 (×92) |
| Nb_min_since_8am | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=1051, top 241.8 (×5) |
| Nb_min_since_last_irrigation | metadata | categorical | *Not specified.* | n=2408, missing=1005, classes=1259, top 1084.8 (×3) |
| Temp_mean_arch | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=72, top 23.696739665618 (×92) |
| Hr_mean_arch | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=72, top 68.1819247646913 (×92) |
| PPFD_mean_arch | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=72, top 232.279047090758 (×92) |
| VPD_mean_arch | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=72, top 0.99718785582584 (×92) |
| Duration_from_entry_to_measure | metadata | categorical | *Not specified.* | n=2408, missing=998, classes=37, top 32.0 (×156) |
| Plant_density_mean | metadata | categorical | *Not specified.* | n=2408, missing=1001, classes=518, top 8.38095238095238 (×69) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Recherche Data Gouv — kind `dataverse`, access `open`, license *Not specified.*: `10.57745/WVAPOL`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://spdx.org/licenses/etalab-2.0.html`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 13 fields, Y: 7 fields, measurements: 0 fields, passport: 23 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `06fcd933389770af7e4bacffb11106f7de5158c64c6813a7f93db9fc669d1c1d`
- **Processing hash:** `f10e06773aedabcf5a30da0a0045377c48444486154ed6f6f8eb57fced0ae37d` | **metadata hash:** `6883b9db571e6245afffa33181175131867550e039f5a7b1ef5437621acb5d69`

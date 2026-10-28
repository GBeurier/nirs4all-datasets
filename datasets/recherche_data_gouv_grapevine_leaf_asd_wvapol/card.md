# Datasheet — Recherche Data Gouv grapevine leaf ASD

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv grapevine leaf ASD. v2.0 standardized NIRS package: 1 spectral source(s), 7 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Robustness of high-throughput prediction of leaf ecophysiological traits using NIRS and poro-fluorometry

## Composition

- **Alignment:** sample level; 2394 sample(s), 2395 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–2 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | ASD dried leaf spectra | ASD | NIR | 400–2500 nm | 2395 | 2101 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=2394, missing=10, range 1.429–9.251, mean 4.601 ± 0.9612 |
| WCf | target | numeric | *Not specified.* | n=2394, missing=945, range 0.6061–0.8584, mean 0.7294 ± 0.0317 |
| WQ | target | numeric | *Not specified.* | n=2394, missing=945, range 41.1–189.5, mean 86.39 ± 17.04 |
| An | target | numeric | *Not specified.* | n=2394, missing=2282, range 0.05647–16.47, mean 6.3 ± 3.579 |
| PSI | target | numeric | *Not specified.* | n=2394, missing=2285, range -1.966–-0.26, mean -0.9652 ± 0.3972 |
| WUEintr | target | numeric | *Not specified.* | n=2394, missing=2285, range 14.13–187.6, mean 90.45 ± 36.42 |
| WUEinst | target | numeric | *Not specified.* | n=2394, missing=2285, range 0.8329–12.39, mean 4.322 ± 2.012 |
| api_url | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.57745/WVAPOL (×2394) |
| article_url | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top https://doi.org/10.1002/ppj2.70059 (×2394) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top 10.57745/WVAPOL (×2394) |
| doi_publication | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top 10.1002/ppj2.70059 (×2394) |
| license | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top Etalab Open License 2.0 (×2394) |
| license_id | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top etalab-2.0 (×2394) |
| license_url | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×2394) |
| rights_status | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top explicit_open (×2394) |
| usage_scope | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top public_reuse_possible (×2394) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top True (×2394) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top NIR (×2394) |
| axis_unit | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top nm (×2394) |
| axis_min | metadata | numeric | *Not specified.* | n=2394, missing=0, range 400–400, mean 400 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2394, missing=0, range 2500–2500, mean 2500 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2394, missing=0, range 2101–2101, mean 2101 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top ASD (×2394) |
| signal_type | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top source NIRS value (×2394) |
| decoder | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top pandas.read_csv(sep=',', decimal=',') (×2394) |
| notes | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=1, top Traits/design/covariates joined by Leaf_ID when present. ASD source contains one duplicated Leaf_ID retained as separate observations. (×2394) |
| Experiment | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=2, top Greenhouse (×1561) |
| Phenotyping_type | metadata | categorical | *Not specified.* | n=2394, missing=0, classes=2, top HT (×2282) |
| IDVar | metadata | categorical | *Not specified.* | n=2394, missing=833, classes=246, top V1576 (×15) |
| Water_treatment | metadata | categorical | *Not specified.* | n=2394, missing=833, classes=3, top WW (×526) |
| Date_leaf_measurement | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=23, top 03/06/2022 (×92) |
| Nb_min_since_8am | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=1051, top 241.8 (×5) |
| Nb_min_since_last_irrigation | metadata | categorical | *Not specified.* | n=2394, missing=991, classes=1259, top 1084.8 (×3) |
| Temp_mean_arch | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=72, top 23.696739665618 (×92) |
| Hr_mean_arch | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=72, top 68.1819247646913 (×92) |
| PPFD_mean_arch | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=72, top 232.279047090758 (×92) |
| VPD_mean_arch | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=72, top 0.99718785582584 (×92) |
| Duration_from_entry_to_measure | metadata | categorical | *Not specified.* | n=2394, missing=984, classes=37, top 32.0 (×156) |
| Plant_density_mean | metadata | categorical | *Not specified.* | n=2394, missing=987, classes=518, top 8.38095238095238 (×69) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Recherche Data Gouv — kind `dataverse`, access `open`, license *Not specified.*: `10.57745/WVAPOL`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://spdx.org/licenses/etalab-2.0.html`
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
- **Redistribution rights:** Dataverse API reports Etalab Open License 2.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `e755301a31281e663f66be260defe9b5a467e3a9ab151d36b2535d5a1386011b`
- **Processing hash:** `61b92d616083690c052584ea2008c306b21a23032d8e7b614c8444c7621b8b0f` | **metadata hash:** `ab5d803e9828baa32ab1cb82e67c04730668c32f17304464ced4689c871c82c9`

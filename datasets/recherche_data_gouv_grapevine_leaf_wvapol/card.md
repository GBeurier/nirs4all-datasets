# Datasheet — Recherche Data Gouv grapevine leaf traits, ASD, MicroNIR and NeoSpectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv grapevine leaf traits, ASD, MicroNIR and NeoSpectra. Origin database composed from 3 standardized v2.0 leaves: 3 spectral source(s), 7 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Robustness of high-throughput prediction of leaf ecophysiological traits using NIRS and poro-fluorometry

## Composition

- **Alignment:** sample level; 2427 sample(s), 6919 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–2 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_asd | ASD dried leaf spectra | ASD | NIR | 400–2500 nm | 2395 | 2101 |
| X_micronir | MicroNIR leaf spectra | MicroNIR | NIR | 908.1–1676 nm | 2408 | 125 |
| X_neospectra | NeoSpectra leaf spectra | NeoSpectra | NIR | 1350–2550 nm | 2116 | 257 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=6919, missing=50, range 1.429–9.251, mean 4.591 ± 0.959 |
| WCf | target | numeric | *Not specified.* | n=6919, missing=2583, range 0.6061–0.8584, mean 0.7293 ± 0.0317 |
| WQ | target | numeric | *Not specified.* | n=6919, missing=2583, range 41.1–189.5, mean 86.4 ± 17.04 |
| An | target | numeric | *Not specified.* | n=6919, missing=6572, range 0.05647–18.62, mean 6.563 ± 3.802 |
| PSI | target | numeric | *Not specified.* | n=6919, missing=6580, range -1.966–-0.26, mean -0.9718 ± 0.3913 |
| WUEintr | target | numeric | *Not specified.* | n=6919, missing=6581, range 14.13–187.6, mean 90.26 ± 36.48 |
| WUEinst | target | numeric | *Not specified.* | n=6919, missing=6581, range 0.8329–12.39, mean 4.319 ± 1.983 |
| api_url | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.57745/WVAPOL (×6919) |
| article_url | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top https://doi.org/10.1002/ppj2.70059 (×6919) |
| doi_dataset | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top 10.57745/WVAPOL (×6919) |
| doi_publication | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top 10.1002/ppj2.70059 (×6919) |
| license | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top Etalab Open License 2.0 (×6919) |
| license_id | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top etalab-2.0 (×6919) |
| license_url | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×6919) |
| rights_status | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top explicit_open (×6919) |
| usage_scope | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top public_reuse_possible (×6919) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top True (×6919) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top NIR (×6919) |
| axis_unit | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top nm (×6919) |
| axis_min | metadata | numeric | *Not specified.* | n=6919, missing=0, range 400–1350, mean 867.4 ± 384 |
| axis_max | metadata | numeric | *Not specified.* | n=6919, missing=0, range 1676–2550, mean 2229 ± 404.1 |
| n_points_original | metadata | numeric | *Not specified.* | n=6919, missing=0, range 125–2101, mean 849.4 ± 912.3 |
| instrument_name | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=3, top MicroNIR (×2408) |
| signal_type | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top source NIRS value (×6919) |
| decoder | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top pandas.read_csv(sep=',', decimal=',') (×6919) |
| notes | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=1, top Traits/design/covariates joined by Leaf_ID when present. ASD source contains one duplicated Leaf_ID retained as separate observations. (×6919) |
| Experiment | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=2, top Greenhouse (×4685) |
| Phenotyping_type | metadata | categorical | *Not specified.* | n=6919, missing=0, classes=2, top HT (×6572) |
| IDVar | metadata | categorical | *Not specified.* | n=6919, missing=2236, classes=246, top V1576 (×43) |
| Water_treatment | metadata | categorical | *Not specified.* | n=6919, missing=2236, classes=3, top WW (×1578) |
| Date_leaf_measurement | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=23, top 03/06/2022 (×276) |
| Nb_min_since_8am | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=1051, top 241.8 (×15) |
| Nb_min_since_last_irrigation | metadata | categorical | *Not specified.* | n=6919, missing=2709, classes=1259, top 1084.8 (×9) |
| Temp_mean_arch | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=72, top 23.696739665618 (×276) |
| Hr_mean_arch | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=72, top 68.1819247646913 (×276) |
| PPFD_mean_arch | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=72, top 232.279047090758 (×276) |
| VPD_mean_arch | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=72, top 0.99718785582584 (×276) |
| Duration_from_entry_to_measure | metadata | categorical | *Not specified.* | n=6919, missing=2688, classes=37, top 32.0 (×468) |
| Plant_density_mean | metadata | categorical | *Not specified.* | n=6919, missing=2697, classes=518, top 8.38095238095238 (×207) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Recherche Data Gouv — kind `dataverse`, access `open`, license *Not specified.*: `10.57745/WVAPOL`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M; frequencies of this identifier describe exported rows without establishing technical replicates.
- **Curated views:** M: 14 fields, Y: 7 fields, passport: 22 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `fd046afd18be97f74a046eb65e1df650cbeb4b3a254d1e1549eee8072ce40cd9`
- **Processing hash:** `fdee0227c529160be0419683da24c9f7da61b25d1a23cfb92c5bf78a9afa8989` | **metadata hash:** `b8297830d48b79312749922a619225b12b7f26a4ed55908c0ce47c483a7d9f43`

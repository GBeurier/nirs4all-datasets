# Datasheet — Recherche Data Gouv grapevine leaf NeoSpectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** recherche
- **Description:** Recherche Data Gouv grapevine leaf NeoSpectra. v2.0 standardized NIRS package: 1 spectral source(s), 7 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, recherche
- **Contributor:** Robustness of high-throughput prediction of leaf ecophysiological traits using NIRS and poro-fluorometry

## Composition

- **Alignment:** sample level; 2116 sample(s), 2116 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | NeoSpectra leaf spectra | NeoSpectra | NIR | 1350–2550 nm | 2116 | 257 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| LMA | target | numeric | *Not specified.* | n=2116, missing=18, range 1.429–9.251, mean 4.572 ± 0.9587 |
| WCf | target | numeric | *Not specified.* | n=2116, missing=673, range 0.6061–0.8584, mean 0.7293 ± 0.03174 |
| WQ | target | numeric | *Not specified.* | n=2116, missing=673, range 41.1–189.5, mean 86.4 ± 17.06 |
| An | target | numeric | *Not specified.* | n=2116, missing=1997, range 0.05647–18.62, mean 6.667 ± 3.912 |
| PSI | target | numeric | *Not specified.* | n=2116, missing=1999, range -1.966–-0.26, mean -0.9761 ± 0.3917 |
| WUEintr | target | numeric | *Not specified.* | n=2116, missing=2000, range 14.13–187.6, mean 90.18 ± 36.42 |
| WUEinst | target | numeric | *Not specified.* | n=2116, missing=2000, range 0.8329–12.39, mean 4.314 ± 1.964 |
| api_url | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top https://entrepot.recherche.data.gouv.fr/api/datasets/:persistentId/?persistentId=doi:10.57745/WVAPOL (×2116) |
| article_url | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top https://doi.org/10.1002/ppj2.70059 (×2116) |
| doi_dataset | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top 10.57745/WVAPOL (×2116) |
| doi_publication | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top 10.1002/ppj2.70059 (×2116) |
| license | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top Etalab Open License 2.0 (×2116) |
| license_id | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top etalab-2.0 (×2116) |
| license_url | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top https://spdx.org/licenses/etalab-2.0.html (×2116) |
| rights_status | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top explicit_open (×2116) |
| usage_scope | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top public_reuse_possible (×2116) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top True (×2116) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top NIR (×2116) |
| axis_unit | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top nm (×2116) |
| axis_min | metadata | numeric | *Not specified.* | n=2116, missing=0, range 1350–1350, mean 1350 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=2116, missing=0, range 2550–2550, mean 2550 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=2116, missing=0, range 257–257, mean 257 ± 0 |
| instrument_name | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top NeoSpectra (×2116) |
| signal_type | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top source NIRS value (×2116) |
| decoder | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top pandas.read_csv(sep=',', decimal=',') (×2116) |
| notes | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=1, top Traits/design/covariates joined by Leaf_ID when present. ASD source contains one duplicated Leaf_ID retained as separate observations. (×2116) |
| Experiment | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=2, top Greenhouse (×1563) |
| Phenotyping_type | metadata | categorical | *Not specified.* | n=2116, missing=0, classes=2, top HT (×1997) |
| IDVar | metadata | categorical | *Not specified.* | n=2116, missing=554, classes=246, top V1576 (×15) |
| Water_treatment | metadata | categorical | *Not specified.* | n=2116, missing=554, classes=3, top WW (×526) |
| Date_leaf_measurement | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=23, top 03/06/2022 (×92) |
| Nb_min_since_8am | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=1051, top 241.8 (×5) |
| Nb_min_since_last_irrigation | metadata | categorical | *Not specified.* | n=2116, missing=713, classes=1259, top 1100.6 (×3) |
| Temp_mean_arch | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=72, top 23.696739665618 (×92) |
| Hr_mean_arch | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=72, top 68.1819247646913 (×92) |
| PPFD_mean_arch | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=72, top 232.279047090758 (×92) |
| VPD_mean_arch | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=72, top 0.99718785582584 (×92) |
| Duration_from_entry_to_measure | metadata | categorical | *Not specified.* | n=2116, missing=706, classes=37, top 32.0 (×156) |
| Plant_density_mean | metadata | categorical | *Not specified.* | n=2116, missing=709, classes=518, top 8.38095238095238 (×69) |

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
- **Content hash:** `fd16cd048eac612d4431c84fc2fe08744941ffc630fb5ad91e9bbf904e1dcd17`
- **Processing hash:** `1ed2f8282391e8ed4dcf3037a77baf9b840cb975b752fe7f1a3253f4a7540341` | **metadata hash:** `bcf0789ba09a39684bbd3fb43e24955596968607cf2d7eee662109dae155808b`

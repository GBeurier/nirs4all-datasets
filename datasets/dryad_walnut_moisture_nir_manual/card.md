# Datasheet — Dryad walnut kernel moisture NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad walnut kernel moisture NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 136 sample(s), 136 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad walnut kernel moisture NIR | *Not specified.* | NIR | 780–2498 nm | 136 | 860 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| moisture_content_percent | target | numeric | *Not specified.* | n=136, missing=0, range 0.01195–0.09915, mean 0.05552 ± 0.01485 |
| split | metadata | categorical | *Not specified.* | n=136, missing=0, classes=2, top calibration (×102) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=136, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\walnut (×136) |
| manual_download_file | metadata | categorical | *Not specified.* | n=136, missing=0, classes=1, top Measured_value+Raw_spectral_data.xlsx (×136) |
| official_source_url | metadata | categorical | *Not specified.* | n=136, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.xksn02vfp (×136) |
| manual_download | metadata | categorical | *Not specified.* | n=136, missing=0, classes=1, top True (×136) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.xksn02vfp`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 7 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Manual download preserved as provenance; public reuse follows source Dryad dataset terms.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `01261d645216b6cb34a0ec59f71b857c0849de290fe577f3844f5ba291735471`
- **Processing hash:** `ce536cf97a3ae1949c654d938c7946815e0ee36d47b496987a5d8b3d7bf9554e` | **metadata hash:** `2f436ce0b2821f1a16cbe94217af98188d2a295d576b321c4ad806344a68fa4b`

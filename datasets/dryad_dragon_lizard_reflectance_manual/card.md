# Datasheet — Dragon lizard reflectance spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dragon lizard reflectance spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD dragon lizard

## Composition

- **Alignment:** sample level; 137 sample(s), 137 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 300–2110 nm | 137 | 906 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| condition | target | categorical | *Not specified.* | n=137, missing=0, classes=4, top 15C (×60) |
| animal_id | metadata | categorical | *Not specified.* | n=137, missing=0, classes=12, top M11 (×12) |
| body_region | metadata | categorical | *Not specified.* | n=137, missing=0, classes=5, top Beard (×45) |
| experiment | metadata | categorical | *Not specified.* | n=137, missing=0, classes=2, top temperature_dependent (×114) |
| manual_download | metadata | categorical | *Not specified.* | n=137, missing=0, classes=1, top True (×137) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=137, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\dragon lizard (×137) |
| manual_download_file | metadata | categorical | *Not specified.* | n=137, missing=0, classes=1, top doi_10_5061_dryad_t34qq__v20160513.zip::Raw reflectance XLS (×137) |
| official_source_url | metadata | categorical | *Not specified.* | n=137, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.t34qq (×137) |
| standardization_batch | metadata | categorical | *Not specified.* | n=137, missing=0, classes=1, top v0.8.60 (×137) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.t34qq`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC0-1.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0ee85d79338acd470533a628fd0f540455de4b07e6b7c1f9c8b85551184bc316`
- **Processing hash:** `c100fdf564d9823504c1c4dfb2239c7689d2cd106f19f33f5bf0f7b67a0a4b20` | **metadata hash:** `5184c06ed9d7964d8a3d2ea5eb272bb262d3aad11a6b224b67e7e9049c5f8613`

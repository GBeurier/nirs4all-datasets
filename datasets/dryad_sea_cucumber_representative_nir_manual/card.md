# Datasheet — Sea cucumber representative NIR spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Sea cucumber representative NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** DRYAD sea cucumber

## Composition

- **Alignment:** sample level; 61 sample(s), 61 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 800.4–2500 nm | 61 | 3439 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| class | target | categorical | *Not specified.* | n=61, missing=0, classes=3, top YT (×27) |
| class_label | metadata | categorical | *Not specified.* | n=61, missing=0, classes=3, top YT (×27) |
| manual_download | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top True (×61) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\see cucumber (×61) |
| manual_download_file | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top representative+original+spectra.rar (×61) |
| official_source_url | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.n1066 (×61) |
| standardization_batch | metadata | categorical | *Not specified.* | n=61, missing=0, classes=1, top v0.8.58 (×61) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.n1066`
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
- **Redistribution rights:** Dryad source recorded as CC0-1.0 in blocked inventory; manual RAR download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `b8742ff575b3dfa95782db7016f39fbb8e1a675033a593e15fffd7da46fb9368`
- **Processing hash:** `03137031ba02716c0662510148a0808c6fa7db15ffdc8cb6a0f06e96f67d94e4` | **metadata hash:** `c86b07fd0cb4c4eab2cd3227edba62d2ebe2b92bbc72361883adb3f1e9a2ca3f`

# Datasheet — Blueberry phenomics NIR spectra

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** wiley
- **Description:** Blueberry phenomics NIR spectra. v2.0 standardized NIRS package: 1 spectral source(s), 2 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, wiley
- **Contributor:** TPPJ / Wiley supplement blueberry

## Composition

- **Alignment:** sample level; 351 sample(s), 351 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | X | *Not specified.* | NIR | 920.5–1676 nm | 351 | 123 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Bloom | target | numeric | *Not specified.* | n=351, missing=0, range 2.644–3.876, mean 3.534 ± 0.2384 |
| Firmness | target | numeric | *Not specified.* | n=351, missing=0, range 177.5–390, mean 265.6 ± 30.14 |
| genotype | metadata | categorical | *Not specified.* | n=351, missing=0, classes=351, top G_1 (×1) |
| manual_download | metadata | categorical | *Not specified.* | n=351, missing=0, classes=1, top True (×351) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=351, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\blueberry (×351) |
| manual_download_file | metadata | categorical | *Not specified.* | n=351, missing=0, classes=1, top ppj270010-sup-0001-suppmat.zip::bb_nir_dat.rda::pheno_nir (×351) |
| official_source_url | metadata | categorical | *Not specified.* | n=351, missing=0, classes=1, top https://acsess.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fppj2.70010&file=ppj270010-sup-0001-SuppMat.zip (×351) |
| standardization_batch | metadata | categorical | *Not specified.* | n=351, missing=0, classes=1, top v0.8.59 (×351) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://acsess.onlinelibrary.wiley.com/action/downloadSupplement?doi=10.1002%2Fppj2.70010&file=ppj270010-sup-0001-SuppMat.zip`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Wiley supplement reuse terms were not fully verified in the blocked inventory; manual download retained as provenance.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `2317d38defc0de3c5b752953f46f2f833fc7f8adcb8f361c4b46fe1b3c5e3604`
- **Processing hash:** `58ae9b73f8d78764c413162a7dd28d9656d2f01244bbe45c04044912ca642429` | **metadata hash:** `d5cd4a7c9dad5f950d5d24913a75dfd4ac7b1f3ec92f8bc92692ed1a83ab9c12`

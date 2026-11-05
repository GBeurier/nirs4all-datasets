# Datasheet — Hawaii avocado — benchtop NIR, SNV

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** dryad
- **Description:** Dryad Hawaii avocado bench-top SNV NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, dryad
- **Contributor:** Dryad manual download

## Composition

- **Alignment:** sample level; 199 sample(s), 199 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Dryad Hawaii avocado bench-top SNV NIR | *Not specified.* | NIR | 1000–2400 nm | 199 | 445 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Variety | target | categorical | *Not specified.* | n=199, missing=0, classes=3, top Sharwil (×115) |
| variety | metadata | categorical | *Not specified.* | n=199, missing=0, classes=3, top Sharwil (×115) |
| instrument_context | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top bench_top_NIRQuest_2022_SNV (×199) |
| manual_download_source_dir | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top D:\VS projects\nirs_db_vf\manual_download\advocado (×199) |
| manual_download_file | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top OO_All199_ave_SNV.xlsx (×199) |
| official_source_url | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top https://datadryad.org/dataset/doi:10.5061/dryad.98sf7m0rj (×199) |
| manual_download | metadata | categorical | *Not specified.* | n=199, missing=0, classes=1, top True (×199) |
| source_sample_id | metadata | categorical | *Not specified.* | n=199, missing=0, classes=199, top 11 (×1) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Dryad — kind `url`, access `open`, license *Not specified.*: `10.5061/dryad.98sf7m0rj`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 8 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `a75ffa58f343ce406e19cb00aa3d8ba270abc0be6ca75bed409d22c6883f36ca`
- **Processing hash:** `020b04e82559dd616d662fa97c58d10b0d0f5113a5c129b549f6d3768e95f139` | **metadata hash:** `cec3f20eb790bacf12d7fdb814659285d30dccc30998ee7b607606641f8a1d29`

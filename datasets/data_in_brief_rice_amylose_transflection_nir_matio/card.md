# Datasheet — Data in Brief rice amylose transflection NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** data
- **Description:** Data in Brief rice amylose transflection NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, data
- **Contributor:** Dataset of Near-infrared spectroscopy measurement for amylose determination using PLS algorithms

## Composition

- **Alignment:** sample level; 313 sample(s), 313 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | transflection_nir | MPA NIR transflection equipment | NIR | 3595–1.249e+04 cm-1 | 313 | 1154 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| amylose_percent | target | numeric | *Not specified.* | n=313, missing=0, range 0–33.75, mean 19.9 ± 5.293 |
| doi_publication | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top 10.1016/j.dib.2017.09.077 (×313) |
| license | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×313) |
| decoder | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top matio.load_from_mat(raw_data=False) (×313) |
| pmc_url | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top https://pmc.ncbi.nlm.nih.gov/articles/PMC5712058/ (×313) |
| license_id | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top cc-by-4.0 (×313) |
| license_url | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×313) |
| rights_status | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top explicit_open (×313) |
| usage_scope | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top public_reuse_possible (×313) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top True (×313) |
| instrument_name | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top MPA NIR transflection equipment (×313) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top NIR (×313) |
| signal_type | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top transflection_spectrum (×313) |
| axis_unit | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top cm^-1 (×313) |
| axis_min | metadata | numeric | *Not specified.* | n=313, missing=0, range 3595–3595, mean 3595 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=313, missing=0, range 1.249e+04–1.249e+04, mean 1.249e+04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=313, missing=0, range 1154–1154, mean 1154 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=313, missing=0, classes=1, top Xcal/Xtest and ycal/ytest concatenated, source split preserved. (×313) |
| source_split | metadata | categorical | *Not specified.* | n=313, missing=0, classes=2, top calibration (×203) |
| source_split_index | metadata | numeric | *Not specified.* | n=313, missing=0, range 1–203, mean 85.66 ± 55.54 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.sciencedirect.com/science/article/pii/S2352340917305176`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://pmc.ncbi.nlm.nih.gov/articles/PMC5712058/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Sample identifier declared in M
- **Curated views:** M: 0 fields, Y: 1 fields, passport: 23 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** PMC article page states open access under the CC BY license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.2.0 | **schema/protocol:** 2.0
- **Content hash:** `e6e0ed3ce3ed904283f5aced4499c2c927eb92d2d11c771f4c857f41357cb7d1`
- **Processing hash:** `21c158f3f209f516157e6ea516fad05636f1013b839f166a6dc047fcd2e3c420` | **metadata hash:** `949807bcfb27b02e4162a0756fe5d4f8b7e036531b8e4fa25122ef13e2c2ebdc`

# Datasheet — Zenodo tomato leaf stress Vis-NIR matio

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** zenodo
- **Description:** Zenodo tomato leaf stress Vis-NIR matio. v2.0 standardized NIRS package: 3 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, zenodo
- **Contributor:** Tomato leaf stress spectra

## Composition

- **Alignment:** sample level; 216 sample(s), 648 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_absorbance | absorbance | *Not specified.* | NIR | 394.9–1021 nm | 216 | 832 |
| X_reflectance | reflectance | *Not specified.* | NIR | 394.9–1021 nm | 216 | 832 |
| X_transmittance | transmittance | *Not specified.* | NIR | 394.9–1021 nm | 216 | 832 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| treatment | target | categorical | *Not specified.* | n=216, missing=0, classes=3, top c (×80) |
| par_condition | target | categorical | *Not specified.* | n=216, missing=0, classes=2, top PAR1000 (×108) |
| day_after_stress | target | categorical | *Not specified.* | n=216, missing=0, classes=4, top 4 (×72) |
| replicate | metadata | categorical | *Not specified.* | n=216, missing=0, classes=7, top r5 (×42) |
| leaf_sample | metadata | categorical | *Not specified.* | n=216, missing=0, classes=6, top L2 (×104) |
| doi_dataset | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top 10.5281/zenodo.12800065 (×216) |
| license | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top Creative Commons Attribution 4.0 International (×216) |
| license_id | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top cc-by-4.0 (×216) |
| license_url | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top https://creativecommons.org/licenses/by/4.0/ (×216) |
| rights_status | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top explicit_open (×216) |
| usage_scope | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top public_reuse_possible (×216) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top True (×216) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top Vis-NIR (×216) |
| axis_unit | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top nm (×216) |
| axis_min | metadata | numeric | *Not specified.* | n=216, missing=0, range 394.9–394.9, mean 394.9 ± 5.698e-14 |
| axis_max | metadata | numeric | *Not specified.* | n=216, missing=0, range 1021–1021, mean 1021 ± 3.419e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=216, missing=0, range 832–832, mean 832 ± 0 |
| decoder | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top mat-io/matio (×216) |
| notes | metadata | categorical | *Not specified.* | n=216, missing=0, classes=1, top MATLAB string labels decoded with matio load_from_mat(raw_data=False). (×216) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- Zenodo — kind `zenodo`, access `open`, license *Not specified.*: `https://zenodo.org/records/12800065`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://creativecommons.org/licenses/by/4.0/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Numbers r1…r7 are experimental factors; leaves and treatment levels remain distinct. No grouping by r alone.
- **Curated views:** M: 1 fields, Y: 3 fields, measurements: 0 fields, passport: 21 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Open per source license.

### Related publications

- *No related publication.*

## Distribution

- **License:** CC-BY-4.0
- **Tier:** public — Open — freely usable and redistributable under the stated license.
- **Redistribution rights:** Zenodo record reports CC BY 4.0.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `579615f13c9ea5ee881508fe62c16649565d9deefbec604bb3c8777ac7ec9911`
- **Processing hash:** `7c66029f565a3176b51b1d06fdbc2c6ec76fa659063b4f57611e14ea24e0d37c` | **metadata hash:** `e77c00e33f38da58f6d97c50febf1fa1678abcb1310256f8556eb6a7f9d35d67`

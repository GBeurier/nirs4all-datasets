# Datasheet — UCPH granules ambient moisture API NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH granules ambient moisture API NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** Granules NIR ambient moisture

## Composition

- **Alignment:** sample level; 648 sample(s), 648 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | granules NIR spectra | *Not specified.* | NIR | 3952–1.154e+04 cm-1 | 648 | 1899 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| api_reference_percent_w_w | target | numeric | *Not specified.* | n=648, missing=0, range 2–15, mean 8.75 ± 4.236 |
| measurement_state | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top ambient_moisture_before_moisturization (×648) |
| measurement_datetime_serial | metadata | categorical | *Not specified.* | n=648, missing=0, classes=648, top 738643.3824305555 (×1) |
| target_file | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top Granules_API_reference_ambient_moisture.mat (×648) |
| license | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top NOASSERTION (×648) |
| rights_status | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top manual_review_needed (×648) |
| usage_scope | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top internal_benchmark_only_until_license_review (×648) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top False (×648) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top NIR (×648) |
| axis_unit | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top cm-1 (×648) |
| axis_min | metadata | numeric | *Not specified.* | n=648, missing=0, range 3952–3952, mean 3952 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=648, missing=0, range 1.154e+04–1.154e+04, mean 1.154e+04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=648, missing=0, range 1899–1899, mean 1899 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top Bruker MPA II NIR, 8 cm-1 resolution, 64 scans, labels parsed from MATLAB dataset object. (×648) |
| original_split | metadata | categorical | *Not specified.* | n=648, missing=648, classes=0, — |
| nir_sample_id | metadata | categorical | *Not specified.* | n=648, missing=0, classes=18, top RHNapN_API02p00_RW1p0 (×36) |
| relative_humidity_percent | metadata | numeric | *Not specified.* | n=648, missing=0, range 0–0, mean 0 ± 0 |
| api_concentration_design_percent | metadata | numeric | *Not specified.* | n=648, missing=0, range 2–15, mean 8.75 ± 4.236 |
| riblet_mass_g | metadata | numeric | *Not specified.* | n=648, missing=0, range 1–2, mean 1.5 ± 0.4086 |
| solid_fraction | metadata | numeric | *Not specified.* | n=648, missing=0, range 0.7798–0.8219, mean 0.8036 ± 0.0113 |
| desiccator | metadata | categorical | *Not specified.* | n=648, missing=648, classes=0, — |
| batch_number | metadata | categorical | *Not specified.* | n=648, missing=0, classes=18, top RHNapN_API02p00_RW1p0 (×36) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://sid.erda.dk/share_redirect/ea3PYMcBzm/Granules.zip`
- *Not specified.* — kind `url`, access `manual`, license *Not specified.*: `https://ucphchemometrics.com/granulesnir/`
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
- **Redistribution rights:** No explicit redistribution license found on checked UCPH/ERDA source.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `4ffe93775a7c9680c58aa236b8eb5335f2027550ce5a6c46350b9893bdbf76d0`
- **Processing hash:** `aa87c7f9b106ed999791f159cea66957c9d1808f9dabf5b3b5803b00dd1a3934` | **metadata hash:** `d6e951674599f0484bed227a77b2638e8fa910254a61a4a0a480a6ade0b58126`

# Datasheet — UCPH granules moisture-controlled API NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ucph
- **Description:** UCPH granules moisture-controlled API NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ucph
- **Contributor:** Granules NIR moisture controlled

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
| measurement_state | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top after_moisture_control_desiccators (×648) |
| measurement_datetime_serial | metadata | categorical | *Not specified.* | n=648, missing=0, classes=648, top 738652.5135185185 (×1) |
| target_file | metadata | categorical | *Not specified.* | n=648, missing=0, classes=1, top Granules_API_reference_moisture_controlled.mat (×648) |
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
| original_split | metadata | categorical | *Not specified.* | n=648, missing=0, classes=2, top Cal (×432) |
| nir_sample_id | metadata | categorical | *Not specified.* | n=648, missing=0, classes=72, top RH11p0_API02p00_RW1p0 (×9) |
| relative_humidity_percent | metadata | numeric | *Not specified.* | n=648, missing=0, range 11–62, mean 37.25 ± 18.4 |
| api_concentration_design_percent | metadata | numeric | *Not specified.* | n=648, missing=0, range 2–15, mean 8.75 ± 4.236 |
| riblet_mass_g | metadata | numeric | *Not specified.* | n=648, missing=0, range 1–2, mean 1.5 ± 0.4086 |
| solid_fraction | metadata | numeric | *Not specified.* | n=648, missing=0, range 0.7798–0.8219, mean 0.8036 ± 0.0113 |
| desiccator | metadata | categorical | *Not specified.* | n=648, missing=0, classes=8, top 11p0b (×81) |
| batch_number | metadata | categorical | *Not specified.* | n=648, missing=0, classes=72, top RH11p0_API02p00_RW1p0 (×9) |

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
- **Content hash:** `37127028be8c233260ae6d2ef2eb08d4993c9fddd10c352dfc2b2435c3b723a5`
- **Processing hash:** `a08069d9b9842996b18357f8dbf38073715388970a6e3be86e5554a958cb9960` | **metadata hash:** `b704983dbe0fa5d840d6dbe092cc9324a83f6cd3b4db66fe6eb3efb3db93279b`

# Datasheet — Nirpy Research Raman spectra mixtures

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research Raman spectra mixtures. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub data

## Composition

- **Alignment:** sample level; 303 sample(s), 303 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research Raman spectra mixtures | *Not specified.* | Raman | 122.3–4326 cm-1 | 303 | 1500 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Albite | target | numeric | *Not specified.* | n=303, missing=0, range 0–1, mean 0.4819 ± 0.2947 |
| Quartz | target | numeric | *Not specified.* | n=303, missing=0, range 0–1, mean 0.2576 ± 0.2382 |
| Orthoclase | target | numeric | *Not specified.* | n=303, missing=0, range 0–1, mean 0.2605 ± 0.2221 |
| repository_url | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×303) |
| license | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top MIT License (×303) |
| license_url | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×303) |
| rights_status | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top explicit_open (×303) |
| usage_scope | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top public_reuse_possible (×303) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top True (×303) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top Raman (×303) |
| axis_unit | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top cm^-1 (×303) |
| axis_min | metadata | numeric | *Not specified.* | n=303, missing=0, range 122.3–122.3, mean 122.3 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=303, missing=0, range 4326–4326, mean 4326 ± 9.11e-13 |
| n_points_original | metadata | numeric | *Not specified.* | n=303, missing=0, range 1500–1500, mean 1500 ± 0 |
| notes | metadata | categorical | *Not specified.* | n=303, missing=0, classes=1, top Converted from Nirpy Research GitHub raw data without interpolation or resampling. (×303) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/Raman_spectra_mixtures.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 0 fields, Y: 3 fields, measurements: 0 fields, passport: 16 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** MIT license permits use, copy, modification, publication, distribution, sublicensing and sale with copyright/license notice.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `5c5a63e1a720176eb48e7085fa1c3917ab269b421e00a79c66333407685769c0`
- **Processing hash:** `505512415cda3aa7641821945c98ad46f1793c5c3d6e70c167c806f1cb31fb9d` | **metadata hash:** `70e4bc5ef77f38fe1706233b14bf9d7f8c59b6b8624cb479621342b9638e3380`

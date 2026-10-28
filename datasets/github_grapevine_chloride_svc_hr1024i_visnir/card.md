# Datasheet — GitHub grapevine chloride SVC HR-1024i VIS-NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** github
- **Description:** GitHub grapevine chloride SVC HR-1024i VIS-NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, github
- **Contributor:** Hyperspectral sensing for high-throughput chloride detection in grapevines

## Composition

- **Alignment:** observation level; 556 sample(s), 556 observation(s) total; sample_id available: True.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | *Not specified.* | SVC HR-1024i | NIR | 339–2515 nm | 556 | 2177 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| chloride_average | target | numeric | *Not specified.* | n=556, missing=0, range 0–7945, mean 1664 ± 1532 |
| chloridometer_reading1 | target | numeric | *Not specified.* | n=556, missing=1, range 0–281, mean 58.84 ± 54.11 |
| chloridometer_reading2 | target | numeric | *Not specified.* | n=556, missing=1, range 0–283, mean 59.26 ± 54.45 |
| chloridometer_reading3 | target | numeric | *Not specified.* | n=556, missing=1, range 0–282, mean 59.21 ± 54.33 |
| scan_id | metadata | categorical | *Not specified.* | n=556, missing=0, classes=556, top HR.060623.0000.sig (×1) |
| trial | metadata | categorical | *Not specified.* | n=556, missing=0, classes=2, top trial02 (×297) |
| pot_number | metadata | numeric | *Not specified.* | n=556, missing=0, range 1–324, mean 147.9 ± 87.69 |
| genotype | metadata | categorical | *Not specified.* | n=556, missing=0, classes=23, top DOAN9024 (×30) |
| replicate | metadata | numeric | *Not specified.* | n=556, missing=0, range 1–5, mean 3.004 ± 1.41 |
| salt_treatment_mM_NaCl | metadata | numeric | *Not specified.* | n=556, missing=0, range 0–75, mean 42.31 ± 31.16 |
| article_url | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top https://acsess.onlinelibrary.wiley.com/doi/10.1002/ppj2.70012 (×556) |
| doi_publication | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top 10.1002/ppj2.70012 (×556) |
| instrument_name | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top SVC HR-1024i (×556) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top VIS-NIR (×556) |
| signal_type | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top reflectance (×556) |
| axis_unit | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top nm (×556) |
| axis_min | metadata | numeric | *Not specified.* | n=556, missing=0, range 339–339, mean 339 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=556, missing=0, range 2515–2515, mean 2515 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=556, missing=0, range 1023–1023, mean 1023 ± 0 |
| n_points_interpolated | metadata | numeric | *Not specified.* | n=556, missing=0, range 2177–2177, mean 2177 ± 0 |
| license | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top NOASSERTION (×556) |
| rights_status | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top no_explicit_repository_license (×556) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top False (×556) |
| decoder | metadata | categorical | *Not specified.* | n=556, missing=0, classes=1, top pandas.read_csv, numpy.interp (×556) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

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
- **Redistribution rights:** Wiley article is Open Access and points to GitHub data, but the GitHub repository API reports no explicit repository license.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `b4a6f0420e815f79a2f930d441d31f34a185e5f5459332ea260fc0a206703fc5`
- **Processing hash:** `bd157f63e8e4f6ffd20ecfdc3709827132e1c1029436cd844e190e2e73265b8f` | **metadata hash:** `c042c92a6b39d49b75e6d5c4bd00793d172c9e027b3ac088a60f6660f621b66b`

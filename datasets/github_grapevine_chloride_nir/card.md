# Datasheet — Grapevine leaf chloride — NIR-S-G1 + SVC HR-1024i

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** github
- **Description:** GitHub grapevine leaf chloride, NIR-S-G1 and SVC HR-1024i. Origin database composed from 2 standardized v2.0 leaves: 2 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, github
- **Contributor:** Hyperspectral sensing for high-throughput chloride detection in grapevines

## Composition

- **Alignment:** sample level; 556 sample(s), 815 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** observation_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X_nirs_g1 | *Not specified.* | NIR-S-G1 | NIR | 901–1702 nm | 259 | 228 |
| X_svc_hr1024i | *Not specified.* | SVC HR-1024i | NIR | 339–2515 nm | 556 | 2177 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| chloride_average | target | numeric | *Not specified.* | n=815, missing=0, range 0–7945, mean 1634 ± 1535 |
| chloridometer_reading1 | target | numeric | *Not specified.* | n=815, missing=2, range 0–281, mean 57.85 ± 54.17 |
| chloridometer_reading2 | target | numeric | *Not specified.* | n=815, missing=2, range 0–283, mean 58.18 ± 54.6 |
| chloridometer_reading3 | target | numeric | *Not specified.* | n=815, missing=2, range 0–282, mean 58.12 ± 54.43 |
| pot_number | metadata | numeric | *Not specified.* | n=815, missing=0, range 1–324, mean 143.1 ± 84.74 |
| trial | metadata | categorical | *Not specified.* | n=815, missing=0, classes=2, top trial01 (×518) |
| genotype | metadata | categorical | *Not specified.* | n=815, missing=0, classes=23, top NM11-081 (×45) |
| replicate | metadata | numeric | *Not specified.* | n=815, missing=0, range 1–5, mean 2.99 ± 1.412 |
| salt_treatment_mM_NaCl | metadata | numeric | *Not specified.* | n=815, missing=0, range 0–75, mean 42.45 ± 31.08 |
| article_url | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top https://acsess.onlinelibrary.wiley.com/doi/10.1002/ppj2.70012 (×815) |
| doi_publication | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top 10.1002/ppj2.70012 (×815) |
| instrument_name | metadata | categorical | *Not specified.* | n=815, missing=0, classes=2, top SVC HR-1024i (×556) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=815, missing=0, classes=2, top VIS-NIR (×556) |
| signal_type | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top reflectance (×815) |
| axis_unit | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top nm (×815) |
| axis_min | metadata | numeric | *Not specified.* | n=815, missing=0, range 339–901, mean 517.6 ± 261.8 |
| axis_max | metadata | numeric | *Not specified.* | n=815, missing=0, range 1702–2515, mean 2257 ± 378.8 |
| n_points_original | metadata | numeric | *Not specified.* | n=815, missing=0, range 228–1023, mean 770.4 ± 370.4 |
| license | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top NOASSERTION (×815) |
| rights_status | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top no_explicit_repository_license (×815) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=815, missing=0, classes=1, top False (×815) |
| decoder | metadata | categorical | *Not specified.* | n=815, missing=0, classes=2, top pandas.read_csv, numpy.interp (×556) |
| scan_id | metadata | categorical | *Not specified.* | n=815, missing=259, classes=556, top HR.060623.0000.sig (×1) |
| n_points_interpolated | metadata | categorical | *Not specified.* | n=815, missing=259, classes=1, top 2177 (×556) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *No origin source recorded.*

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Each trial × pot_number pair is unique. replicate=1…5 is the biological replicate of the genotype × salt design. The three chloridometer readings are analytical measurements in Y; none is a spectral replicate.
- **Curated views:** M: 5 fields, Y: 4 fields, measurements: 0 fields, passport: 19 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `cbfee889281bf3c6c1740ee0dd968502878ff1958f6c46f9e8519331c59b3e67`
- **Processing hash:** `083037fda0c039421a18f9ed0425f8b9b2be1221ae2abdb580e262acc729ec45` | **metadata hash:** `ac7725fc80a3f793a190cf352099a1c3e8a236b1ef033e6ad76546a67e44ff01`

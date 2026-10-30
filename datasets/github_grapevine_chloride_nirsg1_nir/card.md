# Datasheet — GitHub grapevine chloride NIR-S-G1 NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** github
- **Description:** GitHub grapevine chloride NIR-S-G1 NIR. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, github
- **Contributor:** Hyperspectral sensing for high-throughput chloride detection in grapevines

## Composition

- **Alignment:** sample level; 259 sample(s), 259 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | *Not specified.* | NIR-S-G1 | NIR | 901–1702 nm | 259 | 228 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| chloride_average | target | numeric | *Not specified.* | n=259, missing=0, range 0–7936, mean 1568 ± 1542 |
| chloridometer_reading1 | target | numeric | *Not specified.* | n=259, missing=1, range 0–281, mean 55.74 ± 54.36 |
| chloridometer_reading2 | target | numeric | *Not specified.* | n=259, missing=1, range 0–283, mean 55.86 ± 54.95 |
| chloridometer_reading3 | target | numeric | *Not specified.* | n=259, missing=1, range 0–280, mean 55.78 ± 54.68 |
| pot_number | metadata | numeric | *Not specified.* | n=259, missing=0, range 1–266, mean 132.8 ± 77.19 |
| trial | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top trial01 (×259) |
| genotype | metadata | categorical | *Not specified.* | n=259, missing=0, classes=19, top BERL9031 (×15) |
| replicate | metadata | numeric | *Not specified.* | n=259, missing=0, range 1–5, mean 2.961 ± 1.416 |
| salt_treatment_mM_NaCl | metadata | numeric | *Not specified.* | n=259, missing=0, range 0–75, mean 42.76 ± 30.94 |
| article_url | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top https://acsess.onlinelibrary.wiley.com/doi/10.1002/ppj2.70012 (×259) |
| doi_publication | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top 10.1002/ppj2.70012 (×259) |
| instrument_name | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top NIR-S-G1 (×259) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top NIR (×259) |
| signal_type | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top reflectance (×259) |
| axis_unit | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top nm (×259) |
| axis_min | metadata | numeric | *Not specified.* | n=259, missing=0, range 901–901, mean 901 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=259, missing=0, range 1702–1702, mean 1702 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=259, missing=0, range 228–228, mean 228 ± 0 |
| license | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top NOASSERTION (×259) |
| rights_status | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top no_explicit_repository_license (×259) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top False (×259) |
| decoder | metadata | categorical | *Not specified.* | n=259, missing=0, classes=1, top pandas.read_csv (×259) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Each trial × pot_number pair is unique. replicate=1…5 is the biological replicate of the genotype × salt design. The three chloridometer readings are analytical measurements in Y; none is a spectral replicate.
- **Curated views:** M: 3 fields, Y: 4 fields, measurements: 0 fields, passport: 19 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `92ace4da8e57d3623e38a84ed67efa5a402a7f3a806cbe0b995dfb847968e5fb`
- **Processing hash:** `66bbbfb8674c7e7d554ab25543361c3ca2cd3bedbeae13e1f39a7c7e603b18ee` | **metadata hash:** `a62c41364332ee1c1b97a435bc3d75534432fe99d088b6cfb0ec1f17c2e07f63`

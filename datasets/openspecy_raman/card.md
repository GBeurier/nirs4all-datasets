# Datasheet — OpenSpecy RAMAN spectral library subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** openspecy
- **Description:** OpenSpecy RAMAN spectral library subset. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, openspecy
- **Contributor:** OpenSpecy

## Composition

- **Alignment:** observation level; 5000 sample(s), 5000 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | OpenSpecy RAMAN | mixed source instruments, metadata sparse | Raman | 102–1.199e+04 none | 5000 | 1983 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=5000, missing=0, classes=878, top axinite-(fe) (×102) |
| compound_name | target | categorical | *Not specified.* | n=5000, missing=0, classes=878, top axinite-(fe) (×102) |
| polymer_type | target | categorical | *Not specified.* | n=5000, missing=0, classes=24, top mineral (×4790) |
| class_label | target | categorical | *Not specified.* | n=5000, missing=0, classes=24, top mineral (×4790) |
| plastic_or_not | target | categorical | *Not specified.* | n=5000, missing=0, classes=2, top not plastic (×4845) |
| source_label | target | categorical | *Not specified.* | n=5000, missing=0, classes=7, top minerals (×3739) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top RAMAN (×5000) |
| axis_unit | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top cm^-1 (×5000) |
| axis_min | metadata | numeric | *Not specified.* | n=5000, missing=0, range 102–102, mean 102 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=5000, missing=0, range 1.199e+04–1.199e+04, mean 1.199e+04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=5000, missing=0, range 1983–1983, mean 1983 ± 0 |
| preprocessing_original | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top nobaseline OpenSpecy library, no project-side interpolation (×5000) |
| contributor | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| license | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| original_file | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top nobaseline_raw.rds (×5000) |
| file_format | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top RDS OpenSpecy object (×5000) |
| quality_flags | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| notes | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top capped v0.1 export from OpenSpecy nobaseline.rds (×5000) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://d2jrxerjcsjhs7.cloudfront.net/nobaseline.rds`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.openanalysis.org/openspecy/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *No related publication.*

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Redistribution not cleared; verify source terms before release.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `c0f4b1f82817d446013fb288ade15a085dc54e3432003775d47844d30f24fa5e`
- **Processing hash:** `b4e808369166fa5eb1508a09237f2e273d19a5666e697ca83766951156b16134` | **metadata hash:** `2454b2ef76a783d76cdf3ea65a7cc9b5b941a32a19b802d911d54e25c7bf5362`

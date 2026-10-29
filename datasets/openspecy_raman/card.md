# Datasheet — OpenSpecy RAMAN spectral library subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** openspecy
- **Description:** OpenSpecy RAMAN spectral library subset. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, openspecy
- **Contributor:** OpenSpecy

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 5000 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | OpenSpecy RAMAN | mixed source instruments, metadata sparse | Raman | 102–1.199e+04 cm-1 | 5000 | 1983 |

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
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://d2jrxerjcsjhs7.cloudfront.net/nobaseline.rds`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://www.openanalysis.org/openspecy/`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Non déterminé
- **Curated views:** M: 0 fields, Y: 5 fields, passport: 17 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

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

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `41ec391cab2e7589250e8464c443367da055d305206da2dcee5c0cb9f0996d7b`
- **Processing hash:** `4540f6da25accf70e77ce1c2b52294f4388efb331c3568f41cdc5aa398803aa1` | **metadata hash:** `9e2ebee2bf80d2d2674abcfb540028155bbb822e3a5d3c20ea8a429f6826425c`

# Datasheet — OpenSpecy FTIR spectral library subset

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** openspecy
- **Description:** OpenSpecy FTIR spectral library subset. v2.0 standardized NIRS package: 1 spectral source(s), 6 declared target(s). Auto-generated from dataset_card.json (verify before publication).
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
| X | OpenSpecy FTIR | mixed source instruments, metadata sparse | MIR | 102–1.199e+04 cm-1 | 5000 | 1983 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| material_name | target | categorical | *Not specified.* | n=5000, missing=0, classes=2451, top soil (×455) |
| compound_name | target | categorical | *Not specified.* | n=5000, missing=0, classes=2451, top soil (×455) |
| polymer_type | target | categorical | *Not specified.* | n=5000, missing=0, classes=30, top mineral (×2750) |
| class_label | target | categorical | *Not specified.* | n=5000, missing=0, classes=30, top mineral (×2750) |
| plastic_or_not | target | categorical | *Not specified.* | n=5000, missing=0, classes=2, top not plastic (×3541) |
| source_label | target | categorical | *Not specified.* | n=5000, missing=0, classes=7, top polymer, minerals, organic materials (×1988) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top FTIR (×5000) |
| axis_unit | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top cm^-1 (×5000) |
| axis_min | metadata | numeric | *Not specified.* | n=5000, missing=0, range 102–102, mean 102 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=5000, missing=0, range 1.199e+04–1.199e+04, mean 1.199e+04 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=5000, missing=0, range 1983–1983, mean 1983 ± 0 |
| preprocessing_original | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top nobaseline OpenSpecy library, no project-side interpolation (×5000) |
| contributor | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| citation | metadata | categorical | *Not specified.* | n=5000, missing=3276, classes=2, top cowger et al. 'high throughput ftir analysis of macro and microplastics with plate readers' in prep (×1702) |
| license | metadata | categorical | *Not specified.* | n=5000, missing=5000, classes=0, — |
| original_file | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top nobaseline_raw.rds (×5000) |
| file_format | metadata | categorical | *Not specified.* | n=5000, missing=0, classes=1, top RDS OpenSpecy object (×5000) |
| quality_flags | metadata | categorical | *Not specified.* | n=5000, missing=4843, classes=9, top strong difference (×79) |
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
- **Curated views:** M: 0 fields, Y: 5 fields, measurements: 0 fields, passport: 17 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `2d6cc573cd0c7f2bb347f08e5df0fd8f3a991b7839a069471c9bc166508c1e50`
- **Processing hash:** `afaeae87f16267ced31169124060f19dff82c640c255a3d7ed4844c66ef50a13` | **metadata hash:** `ac414e431f4a72074466cdc8116463deef02c15814b325dd7581562b6c7309d8`

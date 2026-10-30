# Datasheet — Beer original extract OHPL NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ohpl
- **Description:** Beer original extract OHPL NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ohpl
- **Contributor:** nanxstats/OHPL

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 60 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | beer | source_export | NIR | 1100–2250 nm | 60 | 576 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| original_extract | target | numeric | *Not specified.* | n=60, missing=0, range 4.23–18.76, mean 11.11 ± 2.439 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): test: 20, train: 40

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nanxstats/OHPL/raw/master/data/beer.rda`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Undetermined
- **Curated views:** M: 0 fields, Y: 1 fields, measurements: 0 fields, passport: 5 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.1016/j.chemolab.2017.07.004](https://doi.org/10.1016/j.chemolab.2017.07.004)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Rights retained from source metadata; review before public redistribution.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `4415bbfff1ab3fd36358eb8997c3efb770dc62638b42a0e2ac3daa5f9a6a42ef`
- **Processing hash:** `ccc0ec09cc6655b70b1c210f40c129ee732967bcd4864cb2678d6b693a9eaa4a` | **metadata hash:** `1e85278e9389974f97f2ebd65caafabfa52ff9afa060e6b2751001babf455a68`

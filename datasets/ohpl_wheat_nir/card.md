# Datasheet — Wheat protein OHPL NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ohpl
- **Description:** Wheat protein OHPL NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ohpl
- **Contributor:** nanxstats/OHPL

## Composition

- **Alignment:** observation level; *Not specified.* sample(s), 100 observation(s) total; sample_id available: False.
- **Exported observations per source unit:** ND (identity/repetition information unavailable).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | wheat | source_export | NIR | 1100–2500 nm | 100 | 701 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| protein | target | numeric | *Not specified.* | n=100, missing=0, range 7.75–14.28, mean 11.41 ± 1.11 |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- **original** (documented, not applied): all: 100

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nanxstats/OHPL/raw/master/data/wheat.rda`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Curation identity contract: Non déterminé
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
- **Content hash:** `1a4835275cf0c5340727b8de9aed08946e9baee24861c9311f74c118bedb03d9`
- **Processing hash:** `bc25a31e9c4434c5cea1eaf9dc055a4dddcc3d49c074c4b568e503ae00fc690f` | **metadata hash:** `951476acb754dc58b69725b5b5ed86d63c5a37620767b1d9df88b9e159d87bbe`

# Datasheet — Beer original extract OHPL NIR

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ohpl
- **Description:** Beer original extract OHPL NIR. v2.0 standardized NIRS package: 1 spectral source(s), 1 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ohpl
- **Contributor:** nanxstats/OHPL

## Composition

- **Alignment:** observation level; 60 sample(s), 60 observation(s) total; sample_id available: False.
- **Repetitions per sample:** 1–1 (mean 1).

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

- **original** (documented, not applied): train: 40, test: 20

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** *Not specified.*

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nanxstats/OHPL/raw/master/data/beer.rda`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** *Not specified.*

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

- **Content version:** 1.0.0 | **schema/protocol:** 2.0
- **Content hash:** `0450403b0673fe245815209d1b5e445219407ef1f1137d8bbbeb07af70a0c4cf`
- **Processing hash:** `d08d4db6e71910e85fc13a7569a82fbcb8d189a8aa096cbff66781e7e6b13940` | **metadata hash:** `76d87db53485d7b9a726cfa809cacc1a97c488598f21ecc798b962b620321674`

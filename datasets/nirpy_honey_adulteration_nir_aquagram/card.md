# Datasheet — Nirpy Research honey adulteration NIR aquagram

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** nirpy
- **Description:** Nirpy Research honey adulteration NIR aquagram. v2.0 standardized NIRS package: 1 spectral source(s), 3 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, nirpy
- **Contributor:** Nirpy Research GitHub Honey2021.csv

## Composition

- **Alignment:** sample level; 165 sample(s), 165 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Nirpy Research honey adulteration NIR aquagram | *Not specified.* | NIR | 1315–1.473e+04 cm-1 | 165 | 450 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| sample_class | target | categorical | *Not specified.* | n=165, missing=0, classes=4, top adulterated_honey (×133) |
| adulterant_code | target | categorical | *Not specified.* | n=165, missing=21, classes=3, top JMAF (×72) |
| adulteration_percent_value | target | categorical | *Not specified.* | n=165, missing=6, classes=12, top 1.0 (×21) |
| repository_url | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top https://github.com/nevernervous78/nirpyresearch (×165) |
| blog_url | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top https://nirpyresearch.com/aquagrams-python-matplotlib/ (×165) |
| license | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top MIT License (×165) |
| license_url | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE (×165) |
| rights_status | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top explicit_open (×165) |
| usage_scope | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top public_reuse_possible (×165) |
| public_release_allowed | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top True (×165) |
| spectroscopy_type | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top NIR (×165) |
| axis_unit | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top cm^-1 (×165) |
| axis_min | metadata | numeric | *Not specified.* | n=165, missing=0, range 1315–1315, mean 1315 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=165, missing=0, range 1.473e+04–1.473e+04, mean 1.473e+04 ± 5.474e-12 |
| axis_direction | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top descending_in_source (×165) |
| secondary_axis_unit | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top nm (×165) |
| secondary_axis_min | metadata | numeric | *Not specified.* | n=165, missing=0, range 679–679, mean 679 ± 0 |
| secondary_axis_max | metadata | numeric | *Not specified.* | n=165, missing=0, range 7610–7610, mean 7610 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=165, missing=0, range 450–450, mean 450 ± 0 |
| adulterant_name | metadata | categorical | *Not specified.* | n=165, missing=21, classes=3, top high_fructose_corn_syrup_inferred_from_spanish_code (×72) |
| honey_percent_inferred | metadata | numeric | *Not specified.* | n=165, missing=15, range 0–100, mean 93.55 ± 17.59 |
| adulteration_percent_operator | metadata | categorical | *Not specified.* | n=165, missing=156, classes=1, top > (×9) |
| replicate_label | metadata | categorical | *Not specified.* | n=165, missing=1, classes=9, top a (×41) |
| parse_note | metadata | categorical | *Not specified.* | n=165, missing=45, classes=2, top Adulterant name expanded from raw code by domain convention, raw code is retained. (×111) |
| notes | metadata | categorical | *Not specified.* | n=165, missing=0, classes=1, top Source CSV has two spectral-axis rows: column headers are cm^-1 while the first data row stores matching nm values despite inverted source labels. The nm row was removed from X and retained here as secondary-axis metadata. (×165) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- GitHub — kind `url`, access `open`, license *Not specified.*: `https://github.com/nevernervous78/nirpyresearch/blob/master/data/Honey2021.csv`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://nirpyresearch.com/aquagrams-python-matplotlib/`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://raw.githubusercontent.com/nevernervous78/nirpyresearch/master/LICENSE`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: sample_id est un compteur de ligne créé ; les libellés source et lettres a…i n’établissent pas une identité physique unique. Le protocole des répétitions reste indéterminé.
- **Curated views:** M: 0 fields, Y: 3 fields, measurements: 0 fields, passport: 33 fields. Original variables and the versioned mapping are retained separately.

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
- **Content hash:** `a329e2256441d9477c972ebc91a2f34cda368c6906fb62e82504a2868de3d57e`
- **Processing hash:** `62382880a48ff3c4c8df971169e4acc197f3f3083996ed42282aed1863f9aae9` | **metadata hash:** `fd06c13825c36523a2892d2005467fb4426b6392762c94884ed83b2f07e735b2`

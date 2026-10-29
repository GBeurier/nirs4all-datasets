# Datasheet — EcoSIS Leaf Traits Compilation reflectance

_Generated from the dataset card and descriptor (Datasheets for Datasets, Gebru et al. 2021)._

## Motivation

- **Domain / purpose:** ecosis
- **Description:** EcoSIS Leaf Traits Compilation reflectance. v2.0 standardized NIRS package: 1 spectral source(s), 4 declared target(s). Auto-generated from dataset_card.json (verify before publication).
- **Keywords:** nir, v2, ecosis
- **Contributor:** Compiled paired leaf traits and leaf spectra dataset

## Composition

- **Alignment:** sample level; 47393 sample(s), 47393 observation(s) total; sample_id available: True.
- **Exported observations per source unit:** 1–1 (mean 1).
- **Documented technical repetitions:** *Not specified.*.
- **Variable grain / join key:** sample_id.

### Sources (X)

| ID | Name | Instrument | Modality | Axis | Observations | Wavelengths |
| --- | --- | --- | --- | --- | --- | --- |
| X | Paired leaf traits and leaf spectra dataset.csv | Lambda-19 Spectrophotometer \| ASD FieldSpec \| ASD FieldSpec 4 \| PSR 3500+ \| SVC HR-1024i \| SVC LC-RP-Pro \| PSR+ \| SVC HR-1024i, PSR Plus \| SVC HR-2014i \| ASD FieldSpec 3 \| SVC HR-1024tm \| ASD FieldSpec Pro \| ASD FieldSpec Pro FR | NIR | 450–2400 nm | 47393 | 196 |

### Variables (Y / metadata)

| Name | Role | Type | Unit | Summary |
| --- | --- | --- | --- | --- |
| Chla+b | target | numeric | *Not specified.* | n=47393, missing=40543, range -999–167.2, mean 33.56 ± 43.88 |
| Ccar | target | numeric | *Not specified.* | n=47393, missing=43148, range -999–28.35, mean 5.975 ± 48.93 |
| EWT | target | numeric | *Not specified.* | n=47393, missing=43810, range -9.999e+07–1374, mean -5.568e+04 ± 2.362e+06 |
| LMA | target | numeric | *Not specified.* | n=47393, missing=1976, range 0.06603–388.9, mean 69.85 ± 35.87 |
| sample_date | metadata | categorical | *Not specified.* | n=47393, missing=34310, classes=421, top 2018 (×1083) |
| english_name | metadata | categorical | *Not specified.* | n=47393, missing=28683, classes=607, top Maize (×1210) |
| latin_name | metadata | categorical | *Not specified.* | n=47393, missing=28928, classes=776, top Zea mays (×1210) |
| plant_functional_type | metadata | categorical | *Not specified.* | n=47393, missing=621, classes=8, top Deciduous broadleaf forests (×26944) |
| latitude | metadata | numeric | *Not specified.* | n=47393, missing=0, range -34.81–71.28, mean 41.69 ± 7.847 |
| longitude | metadata | numeric | *Not specified.* | n=47393, missing=0, range -166–142.1, mean -80.02 ± 39.65 |
| foreoptic_type | metadata | categorical | *Not specified.* | n=47393, missing=276, classes=6, top Leaf clip (×34032) |
| instrument | metadata | categorical | *Not specified.* | n=47393, missing=1068, classes=13, top ASD FieldSpec 3 (×16805) |
| reference | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=31, top (Chlus, 2019) (×25968) |
| publication_doi | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top 10.1111/nph.19807 (×47393) |
| citation | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top Ji et al. 2024, New Phytologist 243:111-131 (×47393) |
| signal_type | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top reflectance (×47393) |
| axis_unit | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top nm (×47393) |
| axis_min | metadata | numeric | *Not specified.* | n=47393, missing=0, range 450–450, mean 450 ± 0 |
| axis_max | metadata | numeric | *Not specified.* | n=47393, missing=0, range 2400–2400, mean 2400 ± 0 |
| n_points_original | metadata | numeric | *Not specified.* | n=47393, missing=0, range 196–196, mean 196 ± 0 |
| rights_status | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top manual_review_needed (×47393) |
| usage_scope | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top private_use_only (×47393) |
| notes | metadata | categorical | *Not specified.* | n=47393, missing=0, classes=1, top Compiled source CSV standardized as-is, no project interpolation, resampling, or historical split applied. (×47393) |

## Statistics — splits

Splits are **documented, never auto-applied** (the supervised task is a consumer choice).

- *No native split documented.*

## Collection process

- **Reference method:** *Not specified.*
- **Conversion status:** partial

### Origin sources (where the bytes live)

- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://ntrs.nasa.gov/citations/20240006155`
- *Not specified.* — kind `url`, access `open`, license *Not specified.*: `https://data.ecosis.org/dataset/leaf-optical-properties-experiment-database--lopex93- \| https://data.ecosis.org/dataset/angers-leaf-optical-properties-database--2003- \| https://github.com/geoxiyang/LeafTraitSpectraSeasonality-Yangetal2016RSE \| https://data.ecosis.org/dataset/2018-cedar-creek-pressed-leaves \| https://data.ecosis.org/dataset/fresh-leaf-cabo-spectra-from-herbarium-project \| https://data.ecosis.org/dataset/fresh-leaf-spectra-to-estimate-foliar-functional-traits-across-neon-domains \| https://data.ecosis.org/dataset/seasonal-fresh-leaf-spectra-and-traits--blackhawk-island--wi \| https://data.ecosis.org/dataset/leaf-reflectance-and-tratis-of-floating-and-emergent-macrophytes \| https://data.ecosis.org/dataset/seasonal-measurements-of-photosynthesis-and-leaf-traits-in-scarlet-oak \| https://data.ecosis.org/dataset/leaf-and-canopy-spectroscopy-and-biochemical-data-of-field-grown-cucurbita-pepo-under-two-stresses \| https://data.ecosis.org/dataset/ngee-tropics-gliht-puerto-rico-campaign-leaf-spectral-reflectance-and-transmittance-march-2017 \| https://data.ecosis.org/dataset/ngee-tropics-february-2017-leaf-spectral-reflectance-measured-in-panama-at-the-pa-slz-canopy-crane \| https://data.ecosis.org/dataset/ngee-tropics-leaf-spectral-reflectance-measured-in-panama-collected-february-to-april-2016 \| https://data.ecosis.org/dataset/nasa-fft-project-leaf-transmittance-morphology-and-biochemistry-for-northern-temperate-forests \| https://data.ecosis.org/dataset/2018-talladega-national-forest--leaf-level-reflectance-spectra-and-foliar-traits \| https://data.ecosis.org/dataset/ngee-arctic-2019-leaf-spectral-reflectance-seward-peninsula-alaska \| https://data.ecosis.org/dataset/ngee-arctic-2017-leaf-spectral-reflectance-teller-watershed-seward-peninsula-alaska \| https://data.ecosis.org/dataset/leaf-spectra-and-physiological-and-chemical-traits-from-maize-grown-under-nitrogen-stress \| https://data.ecosis.org/dataset/ngee-arctic-leaf-spectral-reflectance-utqiagvik--barrow--alaska-2013 \| https://data.ecosis.org/dataset/ngee-arctic-2016-leaf-spectral-reflectance-kougarok-road-watershed-seward-peninsula-alaska \| https://data.ecosis.org/dataset/leaf-spectra-of-36-species-growing-in-rosa-rugosa-invaded-coastal-grassland-communities-in-belgium \| https://data.ecosis.org/dataset/leaf-level-spectra-and-lma-for-a-set-of-trees--forbs--vines-and-grasses-collected-in-madison--wi \| https://data.ecosis.org/dataset/fresh-leaf-spectra-to-estimate-foliar-functional-traits-over-neon-domains-in-eastern-united-states \| https://data.ecosis.org/dataset/fresh-leaf-spectra-to-estimate-lma-over-neon-domains-in-eastern-united-states \| https://data.ecosis.org/dataset/2012-leaf-reflectance-spectra-of-tropical-trees-in-tapajos-national-forest \| https://data.ecosis.org/dataset/2014-leaf-reflectance-spectra-of-tropical-plants-growing-in-biosphere2 \| https://data.ecosis.org/dataset/leaf-spectra--structural-and-biochemical-leaf-traits-of-eight-crop-species \| https://data.ecosis.org/dataset/dried-leaf-spectra-to-estimate-leaf-morphology-and-biochemistry-for-northern-temperate-forests \| https://data.ecosis.org/dataset/productivity-and-characterization-of-soybean-foliar-traits-under-aphid-pressure \| https://data.ecosis.org/dataset/common-milkweed-leaf-responses-to-water-stress-and-elevated-temperature \| ... (36 total)`
- standardization script (maintainer-only) — kind `script`, access `manual`, license *Not specified.*: `source_to_standard.py`

## Preprocessing / cleaning / labeling

- **Conversion warnings:** Y.csv has no observation_id; conversion assumes Y/M paired row order when counts match and M observation order matches an X block. Y row pairing is not independently verified.; Curation identity contract: Identifiant échantillon déclaré dans M
- **Curated views:** M: 9 fields, Y: 4 fields, passport: 19 fields, measurements: 0 fields. Original variables and the versioned mapping are retained separately.

## Uses

- **Permitted use:** Research and benchmarking; private use only.
- **Access policy:** Manual download / private-use-only per source.

### Related publications

- *Not specified.* — [10.1111/nph.19807](https://doi.org/10.1111/nph.19807)

## Distribution

- **License:** LicenseRef-not-cleared
- **Tier:** private — Private — export requires an access token (Dataverse); not openly redistributable.
- **Redistribution rights:** Compiled CSV redistribution rights not cleared.
- **DOI:** *Not specified.*

## Maintenance

- **Content version:** 1.1.0 | **schema/protocol:** 2.0
- **Content hash:** `f0ca9692a28078757d18967ee377c98fa6518dc11fdc20f3acde0cce698fd447`
- **Processing hash:** `50bb764a9d5e654133aa8759ecb350e97a0a6b18101919a81eef3901d9c580df` | **metadata hash:** `49044f177b99b30869e59fc8a3b882b8b2351e07aa2f0d3cd2a62d69199f58e4`

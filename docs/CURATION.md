# Scientific curation and source traceability

The raw variable collection remains available. Curation adds separate,
observation-level **M**, **Y**, **structure**, **passport** and **measurements**
views. It does not remove source columns, average repeated measurements, invent
physical samples, or change access tiers and licenses. This implements the local
review described in [#23](https://github.com/GBeurier/nirs4all-datasets/issues/23)
and [#24](https://github.com/GBeurier/nirs4all-datasets/issues/24).

## Read the scientific views

After rebuilding/importing a canonical dataset:

```python
from nirs4all_datasets import get

ds = get("ucph_granules_moisture_controlled_api_nir", root=".")
M = ds.curated_metadata(source="X")
Y = ds.curated_y(source="X")
groups = ds.curated("structure", source="X")
mapping = ds.curation_report()
original_M = ds.curated("original_M")
```

Private data still need the caller's authorized local import or configured
access. The example does not grant access or change redistribution rights.

`observation_id` identifies the acquisition. `sample_id` identifies the source
unit specified by that dataset's contract; it is nullable in the structure view
when identity is unavailable. Leading zeros are preserved. `source=...` joins
the requested source's observation IDs and preserves its order. Equal row counts
alone never establish a join. Unavailable identity is reported as `null`, not one
sample with thousands of repetitions.

The leading `observation_id` / `sample_id` columns are join keys, not predictive
covariates. A keyless original Y remains keyless in `original_Y`; the mapping
records the aligned observation key as a derivation from M under the pairing
assumption.

The views have these meanings:

| View | Contents |
|---|---|
| `M` | Informative experimental context, excluding empty/constant fields, passport, and declared response copies. |
| `Y` | Informative source-declared targets. A metadata trait is not automatically promoted to a response. |
| `structure` | Source-unit identity, site/subject/lot grouping where present, acquisition indices. Use these fields for group-aware validation. |
| `passport` | Identifiers, provenance, governance, auxiliary fields and fields excluded from informative M/Y, with decisions in the mapping. |
| `measurements` | Other measured traits found in M, kept outside experimental context. |
| `original_M`, `original_Y` | Original table values and column spellings, before normalization or enrichment. |

`y()`, `metadata()` and `variables()` still expose the unified source-variable
collection. When a value varies within a source unit, `variables.parquet` now
keeps **observation grain**, with both IDs, instead of retaining only a first
value or replacing the unit with acquisition identity. `dataset.json` declares
the variables' `join_key`; Python/IO/Croissant readers use it. Native split
assignments that differ within a group are likewise retained by observation and
flagged as a possible group overlap. No split is invented or applied.

The canonical format is **1.1**, the curation contract **1.0**, and the card
protocol **6**. Existing format-1.0 caches remain readable, but need rebuilding
to expose curated views. The curated source views and full mapping are withheld
for the anonymized tier; its existing masked accessors remain available.

## Identity contracts

`src/nirs4all_datasets/curation_contracts.json` holds the dataset-specific
reviewed mappings. It includes all 298 reviewed source IDs, normalized to catalog
slugs with their original spelling retained. The current repository contains
297 of those datasets; the Lyonia wave-3 source is not added to the catalog by
this migration.

Rules are local to a dataset, not general guesses from column names or suffixes:

- Human-arm muscle: subject × arm aspect, with subject retained as another
  grouping level; 40 source units, 50 acquisitions each in the reviewed import.
- Both UCPH Granules: the documented `..._vN.0/.1/.2` contract identifies vials;
  216 vials and three acquisitions per vial in each import. Lots, vials and
  internally averaged instrument scans are distinct concepts.
- Rice: variety × file-local column ID, encoded as a collision-free composite.
- Canopy experiment code, Lake Fire dates and the reused milk labels do not
  establish physical sample identity. Their original labels remain available.
- Herbarium/girdling copies, repeated campaigns, orientations and scan positions
  retain their documented nature. Observation multiplicity does not certify
  technical reacquisition or biological independence.

Counts are recomputed from supplied data. Audited historical counts are evidence,
not hardcoded replacements. Missing contract columns yield an unavailable
identity; an unrelated column is never silently substituted.

## LUCAS and OSSL enrichment

Supply the original soilsite resource locally:

```powershell
$env:NIRS4ALL_OSSL_SOILSITE = "D:\data\ossl_soilsite_L0_v1.2.csv.gz"
```

The converter also recognizes the cache location in the original
`nirs_db_vf/nirs_datasets_ready/ossl_nirs_database/input_data/raw` tree. It does
not download soilsite or execute source scripts automatically.

The join uses **dataset code + layer UUID**, validates source-key uniqueness and
preserves observation order. It carries site, coordinates, period bounds and
location uncertainty, with field-level source names and a resource SHA-256.
For the LUCAS imports only, `campaign_year` is the year of the source period
start, a verified campaign label rather than an exact individual sampling date.

The reviewed VIS-NIR/MIR imports share 40175 unit IDs: 18393 in campaign 2009,
21782 in 2015, and 25228 site IDs, including 14947 sites in both campaigns.
Campaign 2009 has the source period 2009-05-01 to 2012-08-01; campaign 2015 has
2015-03-01 to 2015-10-01. The source location-error field is 1000 m. The country
is empty in that resource and is not reconstructed. Group by the **source site
ID**, not coordinate equality, when retaining campaigns together in validation.

## API references and missing values

`api_reference_percent_w_w` is the UCPH active-ingredient mass concentration,
not computer-API provenance. It remains a numeric Y with unit `% w/w`: 648/648
values in each import, six concentrations (2, 5.25, 8.5, 10, 11.75, 15), 108
observations each. Its design encoding is excluded from predictive M. The
declaration was already correct in the catalog; curation must preserve it.

Missing rules match complete tokens, including controlled `not_available...` /
`not_provided...` variants. Blank, null and other explicit missing forms are
normalized without imputation. **NA, ND and none are not global substitutions**:
they may be valid categories, identifiers, controls or censored results. Source
`datapackage.json` missing-value declarations and explicit field contracts take
precedence. In particular, negative numbers and zero are not globally removed.

A contract can carry a source-confirmed numerical rule:

```json
{
  "missing_rule": {
    "sentinels": ["-999"],
    "confirmed": true,
    "evidence": "versioned source data dictionary, field and section"
  }
}
```

Unconfirmed sentinel rules are rejected. The earlier review's broad negative
sentinel hypotheses are not silently migrated into source facts. Censored
strings such as `<0.1` keep their operator and bound; numeric stats report
censored and invalid counts and compute min/max from exact finite values.
Class codes retain their declared categorical type and leading zeros. Aliases
are coalesced only when overlapping values are compatible and declared units do
not conflict; conflicting homonyms stay separate. Completeness and constant
checks happen after alias coalescing. Mapping entries cover every input column.

## Reproduce the review and migration

A metadata-only preview, without reading the spectral matrices:

```bash
python -m nirs4all_datasets.cli curate /path/to/nirs_db_vf \
  --out incoming/curation-preview --assume-paired-y
```

`--assume-paired-y` explicitly records the legacy Y/M positional assumption. The
canonical converter additionally checks the complete M/X observation order;
this still does not independently prove the missing Y IDs. If it cannot align
Y, the aligned target view is unavailable and the original Y table remains
intact. Duplicate/empty observation IDs and ambiguous soilsite joins fail.

Rebuild existing catalog datasets, preserve rights/routes, and regenerate
canonical data, manifests, cards, Croissant, reports and indexes:

```bash
python scripts/curate_catalog.py /path/to/nirs_db_vf --root . \
  --soilsite /path/to/ossl_soilsite_L0_v1.2.csv.gz --workers 2
```

`--only id1,id2` limits a run. `catalog/curation/summary.json` records per-dataset
outcomes and errors; `datasets.csv` is its compact table. Per-dataset JSON reports
retain the mappings, source hashes, roles, stats, enrichment evidence and identity
conclusions. Heavy raw/canonical tables remain gitignored. Content versions are
bumped for the migration, and policy/soilsite changes invalidate incremental
conversion. Re-running unchanged inputs skips canonical conversion.

`--refresh-curation-only` refreshes views and variable/card metadata without
recomputing spectral analyses. It requires identical input hashes and source-unit
membership; an identity or input change instead requires the full migration.

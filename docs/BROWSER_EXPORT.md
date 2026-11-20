# Public browser export

`nirs4all_datasets.browser_export` is an offline **preparation step** for browser hosts (such as
the nirs4all web app) that run without Python or a backend. It turns explicitly selected
**public** datasets into static JSON assets: one catalog and one asset per spectral source. It
neither uploads nor deploys anything. Hosting the result is a separate release step that needs
explicit authorization (see [Release step](#release-step)).

## Ownership

| Step | Owner |
| --- | --- |
| Resolve, acquire and cache the public dataset | `nirs4all_datasets.get` (packaged public recipe, or canonical DOI) |
| Paths, roles, units and join keys, with one explicitly selected source | `NirsDataset.to_io_spec(source=...)` |
| Loading, joins and materialization | native `nirs4all_io.assembled_full` |
| Decoding in the browser | nirs4all-io JS binding (`decodeAssembledFull`) |
| Target and source choice, and projection | the browser host (for example `mapAssembledToMaterialized` in the web app) |

The exporter adds no loader, join, encoding, filling, subsetting, target selection or split. It
writes the native `assembled_full` result unchanged.

The exporter adds exactly one declaration to the owner spec: the raw-export NA policy
`params.na = {"policy": "ignore"}` on every spec source. Roles and joins stay exactly as
`to_io_spec` declares them. IO's default policy aborts on any missing cell. With `ignore`, IO
keeps every row and feature, records missing X and Y cells as `validity: false`, and fills
nothing. A missing categorical target stays invalid and is not encoded as an extra class. The
per-source NA audit reports `removed_samples: []`. A spec source that already declares another
NA policy is refused. Native splits are joined only as a
documented metadata column (for example `partition` from `split_original`). They are never
applied, and no split is invented.

## Preconditions (rights and safety)

The exporter refuses any of the following **before any acquisition**:

- a tier other than `public` (`private` and `anonymized` are never exported);
- a public descriptor with
  [publication blockers](DESIGN.md#3-governance--visibility--3-tiers) (no open SPDX licence,
  non-open origins, or missing release-governance fields);
- an installed `nirs4all_io` without the native `assembled_full` operation, such as a
  Python-only MVP build (there is no fallback materialization);
- an installed IO whose declared wire profile (`nirs4all_io._assembled.ASSEMBLED_DATASET_VERSION`)
  is not a browser-supported `assembled_schema_version` (**3**). For example, IO 0.2.x emits
  schema 2, which lacks declared numeric bytes and validity masks. Install a nirs4all-io release
  whose native profile emits schema 3 (for example 0.3.2 emits 3). No migration is applied;
- missing, duplicate or malformed IDs. There is **no whole-catalog mode**, and IDs are always
  explicit;
- an output that is not empty, or that lies inside a Git work tree (payloads never enter Git).

The runtime descriptor that `get()` actually serves is checked again after resolution. Each
source asset is also refused (and nothing is left at the output) when:

- the native result's `assembled_schema_version` is not 3 (this also covers IO builds that
  declare no profile);
- native IO returns fewer or more rows than the canonical observations of that source;
- the result is not strict JSON (`NaN`/`Infinity`);
- the asset would contain the local dataset path.

Before you host anything, check each dataset's own licence terms and attribution requirements
([LICENSING](../LICENSING.md)). The exporter copies the licence, citation, origins and
publications into every asset's provenance. It does **not** grant hosting rights beyond what
each licence allows.

## Preparing assets

Run this from any environment with `nirs4all-datasets` and a native `nirs4all-io` whose profile
emits assembled schema 3:

```bash
python -m nirs4all_datasets.browser_export \
  --ids barley_moisture_perten other_public_id \
  --out /srv/stage/nirs4all-browser-datasets \
  --cache-dir ~/.cache/nirs4all-datasets
```

- `--ids` is required. Values are space- or comma-separated.
- `--out` must be absent or an empty directory, outside Git. The directory is written to a
  sibling staging directory and then renamed into place, so a failed run leaves nothing.
- `--cache-dir` is forwarded to `get()`. Already cached datasets are reused without network.
  Uncached public datasets are downloaded from their documented origins.
- `--root` defaults to a fresh, empty directory, so the **packaged catalog** is used and no
  `catalog/` or `datasets/` under the current directory can shadow it. Pass a checkout root
  explicitly only when you want its descriptors and local canonical data.

Datasets that need a guestbook response, or that have no auto-fetchable public origin, fail with
the same actionable error that `get()` gives.

## Output layout and wire contract

```text
<out>/catalog.json
<out>/sources/<dataset_id>/<source_id>.json
```

`catalog.json`:

```json
{
  "schema": "nirs4all.datasets.public-browser.v1",
  "datasets": [
    {
      "id": "barley_moisture_perten",
      "name": "Barley Perten moisture NIR",
      "tier": "public",
      "license": "CC-BY-4.0",
      "description": "…",
      "sources": [
        {"id": "X", "name": "…", "url": "sources/barley_moisture_perten/X.json", "sha256": "…", "size_bytes": 415568}
      ]
    }
  ]
}
```

`description` and the source `name` are optional. Each `url` is **relative** and resolves
against the URL the catalog was fetched from. `sha256` and `size_bytes` describe the exact
asset bytes.

Each source asset:

```json
{
  "schema": "nirs4all.datasets.browser-dataset.v1",
  "dataset_id": "barley_moisture_perten",
  "source_id": "X",
  "provenance": {
    "dataset": {
      "id": "…", "name": "…", "tier": "public", "license": "…", "citation": "…", "doi": null, "permitted_use": "…", "access_policy": "…",
      "ids": {"observation_id": "observation_id", "sample_id": "sample_id", "sample_id_available": false},
      "alignment_level": "observation"
    },
    "origin_sources": [{"kind": "…", "mode": "…", "locator": "…", "access": "open", "license": null, "title": "…"}],
    "publications": [],
    "source": {"source_id": "X", "name": "…", "instrument_name": "…", "modality": "NIR", "axis_unit": "nm", "signal_type": "auto"},
    "materialization": {
      "operation": "nirs4all_io.assembled_full",
      "nirs4all_io_version": "…",
      "nirs4all_datasets_version": "…",
      "assembled_schema_version": 3,
      "io_spec": {"…": "the to_io_spec(source=…) spec plus params.na={policy:ignore}, with inputs relative to the dataset directory"},
      "inputs": [{"path": "canonical/sources/X.parquet", "sha256": "…", "size_bytes": 0}]
    },
    "native_splits": {"exposed_as_metadata": [], "applied": false, "note": "…"},
    "warnings": []
  },
  "assembled": {"…": "native assembled_full output, unchanged"}
}
```

`assembled` contains every row of the selected source in canonical order. It also contains every
declared target and metadata column, the `observation_id` and `sample_id` identity columns,
feature headers and axis units. Its wire version is the IO-owned `assembled_schema_version`,
which is always 3 here.

`provenance.dataset.ids` and `alignment_level` preserve the descriptor's identity semantics.
When `sample_id_available` is false, `sample_id` values are per-observation placeholders, not
established physical specimen identities. A browser host must retain this distinction when
offering grouping, repetition aggregation or group-aware validation.

In schema 3, numeric blocks carry `dtype`, little-endian `data_bytes_hex`, a per-cell
`validity` mask and `precision`. Targets are typed columns (`numeric`, `classification_string`,
…), with codebooks in `y_categorical`. Numeric axes live in `feature_axes`, and join and NA
audits in `audits`. The exporter records the IO version but does not reinterpret its output.

## Integration in a browser host

1. Host the prepared directory as static files (see [Release step](#release-step)). The web app
   reads `VITE_PUBLIC_DATASETS_CATALOG_URL`. Its default is
   `https://datasets.nirs4all.org/browser/catalog.json`. Do not assume that endpoint is
   deployed.
2. Fetch `catalog.json`. Resolve each source `url` against the catalog URL.
3. Fetch the selected source asset, and check `size_bytes` and `sha256` before using it.
4. Decode `assembled` with nirs4all-io's `decodeAssembledFull`. Then project it with the host's
   existing mapping, with an explicit choice of target. No first-target default is implied.

## Release step

The exporter only prepares files. Uploading or redeploying them on a public host is an explicit
release action. It follows the established site workflow and the repository's delivery
authorization ([AGENTS.md](../AGENTS.md), [release summary](RELEASING.md)). The exporter is not
part of the public-site build by default.

Before release:

- re-run the export from the released `nirs4all-datasets` and `nirs4all-io` versions;
- review each dataset's licence and attribution;
- keep the output out of Git (heavy payloads are never committed);
- verify the served `catalog.json` and asset checksums after deployment.

## Limits

- Assets are plain JSON. Large datasets produce large files, and native IO's default load
  limits apply.
- The asset reflects the installed IO version's `assembled_full` wire, which is 3 only.
  Re-export after an IO wire change.
- Only public datasets that `get()` can materialize are exportable.

# Publishing protected data to a personal Dataverse (FUTURE)

> **Public datasets are NOT published here.** This catalog never re-hosts open data — a public dataset
> is only ever *linked to its origin* (the Zenodo / data-Dataverse / vendor archive that published it),
> and `get()` fetches it from there. Publishing is a **future capability** reserved for **protected**
> data — the `private` and `anonymized` tiers — on a *personal* Dataverse, used as a token-gated
> fallback for data whose origin cannot be linked (no automatable source) or whose origin has rotted.
> The orchestration and CLI below exist (covered by unit tests with a mocked client) but the live
> end-to-end path is not exercised yet; **rehearse on the sandbox first** when it is enabled.

This is the end-to-end walkthrough for putting **protected** datasets on a personal Dataverse
(Recherche Data Gouv / CIRAD) with `nirs4all-datasets`, and for reading them back with a token. The
production steps are identical to the sandbox; only the instance + collection differ.

| | Sandbox (rehearse here) | Production |
|---|---|---|
| Instance | `https://demo.recherche.data.gouv.fr` | `https://entrepot.recherche.data.gouv.fr` |
| Use for | testing the full flow, throw-away datasets | the real, citable datasets |

The CLI does the upload for you (create dataset → upload files `tabIngest=false` → publish → mint DOI).
You never touch the web upload form.

---

## 0. One-time: get a token and point the tools at the sandbox

1. Create an account on the sandbox, then copy your **API token** from your account page
   (it is per-user — it authenticates "as you", so treat it like a password).
2. Make it available to the CLI (resolution order: explicit arg → env → `~/.config/nirs4all-datasets/config.toml`
   → project `.env`):

```bash
export NIRS4ALL_DATAVERSE_INSTANCE="https://demo.recherche.data.gouv.fr"
export NIRS4ALL_DATAVERSE_TOKEN="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# (or:  ~/.config/nirs4all-datasets/config.toml  with  [dataverse] instance=... token=...  ; chmod 600)
```

3. Have a **collection alias** to publish into (create one in the sandbox UI, or ask for one). The
   alias is the short name in the collection's URL, e.g. `nirs4all`.

You can also pass `--instance https://demo.recherche.data.gouv.fr` on each command instead of the env var.

The token travels only in the `X-Dataverse-key` header, is never logged, and is never sent on a redirect
to signed object storage.

---

## 1. Pick a protected dataset and set its tier

The descriptor (`catalog/datasets/<id>.yaml`) decides access via its `tier`. Publishing here is for the
protected tiers only:

```yaml
tier: private        # public | private | anonymized
governance:
  license: LicenseRef-not-cleared   # protected data need not carry an open license
  owner_steward: "..."
  redistribution_rights: "Private use only; redistribution not cleared."
  consent_ethics_status: "..."
  anonymization_status: "..."
```

- **`private`** → everything is shown in the catalog/site, but files are uploaded **access-restricted**;
  only Dataverse accounts you grant access to can download them (with their own token). Metadata stays
  visible.
- **`anonymized`** → like `private`, plus the served data masks variable names and z-scores numeric
  targets (so you can publish metrics without revealing real values/identities).
- **`public`** is *not published here* — leave it linked to its origin. The governance gate
  (`publication_blockers()`) only checks the `public` tier, so a public descriptor must carry an open
  license + open origins; a `private`/`anonymized` descriptor is publishable to your personal Dataverse
  without those open-data requirements.

## 2. Validate before any network call

```bash
python catalog/scripts/validate.py --check-publish     # schema + publishability of public-tier datasets
```

## 3. First publication

```bash
n4a-datasets publish <id> --collection nirs4all --contact-email you@cirad.fr
```

This creates the dataset, uploads `datasets/<id>/canonical/` (+ `raw/`) with **`tabIngest=false`** (so
bytes stay pristine and SHA-256-verifiable), restricts the files because `tier != public`, publishes the
version, and **mints a DOI**. On success it automatically:

- writes the DOI + version back into `catalog/datasets/<id>.yaml` (`dataverse.doi`, `dataverse.dataset_version`),
- records the Dataverse **file ids + native checksums** in `datasets/<id>/manifest.json` (this is what
  makes token-gated download work), and
- rebuilds the card / Croissant / catalog.

Commit those updated files afterwards (`catalog/datasets/<id>.yaml`,
`datasets/<id>/{card.json,card.md,croissant.json,manifest.json}`).

## 4. Verify on the sandbox

Open the dataset's DOI landing page in the sandbox UI. Check the files, the metadata, and that the files
show as **restricted**.

## 5. Read it back (this is the payoff)

```python
import nirs4all_datasets as n4ad

ds = n4ad.get("<id>", token="...")    # private/anonymized: Dataverse access API with a permitted token
# the token is also auto-resolved from settings if you omit it for a non-public dataset
```

or from the shell: `n4a-datasets get <id> [--token ...]`. If the canonical data is still present locally,
`get` uses it directly (no download). Downloading only succeeds if the token belongs to an account you
granted access to (next section); without access, Dataverse refuses the restricted files.

> A `public` dataset never reaches this path — `get("<public-id>")` fetches its bytes from the origin
> DOI/URL via pooch, no token, no personal Dataverse.

## 6. Manage access (protected datasets)

```bash
n4a-datasets grant  <id> --to @collaborator --role fileDownloader   # let a user download
n4a-datasets grant  <id> --to "&my-group"                           # or a Dataverse group
n4a-datasets revoke <id> --to @collaborator                         # remove access
n4a-datasets restrict <id>          # make all files restricted (then republishes a minor version)
n4a-datasets restrict <id> --off    # make them downloadable again
```

Roles and restriction can be changed at any time after publication.

## 7. Update the data (new version)

Re-build the changed dataset (so `datasets/<id>/canonical` reflects the new bytes), then run the same
publish command — it **auto-detects** the existing DOI and publishes a **new version** (the DOI stays
stable; the version increments). The manifest's checksums + `dataset_version` are refreshed so `get`
keeps verifying the right bytes.

```bash
n4a-datasets build-all --source-tree <src> --only <id> --force   # refresh canonical from source
n4a-datasets publish <id>                                        # -> new version, same DOI
```

## 8. Clean up a botched sandbox attempt

If a publish failed mid-way and left a draft, delete the draft from the sandbox UI (or via the API) and
retry. Sandbox datasets are disposable.

---

## Going to production

Repeat with the production instance + a real collection:

```bash
export NIRS4ALL_DATAVERSE_INSTANCE="https://entrepot.recherche.data.gouv.fr"
n4a-datasets publish <id> --collection <prod-alias> --contact-email you@cirad.fr
```

Then commit the descriptor/card/manifest changes and push — the catalog site shows the DOI + version.

## Notes & current limits

- This is a **future** path: the Dataverse write methods (publish/update/grant/restrict) are covered by
  unit tests with a mocked client; the **sandbox run is the first real end-to-end test** — do it before
  production once the personal Dataverse is enabled.
- Only **protected** (`private` / `anonymized`) datasets are published here. Public data is linked to its
  origin and never re-hosted.
- One collection can hold several restricted datasets (access is per dataset/file).
- A token authenticates a *user*; "private" = restricted files + access granted to specific accounts.

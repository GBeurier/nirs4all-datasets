# Publishing to Dataverse — sandbox smoke-test, then production

This is the end-to-end walkthrough for putting datasets on Dataverse (Recherche Data Gouv / CIRAD)
with `nirs4all-datasets`, and for reading them back — public or private. **Always rehearse on the
sandbox first**; the production steps are identical, only the instance + collection differ.

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
2. Make it available to the CLI (resolution order: env → `~/.config/nirs4all-datasets/config.toml`
   → project `.env`):

```bash
export NIRS4ALL_DATAVERSE_INSTANCE="https://demo.recherche.data.gouv.fr"
export NIRS4ALL_DATAVERSE_TOKEN="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
# (or:  ~/.config/nirs4all-datasets/config.toml  with  [dataverse] instance=... token=...  ; chmod 600)
```

3. Have a **collection alias** to publish into (create one in the sandbox UI, or ask for one). The
   alias is the short name in the collection's URL, e.g. `nirs4all`.

You can also pass `--instance https://demo.recherche.data.gouv.fr` on each command instead of the env var.

---

## 1. Pick a dataset and set its governance

The descriptor (`catalog/datasets/<id>.yaml`) is where public/private is decided. Edit its `governance`:

```yaml
governance:
  license: CC-BY-4.0          # an OPEN SPDX licence is REQUIRED for visibility: public
  visibility: public          # public | restricted | embargo
  confidentiality_class: public   # public | internal ; 'confidential' is a hard stop (never published)
  # ...review the rest (consent/anonymization are auto-placeholders for generated descriptors):
  redistribution_rights: "Open redistribution under CC-BY-4.0."
  consent_ethics_status: "Not applicable (no human subjects)."
  anonymization_status: "Not applicable."
```

- **Public** dataset → `visibility: public` + `confidentiality_class: public` + an open licence. Anyone
  downloads it (no token).
- **Private** dataset → `visibility: restricted`. Files are uploaded **access-restricted**; only
  Dataverse accounts you grant access to can download (with their own token). Metadata stays visible.

> The governance gate refuses publication if the data is `confidential`, if a `public` dataset lacks an
> open licence / public confidentiality, or if a required governance field is blank.

## 2. Validate before any network call

```bash
python catalog/scripts/validate.py --check-publish     # schema + publishability of public/embargo datasets
```

## 3. First publication

```bash
n4a-datasets publish <id> --collection nirs4all --contact-email you@cirad.fr
```

This creates the dataset, uploads `datasets/<id>/canonical/` (+`raw/`), restricts the files if
`visibility != public`, publishes the version, and **mints a DOI**. On success it automatically:
- writes the DOI + version back into `catalog/datasets/<id>.yaml` (`dataverse.doi`, `dataverse.dataset_version`),
- records the Dataverse **file ids + native checksums** in `datasets/<id>/manifest.json` (this is what
  makes private download work), and
- rebuilds the card / Croissant / catalog.

Commit those updated files afterwards (`catalog/datasets/<id>.yaml`, `datasets/<id>/{card.json,card.md,croissant.json,manifest.json}`).

## 4. Verify on the sandbox

Open the dataset's DOI landing page in the sandbox UI. Check the files, the metadata, and — for a
private dataset — that the files show as **restricted**.

## 5. Read it back (this is the payoff)

```python
import nirs4all_datasets as n4ad

ds = n4ad.load("<id>")                 # PUBLIC: downloads by DOI via pooch, checksum-verified, cached
ds = n4ad.load("<id>", token="...")    # PRIVATE: Dataverse access API with a permitted token
# token is also auto-resolved from settings for a restricted dataset if you omit it
```
or from the shell: `n4a-datasets load <id> [--token ...]`. If the canonical data is still present
locally, `load` uses it directly (no download).

For a **private** dataset, downloading only succeeds if the token belongs to an account you granted
access to (next section). Without access, Dataverse refuses the restricted files.

## 6. Manage access (private datasets)

```bash
n4a-datasets grant  <id> --to @collaborator --role fileDownloader   # let a user download
n4a-datasets grant  <id> --to "&my-group"                           # or a Dataverse group
n4a-datasets revoke <id> --to @collaborator                         # remove access
n4a-datasets restrict <id>          # make all files restricted (then republishes a minor version)
n4a-datasets restrict <id> --off    # make them public again
```
Roles and restriction can be changed at any time after publication.

## 7. Update the data (new version)

Re-ingest the changed dataset (so `datasets/<id>/canonical` reflects the new bytes), then run the same
publish command — it **auto-detects** the existing DOI and publishes a **new version** (the DOI stays
stable; the version increments). The manifest's checksums + `dataset_version` are refreshed so `load`
keeps verifying the right bytes.

```bash
n4a-datasets build-all --source-tree <src> --only <id> --force   # refresh canonical from source
n4a-datasets publish <id>                                        # -> new version, same DOI
```

## 8. Clean up a botched sandbox attempt

If a publish failed mid-way and left a draft, delete the draft from the sandbox UI (or via the API)
and retry. Sandbox datasets are disposable.

---

## Going to production

Repeat with the production instance + a real collection:

```bash
export NIRS4ALL_DATAVERSE_INSTANCE="https://entrepot.recherche.data.gouv.fr"
n4a-datasets publish <id> --collection <prod-alias> --contact-email you@cirad.fr
```

Then commit the descriptor/card/manifest changes and push — the catalog site shows the DOI + version.

## Notes & current limits

- The Dataverse write paths (publish/update/grant/restrict) are covered by unit tests with a mocked
  client; the **sandbox run is the first real end-to-end test** — do it before production.
- One collection can hold both public and restricted datasets (access is per dataset/file).
- A token authenticates a *user*; "private" = restricted files + access granted to specific accounts.

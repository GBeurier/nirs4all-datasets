# Releasing

Three independent release flows: the **package** (PyPI), the **datasets** (Dataverse, for protected data),
and the **human validation** sign‑off.

## 1. The package → PyPI

The package builds cleanly and passes `twine check` (sdist + `py3-none-any` wheel). It depends only on
published packages — `nirs4all` is an **optional** `[nirs4all]` extra, so `pip install nirs4all-datasets`
resolves without the unpublished siblings.

### One‑time setup (no API token — Trusted Publishing / OIDC)

1. **Reserve the name / first upload.** Either create the project on PyPI by doing one manual upload
   from a maintainer machine:
   ```bash
   python -m build && python -m twine check dist/*
   python -m twine upload dist/*          # asks for your PyPI token once
   ```
   …or create an empty project + a *pending* Trusted Publisher (PyPI now supports project‑less pending
   publishers).
2. **Add the Trusted Publisher** on PyPI → *Your project → Publishing → Add a GitHub publisher*:
   - Owner `GBeurier`, repository `nirs4all-datasets`, workflow `release.yml`, environment `pypi`.
3. **Create the GitHub environment** `pypi` (repo → Settings → Environments) — optionally require manual
   approval so a tag does not publish unattended.

### Cut a release

```bash
# 1. bump the version
#    pyproject.toml:  version = "0.2.0"        (drop the .devN suffix for a real release)
# 2. commit + tag
git commit -am "release: v0.2.0"
git tag v0.2.0
git push origin main --tags
```

The tag triggers [`.github/workflows/release.yml`](../.github/workflows/release.yml): it builds, runs
`twine check`, and publishes to PyPI via OIDC (gated on the `pypi` environment). Verify with
`pip install nirs4all-datasets` in a clean venv.

> **Caveat — runtime catalog.** The wheel ships the *code*, not the *catalog* (descriptors/index/cards
> live in git). Until the catalog index is bundled into the wheel (or fetched from GitHub on demand,
> pooch‑style — the planned next step), a pip‑installed consumer must point `get(root=<checkout>)` at a
> clone of this repo. The package is publishable today; this only affects fully standalone `get()`.

## 2. The datasets → Dataverse (protected data)

**Public datasets are not published here** — they are linked to their origin. **Private / anonymized**
datasets can later be uploaded to a *personal* Dataverse so consumers can `get(token=…)` them. The list of
datasets awaiting upload is generated in [`PRIVATE_DATASETS.md`](PRIVATE_DATASETS.md) (`n4a-datasets status`).

- **Token:** `NIRS4ALL_DATAVERSE_TOKEN` env var, or `~/.config/nirs4all-datasets/config.toml` (chmod 600),
  or a project `.env`. The token travels only in `X-Dataverse-key`, is never logged, and is never sent on
  an S3 redirect. Prefer the **sandbox** (`demo.recherche.data.gouv.fr`) before production.
- **Locally:**
  ```bash
  n4a-datasets publish <id> --collection <alias> --contact-email you@example.org   # mints a DOI (first time)
  n4a-datasets restrict <id>            # access-gate all files, publish a minor version
  n4a-datasets grant <id> --to @user    # let a user download restricted files
  ```
- **In CI:** the manual [`publish.yml`](../.github/workflows/publish.yml) workflow (workflow_dispatch,
  gated on the protected `dataverse-publish` environment; token = the `DATAVERSE_TOKEN` secret).
- The governance gate (`validate.py --check-publish`) refuses a public dataset that is not openly
  licensed/sourced. Full walkthrough: [`PUBLISHING.md`](PUBLISHING.md).

On success the minted DOI is written back into `catalog/datasets/<id>.yaml`, so the dataset moves from
`upload_pending` to `on_dataverse` in the status reports automatically.

## 3. Human validation sign‑off

Validation is tracked in `catalog/validation.yaml` (never touched by `bootstrap`). To review a dataset,
edit its record and bump `validation` `pending → reviewed → approved` (add `reviewed_by` / `reviewed_at` /
`notes`), then refresh the reports:

```bash
n4a-datasets status --root .     # rewrites docs/DATASET_STATUS.md + docs/PRIVATE_DATASETS.md
git add catalog/validation.yaml docs/DATASET_STATUS.md docs/PRIVATE_DATASETS.md && git commit
```

## Release checklist

- [ ] Green gate: `ruff check .` · `mypy --config-file pyproject.toml src` · `validate.py` (+ `--check-publish`) · `pytest -q`
- [ ] `catalog`, `health-check`, `status` re‑run and committed (the index/health/status reports are up to date)
- [ ] version bumped in `pyproject.toml`; `python -m build && twine check dist/*` clean
- [ ] tag `vX.Y.Z` pushed (PyPI) / `publish.yml` dispatched per dataset (Dataverse)

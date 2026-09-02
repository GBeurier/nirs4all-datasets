# Releasing

Three independent release flows: the **package** (PyPI), the **datasets** (Dataverse, for protected data),
and the **human validation** sign‑off.

## 1. The package → PyPI

The package is a multi-surface release: platform wheels and an sdist, Rust
crates, npm/WASM, R, MATLAB/Octave, C ABI, and source/provenance artifacts. The
canonical operational procedure is
[`docs/dev/release_process.md`](https://github.com/GBeurier/nirs4all-datasets/blob/main/docs/dev/release_process.md);
this page only summarizes
the catalog-specific flows.

For the V1 train, public release is fail-closed on the exact contract in
[`release/train-v1.toml`](../release/train-v1.toml): Datasets 0.3.9 consumes
Formats 0.2.8 and IO 0.1.12. Run the offline consistency check at any time:

```bash
python scripts/check_release_train.py
```

Immediately before tagging or publishing, require the actual registry state:

```bash
python scripts/check_release_train.py --release --check-registry
```

This second command must stay **HOLD** until the upstream crates are published
in order (DMD 0.2.10, Formats 0.2.8, then IO 0.1.12). Local sibling/path builds
are useful qualification evidence but cannot
prove that a released wheel, crate, or source package resolves from public
registries.

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
   - Owner `GBeurier`, repository `nirs4all-datasets`, workflow `release-python.yml`, environment `pypi`.
3. **Create the GitHub environment** `pypi` (repo → Settings → Environments) — optionally require manual
   approval so a tag does not publish unattended.

### Cut a release

```bash
scripts/bump_version.sh --bump 0.3.9
scripts/bump_version.sh --check
python scripts/check_release_train.py --release --check-registry
git commit -am "chore(release): bump datasets to 0.3.9"
git tag v0.3.9
git push origin main --tags
```

The tag triggers the per-surface `release-*.yml` workflows documented in the
canonical release process. Python publishes through
[`release-python.yml`](../.github/workflows/release-python.yml) and the protected
`pypi` environment. Verify the published package in a clean virtual environment.

> **Caveat — runtime catalog.** The wheel ships the code **and** the bundled
> cross-language `catalog/index.json`, but the assembled catalog
> (`catalog/datasets.yaml`), descriptors, cards, and manifests still live in the
> registry checkout. A pip-installed Python consumer therefore still points
> `get(root=<checkout>)` at a clone of this repo for the high-level
> `get()/list()/card()` surface. Non-Python bindings can consume the bundled or
> committed `catalog/index.json` directly.

## 2. The datasets → Dataverse (protected data)

**Public datasets are not published here** — they are linked to their origin. **Private / anonymized**
datasets can later be uploaded to a *personal* Dataverse so consumers can `get(token=…)` them. The list of
datasets awaiting upload is generated locally by `n4a-datasets status` (a maintainer-only worklist, not
published here).

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

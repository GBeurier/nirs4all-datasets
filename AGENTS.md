# Datasets contributor instructions

## Ownership and source fidelity

Datasets owns catalog/descriptors, provenance, acquisition/cache, canonical writing/manifests, cards/datasheets/Croissant, origin health, content services and host orchestration. Raw measured reality is not an invented benchmark task: keep sources/axes separate, asymmetric repetitions aligned by sample identity rather than positions, all variables and only origin-declared targets; document native partitions without applying or inventing them. Catalog origin bytes stay at the origin, never re-hosted or committed as heavy payloads.

Never duplicate NIRS/IO parsers or scientific kernels. Optional SDK/IO/Formats/Methods bridges retain their owner responsibilities and lazy availability. Acquisition is native; qualification/card/site/health/anonymization/catalog assembly stay in their declared Python host layer, not ported across the ABI. Use [architecture](docs/ARCHITECTURE.md#2-module-map), [design](docs/DESIGN.md) and current manifests/contracts to discover supported operations; old version labels are not universal capability claims.

Read the [curation ownership roadmap](docs/maintenance/curation_ownership_roadmap.md) before curation/cache/qualification/native-boundary work. Its IO/DAG/DMD restrictions apply to that curation work; the old AGENTS DAG/DMD user constraint is not a universal ban on currently authorized owner fixes. Keep original columns, missing/censor evidence, declared dependencies and observation grain; consume matching native methods, never add duplicate PCA merely to transfer ownership. Preserve existing protocol-specific SDK PCA until complete parity is established.

## Critical data, privacy and credentials

Every displayed anonymized surface must derive fields through `anonymize.public_card` / `public_descriptor`; never render raw anonymized descriptor fields. Follow [tiers and anonymization](docs/ARCHITECTURE.md#5-tiers-and-anonymization-loadbearing).

Dataverse tokens travel only in `X-Dataverse-key`, are never logged, and never follow a redirect with the key attached. Preserve explicit argument → `NIRS4ALL_DATAVERSE_TOKEN` → private config → project `.env` precedence and chmod 600 in [token setup](README.md#api-token--where-to-put-it); project-service credentials are separate.

Keep schema validity distinct from tier-gated `publication_blockers()`: public requires open SPDX license, open origins and release-governance fields; private/anonymized descriptors remain valid without open publication. Never merge origin members with different licences or infer rights from a checksum. Follow [governance](docs/DESIGN.md#3-governance--visibility--3-tiers) and [protected publishing limits](docs/PUBLISHING.md#notes--current-limits), not a blanket rehosting exception.

The separate [private store](docs/PRIVATE_STORE.md#assertions-and-evidence) admits manifest-first asserted descriptors and opaque submitted private bytes outside Git/catalog/cache. Unknown provenance stays unverified; hash-only integrity establishes neither origin nor rights. Refuse declared public-origin-download bytes and fetch/mirror requests before payload intake; perform no origin detection/acquisition/IO parsing/qualification or catalog/card generation.

The offline store never authenticates callers. For authenticated gates, the optional [project service](docs/PROJECT_SERVICE.md#authentication-and-routes) requires the owner's accepted installed wheel for Access; the service must authenticate before body reads, with exact project rights, restart snapshots and no mandatory Cluster dependency. Retain private no-follow storage, project-local integrity/idempotence, admission/deadline/cancellation/logging and [remaining platform/evidence limits](docs/PROJECT_SERVICE.md#remaining-limits). Implementation tests are not final WORK acceptance.

## Maintenance and commands

Re-run the maturin editable install after every Rust change to avoid a stale `_n4ds.abi3.so`; the root pyproject builds the embedded extension and editable sibling bridges require their declared toolchains. Keep Python 3.11+, Google docstrings/public types, `py.typed`, configured Ruff 220/mypy, Rust 2021/rustfmt, stable lowercase dataset slugs and the `n4ds_` C ABI prefix.

For product changes, add focused pytest coverage in `tests/` using `tests/conftest.py`, and mark live-origin checks `@pytest.mark.network`. Rust changes retain crate/workspace tests; binding changes retain their relevant build and smoke, including the WASM Node smoke after its build. These requirements remain future product gates, not executed evidence for instruction edits.

From this checkout and its package environment, preserve the original local Python/Rust/catalog entrypoints. `uv pip install` uses the editable `[tool.uv.sources]` sibling paths for `nirs4all`, `nirs4all-io` and `nirs4all-formats`. Cargo requires `../nirs4all-formats` and `../nirs4all-io` locally; `scripts/ensure_rust_deps.sh` checks them out in CI:

```bash
uv venv && uv pip install -e ".[dev]"
ruff check .
mypy --config-file pyproject.toml src
python catalog/scripts/validate.py
python catalog/scripts/validate.py --check-publish
python -m nirs4all_datasets.cli catalog --root . && git diff --exit-code catalog/datasets.yaml
pytest -q
pytest -m "not network"
cargo fmt --all --check
cargo clippy --workspace --all-targets -- -D warnings
cargo test --workspace
```

Network-marked checks are opt-in; unit origin/Dataverse tests use fake sessions. Preserve canonical round-trip skips on unsupported older oracle versions. Regenerate and keep both catalog/datasets.yaml and catalog/index.json current, not only the CI-diffed YAML; human catalog/validation.yaml is never bootstrap output.

Use the separate [quality gates](docs/maintenance/quality_gates.md#local-green-gate), [release checklist](docs/maintenance/release_checklist.md#pre-release-do-all-before-tagging), [release blockers](docs/dev/release_process.md#pre-release-gates-release-blockers) and [release summary](docs/RELEASING.md). Preserve the Rust-toolchain maturin prerequisite, workspace-excluded bindings/C-ABI snapshots, exact dependency train/HOLD and immutable published artifacts, independent ABI version/symbol checks, cross-manifest sync and owner license-identity checks. No release, registry or scientific gate is declared green here.

The original CLI grammar below remains reference-only. These lifecycle operations keep their original prerequisites and effects; publish/governance commands remain FUTURE protected-personal-Dataverse operations, not a permission grant. See [CONTRIBUTING](CONTRIBUTING.md) and [PUBLISHING](docs/PUBLISHING.md); standardized bundle import never executes bundle scripts.

```bash
# Author / build the catalog
n4a-datasets bootstrap <source_tree> [--prune] [--force]            # bootstrap.py: a descriptor per v2.0/<leaf>
n4a-datasets add <raw_source> <id>                                  # one raw source -> canonical + card + index
n4a-datasets build-all --source-tree <tree> [--only a,b] [--force]  # bulk.py: parallel organize+qualify, then index
                       [--protocol-refresh] [--skip-assets] [--site]
n4a-datasets import-standardized <bundle> <id> --out <dir>          # v2.0 bundle -> canonical, never runs its scripts
n4a-datasets curate <source_tree> [--only a,b]                      # curation.py: traced M/Y views -> catalog/curation/<id>.json
n4a-datasets qualify <id> [--anonymize]                             # (re)build one card.json (+ card.anon.json)
n4a-datasets health-check [--only a,b]                              # health.py: probe open origins -> catalog/health.json
n4a-datasets catalog                                                # regenerate catalog/datasets.yaml + index.json
n4a-datasets index                                                  # regenerate only catalog/index.json
n4a-datasets status                                                 # docs/DATASET_STATUS.md + docs/PRIVATE_DATASETS.md
n4a-datasets retrieval-audit                                        # static retrieval-readiness worklist -> catalog/retrieval_audit.json
n4a-datasets site [--out site]                                      # site/: interactive static catalog
n4a-datasets list [--tier ...] [--domain ...] [--spectro-family ...]   # inspect the local catalog
n4a-datasets card <id>                                              # print one identity card (JSON)

# Access
n4a-datasets get <id> [--source X1] [--token ...] [--instance ...]  # canonical NirsDataset: local-first, else fetch
n4a-datasets retrieve <id>                                          # raw origin bytes, staged by the Rust reader stack

# Publish + governance (FUTURE — personal Dataverse for protected data; see docs/PUBLISHING.md)
n4a-datasets publish <id> --collection <alias> --contact-email <addr>  # first publish mints a DOI; later = version update
n4a-datasets restrict <id> [--off]                                  # (un)restrict all files, then publish a minor version
n4a-datasets grant|revoke <id> --to @user|&group [--role fileDownloader]
```

Keep [content/metadata hash axes](CONTRIBUTING.md#bulk-authoring-many-datasets-at-once), managed-descriptor/prune protections and [incrementality](docs/ARCHITECTURE.md#6-incrementality--the-two-axes). For the scoped curation correction, declared type/role/unit/dependencies affect processing/cache identity under the roadmap; older architecture shorthand calling variable-role purely descriptive does not override that correction. Never rewrite old hashes to simulate a rebuild. Follow [canonical layout](docs/ARCHITECTURE.md#4-canonical-ondisk-layout), [Parquet/tabIngest rules](docs/PUBLISHING.md#3-first-publication), [public validation](docs/PUBLISHING.md#2-validate-before-any-network-call) and [enum/convention mirrors](docs/ARCHITECTURE.md#9-conventions). Use the [residual instruction note](docs/maintenance/agent_invariants.md) only for uncovered maintenance rules and invocation variants.

Use scoped Conventional Commits, including `data(<id>): add <name>` for data additions, and report actual commands, issue/context and regeneration effects; screenshots apply only to visible changes. Correct English narratives in source contracts/descriptors before verifying regenerated cards. Author/commit as `GBeurier <95907737+GBeurier@users.noreply.github.com>` and verify authenticated GBeurier authority before authorized remote writes; credential location follows applicable workspace/operator policy, never another account or exposed secrets. Follow [LICENSING](LICENSING.md): owner code/commercial/content terms and each dataset's own SPDX rights, with release manifest license checks unchanged.

## Working rules

Read applicable local and deeper instructions before editing. Preserve dirty/concurrent work and make only authorized changes. When a workspace policy exists at `../AGENTS.md`, read it within the current user scope; this local policy also works in a standalone checkout. An existing `CLAUDE.md` is a compatibility entrypoint, not a second policy dependency.

Use CodeGraph FIRST for implementation navigation only when this checkout has its own `.codegraph/`; use its exact projectPath or run the CLI here. Never auto-index or substitute an ancestor index. Unindexed code, docs and configs use ordinary source navigation; source, tests and build tools remain final authority.

Keep secrets, private data, generated workspaces, caches and build outputs out of Git. Respect owner licenses and fixture restrictions, record actual commands/exits/skips, and preserve scoped authorization: command examples do not grant installation, science, publishing, hosting or frontend work.

All application and project content must be in English, including UI text, subtitles, tooltips, errors, documentation, comments and docstrings, test and fixture prose, reports, pull requests, commits, and generated content. Conversation with the maintainer may be in French. Preserve proper names, identifiers, filenames, source quotations, and historical or provenance records where translation would change their meaning or provenance.

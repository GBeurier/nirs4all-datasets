# Quality gates — nirs4all-datasets

A maturin (Rust + Python) package with R / MATLAB / WASM bindings and a multi-registry release fleet.

## Local green gate

```bash
pip install -e ".[dev]"        # builds the Rust extension via maturin (needs a Rust toolchain)
ruff check .                   # lint (line-length 220, py311)
mypy --config-file pyproject.toml src   # types (matches CI; avoids non-package data trees)
pytest -q                      # Python suite (network-marked tests self-skip)
```

The C ABI snapshot, WASM (`wasm-pack`), and R/MATLAB bindings are validated in CI (`abi-check.yml`,
`ci.yml`) rather than in the default local gate.

Optional local hooks (`pre-commit` fetched on demand): `uvx pre-commit run --all-files`.

## CI gates (`.github/workflows/`)

| workflow | trigger | gate |
|---|---|---|
| `ci.yml` | push/PR `main`, `rc/**` | Rust build + tests, WASM build, `npm pack --dry-run` |
| `abi-check.yml` | push/PR | C ABI snapshot diff |
| `docs.yml` | push/PR | docs build + Pages |
| `version-guard.yml` / `version-sync.yml` | push/PR | manifest not ahead of tag; cross-manifest version sync |
| `release-{python,crates,npm,r,matlab,source}.yml` | **tag `v*` / dispatch** | build + publish (PyPI / crates.io / npm / CRAN / MATLAB) — **never on branch push** |

All third-party actions are **SHA-pinned** (56 pins across 12 workflows), Dependabot-tracked; the sole
exception is `dtolnay/rust-toolchain@stable`, left floating **by design** (always latest stable Rust).

## Known gaps / flags (deepest-hardening roadmap)

- **License header mismatch:** `CHANGELOG.md` carries `SPDX-License-Identifier: MIT` while `pyproject.toml`
  declares `CeCILL-2.1 OR AGPL-3.0-or-later`. **Left unchanged — license identity is a maintainer decision;
  reconcile before release.**
- No enforced coverage floor.
- Release fleet is multi-registry to immutable stores — see `release_checklist.md`.

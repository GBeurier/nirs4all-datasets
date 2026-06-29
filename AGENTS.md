# Repository Guidelines

## Project Structure & Module Organization

This repository combines a Python package, a Rust acquisition core, catalog metadata, and generated dataset cards. Python code lives in `src/nirs4all_datasets/`, with CLI entry points in `cli.py` and site generation under `src/nirs4all_datasets/site/`. Rust crates are in `crates/`; language bindings live in `bindings/python`, `bindings/wasm`, `bindings/r`, and `bindings/matlab`. Dataset descriptors are in `catalog/datasets/*.yaml`; generated cards, manifests, and Croissant files are in `datasets/<id>/`. Tests are in `tests/`, docs in `docs/`, and branding assets in `assets/brand/`.

## Build, Test, and Development Commands

- `uv venv && uv pip install -e ".[dev]"`: create a dev environment and build the embedded Rust extension through maturin.
- `ruff check .`: lint Python files using the project Ruff configuration.
- `mypy --config-file pyproject.toml src`: type-check the Python package.
- `python catalog/scripts/validate.py`: validate every catalog descriptor.
- `python -m nirs4all_datasets.cli catalog --root . && git diff --exit-code catalog/datasets.yaml`: regenerate and verify the committed catalog index.
- `pytest -q` or `pytest -m "not network"`: run Python tests; network tests are opt-in.
- `cargo fmt --all --check`, `cargo clippy --workspace --all-targets -- -D warnings`, `cargo test --workspace`: run the Rust green gate.

## Coding Style & Naming Conventions

Python targets 3.11+, uses Ruff with a 220-character line length, and follows typed-package conventions (`py.typed`). Keep modules snake_case and tests named `test_*.py`. Rust uses edition 2021 and standard `rustfmt`; exported C ABI symbols must keep the `n4ds_` prefix. Dataset IDs are stable lowercase slugs matching `^[a-z0-9]+(_[a-z0-9]+)*$`.

## Testing Guidelines

Add focused pytest coverage in `tests/`, reusing fixtures from `tests/conftest.py`. Mark live-origin checks with `@pytest.mark.network` so CI can exclude them. For Rust changes, include crate-level tests where practical and run the workspace test command. Binding changes should include the relevant smoke test, such as `node bindings/wasm/tests/node_smoke.cjs` after a WASM build.

## Commit & Pull Request Guidelines

Recent history uses Conventional Commit-style subjects, for example `fix(packaging): ...`, `ci: ...`, and `chore(release): ...`; dataset additions commonly use `data(<id>): add <name>`. Keep commits scoped and include regenerated catalog files when commands change them. Pull requests should describe the behavior or dataset change, list the validation commands run, link related issues, and include screenshots only for visible site or documentation changes.

## Security & Configuration Tips

Never commit tokens or heavy raw/canonical dataset bytes. Use `NIRS4ALL_DATAVERSE_TOKEN`, `~/.config/nirs4all-datasets/config.toml`, or a gitignored `.env` for protected Dataverse access. Public datasets must keep open, verifiable origins and SPDX license metadata.

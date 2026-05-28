"""Command-line interface (``n4a-datasets``).

Thin orchestration over the library modules. Heavy dependencies (nirs4all, matplotlib) are
imported lazily inside the commands that need them, so ``--help``, ``catalog``, ``list`` and
``card`` work in a minimal environment.
"""
from __future__ import annotations

import json
from pathlib import Path

import typer
import yaml

app = typer.Typer(add_completion=False, help="Store, qualify, and organize NIRS reference datasets.")


def _descriptor(root: Path, dataset_id: str):
    from nirs4all_datasets.schema import DatasetDescriptor

    path = root / "catalog" / "datasets" / f"{dataset_id}.yaml"
    if not path.exists():
        raise typer.BadParameter(f"no descriptor for {dataset_id!r} at {path}")
    return DatasetDescriptor(**(yaml.safe_load(path.read_text(encoding="utf-8")) or {}))


@app.command()
def catalog(root: Path = typer.Option(Path("."), help="Registry root.")) -> None:
    """(Re)assemble catalog/datasets.yaml from all descriptors + cards."""
    from nirs4all_datasets.catalog import build_catalog

    result = build_catalog(root)
    typer.echo(f"catalog: {result['n_datasets']} dataset(s) -> {root / 'catalog' / 'datasets.yaml'}")


@app.command("list")
def list_cmd(
    root: Path = typer.Option(Path("."), help="Registry root."),
    task: str | None = typer.Option(None, help="Filter by task type."),
    visibility: str | None = typer.Option(None, help="Filter by visibility."),
) -> None:
    """List catalog datasets (optionally filtered)."""
    from nirs4all_datasets.catalog import search

    entries = search(root, task_type=task, visibility=visibility)
    if not entries:
        typer.echo("(no datasets)")
        return
    for entry in entries:
        typer.echo(f"{entry['id']:<30} {entry['task_type']:<12} n={entry.get('n_samples')} vis={entry['visibility']} doi={entry.get('doi')}")


@app.command()
def card(dataset_id: str, root: Path = typer.Option(Path("."), help="Registry root.")) -> None:
    """Print a dataset's identity card (JSON)."""
    from nirs4all_datasets.catalog import get_card

    data = get_card(root, dataset_id)
    if data is None:
        typer.echo(f"no card for {dataset_id!r} (run: n4a-datasets qualify {dataset_id})", err=True)
        raise typer.Exit(1)
    typer.echo(json.dumps(data, indent=2))


@app.command()
def add(
    source: Path,
    dataset_id: str,
    root: Path = typer.Option(Path("."), help="Registry root."),
    signal: str | None = typer.Option(None, help="Signal to use for multi-signal instrument files."),
) -> None:
    """Ingest raw SOURCE into datasets/<id>, build its card, and refresh the catalog."""
    from nirs4all_datasets.catalog import build_catalog
    from nirs4all_datasets.organize import organize
    from nirs4all_datasets.qualify.profile import build_card

    descriptor = _descriptor(root, dataset_id)
    result = organize(source, descriptor, root / "datasets", signal=signal)
    typer.echo(f"organize: {'skipped (unchanged)' if result.skipped else 'processed'} -> {result.dataset_dir}")
    if not result.skipped or not (result.dataset_dir / "card.json").exists():
        build_card(result.dataset_dir, descriptor)
        typer.echo("card built")
    build_catalog(root)


@app.command()
def qualify(dataset_id: str, root: Path = typer.Option(Path("."), help="Registry root.")) -> None:
    """(Re)build a dataset's identity card from its canonical data."""
    from nirs4all_datasets.qualify.profile import build_card

    descriptor = _descriptor(root, dataset_id)
    build_card(root / "datasets" / dataset_id, descriptor)
    typer.echo(f"card: datasets/{dataset_id}/card.json")


@app.command()
def publish(
    dataset_id: str,
    collection: str = typer.Option(..., help="Dataverse collection alias to publish into."),
    contact_email: str = typer.Option(..., help="Dataset contact email (required by Dataverse)."),
    root: Path = typer.Option(Path("."), help="Registry root."),
    instance: str | None = typer.Option(None, help="Dataverse instance URL override."),
) -> None:
    """Publish a dataset to Dataverse (governance-gated, first publication)."""
    from nirs4all_datasets.config import get_settings
    from nirs4all_datasets.dataverse import DataverseClient
    from nirs4all_datasets.publish import publish_dataset

    descriptor = _descriptor(root, dataset_id)
    settings = get_settings(instance=instance)
    client = DataverseClient(settings.instance, token=settings.require_token())
    result = publish_dataset(descriptor, root / "datasets" / dataset_id, client, collection=collection, contact_email=contact_email)
    typer.echo(f"published {dataset_id}: DOI {result['doi']} ({result['files']} files)")


@app.command()
def bootstrap(
    source_tree: Path,
    root: Path = typer.Option(Path("."), help="Registry root."),
    xlsx: Path | None = typer.Option(None, help="DatabaseDetail.xlsx master sheet (optional metadata enrichment)."),
    force: bool = typer.Option(False, help="Overwrite managed descriptors even when unchanged."),
) -> None:
    """Auto-generate schema-valid descriptors for every dataset leaf under SOURCE_TREE."""
    from nirs4all_datasets.catalog import build_catalog
    from nirs4all_datasets.discover import bootstrap as run_bootstrap

    report = run_bootstrap(source_tree, root, xlsx_path=xlsx, force=force)
    typer.echo(f"bootstrap: created={len(report['created'])} updated={len(report['updated'])} skipped={len(report['skipped'])} errors={len(report['errors'])}")
    for err in report["errors"][:10]:
        typer.echo(f"  ERROR {err['leaf']}: {err['error']}", err=True)
    build_catalog(root)


@app.command("build-all")
def build_all_cmd(
    source_tree: Path = typer.Option(..., help="Read-only source tree the descriptors were generated from."),
    root: Path = typer.Option(Path("."), help="Registry root."),
    workers: int | None = typer.Option(None, help="Parallel workers (default: CPU-2, capped at 6)."),
    only: str | None = typer.Option(None, help="Comma-separated dataset ids to (re)build."),
    skip_assets: bool = typer.Option(False, help="Skip plot rendering (faster cards)."),
    force: bool = typer.Option(False, help="Rebuild even when unchanged."),
    site: bool = typer.Option(True, help="Build the static site afterwards."),
) -> None:
    """Organize + qualify all datasets (parallel), refresh the catalog, and build the site."""
    from nirs4all_datasets.bulk import build_all, write_report
    from nirs4all_datasets.catalog import build_catalog

    only_ids = [s.strip() for s in only.split(",") if s.strip()] if only else None

    def _progress(done: int, total: int, rec: dict) -> None:
        mark = {"ok": "✓", "partial": "~", "skipped": "·", "failed": "✗"}.get(rec["status"], "?")
        suffix = f"  ({rec.get('reason')})" if rec["status"] == "failed" else ""
        typer.echo(f"[{done}/{total}] {mark} {rec['id']}{suffix}")

    report = build_all(root, source_tree, workers=workers, only=only_ids, skip_assets=skip_assets, force=force, progress=_progress)
    write_report(report, root / "bulk_report.json")
    typer.echo(f"build-all: {report['counts']} -> {root / 'bulk_report.json'}")
    build_catalog(root)
    if site:
        from nirs4all_datasets.site import build_site

        typer.echo(f"site: {build_site(root, root / 'site')}")


@app.command("site")
def site_cmd(
    root: Path = typer.Option(Path("."), help="Registry root."),
    out: Path = typer.Option(Path("site"), help="Output directory for the static site."),
) -> None:
    """Build the interactive static catalog site from the catalog + generated cards."""
    from nirs4all_datasets.site import build_site

    typer.echo(f"site: {build_site(root, out)}")


@app.command()
def load(dataset_id: str, root: Path = typer.Option(Path("."), help="Registry root.")) -> None:
    """Load a local dataset and print a one-line summary (smoke test)."""
    from nirs4all_datasets.access import load_local

    dataset = load_local(root / "datasets" / dataset_id).get_dataset_at(0)
    typer.echo(f"loaded {dataset_id}: {dataset.num_samples} samples x {dataset.num_features} features ({dataset.task_type})")


if __name__ == "__main__":  # pragma: no cover
    app()

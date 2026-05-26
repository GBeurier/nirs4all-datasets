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
def load(dataset_id: str, root: Path = typer.Option(Path("."), help="Registry root.")) -> None:
    """Load a local dataset and print a one-line summary (smoke test)."""
    from nirs4all_datasets.access import load_local

    dataset = load_local(root / "datasets" / dataset_id).get_dataset_at(0)
    typer.echo(f"loaded {dataset_id}: {dataset.num_samples} samples x {dataset.num_features} features ({dataset.task_type})")


if __name__ == "__main__":  # pragma: no cover
    app()

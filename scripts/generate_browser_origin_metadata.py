"""Project public origin metadata for the filesystem-free acquisition surface."""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    index_path = root / "catalog/index.json"
    recipes_path = root / "src/nirs4all_datasets/public_pull/ecosis_recipes.json"
    other_path = root / "src/nirs4all_datasets/public_pull/other.py"
    public = {key: value for key, value in json.loads(index_path.read_bytes())["datasets"].items()
              if value["tier"] == "public" and value["descriptor"]["tier"] == "public"}
    recipes = {key: value for key, value in json.loads(recipes_path.read_bytes()).items() if key in public}
    for recipe in recipes.values():
        recipe["metadata_constants"] = {"ecosis_resource_id": recipe.get("resource_id")}
        if recipe.get("child"):
            recipe["metadata_constants"]["SpectralRep"] = 1
    # The existing Other._zenodo/13122321 recipe reads one CSV, normalizes
    # its first 13 metadata names, and deliberately keeps scans observation-aligned.
    zenodo = next(ast.literal_eval(node.value) for node in ast.parse(other_path.read_text()).body
                  if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == "_ZENODO" for target in node.targets))
    soil_id = "zenodo_neospectra_soil_nir_ccby"
    record, filename = zenodo[soil_id]
    url = f"https://zenodo.org/api/records/{record}/files/{filename}/content"
    if soil_id in public:
        recipes[soil_id] = {"url": url, "filename": filename, "resource_id": filename, "sample_column": None,
                           "metadata_columns": {}, "metadata_prefix_count": 13, "generated_observation_identity": True,
                           "observation_id_width": 5, "metadata_constants": {"dataset_id": soil_id, "origin_url": url}}
    value = {
        "schema": "nirs4all.datasets.browser-origin-metadata.v1",
        "index_sha256": hashlib.sha256(index_path.read_bytes()).hexdigest(),
        "recipes_sha256": hashlib.sha256(recipes_path.read_bytes() + b"\0" + other_path.read_bytes()).hexdigest(),
        "recipe_sources": {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest() for path in [recipes_path, other_path]},
        "datasets": {key: {"descriptor": item["descriptor"], "retrieval": item["retrieval"]} for key, item in public.items()},
        "table_recipes": recipes,
    }
    text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    output = root / "crates/nirs4all-datasets-core/src/browser_origin_metadata.json"
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    if parser.parse_args().check:
        if output.read_text(encoding="utf-8") != text:
            raise SystemExit("Browser origin metadata is stale; run this script without --check")
    else:
        output.write_text(text, encoding="utf-8")
    print(f"Browser origin metadata: {len(public)} public descriptors; {len(text.encode())} bytes; no dataset payloads")


if __name__ == "__main__":
    main()

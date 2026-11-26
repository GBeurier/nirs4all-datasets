"""Stage exact license texts for the locked WASM dependency closure."""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_CLOSURE = "2b64001695ebe0e00bc066e2999697a0455a349d726550f083d6805994754b6e"


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package", type=Path)
    args = parser.parse_args()
    package = args.package.resolve()
    package_json = json.loads((package / "package.json").read_text())
    version = tomllib.loads((ROOT / "Cargo.toml").read_text())["workspace"]["package"]["version"]
    if package_json["version"] != version:
        raise SystemExit("Generated package version differs from the source workspace")
    command = ["cargo", "metadata", "--locked", "--offline", "--manifest-path", "bindings/wasm/Cargo.toml", "--format-version=1"]
    metadata = json.loads(subprocess.check_output(command, cwd=ROOT, text=True))
    lines = sorted(f"{item['name']}@{item['version']}|{item.get('license') or 'NO-LICENSE'}" for item in metadata["packages"])
    closure = digest(("\n".join(lines) + "\n").encode())
    if closure != EXPECTED_CLOSURE:
        raise SystemExit(f"Locked WASM license closure changed ({closure}); inspect every expression before updating the guard")
    payload: dict[str, bytes] = {}
    components = []
    for item in sorted(metadata["packages"], key=lambda value: (value["name"], value["version"])):
        source = Path(item["manifest_path"]).parent
        texts = {path.name: path.read_bytes() for path in source.iterdir()
                 if path.is_file() and path.name.upper().startswith(("LICENSE", "COPYING", "NOTICE", "UNLICENSE"))}
        if item["name"].startswith("nirs4all-") and item["source"] is None:
            owner = ROOT if item["name"].startswith("nirs4all-datasets-") else next(
                (path for path in (source, *source.parents[:4]) if (path / ".git").exists()), None)
            if owner is None:
                raise SystemExit(f"Cannot locate the declared source owner's notices: {item['name']}")
            for name in ("LICENSE", "LICENSING.md", "THIRD_PARTY_NOTICES.md", "COPY_PROVENANCE.md"):
                if (owner / name).is_file():
                    texts[f"owner/{name}"] = (owner / name).read_bytes()
            if (owner / "LICENSES").is_dir():
                texts.update({f"owner/LICENSES/{path.relative_to(owner / 'LICENSES').as_posix()}": path.read_bytes()
                              for path in (owner / "LICENSES").rglob("*") if path.is_file()})
        if item.get("license_file"):
            path = source / item["license_file"]
            texts[f"declared/{path.name}"] = path.read_bytes()
        if not texts:
            raise SystemExit(f"No actual license text found for {item['name']}@{item['version']}")
        files = {}
        for name, data in sorted(texts.items()):
            relative = f"LICENSES/THIRD-PARTY/{item['name']}-{item['version']}/{name}"
            payload[relative] = data
            files[relative] = digest(data)
        components.append({"name": item["name"], "version": item["version"], "license": item["license"], "files": files})
    payload["THIRD_PARTY_NOTICES.md"] = (ROOT / "THIRD_PARTY_NOTICES.md").read_bytes()
    payload["LICENSE-CeCILL-2.1"] = (ROOT / "LICENSES/CeCILL-2.1.txt").read_bytes()
    for relative, data in payload.items():
        destination = package / relative
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(data)
    receipt = {"schema": "nirs4all-datasets.wasm-license-closure.v1", "version": version,
               "scope": "Locked Cargo metadata closure, including build dependencies; not a publication or runtime-reachability claim",
               "closure_sha256": closure, "components": components}
    (package / "nirs4all-datasets-wasm.licenses.json").write_text(json.dumps(receipt, indent=2) + "\n")
    package_json["files"] = list(dict.fromkeys([*package_json.get("files", []), "LICENSE", "LICENSE-CeCILL-2.1", "THIRD_PARTY_NOTICES.md", "LICENSES", "nirs4all-datasets-wasm.licenses.json"]))
    (package / "package.json").write_text(json.dumps(package_json, indent=2) + "\n")
    print(f"WASM license closure {closure}: {len(components)} packages, {len(payload)} exact text files")


if __name__ == "__main__":
    main()

"""Origin acquisition and table staging shared by public dataset recipes."""
from __future__ import annotations

import hashlib
import json
import re
import tarfile
import time
import zipfile
from pathlib import Path
from typing import Any
from urllib.parse import parse_qsl, quote, unquote, urlencode, urlparse, urlunparse

import pandas as pd
import requests
from filelock import FileLock
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


def _public_url(url: str) -> str:
    """Keep provenance pointers without temporary signatures or guestbook record tokens."""
    parsed = urlparse(url)
    allowed = {"persistentId", "format", "version", "id", "folder_id", "download"}
    return urlunparse(parsed._replace(netloc=parsed.netloc.rsplit("@", 1)[-1], query=urlencode([(k, v) for k, v in parse_qsl(parsed.query) if k in allowed]), fragment=""))


class PullContext:
    """An isolated build directory backed by the native download cache."""

    def __init__(self, dataset_id: str, directory: Path, cache_dir: Path, *, timeout: int = 90, guestbook_response: dict[str, Any] | None = None, max_total_bytes: int = 20_000_000_000) -> None:
        self.dataset_id = dataset_id
        self.directory = directory
        self.leaf = directory / "standardized"
        self.leaf.mkdir(parents=True, exist_ok=True)
        self.cache_dir = cache_dir
        self.timeout = timeout
        self.guestbook_response = guestbook_response
        self.max_total_bytes = max_total_bytes
        self.downloaded_bytes = 0
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "nirs4all-datasets public origin reader"
        retry = Retry(total=4, backoff_factor=1, status_forcelist=(429, 500, 502, 503, 504), respect_retry_after_header=True)
        self.session.mount("https://", HTTPAdapter(max_retries=retry))
        self.session.mount("http://", HTTPAdapter(max_retries=retry))
        self.downloads: list[dict[str, Any]] = []

    def get_json(self, url: str, **params: Any) -> dict[str, Any]:
        response = self.session.get(url, params=params or None, timeout=self.timeout)
        response.raise_for_status()
        result: dict[str, Any] = response.json()
        return result

    def download(self, url: str, filename: str | None = None, *, sha256: str | None = None, size: int | None = None, origin_url: str | None = None) -> Path:
        """Fetch an origin resource without concurrent writers sharing a partial file."""
        identity = hashlib.sha256((origin_url or url).encode()).hexdigest()
        locks = self.cache_dir / ".resource-locks"
        locks.mkdir(parents=True, exist_ok=True)
        with FileLock(str(locks / (identity + ".lock")), timeout=3600):
            return self._download(url, filename, sha256=sha256, size=size, origin_url=origin_url)

    def _download(self, url: str, filename: str | None = None, *, sha256: str | None = None, size: int | None = None, origin_url: str | None = None) -> Path:
        """Fetch a public resource through the Rust streaming/atomic downloader."""
        from nirs4all_datasets import _acquire

        if urlparse(url).scheme not in {"https", "http"}:
            raise ValueError(f"origin must be an HTTP(S) URL: {url!r}")
        pointer = _public_url(origin_url or url)
        resource_id = hashlib.sha256((origin_url or url).encode()).hexdigest()[:24]
        name = Path(filename or unquote(urlparse(url).path).rstrip("/").rsplit("/", 1)[-1] or "download").name
        resource = {"id": resource_id, "role": "data", "required": True, "file_name": name, "selector": {"kind": "direct_url", "value": url}}
        if sha256:
            resource["sha256"] = sha256
        if size is not None:
            resource["size"] = size
        request = {"dataset_id": "public_origins", "route": {"id": resource_id, "provider": "url", "method": "raw_retrieve", "access": "open", "locator": url, "resources": [resource]}}
        for attempt in range(4):
            result = _acquire.retrieve_raw(request, {"cache_dir": str(self.cache_dir), "timeout_secs": self.timeout, "max_total_bytes": max(0, self.max_total_bytes - self.downloaded_bytes)})
            statuses = result.get("resources") or []
            reason = "; ".join(str(s.get("reason") or s.get("status")) for s in statuses)
            transient = re.search(r"\b(?:429|500|502|503|504)\b|io:|transport|timed out|unexpected eof|ended at|end of file|connection reset|failed to read", reason, re.IGNORECASE)
            if result.get("ok") or not transient or attempt == 3:
                break
            # Let the provider recover; an access denial is never retried as a different identity.
            time.sleep(30 if "429" in reason else 2 ** attempt)
        if not result.get("ok") or not statuses or not statuses[0].get("path"):
            reason = "; ".join(str(s.get("reason") or s.get("status")) for s in statuses)
            reason = re.sub(r"https?://[^\s\"'<>]+", lambda match: _public_url(match.group()), reason)
            reason = re.sub(r"(?i)(token|signature|credential)=[^&\s]+", r"\1=<redacted>", reason)
            raise RuntimeError(f"could not download original resource {pointer}: {reason or 'download failed'}")
        status = statuses[0]
        if status.get("status", "").startswith("downloaded"):
            self.downloaded_bytes += int(status.get("bytes") or 0)
        self.downloads.append({"url": pointer, "name": name, "sha256": status.get("sha256"), "size": status.get("bytes")})
        return Path(status["path"])

    def iter_bytes(self, response: requests.Response, chunk_size: int = 65536) -> Any:
        """Bound the bytes consumed from an origin's streaming archive response."""
        for chunk in response.iter_content(chunk_size):
            self.downloaded_bytes += len(chunk)
            if self.downloaded_bytes > self.max_total_bytes:
                raise ValueError("original-source retrieval exceeds max_total_bytes")
            yield chunk

    def dataverse_file(self, file_id: int, filename: str, *, guestbook_id: int, origin: str = "https://dataverse.harvard.edu") -> Path:
        """Download through the source's documented guestbook API using explicit user answers.

        No identity is invented, and supplied profile fields and signed URLs are
        never included in the cache's provenance document.
        """
        requirements = self.get_json(f"{origin}/api/guestbooks/{guestbook_id}")["data"]
        response = self.guestbook_response or {"answers": []}
        missing = [key for key in ("name", "email", "institution", "position") if requirements.get(key + "Required") and not response.get(key)]
        answers = {str(a.get("id")): a.get("value") for a in response.get("answers", [])}
        missing.extend(f"answer {q['id']}: {q['question']}" for q in requirements.get("customQuestions", []) if q.get("required") and not answers.get(str(q["id"])))
        if missing:
            raise ValueError(f"{self.dataset_id}: the original source requires guestbook_response with {', '.join(missing)}. Requirements: {origin}/api/guestbooks/{guestbook_id}. No response has been submitted.")
        endpoint = f"{origin}/api/access/datafile/{file_id}"
        reply = self.session.post(endpoint, params={"format": "original", "signed": "true"}, json={"guestbookResponse": response}, timeout=self.timeout)
        reply.raise_for_status()
        data = reply.json()
        signed_url = data.get("data", {}).get("signedUrl")
        if not signed_url:
            raise ValueError(f"{self.dataset_id}: source did not provide a download URL after guestbook submission")
        return self.download(signed_url, filename, origin_url=endpoint + "?format=original")

    def provider_files(self, provider: str, locator: str) -> list[dict[str, Any]]:
        """Resolve public repository metadata into original file URLs."""
        if provider == "zenodo":
            match = re.search(r"(?:zenodo[./]|records/)(\d+)", locator)
            if match is None:
                raise ValueError(f"invalid Zenodo record: {locator}")
            data = self.get_json(f"https://zenodo.org/api/records/{match[1]}")
            out = []
            for entry in data.get("files", []):
                item = {"name": entry["key"], "url": entry["links"]["self"], "size": entry.get("size")}
                checksum = str(entry.get("checksum") or "")
                if checksum.startswith("sha256:"):
                    item["sha256"] = checksum[7:]
                out.append(item)
            return out
        if provider == "figshare":
            match = re.search(r"(?:figshare[./]|articles/)(\d+)", locator)
            if match is None:
                raise ValueError(f"invalid Figshare article: {locator}")
            data = self.get_json(f"https://api.figshare.com/v2/articles/{match[1]}")
            return [{"name": f["name"], "url": f["download_url"], "size": f.get("size")} for f in data.get("files", [])]
        if provider == "dataverse":
            doi = re.search(r"10\.\d{4,9}/[^\s?#]+", locator)
            if doi is None:
                raise ValueError(f"invalid Dataverse DOI: {locator}")
            origin = "https://dataverse.harvard.edu" if doi[0].startswith("10.7910/") else "https://entrepot.recherche.data.gouv.fr"
            if doi[0].startswith("10.18167/"):
                origin = "https://dataverse.cirad.fr"
            data = self.get_json(f"{origin}/api/datasets/:persistentId/", persistentId="doi:" + doi[0])
            files = data["data"]["latestVersion"]["files"]
            return [{"name": f["dataFile"]["filename"], "url": f"{origin}/api/access/datafile/{f['dataFile']['id']}?format=original", "size": f["dataFile"].get("filesize")} for f in files if not f.get("restricted")]
        if provider == "dryad":
            doi = re.search(r"10\.5061/[^\s?#]+", locator)
            if doi is None:
                raise ValueError(f"invalid Dryad DOI: {locator}")
            data = self.get_json("https://datadryad.org/api/v2/datasets/doi:" + quote(doi[0], safe=""))
            link = data["_links"]["stash:version"]["href"]
            version_data = self.get_json("https://datadryad.org" + link if link.startswith("/") else link)
            download = version_data["_links"]["stash:download"]["href"]
            url = "https://datadryad.org" + download if download.startswith("/") else download
            return [{"name": "dryad-" + link.rstrip("/").rsplit("/", 1)[-1] + ".zip", "url": url}]
        if provider == "mendeley":
            match = re.search(r"(?:datasets/|10\.17632/)([a-z0-9]+)(?:[./](\d+))?", locator)
            if match is None:
                raise ValueError(f"invalid Mendeley dataset: {locator}")
            dataset, version_number = match[1], match[2] or "1"
            folders = self.get_json(f"https://data.mendeley.com/public-api/datasets/{dataset}/folders/{version_number}")
            folder_items = folders if isinstance(folders, list) else folders.get("folders", folders.get("data", []))
            out, seen = [], set()
            for folder_id in ["root", *[f["id"] for f in folder_items]]:
                offset = 0
                while True:
                    data = self.get_json(f"https://data.mendeley.com/public-api/datasets/{dataset}/files", **{"folder_id": folder_id, "version": version_number, "$start": offset, "$limit": 1000})
                    entries = data if isinstance(data, list) else data.get("files", data.get("data", []))
                    for f in entries:
                        details = f.get("content_details") or {}
                        url = f.get("download_url") or details.get("download_url")
                        if url and url not in seen:
                            seen.add(url)
                            out.append({"name": f["filename"], "url": url, "size": f.get("size") or details.get("size")})
                    if len(entries) < 1000:
                        break
                    offset += 1000
            return out
        if provider in {"ckan", "ecosis"}:
            parsed = urlparse(locator)
            package = parsed.path.rstrip("/").rsplit("/", 1)[-1] if parsed.scheme else locator
            data = self.get_json("https://data.ecosis.org/api/3/action/package_show", id=package)
            return [{"name": r.get("name") or r["id"], "url": r["url"], "size": r.get("size"), "id": r["id"]} for r in data["result"].get("resources", [])]
        raise ValueError(f"unsupported public repository provider {provider!r}")

    def extract(self, path: Path) -> Path:
        """Unpack an origin archive without allowing paths outside the staging directory."""
        destination = self.directory / ("extracted-" + hashlib.sha256(str(path).encode()).hexdigest()[:16])
        destination.mkdir(parents=True, exist_ok=True)
        if zipfile.is_zipfile(path):
            with zipfile.ZipFile(path) as archive:
                for member in archive.infolist():
                    target = (destination / member.filename).resolve()
                    if not target.is_relative_to(destination.resolve()) or (member.external_attr >> 16) & 0o170000 == 0o120000:
                        raise ValueError(f"unsafe archive member {member.filename!r}")
                archive.extractall(destination)
        elif tarfile.is_tarfile(path):
            with tarfile.open(path) as archive:
                for tar_member in archive.getmembers():
                    if not (destination / tar_member.name).resolve().is_relative_to(destination.resolve()) or tar_member.issym() or tar_member.islnk() or tar_member.isdev():
                        raise ValueError(f"unsafe archive member {tar_member.name!r}")
                archive.extractall(destination, filter="data")
        else:
            raise ValueError(f"unsupported origin archive: {path.name}")
        return destination

    def write_tables(self, sources: dict[str, pd.DataFrame], targets: pd.DataFrame | None = None, metadata: pd.DataFrame | None = None) -> Path:
        for name, table in [*sources.items(), ("Y", targets), ("M", metadata)]:
            if table is None:
                continue
            if "observation_id" not in table:
                raise ValueError(f"{name} table must declare observation_id")
            table.to_csv(self.leaf / f"{name}.csv", sep=";", index=False)
        return self.leaf

"""Configuration and secret resolution for nirs4all-datasets.

Resolves the Dataverse instance URL and API token from, in order of precedence:
explicit arguments, environment variables, a user config file
(``~/.config/nirs4all-datasets/config.toml``), then a project ``.env`` file.

The API token is wrapped in :class:`pydantic.SecretStr` so it is masked in logs
and reprs, and is only required for uploads/publishing and private downloads --
public datasets are fetched without a token.
"""
from __future__ import annotations

import os
import stat
import tomllib
from dataclasses import dataclass
from pathlib import Path

from pydantic import SecretStr

#: Default Dataverse instance (Recherche Data Gouv production).
DEFAULT_INSTANCE = "https://entrepot.recherche.data.gouv.fr"

TOKEN_ENV = "NIRS4ALL_DATAVERSE_TOKEN"
INSTANCE_ENV = "NIRS4ALL_DATAVERSE_INSTANCE"
CONFIG_ENV = "NIRS4ALL_DATASETS_CONFIG"


def default_config_path() -> Path:
    """Return the user config path, honoring the ``NIRS4ALL_DATASETS_CONFIG`` override."""
    override = os.environ.get(CONFIG_ENV)
    if override:
        return Path(override).expanduser()
    return Path.home() / ".config" / "nirs4all-datasets" / "config.toml"


@dataclass(frozen=True)
class Settings:
    """Resolved Dataverse access settings.

    Attributes:
        instance: Base URL of the Dataverse instance (no trailing slash).
        token: API token, or ``None`` when not configured. Masked in repr.
    """

    instance: str
    token: SecretStr | None = None

    @property
    def has_token(self) -> bool:
        """Whether an API token is configured."""
        return self.token is not None

    def require_token(self) -> str:
        """Return the plaintext token, raising a clear error if none is configured.

        Raises:
            RuntimeError: If no token is available, with guidance on how to set one.
        """
        if self.token is None:
            raise RuntimeError(
                f"No Dataverse API token configured. Set the {TOKEN_ENV} environment "
                f"variable, or add it to {default_config_path()} under:\n\n"
                '    [dataverse]\n    token = "..."\n\n'
                "A token is only needed for upload/publish and private downloads."
            )
        return self.token.get_secret_value()


def _check_config_permissions(path: Path) -> None:
    """Reject a config file that is group- or world-accessible (POSIX only)."""
    if os.name != "posix":
        return
    mode = path.stat().st_mode
    if stat.S_IMODE(mode) & 0o077:
        raise PermissionError(
            f"Config file {path} is group/world-accessible but holds a secret. "
            f"Restrict it with: chmod 600 {path}"
        )


def _load_config_file(path: Path) -> dict[str, str]:
    """Load the ``[dataverse]`` table from a TOML config file."""
    with path.open("rb") as fh:
        data = tomllib.load(fh)
    section = data.get("dataverse", {})
    return {key: str(value) for key, value in section.items() if value is not None}


def _load_dotenv(path: Path) -> dict[str, str]:
    """Read a ``.env`` file into a dict without mutating ``os.environ``."""
    from dotenv import dotenv_values

    return {key: value for key, value in dotenv_values(path).items() if value is not None}


def get_settings(
    *,
    instance: str | None = None,
    token: str | None = None,
    config_path: Path | None = None,
) -> Settings:
    """Resolve :class:`Settings` from arguments, env vars, config file, then ``.env``.

    Precedence (highest first): explicit arguments, environment variables, the user
    config TOML, a project ``.env``. The instance falls back to
    :data:`DEFAULT_INSTANCE`; the token may remain ``None``.

    Args:
        instance: Explicit instance URL override.
        token: Explicit token override.
        config_path: Override path to the config TOML.

    Returns:
        The resolved :class:`Settings`.
    """
    cfg: dict[str, str] = {}
    path = config_path or default_config_path()
    if path.exists():
        _check_config_permissions(path)
        cfg = _load_config_file(path)

    dotenv: dict[str, str] = {}
    env_file = Path(".env")
    if env_file.exists():
        dotenv = _load_dotenv(env_file)

    resolved_instance = (
        instance
        or os.environ.get(INSTANCE_ENV)
        or cfg.get("instance")
        or dotenv.get(INSTANCE_ENV)
        or DEFAULT_INSTANCE
    )
    resolved_token = (
        token
        or os.environ.get(TOKEN_ENV)
        or cfg.get("token")
        or dotenv.get(TOKEN_ENV)
    )

    return Settings(
        instance=resolved_instance.rstrip("/"),
        token=SecretStr(resolved_token) if resolved_token else None,
    )

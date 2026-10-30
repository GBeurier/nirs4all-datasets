"""Exercise the Methods boundary without retaining a Python numerical fallback."""
from __future__ import annotations

import builtins

import numpy as np
import pytest

from nirs4all_datasets.qualify import metrics


def test_native_roughness_attaches_axis_and_producer() -> None:
    native = pytest.importorskip("n4m.roles")
    if not hasattr(native, "SpectralNoiseProxy"):
        pytest.skip("Methods SpectralNoiseProxy is unavailable")
    spectra = np.random.RandomState(8).normal(1.0, 0.02, (15, 20))
    axis = np.linspace(1000.0, 1400.0, spectra.shape[1])
    measured = native.SpectralNoiseProxy().run(spectra)
    result = metrics.spectral_noise(spectra, axis)
    assert result["noise_rms"] == measured["global_noise_sigma"]
    assert result["snr"] == measured["global_signal_noise_ratio"]
    assert result["bandwise_snr_min"] == measured["bandwise_min"]
    assert result["worst_band_axis"] == axis[int(measured["worst_band_index"])]
    assert result["roughness_sigma_proxy"] == result["noise_rms"]
    assert result["producer"]["name"] == "nirs4all-methods"
    assert result["producer"]["protocol_version"] == "spectral-second-difference-mad-index.v1"


def test_quality_aggregate_preserves_its_strict_missing_data_protocol() -> None:
    native = pytest.importorskip("n4m.roles")
    if not hasattr(native, "SpectralNoiseProxy"):
        pytest.skip("Methods SpectralNoiseProxy is unavailable")
    spectra = np.random.RandomState(12).normal(1.0, 0.02, (15, 20))
    spectra[0, 0] = np.nan
    assert metrics.spectral_noise(spectra)["noise_rms"] is not None
    assert metrics.spectral_quality(spectra)["noise_proxy_db"] is None


def test_older_native_outputs_keep_globals_and_mark_missing_bandwise(monkeypatch: pytest.MonkeyPatch) -> None:
    import sys
    import types

    class GlobalOnlyProcedure:
        def run(self, x):
            return {"global_noise_sigma": 0.1, "global_noise_sigma_status": [0], "global_signal_noise_ratio": 20.0, "global_signal_noise_ratio_status": [0]}

    monkeypatch.setitem(sys.modules, "n4m", types.SimpleNamespace(abi_version=lambda: (2, 20, 0), version=lambda: "1.3.10"))
    monkeypatch.setitem(sys.modules, "n4m.roles", types.SimpleNamespace(SpectralNoiseProxy=GlobalOnlyProcedure))
    result = metrics.spectral_noise(np.ones((3, 5)))
    assert result["noise_rms"] == 0.1 and result["snr"] == 20.0
    assert result["availability"] == "partial"
    assert result["bandwise_snr_min"] is None


def test_missing_native_roughness_is_explicit_and_never_falls_back(monkeypatch: pytest.MonkeyPatch) -> None:
    original = builtins.__import__

    def without_methods(name, *args, **kwargs):
        if name == "n4m" or name.startswith("n4m."):
            raise ImportError("Methods intentionally unavailable")
        return original(name, *args, **kwargs)

    monkeypatch.setattr(builtins, "__import__", without_methods)
    spectra = np.array([[0.0, 1.0, 3.0, 7.0], [0.0, 2.0, 6.0, 14.0]])
    result = metrics.spectral_noise(spectra)
    assert result["availability"] == "unavailable"
    assert "ABI >= 2.20" in result["unavailable_reason"]
    assert result["noise_rms"] is None and result["roughness_sigma_proxy"] is None
    assert metrics.spectral_quality(spectra)["noise_proxy_db"] is None

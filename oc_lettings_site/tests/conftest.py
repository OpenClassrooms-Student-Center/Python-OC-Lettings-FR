"""
Fixture module for oc_lettings_site tests
"""
import pytest

from _pytest.monkeypatch import MonkeyPatch


@pytest.fixture(autouse=True)
def disable_sentry(monkeypatch: MonkeyPatch):
    monkeypatch.setattr(
        "monitoring.sentry_sdk.init",
        lambda *args, **kwargs: None
    )

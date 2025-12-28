import pytest

import timezone


def test_get_IANA_tz_returns_timezone(monkeypatch):
    def fake_timezone_at(*, lat: float, lng: float):
        assert lat == 38.7167
        assert lng == -9.1333
        return "Europe/Lisbon"

    monkeypatch.setattr(timezone, "timezone_at", fake_timezone_at)

    tz = timezone.get_IANA_tz(38.7167, -9.1333)
    assert tz == "Europe/Lisbon"


def test_get_IANA_tz_raises_when_none(monkeypatch):
    def fake_timezone_at(*, lat: float, lng: float):
        return None

    monkeypatch.setattr(timezone, "timezone_at", fake_timezone_at)

    with pytest.raises(ValueError, match="No timezone ID found"):
        timezone.get_IANA_tz(0.0, 0.0)

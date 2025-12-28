from types import SimpleNamespace

import pytest
from geopy.exc import GeopyError

import geo


def test_empty_string_raises_value_error():
    with pytest.raises(ValueError, match="Location cannot be empty string"):
        geo.get_place_coordinates("   ")


def test_unknown_place_raises_value_error(monkeypatch):
    def fake_geocode(_query: str):
        return None

    monkeypatch.setattr(geo.geolocator, "geocode", fake_geocode)

    with pytest.raises(ValueError, match=r"no such place found"):
        geo.get_place_coordinates("Atlantis")


def test_geopy_error_raises_runtime_error(monkeypatch):
    def fake_geocode(_query: str):
        raise GeopyError("service down")

    monkeypatch.setattr(geo.geolocator, "geocode", fake_geocode)

    with pytest.raises(RuntimeError, match=r'Geocode failed for location "Lisbon":'):
        geo.get_place_coordinates("Lisbon")


def test_success_returns_geolocation(monkeypatch):
    def fake_geocode(_query: str):
        # minimal object with the attributes your code reads
        return SimpleNamespace(latitude=38.7167, longitude=-9.1333)

    monkeypatch.setattr(geo.geolocator, "geocode", fake_geocode)

    result = geo.get_place_coordinates(" Lisbon ")
    assert result.place_name == "Lisbon"
    assert result.latitude == 38.7167
    assert result.longitude == -9.1333

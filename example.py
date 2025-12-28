from astro import HouseSystem, get_chart
from geo import get_place_coordinates
from timezone import get_IANA_tz


def main():
    coordinates = get_place_coordinates("Gdynia, Poland")
    timezone_id = get_IANA_tz(
        latitude=coordinates.latitude, longitude=coordinates.longitude
    )

    data = get_chart(
        date="2025-12-28",
        time="18:30",
        latitude=coordinates.latitude,
        longitude=coordinates.longitude,
        house_system=HouseSystem.REGIOMONTANUS,
        timezone_IANA_id=timezone_id,
    )
    print("Data", data.model_dump_json(indent=2))


if __name__ == "__main__":
    main()

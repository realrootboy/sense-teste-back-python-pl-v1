from entities.location import to_json
from repositories.pg_location import get_all_locations


def handle_location_get():
    locations = get_all_locations()
    locations = [to_json(location) for location in locations]

    json = {
        'localidades': locations
    }
    return json, 200
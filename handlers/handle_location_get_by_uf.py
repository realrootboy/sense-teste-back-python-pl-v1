from entities.location import to_json
from repositories.pg_location import get_address_by_uf


def handle_location_get_by_uf(uf):
    locations = get_address_by_uf(uf)
    locations = [to_json(location) for location in locations]

    json = {
        'localidades': locations
    }
    return json, 200
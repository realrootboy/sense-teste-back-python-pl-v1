from repositories.pg_location import check_if_address_exists, save_address
from services.via_cep import get_address_by_zip_code


def handle_cep_post(body):
    zip_code = body['cep']
    if check_if_address_exists(zip_code):
        return 'Address already exists', 400
    
    try:
        location = get_address_by_zip_code(zip_code)
        save_address(location)
        return 'Address saved', 201
    except:
        return 'Address not found', 404
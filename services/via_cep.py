import requests

from entities.location import Location

base_url = 'https://viacep.com.br/ws/'

def get_address_by_zip_code(zip_code):
    response = requests.get(base_url + zip_code + '/json/')
    json = response.json()
    location = Location(
        json['cep'],
        json['logradouro'],
        json['complemento'],
        json['bairro'],
        json['localidade'],
        json['uf'],
        json['ibge'],
        json['gia'],
        json['ddd'],
        json['siafi']
    )
    return location

from flask import Blueprint, request

from handlers.handle_cep_post import handle_cep_post
from handlers.handle_location_get import handle_location_get
from handlers.handle_location_get_by_uf import handle_location_get_by_uf

cep_blueprint = Blueprint('cep', __name__)

# post method that receives a cep on the body
@cep_blueprint.route('/api/localidades', methods=['POST'])
def post_cep():
    json = request.get_json()
    return handle_cep_post(body=json)

# get method return all locations
@cep_blueprint.route('/api/localidades', methods=['GET'])
def get_locations():
    return handle_location_get()

# get method that receives a uf on the url and return all locations with this uf
@cep_blueprint.route('/api/localidades/<uf>', methods=['GET'])
def get_locations_by_uf(uf):
    return handle_location_get_by_uf(uf)


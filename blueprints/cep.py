from flask import Blueprint, request

from handlers.handle_cep_post import handle_cep_post
from handlers.handle_location_get import handle_location_get
from handlers.handle_location_get_by_uf import handle_location_get_by_uf

cep_blueprint = Blueprint('cep', __name__)

# post method that receives a cep on the body
@cep_blueprint.route('/api/localidades/', methods=['POST'])
def post_cep():
    json = request.get_json()
    return handle_cep_post(body=json)

# get method return all locations
@cep_blueprint.route('/api/localidades/', methods=['GET'])
def get_locations():
    uf = request.args.get('uf')
    if uf:
        return handle_location_get_by_uf(uf)
    else:
        return handle_location_get()



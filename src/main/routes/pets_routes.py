from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import PetListerComposer
from src.main.composer.pet_deleter_composer import PetDeleterComposer

pets_routes = Blueprint("pets_routes", __name__)

@pets_routes.route("/pets", methods=["GET"])
def list_pets():
    http_request = HttpRequest()
    http_response = PetListerComposer.compose().handle(http_request)
    return jsonify(http_response.body), http_response.status_code

@pets_routes.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    http_request = HttpRequest(param={"name": name})
    http_response = PetDeleterComposer.compose().handle(http_request)
    return jsonify(http_response.body), http_response.status_code

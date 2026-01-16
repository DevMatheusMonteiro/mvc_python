from flask import Blueprint, jsonify
from src.views.http_types.http_request import HttpRequest
from src.main.composer.pet_lister_composer import PetListerComposer
from src.main.composer.pet_deleter_composer import PetDeleterComposer
from src.errors.error_handler import ErrorHandler

pets_routes = Blueprint("pets_routes", __name__)

@pets_routes.route("/pets", methods=["GET"])
def list_pets():
    try:
        http_request = HttpRequest()
        http_response = PetListerComposer.compose().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        error_response = ErrorHandler.handle_error(e)
        return jsonify(error_response.body), error_response.status_code

@pets_routes.route("/pets/<name>", methods=["DELETE"])
def delete_pet(name):
    try:
        http_request = HttpRequest(param={"name": name})
        http_response = PetDeleterComposer.compose().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        error_response = ErrorHandler.handle_error(e)
        return jsonify(error_response.body), error_response.status_code

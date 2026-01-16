from flask import Blueprint, jsonify, request
from src.views.http_types.http_request import HttpRequest
from src.main.composer.person_creator_composer import PersonCreatorComposer
from src.main.composer.person_finder_composer import PersonFinderComposer
from src.errors.error_handler import ErrorHandler

person_routes = Blueprint("person_routes", __name__)

@person_routes.route("/people", methods=["POST"])
def create_person():
    try:
        http_request = HttpRequest(body=request.json)
        http_response = PersonCreatorComposer.compose().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        error_response = ErrorHandler.handle_error(e)
        return jsonify(error_response.body), error_response.status_code

@person_routes.route("/people/<person_id>", methods=["GET"])
def find_person(person_id):
    try:
        http_request = HttpRequest(param={"person_id": int(person_id)})
        http_response = PersonFinderComposer.compose().handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as e:
        error_response = ErrorHandler.handle_error(e)
        return jsonify(error_response.body), error_response.status_code

from flask import Blueprint, jsonify

pets_routes = Blueprint("pets_routes", __name__)

@pets_routes.route("/pets", methods=["GET"])
def list_pets():
    return jsonify({"pets": ["Dog", "Cat", "Parrot"]}), 200

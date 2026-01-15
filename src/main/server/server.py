from flask import Flask
from flask_cors import CORS
from src.models.sqlite.settings.connection import db_connection_handler

from ..routes.pets_routes import pets_routes
from ..routes.person_routes import person_routes

db_connection_handler.connect()

app = Flask(__name__)
CORS(app)
app.register_blueprint(pets_routes)
app.register_blueprint(person_routes)

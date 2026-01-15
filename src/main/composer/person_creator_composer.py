from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repositories.people_repository import PeopleRepository
from src.controllers.person_creator_controller import PersonCreatorController
from src.views.person_creator_view import PersonCreatorView

class PersonCreatorComposer:
    @staticmethod
    def compose():
        model = PeopleRepository(db_connection_handler)
        controller = PersonCreatorController(model)
        view = PersonCreatorView(controller)
        return view

from src.controllers.interfaces.person_creator_controller_interface import IPersonCreatorController
from src.validators.person_creator_validator import PersonCreatorValidator
from .interfaces.view_interface import IView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonCreatorView(IView):
    def __init__(self, controller: IPersonCreatorController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        PersonCreatorValidator.validate_data(http_request)
        person_info = http_request.body
        created_person = self.__controller.create(person_info)
        return HttpResponse(status_code=201, body=created_person)

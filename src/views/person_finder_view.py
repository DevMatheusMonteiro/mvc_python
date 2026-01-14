from src.controllers.interfaces.person_finder_controller_interface import IPersonFinderController
from .interfaces.view_interface import IView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PersonFinderView(IView):
    def __init__(self, controller: IPersonFinderController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param.get("person_id")
        found_person = self.__controller.find(person_id)
        return HttpResponse(status_code=200, body=found_person)

from src.controllers.interfaces.pet_lister_controller_interface import IPetListerController
from .interfaces.view_interface import IView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetListerView(IView):
    def __init__(self, controller: IPetListerController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        found_pets = self.__controller.list_pets()
        return HttpResponse(status_code=200, body=found_pets)
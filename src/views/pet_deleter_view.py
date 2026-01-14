from src.controllers.interfaces.pet_deleter_controller_interface import IPetDeleterController
from .interfaces.view_interface import IView
from .http_types.http_request import HttpRequest
from .http_types.http_response import HttpResponse

class PetDeleterView(IView):
    def __init__(self, controller: IPetDeleterController) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pet_name = http_request.param.get("name")
        self.__controller.delete_pet(pet_name)
        return HttpResponse(status_code=204)

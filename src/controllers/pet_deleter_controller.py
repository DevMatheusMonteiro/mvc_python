from ..models.interfaces.pet_repository_interface import IPetsRepository
from .interfaces.pet_deleter_controller_interface import IPetDeleterController

class PetDeleterController(IPetDeleterController):
    def __init__(self, pet_repository: IPetsRepository) -> None:
        self.__pet_repository = pet_repository

    def delete_pet(self, name: str) -> None:
        self.__pet_repository.delete(name)

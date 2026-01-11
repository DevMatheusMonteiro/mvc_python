from ..models.interfaces.pet_repository_interface import IPetsRepository

class PetDeleterController:
    def __init__(self, pet_repository: IPetsRepository) -> None:
        self.__pet_repository = pet_repository

    def delete_pet(self, name: str) -> None:
        self.__pet_repository.delete(name)

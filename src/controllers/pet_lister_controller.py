from ..models.interfaces.pet_repository_interface import IPetsRepository
from ..models.sqlite.entities.pets import Pets
from .interfaces.pet_lister_controller_interface import IPetListerController

class PetListerController(IPetListerController):
    def __init__(self, pet_repository: IPetsRepository) -> None:
        self.__pet_repository = pet_repository

    def list_pets(self) -> dict:
        pets = self.__get_pets_from_db()
        return self.__format_response(pets)

    def __get_pets_from_db(self) -> list[Pets]:
        pets = self.__pet_repository.find_all()
        return pets

    def __format_response(self, pets_data:list[Pets]) -> dict:
        formatted_pets = []
        for pet in pets_data:
            formatted_pets.append({
                "id": pet.id,
                "name": pet.name,
                "type": pet.type,
            })
        return {
            "type": "Pets",
            "count": len(formatted_pets),
            "attributes": formatted_pets
        }

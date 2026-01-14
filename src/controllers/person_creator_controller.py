import re
from ..models.interfaces.people_repository_interface import IPeopleRepository
from .interfaces.person_creator_controller_interface import IPersonCreatorController

class PersonCreatorController(IPersonCreatorController):
    def __init__(self, people_repository: IPeopleRepository) -> None:
        self.__people_repository = people_repository

    def create(self, data: dict) -> dict:
        first_name=data["first_name"]
        last_name=data["last_name"]
        age=data["age"]
        pet_id=data["pet_id"]
        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        return self.__format_response(data)

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expression to match non-alphabetic characters
        non_valid_characters = re.compile(r'[^a-zA-Z]')
        if non_valid_characters.search(first_name) or non_valid_characters.search(last_name):
            raise ValueError("First name and last name must contain only alphabetic characters.")

    def __insert_person_in_db(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.__people_repository.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            pet_id=pet_id
        )

    def __format_response(self, person_data: dict) -> dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": person_data
            }
        }

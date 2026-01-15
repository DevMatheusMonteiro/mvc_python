from ..models.interfaces.people_repository_interface import IPeopleRepository
from ..models.sqlite.entities.people import People
from .interfaces.person_finder_controller_interface import IPersonFinderController

class PersonFinderController(IPersonFinderController):
    def __init__(self, people_repository: IPeopleRepository) -> None:
        self.__people_repository = people_repository

    def find(self, person_id: int) -> dict:
        person = self.__find_by_id_in_db(person_id)
        return self.__format_response(person)
    def __find_by_id_in_db(self, person_id: int) -> People:
        person = self.__people_repository.find(person_id)
        if not person:
            raise Exception("Person not found.")
        return person

    def __format_response(self, person_data: People) -> dict:
        print(person_data)
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person_data.first_name,
                    "last_name": person_data.last_name,
                    "age": person_data.age,
                    "pet_name": person_data.pet_name,
                    "pet_type": person_data.pet_type
                }
            }
        }

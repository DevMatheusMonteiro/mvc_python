import pytest
from .person_creator_controller import PersonCreatorController

class PeopleRepositoryMock:
    def __init__(self) -> None:
        self.created_person = None

    def create(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        self.created_person = {
            "first_name": first_name,
            "last_name": last_name,
            "age": age,
            "pet_id": pet_id
        }

def test_create():
    people_repository_mock = PeopleRepositoryMock()
    controller = PersonCreatorController(people_repository=people_repository_mock)

    person_data = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }

    response = controller.create(person_data)

    assert people_repository_mock.created_person == person_data
    assert response == {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": person_data
        }
    }

def test_create_error():
    people_repository_mock = PeopleRepositoryMock()
    controller = PersonCreatorController(people_repository=people_repository_mock)


    with pytest.raises(Exception) as excinfo:
        controller.create({
            "first_name": "John123",
            "last_name": "Doe",
            "age": 30,
            "pet_id": 1
        })
    assert str(excinfo.value) == "First name and last name must contain only alphabetic characters."

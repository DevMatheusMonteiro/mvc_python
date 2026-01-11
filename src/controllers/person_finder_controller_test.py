import pytest
from .person_finder_controller import PersonFinderController

class MockPerson:
    def __init__(self, data: dict):
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.pet_name = data["pet_name"]
        self.pet_type = data["pet_type"]
class MockPeopleRepository:
    def __init__(self):
        self.people = {
            1: MockPerson(
                data={
                    "first_name": "John",
                    "last_name": "Doe",
                    "age": 30,
                    "pet_name": "Rex",
                    "pet_type": "Dog"
                }
            ),
            2: MockPerson(
                data={
                    "first_name": "Jane",
                    "last_name": "Smith",
                    "age": 25,
                    "pet_name": "Whiskers",
                    "pet_type": "Cat"
                }
            )
        }

    def find(self, person_id: int):
        return self.people.get(person_id, None)

def test_find():
    mock_repository =  MockPeopleRepository()
    controller = PersonFinderController(mock_repository)
    response = controller.find(1)
    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 30,
                "pet_name": "Rex",
                "pet_type": "Dog"
            }
        }
    }
    assert response == expected_response

def test_find_error():
    mock_repository =  MockPeopleRepository()
    controller = PersonFinderController(mock_repository)

    with pytest.raises(Exception) as exc_info:
        controller.find(3)
    assert str(exc_info.value) == "Person not found."

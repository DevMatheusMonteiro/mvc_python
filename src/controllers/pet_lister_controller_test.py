from .pet_lister_controller import PetListerController

class MockPetRepository:
    def find_all(self):
        return [
            type("Pet", (), {"id": 1, "name": "Buddy", "type": "Dog"})(),
            type("Pet", (), {"id": 2, "name": "Mittens", "type": "Cat"})(),
        ]
def test_list_pets():
    mock_repo = MockPetRepository()
    controller = PetListerController(mock_repo)

    response = controller.list_pets()

    expected_response = {
        "type": "Pets",
        "count": 2,
        "attributes": [
            {"id": 1, "name": "Buddy", "type": "Dog"},
            {"id": 2, "name": "Mittens", "type": "Cat"},
        ],
    }

    assert response == expected_response

import pytest
from ..settings.connection import db_connection_handler
from .pets_repository import PetsRepository
from .people_repository import PeopleRepository

db_connection_handler.connect()

@pytest.mark.skip(reason="Interaction with database - requires database setup")
def test_list_pets_returns_list():
    repo = PetsRepository(db_connection_handler)
    pets = repo.list()
    print(pets)
    assert isinstance(pets, list)

@pytest.mark.skip(reason="Interaction with database - requires database setup")
def test_delete_pet():
    repo = PetsRepository(db_connection_handler)

    repo.delete("belinha")

@pytest.mark.skip(reason="Interaction with database - requires database setup")
def test_create_person():
    repo = PeopleRepository(db_connection_handler)
    repo.create("John", "Doe", 30, 2)

@pytest.mark.skip(reason="Interaction with database - requires database setup")
def test_get_person_by_id():
    repo = PeopleRepository(db_connection_handler)
    person = repo.find(1)
    assert person is not None
    assert person.first_name == "John"
    assert person.last_name == "Doe"
    assert person.pet_name == "cao"
    assert person.pet_type == "dog"

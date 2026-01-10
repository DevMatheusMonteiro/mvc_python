import pytest
from ..settings.connection import db_connection_handler
from .pets_repository import PetsRepository

# db_connection_handler.connect()

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

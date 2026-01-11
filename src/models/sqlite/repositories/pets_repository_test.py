from unittest import mock
import pytest
from sqlalchemy.orm.exc import NoResultFound
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from ..entities.pets import Pets
from .pets_repository import PetsRepository

class MockConnection:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [mock.call.query(Pets)], # query
                    [
                        Pets(name="dog", type="dog"),
                        Pets(name="cat", type="cat")
                    ], # result
                )
            ])

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

class MockConnectionNoResult:
    def __init__(self):
        self.session = UnifiedAlchemyMagicMock()
        self.session.query.side_effect = self.__raise_for_no_result_found

    def __raise_for_no_result_found(self, *args, **kwargs):
        raise NoResultFound("No result found")

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def test_list_pets():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)
    response = repo.list()


    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
    assert response[0].type == "dog"
    assert isinstance(response[0], Pets)
    assert isinstance(response, list)

def test_list_pets_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)
    response = repo.list()


    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_not_called()
    mock_connection.session.filter.assert_not_called()

    assert response == []

def test_delete_pet():
    mock_connection = MockConnection()
    repo = PetsRepository(mock_connection)

    repo.delete("belinha")

    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.filter.assert_called_once_with(Pets.name == "belinha")
    mock_connection.session.delete.assert_called_once()
    mock_connection.session.commit.assert_called_once()

def test_delete_pet_no_result():
    mock_connection = MockConnectionNoResult()
    repo = PetsRepository(mock_connection)

    with pytest.raises(Exception):
        repo.delete("belinha")

    mock_connection.session.rollback.assert_called_once()

from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from ..entities.pets import Pets
from .pets_repository import PetsRepository

class MockConnectionHandler:
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
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

def test_list_pets():
    mock_connection = MockConnectionHandler()
    repo = PetsRepository(mock_connection)
    response = repo.list()


    mock_connection.session.query.assert_called_once_with(Pets)
    mock_connection.session.all.assert_called_once()
    mock_connection.session.filter.assert_not_called()

    assert response[0].name == "dog"
    assert response[0].type == "dog"
    assert isinstance(response[0], Pets)
    assert isinstance(response, list)

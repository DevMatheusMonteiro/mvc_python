from .pet_deleter_controller import PetDeleterController

def test_delete_pet(mocker):
    mock_repo = mocker.Mock()
    controller = PetDeleterController(mock_repo)
    controller.delete_pet("Buddy")

    mock_repo.delete.assert_called_once_with("Buddy")

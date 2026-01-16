from .person_creator_validator import PersonCreatorValidator

class MockHttpRequest:
    def __init__(self, body) -> None:
        self.body = body

def test_validate_data_with_valid_data() -> None:
    valid_body = {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "pet_id": 1
    }
    http_request = MockHttpRequest(body=valid_body)
    try:
        PersonCreatorValidator.validate_data(http_request)
    except Exception:
        assert False, "validate_data raised an exception with valid data"

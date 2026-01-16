from pydantic import BaseModel, constr, ValidationError
from src.views.http_types.http_request import HttpRequest
from src.errors.error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class PersonCreatorValidator(BaseModel):
    first_name: constr(min_length=1) # type: ignore
    last_name: constr(min_length=1) # type: ignore
    age: int
    pet_id: int

    @classmethod
    def validate_data(cls, http_request: HttpRequest) -> None:
        try:
            cls(**http_request.body)
        except ValidationError as e:
            raise HttpUnprocessableEntityError(e.errors()) from e

from src.views.http_types.http_response import HttpResponse
from .error_types.http_bad_request import HttpBadRequestError
from .error_types.http_not_found import HttpNotFoundError
from .error_types.http_unprocessable_entity import HttpUnprocessableEntityError

class ErrorHandler:
    @staticmethod
    def handle_error(error: Exception) -> HttpResponse:
        if isinstance(error, (HttpBadRequestError,
                              HttpNotFoundError,
                              HttpUnprocessableEntityError)):
            return HttpResponse(
                status_code=400,
                body={"errors": [
                    {
                        "title": error.name,
                        "detail": error.message
                    }
                ]})

        return HttpResponse(
            status_code=500,
            body={"errors": [
                {
                    "title": error.name,
                    "detail": error.message
                }
            ]})

from fastapi.responses import ORJSONResponse
from typing import Any
from . import code
from .schemas import ResponseSchema


class APIJSONResponse(ORJSONResponse):
    media_type = "application/json"

    def render(self, content: Any) -> bytes:
        response_dict = ResponseSchema(code=code.CODE_200_OK, data=content, msg='success').dict()
        return super().render(response_dict)



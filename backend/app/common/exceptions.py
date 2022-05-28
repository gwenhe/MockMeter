import traceback

from fastapi import Request, status
from fastapi.responses import ORJSONResponse
from fastapi.exceptions import RequestValidationError

from .ext import app
from .http import code, ResponseSchema

default_exception_msg = '系统异常'


class HTTPException(Exception):
    def __init__(self, msg: str = default_exception_msg, code: int = code.CODE_422_UNPROCESSABLE_ENTITY,
                 status_code: int = status.HTTP_200_OK,
                 headers: dict = None):
        self.code = code
        self.msg = msg
        self.status_code = status_code
        self.headers = headers


@app.exception_handler(HTTPException)
async def unicorn_exception_handler(request: Request, exc: HTTPException):
    return ORJSONResponse(
        status_code=exc.status_code,
        content=ResponseSchema(code=exc.code, msg=exc.msg).dict(),
        headers=exc.headers,
    )


@app.exception_handler(RequestValidationError)
async def validation_error_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    print(errors)
    for i in errors:
        error_type = i['type']
        print(error_type)
        field = errors[0].get('loc', ['unknown'])[-1]
        print(field)
    content = ResponseSchema(code=code.CODE_422_UNPROCESSABLE_ENTITY, msg=default_exception_msg, data=errors).dict()
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=content,
    )


@app.exception_handler(Exception)
async def all_exception_handler(request: Request, exc: Exception):
    content = ResponseSchema(code=code.CODE_500_INTERNAL_SERVER_ERROR, msg=default_exception_msg).dict()
    content['error'] = str(exc)
    return ORJSONResponse(
        status_code=status.HTTP_200_OK,
        content=content,
    )

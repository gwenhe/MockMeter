from typing import Optional, Any
import datetime
from pydantic import BaseModel, Field
from . import code


class ResponseSchema(BaseModel):
    code: int = Field(..., description='失败时返回的code')
    msg: str = Field(..., description='失败时返回的信息')
    data: Any = Field(None, description='')


class Fail(ResponseSchema):
    code: int = Field(default=code.CODE_422_UNPROCESSABLE_ENTITY, description='请求参数有误')


class Unauthorized(ResponseSchema):
    code: int = Field(default=code.CODE_401_UNAUTHORIZED, description='登录过期')


class Error(ResponseSchema):
    code: int = Field(default=code.CODE_500_INTERNAL_SERVER_ERROR, description='系统内部错误')
    error: str = Field(description='错误原因')


class ResponseExample:
    fail = {code.CODE_422_UNPROCESSABLE_ENTITY: {"model": Fail}}
    unauthorized = {code.CODE_401_UNAUTHORIZED: {"model": Unauthorized}}
    error = {code.CODE_500_INTERNAL_SERVER_ERROR: {"model": Error}}


resp = ResponseExample()

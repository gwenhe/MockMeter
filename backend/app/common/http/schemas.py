from typing import Optional, Any
import datetime
from pydantic import BaseModel, Field
from . import code


class ResponseSchema(BaseModel):
    code: int
    msg: str = Field(None, description='失败时返回的信息')
    data: Any = Field(None, description='')


class ResponseExample:
    fail = {code.CODE_422_UNPROCESSABLE_ENTITY: {"model": ResponseSchema}}
    unauthorized = {code.CODE_401_UNAUTHORIZED: {"model": ResponseSchema}}


resp = ResponseExample()

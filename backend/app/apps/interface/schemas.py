from typing import Optional, Union, Dict, List
import datetime
from pydantic import BaseModel, Field
from common.schemas import BaseDBSchema
from pydantic import BaseModel


class RequestSchema(BaseModel):
    project_id: int = None
    interface_path: str = None
    client_ip: str = None
    method: str
    path_params: dict = None
    query_params: dict = None
    json_dict: Union[Dict, List] = None
    form: dict = None
    file: dict = None
    body: str = None
    headers: dict = None
    cookies: dict = None


class ResponseSchema(BaseModel):
    delay_time: int = None
    status_code: int
    media_type: str = None
    body: Union[Dict, List, str, int, bool, bytes] = None
    headers: Dict = None
    cookies: Dict = None


class InterfaceDB(BaseDBSchema):
    project_id: int = None
    interface_name: str = None
    interface_path: str = None
    mock_info: str = None
    script_path: str = None


class ScriptDB(BaseDBSchema):
    interface_id: int = None
    script_desc: str = None
    script_path: str = None
    expiration_time: datetime.datetime = None


class RecordDB(BaseDBSchema):
    interface_id: int = None
    interface_path: str = None
    request_info: str = None
    response_info: str = None


class InterfaceCreate(BaseDBSchema):
    project_id: int = Field(...)
    interface_path: str = Field(...)
    mock: ResponseSchema = Field(...)

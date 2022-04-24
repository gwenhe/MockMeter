from typing import Optional, Union, Dict, List

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

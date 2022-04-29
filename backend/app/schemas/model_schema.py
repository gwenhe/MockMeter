from typing import Optional
import datetime
from pydantic import BaseModel


class BaseDB(BaseModel):
    id: int = None
    create_time: datetime.datetime = None
    update_time: datetime.datetime = None

    class Config:
        orm_mode = True


class InterfaceDB(BaseDB):
    project_id: int = None
    interface_name: str = None
    interface_path: str = None
    mock_info: str = None
    script_path: str = None


class ScriptDB(BaseDB):
    interface_id: int = None
    script_desc: str = None
    script_path: str = None
    expiration_time: datetime.datetime = None


class RecordDB(BaseDB):
    interface_id: int = None
    interface_path: str = None
    request_info: str = None
    response_info: str = None


if __name__ == '__main__':
    InterfaceDB(id=1)

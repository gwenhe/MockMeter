from typing import Optional
import datetime
from pydantic import BaseModel, Field


class BaseDBSchema(BaseModel):
    id: int = None
    create_time: datetime.datetime = None
    update_time: datetime.datetime = None

    class Config:
        orm_mode = True

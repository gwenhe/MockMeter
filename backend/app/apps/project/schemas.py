from typing import Optional, Union, Dict, List
from pydantic import BaseModel, Field
from common.schemas import BaseDBSchema
from pydantic import BaseModel


class ProjectBase(BaseModel):
    project_name: str
    desc: str = Field(None)


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectInDBBase(BaseDBSchema):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Project(ProjectInDBBase, ProjectBase):
    pass


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass

from typing import Optional, Union, Dict, List
from pydantic import BaseModel, Field
from common.schemas import BaseDBSchema
from common.db.ext import PageReqSchema, PageResSchema


class ProjectBase(BaseModel):
    project_name: str
    remarks: str = Field(None)


class ProjectCreate(ProjectBase):
    pass


class ProjectUpdate(ProjectBase):
    pass


class ProjectList(PageReqSchema):
    project_name: str = Field(None, description='项目名称-模糊查询')



""""""


class ProjectInDBBase(BaseDBSchema, ProjectBase):
    class Config:
        orm_mode = True


# Additional properties to return via API
class Project(ProjectInDBBase):
    pass


class ProjectInDBList(PageResSchema):
    items: List[Project]


# Properties properties stored in DB
class ProjectInDB(ProjectInDBBase):
    pass

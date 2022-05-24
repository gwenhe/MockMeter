from typing import Optional, Union, Dict, List
from pydantic import BaseModel, Field
from common.schemas import BaseDBSchema
from common.db.ext import PageReqSchema, PageResSchema


class ProjectBase(BaseModel):
    project_name: str = Field(None)
    remarks: str = Field(None)


class ProjectCreate(ProjectBase):
    project_name: str = Field(...)


class ProjectUpdate(BaseModel):
    project_id: int = Field(...)
    project_data: ProjectBase = Field(...)


class ProjectDelete(BaseModel):
    project_id: str = Field(...)


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


"""
Service
"""


class ServiceBase(BaseModel):
    service_name: str = Field(None)
    remarks: str = Field(None)


class Test(BaseModel):
    # 必传字段
    # service1: str = Field(..., max_length=5)
    # 非必传
    service2: str = Field(None)
    # 长度限制
    service3: str = Field(None)
    # 枚举
    #
    remarks: str = Field(None)

    class Config:
        max_anystr_length = 10
        error_msg_templates = {
            'value_error.any_str.max_length': '长度:{limit_value}',
        }


# Test(service3='23982893823982398239')
# from typing import Optional
# import datetime
# from pydantic import BaseModel, Field
# from app.schemas.mock import ResponseSchema
#
#
# class ProjectBase(BaseModel):
#     project_name: str = Field(..., description='项目名称')
#
#
# class ProjectCreate(ProjectBase):
#     pass
#
#
#
#
# class InterfaceDB(BaseDB):
#     project_id: int = None
#     interface_name: str = None
#     interface_path: str = None
#     mock_info: str = None
#     script_path: str = None
from __future__ import annotations
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse, ORJSONResponse
from sqlalchemy.ext.asyncio import AsyncSession
from common.dependencies import get_db
from common.http import APIJSONResponse, code, resp
from common.exceptions import HTTPException
from . import schemas, crud

router = APIRouter(
    prefix="/project",
    tags=["项目"],
    default_response_class=APIJSONResponse,
    responses=resp.fail | resp.unauthorized,
)
from typing import List


@router.post('/get', name='获取项目列表', response_model=List[schemas.Project])
async def project_get():
    pass


@router.post('/create', name='创建项目', response_model=schemas.Project)
async def project_create(project_in: schemas.ProjectCreate, db: AsyncSession = Depends(get_db)):
    project = await crud.project.get_by_name(db, project_in.project_name)
    if project:
        raise HTTPException('项目已存在')
    project = await crud.project.create(db, obj_in=project_in)
    return project

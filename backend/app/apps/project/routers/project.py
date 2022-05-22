from __future__ import annotations
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from common.dependencies import get_db
from common.exceptions import HTTPException
from .. import schemas, crud

from . import router


@router.get('/{project_id}', name='获取项目信息', response_model=schemas.Project)
async def read_project(project_id: int, db: AsyncSession = Depends(get_db)):
    project = await crud.project.get_correct(db, project_id)
    return project


@router.post('/get_list', name='获取项目列表', response_model=schemas.ProjectInDBList)
async def read_project_list(query: schemas.ProjectList, db: AsyncSession = Depends(get_db)):
    pages = await crud.project.get_pages(db, query)
    return pages


@router.post('/create', name='创建项目', response_model=schemas.Project)
async def create_project(project_in: schemas.ProjectCreate, db: AsyncSession = Depends(get_db)):
    project = await crud.project.get_by_name(db, project_in.project_name)
    if project:
        raise HTTPException('项目已存在')
    project = await crud.project.create(db, obj_in=project_in)
    return project


@router.post('/update', name='更新项目信息')
async def update_project(project_in: schemas.ProjectUpdate, db: AsyncSession = Depends(get_db)):
    await crud.project.update(db, project_in.project_id, project_in.project_data)


@router.post('/delete', name='删除项目')
async def delete_project(project_in: schemas.ProjectDelete, db: AsyncSession = Depends(get_db)):
    await crud.project.remove(db, project_in.project_id)

# from fastapi import APIRouter, Depends, File, UploadFile, Form
# from app.dependencies import get_db
# from sqlalchemy.ext.asyncio import AsyncSession
#
# from app.schemas.project_schema import ProjectCreate
#
# router = APIRouter(
#     prefix="/project",
#     tags=["项目"],
#     responses={404: {"description": "Not found"}},
# )
#
#
# @router.post('/create')
# async def project_create(project_info: ProjectCreate, db: AsyncSession = Depends(get_db)):
#     pass

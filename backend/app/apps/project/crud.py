from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from common.db.crud import CRUDBase
from common.db.ext import paginate, Pagination
from .models import MockProject
from . import schemas


class CRUDProject(CRUDBase[MockProject, schemas.ProjectCreate, schemas.ProjectUpdate]):

    @staticmethod
    async def get_by_name(db: AsyncSession, project_name: str) -> MockProject:
        stmt = select(MockProject).where(
            MockProject.project_name == project_name, MockProject.is_del == 0
        )
        result = await db.execute(stmt)
        return result.scalars().first()

    @staticmethod
    async def get_pages(db: AsyncSession, page: schemas.ProjectList) -> Pagination:
        if page.project_name:
            stmt = select(MockProject).where(
                MockProject.is_del == 0,
                MockProject.project_name.like('%{project_name}%'.format(project_name=page.project_name)),

            )
        else:
            stmt = select(MockProject).where(MockProject.is_del == 0)
        paginate_obj = await paginate(db, stmt, page.page, page.per_page)
        return paginate_obj


project = CRUDProject(MockProject)

from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select
from common.db.crud import CRUDBase
from .models import MockProject
from . import schemas


class CRUDProject(CRUDBase[MockProject, schemas.ProjectCreate, schemas.ProjectUpdate]):

    @staticmethod
    async def get_by_name(db: AsyncSession, project_name: str) -> MockProject:
        stmt = select(MockProject).where(
            MockProject.project_name == project_name
        )
        result = await db.execute(stmt)
        return result.scalars().first()


project = CRUDProject(MockProject)

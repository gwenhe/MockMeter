import pytest
from app.db.session import SessionLocal
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope="session")
async def db() -> AsyncSession:
    async with SessionLocal() as db:
        yield db

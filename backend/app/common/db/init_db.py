import asyncio
# from .session import engine, SessionLocal
# from .models import BaseModel
from common.db.session import engine, SessionLocal
from common.db.models import BaseModel
from apps.project import models
from apps.interface import models


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.drop_all)
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)


if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(init_db())
    # asyncio.run(init_db)

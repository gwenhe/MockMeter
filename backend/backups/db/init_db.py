# from app.db.base_class import Base, BaseModel
# from app.db.session import engine, SessionLocal
# from app import models
# import asyncio
#
#
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(BaseModel.metadata.drop_all)
#     async with engine.begin() as conn:
#         await conn.run_sync(BaseModel.metadata.create_all)
#
#
# if __name__ == '__main__':
#     asyncio.get_event_loop().run_until_complete(init_db())
#     # asyncio.run(init_db)

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
#
# from app.core.config import settings
#
# engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI,
#                              future=True,
#                              max_overflow=-1,
#                              pool_size=30,
#                              # encoding='utf-8',
#                              # echo=True
#                              )
# SessionLocal = sessionmaker(bind=engine, class_=AsyncSession)

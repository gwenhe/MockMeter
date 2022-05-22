from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from .models import Base
from sqlalchemy.sql import select, update, delete, insert
from fastapi.encoders import jsonable_encoder

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        # self.schema = schema

    async def get(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        stmt = select(self.model).where(self.model.id == id)
        result = await db.execute(stmt)
        return result.scalars().first()

    # async def create(self, db: Session, obj_in: SchemaType) -> Optional[SchemaType]:
    #     insert_data = obj_in.dict()
    #     del insert_data['id']
    #     db_obj = self.model(**insert_data)
    #     db.add(db_obj)
    #     # stmt = insert(self.model).values(insert_data)
    #     # await db.execute(stmt)
    #     await db.commit()
    #     await db.refresh(db_obj)
    #     return self.schema.from_orm(db_obj)

    async def create(self, db: AsyncSession, *, obj_in: CreateSchemaType) -> ModelType:
        obj_in_data = jsonable_encoder(obj_in)
        db_obj = self.model(**obj_in_data)  # type: ignore
        db.add(db_obj)
        await db.commit()
        await db.refresh(db_obj)
        return db_obj

    async def delete(self, db: AsyncSession, id: int):
        stmt = delete(self.model).where(self.model.id == id)
        await db.execute(stmt)
        await db.commit()

    async def update(self, db: AsyncSession, id: Any, obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> None:
        if isinstance(obj_in, dict):
            update_data = obj_in
        else:
            update_data = obj_in.dict(exclude_unset=True)
        stmt = update(self.model).where(self.model.id == id, self.model.is_del == 0).values(update_data)
        await db.execute(stmt)
        await db.commit()

    # async def update(self, db: AsyncSession, id: Any, db_obj: ModelType,
    #                  obj_in: Union[UpdateSchemaType, Dict[str, Any]]) -> None:
    #     obj_data = obj_in.dict()
    #     update_data = {}
    #     del obj_data['id']
    #     for field in obj_data:
    #         value = obj_data.get(field)
    #     if value is not None:
    #         update_data[field] = value
    #     stmt = update(self.model).where(self.model.id == id).values(update_data)
    #     await db.execute(stmt)
    #     await db.commit()
    async def get_correct(self, db: AsyncSession, id: Any) -> Optional[ModelType]:
        """
        过滤未删除的状态
        """
        stmt = select(self.model).where(self.model.id == id, self.model.is_del == 0)
        result = await db.execute(stmt)
        return result.scalars().first()

    async def remove(self, db: AsyncSession, id: int) -> None:
        """
        伪删除
        """
        stmt = update(self.model).where(self.model.id == id).values(is_del=1)
        await db.execute(stmt)
        await db.commit()

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar, Union

from fastapi.encoders import jsonable_encoder

from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.base_class import Base
from sqlalchemy.sql import select, update, delete, insert

ModelType = TypeVar("ModelType", bound=Base)
SchemaType = TypeVar("SchemaType", bound=BaseModel)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase(Generic[ModelType, SchemaType]):
    def __init__(self, model: Type[ModelType], schema: Type[SchemaType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class
        * `schema`: A Pydantic model (schema) class
        """
        self.model = model
        self.schema = schema

    async def get(self, db: Session, id: Any) -> Optional[SchemaType]:
        stmt = select(self.model).where(self.model.id == id)
        result = await db.execute(stmt)
        model_obj = result.scalars().first()
        return self.schema.from_orm(model_obj)

    async def create(self, db: Session, obj_in: SchemaType) -> Optional[SchemaType]:
        insert_data = obj_in.dict()
        del insert_data['id']
        db_obj = self.model(**insert_data)
        db.add(db_obj)
        # stmt = insert(self.model).values(insert_data)
        # await db.execute(stmt)
        await db.commit()
        await db.refresh(db_obj)
        return self.schema.from_orm(db_obj)

    async def remove(self, db: Session, id: int) -> None:
        stmt = delete(self.model).where(self.model.id == id)
        await db.execute(stmt)
        await db.commit()

    async def update(self, db: Session, id: Any, obj_in: SchemaType) -> None:
        obj_data = obj_in.dict()
        update_data = {}
        del obj_data['id']
        for field in obj_data:
            value = obj_data.get(field)
            if value is not None:
                update_data[field] = value
        stmt = update(self.model).where(self.model.id == id).values(update_data)
        await db.execute(stmt)
        await db.commit()

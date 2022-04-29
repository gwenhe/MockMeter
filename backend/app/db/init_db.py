from app.db.base_class import Base, BaseModel
from app.db.session import engine, SessionLocal
from app import models


def init_db():
    BaseModel.metadata.drop_all(engine)
    BaseModel.metadata.create_all(engine)


if __name__ == '__main__':
    init_db()

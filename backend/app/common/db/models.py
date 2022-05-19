import datetime
from typing import Any
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from sqlalchemy.ext.declarative import declarative_base

BaseModel = declarative_base()


@as_declarative()
class Base(object):
    id: Any
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class TimeRecordModelMixin(object):
    """提供操作时间类Model方法 """

    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()

    id = Column(Integer, primary_key=True)
    create_time = Column(DATETIME, default=datetime.datetime.now, comment='创建时间')
    update_time = Column(DATETIME, default=None, onupdate=datetime.datetime.now, comment='修改时间')
    is_del = Column(Integer, default=0, comment='0:未删除,1:已删除')

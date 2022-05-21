from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from common.db.models import TimeRecordModelMixin, BaseModel
from sqlalchemy.orm import relationship


class MockProject(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'mock_project'
    __table_args__ = ({'comment': 'mock项目'})

    project_name = Column(String(200), comment='项目名称')
    remarks = Column(String(2000), comment='项目描述')


class MockService(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'mock_service'
    __table_args__ = ({'comment': 'mock服务'})
    service_name = Column(String(200), comment='服务名称')
    remarks = Column(String(2000), comment='项目描述')

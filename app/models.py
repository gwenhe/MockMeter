from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from app.db.base_class import TimeRecordModelMixin, BaseModel
from sqlalchemy.orm import relationship


class Project(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'project'
    __table_args__ = ({'comment': '项目表'})

    project_name = Column(String(200), comment='项目名称')
    desc = Column(String(2000), comment='项目描述')


class Interface(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'interface'
    __table_args__ = ({'comment': '接口表'})

    project_id = Column(Integer, comment='project.id')
    interface_name = Column(String(200), comment='接口名称')
    interface_path = Column(String(200), comment='接口路径')
    mock_info = Column(TEXT, comment='mock数据：json')
    script_path = Column(String(200), comment='脚本路径')


class Script(BaseModel, TimeRecordModelMixin):
    interface_id = Column(Integer, comment='interface.id')
    script_desc = Column(String(200), comment='脚本描述')
    script_path = Column(String(200), comment='脚本路径')
    expiration_time = Column(DATETIME, comment='过期时间')


class Record(BaseModel, TimeRecordModelMixin):

    __tablename__ = 'record'
    __table_args__ = ({'comment': 'mock调用记录'})
    interface_id = Column(Integer, comment='interface.id')
    interface_path = Column(String(200), comment='接口路径')
    request_info = Column(TEXT, comment='请求信息json')
    response_info = Column(TEXT, comment='响应信息json')

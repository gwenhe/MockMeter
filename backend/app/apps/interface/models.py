from sqlalchemy import Column, Integer, String, DATETIME, TEXT
from common.db.models import TimeRecordModelMixin, BaseModel
from sqlalchemy.orm import relationship


class MockInterface(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'mock_interface'
    __table_args__ = ({'comment': 'mock接口'})

    mock_group_id = Column(Integer, comment='mock_group.id')
    interface_name = Column(String(200), comment='接口名称')
    interface_path = Column(String(200), comment='接口路径')
    mock_info = Column(TEXT, comment='mock数据：json')
    script_path = Column(String(200), comment='脚本路径')


class MockScript(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'mock_script'
    __table_args__ = ({'comment': 'mock接口'})

    interface_id = Column(Integer, comment='interface.id')
    script_name = Column(String(200), comment='脚本描述')
    script_path = Column(String(200), comment='脚本路径')
    expiration_time = Column(DATETIME, comment='过期时间')


class MockRecord(BaseModel, TimeRecordModelMixin):
    __tablename__ = 'mock_record'
    __table_args__ = ({'comment': 'mock调用记录'})
    interface_id = Column(Integer, comment='interface.id')
    interface_path = Column(String(200), comment='接口路径')
    request_info = Column(TEXT, comment='请求信息json')
    response_info = Column(TEXT, comment='响应信息json')

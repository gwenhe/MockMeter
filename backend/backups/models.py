# from sqlalchemy import Column, Integer, String, DATETIME, TEXT
# from app.db.base_class import TimeRecordModelMixin, BaseModel
# from sqlalchemy.orm import relationship
#
#
# class MockProject(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_project'
#     __table_args__ = ({'comment': 'mock项目'})
#
#     project_name = Column(String(200), comment='项目名称')
#     desc = Column(String(2000), comment='项目描述')
#
#
# class MockService(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_service'
#     __table_args__ = ({'comment': 'mock服务'})
#     service_name = Column(String(200), comment='服务名称')
#     desc = Column(String(2000), comment='项目描述')
#
#
# class MockGroup(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_group'
#     __table_args__ = ({'comment': 'mock接口分组'})
#
#     mock_service_id = Column(Integer, comment='mock_service.id')
#     group_name = Column(String(200), comment='分组名称')
#     group_level = Column(Integer, comment='分组级别')
#     group_parent_id = Column(Integer, comment='分组父id')
#
#
# class MockInterface(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_interface'
#     __table_args__ = ({'comment': 'mock接口'})
#
#     mock_group_id = Column(Integer, comment='mock_group.id')
#     interface_name = Column(String(200), comment='接口名称')
#     interface_path = Column(String(200), comment='接口路径')
#     mock_info = Column(TEXT, comment='mock数据：json')
#     script_path = Column(String(200), comment='脚本路径')
#
#
# class MockScript(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_script'
#     __table_args__ = ({'comment': 'mock接口'})
#
#     interface_id = Column(Integer, comment='interface.id')
#     script_name = Column(String(200), comment='脚本描述')
#     script_path = Column(String(200), comment='脚本路径')
#     expiration_time = Column(DATETIME, comment='过期时间')
#
#
# class MockRecord(BaseModel, TimeRecordModelMixin):
#     __tablename__ = 'mock_record'
#     __table_args__ = ({'comment': 'mock调用记录'})
#     interface_id = Column(Integer, comment='interface.id')
#     interface_path = Column(String(200), comment='接口路径')
#     request_info = Column(TEXT, comment='请求信息json')
#     response_info = Column(TEXT, comment='响应信息json')

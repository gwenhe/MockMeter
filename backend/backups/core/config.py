# import os
# import yaml
# from typing import Any, Dict, List, Optional, Union
# from pydantic import BaseSettings, validator
#
# project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# config_dir = os.path.join(project_dir, 'config.yaml')
# # 数据文件
# data_dir = os.path.join(project_dir, 'data')
# script_dir = os.path.join(data_dir, 'api_script')
# share_dir = os.path.join(data_dir, 'share')
# file_dir = os.path.join(data_dir, 'file')
#
# temp_script = os.path.join(data_dir, 'temp_script')
#
#
# def read_yaml(file_path) -> Union[List, Dict]:
#     with open(file_path, encoding="utf-8") as f:
#         yaml_data = yaml.load(f.read(), Loader=yaml.FullLoader)
#     return yaml_data
#
#
# def get_conf() -> Union[List, Dict]:
#     return read_yaml(config_dir)
#
#
# class Settings(BaseSettings):
#     SQLALCHEMY_DATABASE_URI: str = None
#
#     @validator("SQLALCHEMY_DATABASE_URI", pre=True)
#     def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> str:
#         mysql = get_conf().get('mysql')
#         """:type: Dict"""
#         return 'mysql+aiomysql://{user}:{password}@{server}/{db}?charset=UTF8MB4'.format(
#             user=mysql.get('user'),
#             password=mysql.get('password'),
#             server=mysql.get('server'),
#             db=mysql.get('db'),
#         )
#
#     class Config:
#         case_sensitive = True
#
#
# settings = Settings()

# import datetime
# from typing import List
# from sqlalchemy.orm import Session
# from app.crud.base import CRUDBase
# from sqlalchemy.sql import select
# from app.models import MockInterface, MockRecord, MockScript, MockProject
# from app.schemas.model_schema import InterfaceDB, ScriptDB, RecordDB
# from app.core.config import temp_script
# import os
#
#
# # class CRUDProject(CRUDBase[MockProject, ])
#
# class CRUDInterface(CRUDBase[MockInterface, InterfaceDB]):
#
#     async def get_interface_info(self, db: Session, project_id: int, interface_path: str) -> MockInterface:
#         stmt = select(self.model).where(
#             MockInterface.project_id == project_id, MockInterface.interface_path == interface_path
#         )
#         result = await db.execute(stmt)
#         return result.scalars().first()
#
#
# interface = CRUDInterface(MockInterface, InterfaceDB)
#
#
# class CRUDScript(CRUDBase[MockScript, ScriptDB]):
#
#     async def get_script(self, db: Session, interface_id) -> List:
#         stmt = select(self.model).where(
#             MockScript.interface_id == interface_id, MockScript.expiration_time >= datetime.datetime.now()
#         )
#         result = await db.execute(stmt)
#
#         script_item = result.scalars().all()
#         script_path_list = []
#         if script_item:
#             for i in script_item:
#                 api_script_dir = os.path.join(temp_script, i.script_path)
#                 script_path_list.append(api_script_dir)
#             return script_path_list
#         return script_path_list
#
#
# script = CRUDScript(MockScript, ScriptDB)
#
#
# class CRUDRecord(CRUDBase[MockRecord, RecordDB]):
#     pass
#
#
# record = CRUDRecord(MockRecord, RecordDB)

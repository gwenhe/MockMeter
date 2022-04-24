import datetime
from typing import Any, Dict, Optional, Union
from sqlalchemy.orm import Session
from app.crud.base import CRUDBase
from sqlalchemy.sql import select, update, delete, insert
from app.models import Project, Interface, Record, Script
from app.schemas.model_schema import InterfaceDB, ScriptDB, RecordDB
from app.core.config import script_dir, temp_script
import os


class CRUDInterface(CRUDBase[Interface, InterfaceDB]):

    async def get_interface_info(self, db: Session, project_id: int, interface_path: str) -> Interface:
        stmt = select(self.model).where(
            Interface.project_id == project_id, Interface.interface_path == interface_path
        )
        result = await db.execute(stmt)
        return result.scalars().first()


interface = CRUDInterface(Interface, InterfaceDB)


class CRUDScript(CRUDBase[Script, ScriptDB]):

    async def get_script(self, db: Session, interface_id) -> []:
        stmt = select(self.model).where(
            Script.interface_id == interface_id, Script.expiration_time >= datetime.datetime.now()
        )
        result = await db.execute(stmt)

        script_item = result.scalars().all()
        script_path_list = []
        if script_item:
            for i in script_item:
                api_script_dir = os.path.join(temp_script, i.script_path)
                script_path_list.append(api_script_dir)
            return script_path_list
        return script_path_list


script = CRUDScript(Script, ScriptDB)


class CRUDRecord(CRUDBase[Record, RecordDB]):
    pass


record = CRUDRecord(Record, RecordDB)

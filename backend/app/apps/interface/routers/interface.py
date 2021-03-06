import random
import string
import os
import datetime
import json
from fastapi import Depends, File, UploadFile, Form
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession as Session
from common.config import script_dir, file_dir, share_dir, temp_script
from common.dependencies import get_db

from .. import crud
from .. import schemas as model_schema
from ..utils import data_handle
from . import router


async def save_file(file: UploadFile, path: str, file_name: str = None, variable: str = None) -> str:
    contents = await file.read()
    if variable:
        contents = contents.decode('utf-8')
        variable = json.loads(variable)
        for i in variable:
            pattern = '{' + i + '}'
            contents = data_handle.replace_str(contents, pattern, variable[i])
        contents = contents.encode('utf-8')
    if file_name is None:
        random_str = random.sample(string.ascii_letters, 20)
        file_name = ''.join(random_str)
    script_path = os.path.join(path, file_name)
    with open(script_path, 'wb') as f:
        f.write(contents)
    return str(file_name)

#
# @router.post('/create')
# async def interface_create(db: Session = Depends(get_db), project_id: int = Form(...), interface_path: str = Form(...),
#                            mock_file: UploadFile = File(...), script_file: UploadFile = File(default=None)):
#     interface = await crud.interface.get_interface_info(db, project_id, interface_path)
#     file_name = None
#     if script_file:
#         file_name = interface_path.replace('/', '-')
#         await save_file(script_file, script_dir, file_name)
#     mock_info = await mock_file.read()
#     interface_schema = model_schema.InterfaceDB(
#         interface_path=interface_path,
#         mock_info=mock_info,
#         script_path=file_name,
#         project_id=project_id
#     )
#     if interface:
#         interface_schema.id = interface.id
#         db_obj = await crud.interface.update(db, interface.id, interface_schema)
#     else:
#         db_obj = await crud.interface.create(db, interface_schema)
#     return {
#         'code': 200,
#         'data': db_obj
#     }
#
#
# @router.post('/set_script')
# async def set_script(db: Session = Depends(get_db), file: UploadFile = File(...), project_id: int = Form(...),
#                      interface_path: str = Form(...), variable: str = Form(default=None),
#                      effective_time: int = Form(default=10)):
#     """
#     ??????????????????
#     """
#     interface = await crud.interface.get_interface_info(db, project_id, interface_path)
#     if interface is None:
#         return JSONResponse(content={'error_code': 404, 'error_msg': '????????????api'}, status_code=404)
#     file_name = await save_file(file, temp_script, variable=variable)
#     expiration_time = datetime.datetime.now() + datetime.timedelta(minutes=effective_time)
#     db_obj = await crud.script.create(db, model_schema.ScriptDB(
#         interface_id=interface.id,
#         script_path=file_name,
#         expiration_time=expiration_time
#     ))
#     return {
#         'code': 200,
#         'data': db_obj
#     }
#
#
# @router.post('/file_upload')
# async def file_upload(file_type: int = Form(...), file: UploadFile = File(...)):
#     file_name = file.filename
#     file_path = None
#     if file_type == 0:
#         file_path = file_dir
#     elif file_type == 1:
#         file_path = share_dir
#     await save_file(file, file_path, file_name)
#     return {
#         'code': 200,
#         'data': {
#             'file_path': file_path,
#             'file_name': file_name,
#         }
#     }

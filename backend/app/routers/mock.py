import json
from fastapi import APIRouter, Depends
from fastapi.responses import Response, JSONResponse
from app.dependencies import get_request, get_db
from sqlalchemy.orm import Session
from app import crud
from app.core.execution import exec_python_script
from app.core.config import script_dir
from app.schemas.mock import RequestSchema, ResponseSchema
from app.schemas import model_schema
import os
import asyncio

router = APIRouter(
    prefix="/mock",
    tags=["Mock API"],
    responses={404: {"description": "Not found"}},
)

from fastapi import BackgroundTasks


async def call_record(interface: model_schema.InterfaceDB, request: RequestSchema, response: ResponseSchema,
                      db: Session) -> model_schema.RecordDB:
    return await crud.record.create(db, model_schema.RecordDB(
        interface_id=interface.id,
        interface_path=interface.interface_path,
        request_info=request.json(),
        response_info=response.json(),
    ))


@router.api_route('/http/{project_id:int}/{interface_path:path}',
                  methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE', 'COPY', 'HEAD', 'OPTIONS', 'LINK', 'UNLINK',
                           'PURGE', 'LOCK', 'UNLOCK', 'PROPFIND', 'VIEW'])
async def mock_http(background_tasks: BackgroundTasks, project_id, interface_path,
                    request: RequestSchema = Depends(get_request),
                    db: Session = Depends(get_db)):
    request.project_id = project_id
    request.interface_path = '/' + interface_path
    interface = await crud.interface.get_interface_info(db, request.project_id, request.interface_path)
    if interface is None:
        return JSONResponse(content={'error_code': 404, 'error_msg': '不存在的api'}, status_code=404)
    response = ResponseSchema(**json.loads(interface.mock_info))

    script_path_list = await crud.script.get_script(db, interface.id)
    if interface.script_path is not None:
        api_script_dir = os.path.join(script_dir, interface.script_path)
        script_path_list.insert(0, api_script_dir)
    for i in script_path_list:
        response = await exec_python_script(background_tasks, i, request, response)
        if isinstance(response, Response):
            response_schema = ResponseSchema(
                status_code=response.status_code,
                media_type=response.media_type,
                body=response.body,
                headers=dict(response.headers),
            )
            await call_record(interface, request, response_schema, db)
            return response
    if response.media_type == 'application/json':
        response.body = json.dumps(response.body, ensure_ascii=False)
    if response.delay_time:
        await asyncio.sleep(response.delay_time)
    await call_record(interface, request, response, db)
    return Response(
        status_code=response.status_code,
        media_type=response.media_type,
        content=str(response.body),
        headers=response.headers,
    )

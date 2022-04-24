from typing import Union, Dict, List
import os
import sys
from fastapi import BackgroundTasks
from app.core.config import script_dir, data_dir
from app.core.exception import ResponseMock, JSONResponseMock, HTTPException, PlainTextResponseMock, \
    StreamingResponseMock, FileResponseMock, HTTPExceptionMock
from app.schemas.mock import RequestSchema, ResponseSchema

sys.path.append(data_dir)
import asyncio
import anyio
from asyncer import asyncify


async def exec_python_script(async_tasks: BackgroundTasks, script_path: str, request: RequestSchema = None,
                             response: ResponseSchema = None):
    """
    :param async_tasks:
    :param script_path: 完全路径
    :param request:
    :param response:
    :return:
    """
    print(script_path)
    with open(script_path, encoding="utf-8") as f:
        source = f.read()
        # executable = compile(source, script_path, 'exec')
    try:
        # await asyncio.to_thread(exec, source)
        await asyncify(exec)(source, globals(), locals())
        # await exec(source)
    except HTTPExceptionMock as response_obj:
        return response_obj
    else:
        return response

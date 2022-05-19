import sys
from fastapi import BackgroundTasks
from common.config import data_dir
from .mock_exception import HTTPExceptionMock
from ..schemas import RequestSchema, ResponseSchema

sys.path.append(data_dir)
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

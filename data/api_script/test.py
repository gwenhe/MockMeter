if 1 == 0:
    from app.schemas.mock import RequestSchema, ResponseSchema
    from app.core.exception import JSONResponseMock
    request: RequestSchema = None
    response: ResponseSchema = None

from share import push
import importlib
importlib.reload(push)

async_tasks.add_task(push.lending_push, data="我是data3")

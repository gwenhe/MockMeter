from fastapi import Request
from multipart.multipart import parse_options_header
from ..schemas import RequestSchema


async def get_request(request: Request) -> RequestSchema:
    request_schema = RequestSchema(
        client_ip=request.client[0],
        method=request.method,
        query_params=dict(request.query_params),
        cookies=request.cookies,
        headers=dict(request.headers),
    )
    content_type_header = request.headers.get("Content-Type")
    content_type, options = parse_options_header(content_type_header)
    if b'application/json' in content_type:
        request_schema.json_dict = await request.json()
        request_schema.body = await request.body()
    elif content_type == b"application/x-www-form-urlencoded":
        request_schema.file = await request.form()
    elif content_type == b"multipart/form-data":
        request_schema.file = await request.form()
    else:
        request_schema.body = await request.body()
    return request_schema

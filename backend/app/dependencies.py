from fastapi import Header, HTTPException, Request
from multipart.multipart import parse_options_header
from typing import Dict, Generator

from app.db.session import SessionLocal
from app.schemas.mock import RequestSchema


from sqlalchemy.ext.asyncio import AsyncSession


async def get_db() -> AsyncSession:
    async with SessionLocal() as db:
        yield db


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


async def get_token_header(x_token: str = Header(...)):
    if x_token != "fake-super-secret-token":
        raise HTTPException(status_code=400, detail="X-Token header invalid")


async def get_query_token(token: str):
    if token != "jessica":
        raise HTTPException(status_code=400, detail="No Jessica token provided")

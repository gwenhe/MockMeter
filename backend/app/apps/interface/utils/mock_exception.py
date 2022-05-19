from fastapi import Request, HTTPException
from fastapi.responses import Response, JSONResponse, HTMLResponse, PlainTextResponse, StreamingResponse, FileResponse


class HTTPExceptionMock(Exception):
    pass


class ResponseMock(Response, HTTPExceptionMock):
    pass


class JSONResponseMock(JSONResponse, HTTPExceptionMock):
    pass


class HTMLResponseMock(HTMLResponse, HTTPExceptionMock):
    pass


class PlainTextResponseMock(PlainTextResponse, HTTPExceptionMock):
    pass


class StreamingResponseMock(StreamingResponse, HTTPExceptionMock):
    pass


class FileResponseMock(FileResponse, HTTPExceptionMock):
    pass

# @app.exception_handler(HTTPExceptionMock)
# async def unicorn_exception_handler(request: Request, exc: HTTPExceptionMock):
#     return exc

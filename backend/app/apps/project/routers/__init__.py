from fastapi import APIRouter
from common.http import APIJSONResponse, code, resp

router = APIRouter(
    prefix="/project",
    tags=["项目"],
    default_response_class=APIJSONResponse,
    responses=resp.fail | resp.unauthorized | resp.error,
)
from .project import *
from .service import *

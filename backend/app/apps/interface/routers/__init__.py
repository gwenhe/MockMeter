from fastapi import APIRouter, Depends, File, UploadFile, Form

router = APIRouter(
    prefix="/interface",
    tags=["接口管理"],
    responses={404: {"description": "Not found"}},
)
from . import interface, mock

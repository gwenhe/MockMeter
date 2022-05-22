from __future__ import annotations
from typing import Any
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from common.dependencies import get_db
from common.exceptions import HTTPException
from .. import schemas, crud

from . import router


@router.post('/create_service')
def create_service() -> Any:
    pass

from app.crud.crud_models import interface
from sqlalchemy.ext.asyncio import AsyncSession
import pytest
import os


def test_interface_update(db: AsyncSession) -> None:
    res = interface.get_interface_info(db, 1, '/test')
    assert res.id == 1
    # res = interface.update(db, 15, {'interface_name': '测试用了', 'interface_path': '/test'})
    # print(res.id)


if __name__ == '__main__':
    pytest.main(['-vs'])

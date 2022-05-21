from math import ceil
from sqlalchemy.sql import Select, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import func
from pydantic import BaseModel, Field
from typing import List


class Pagination(object):

    def __init__(self, page, per_page, total, items):
        self.page = page
        self.per_page = per_page
        self.total = total
        self.items = items

    @property
    def pages(self):
        """The total number of pages"""
        if self.per_page == 0:
            pages = 0
        else:
            pages = int(ceil(self.total / float(self.per_page)))
        return pages

    # def prev(self, error_out=False):
    #     """Returns a :class:`Pagination` object for the previous page."""
    #     assert self.query is not None, 'a query object is required ' \
    #                                    'for this method to work'
    #     return self.query.paginate(self.page - 1, self.per_page, error_out)

    @property
    def prev_num(self):
        """Number of the previous page."""
        if not self.has_prev:
            return None
        return self.page - 1

    @property
    def has_prev(self):
        return self.page > 1

    # def next(self, error_out=False):
    #     """Returns a :class:`Pagination` object for the next page."""
    #     assert self.query is not None, 'a query object is required ' \
    #                                    'for this method to work'
    #     return self.query.paginate(self.page + 1, self.per_page, error_out)

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def next_num(self):
        if not self.has_next:
            return None
        return self.page + 1


async def paginate(db: AsyncSession, stem: Select, page: int = 1, per_page: int = 20) -> Pagination:
    if page < 1:
        page = 1

    if per_page < 0:
        per_page = 20

    stmt_items = stem.limit(per_page).offset((page - 1) * per_page)
    stmt_total = select(func.count(stem.c.id))

    result_items = await db.execute(stmt_items)
    result_total = await db.execute(stmt_total)

    items = result_items.scalars().all()
    total = result_total.scalars().one()

    return Pagination(page, per_page, total, items)


class PageResSchema(BaseModel):
    total: int = Field(None, description='总数')
    pages: int = Field(None, description='总页数')
    per_page: int = Field(None, description='每页条数')
    page: int = Field(None, description='当前页码')
    has_prev: bool = Field(None, description='上一页是否存在')
    prev_num: int = Field(None, description='上一页页码')
    has_next: bool = Field(None, description='下一页是否存在')
    next_num: int = Field(None, description='下一页页码')
    # 重写该属性
    items: List = Field(None, description='当前页数据列表')

    class Config:
        orm_mode = True


class PageReqSchema(BaseModel):
    page: int = Field(default=1, description='当前页码')
    per_page: int = Field(default=20, description='每页条数')

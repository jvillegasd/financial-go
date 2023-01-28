from typing import Optional, Any
from dataclasses import dataclass
from src.schemas.base.vanilla import BaseSchema


@dataclass
class PaginationCursor(BaseSchema):
    prev: Optional[int]
    next: int
    per_page: int


@dataclass
class ModelPagination(BaseSchema):
    records: list[Any]
    cursor: PaginationCursor


@dataclass
class QueryParamPagination(BaseSchema):
    per_page: Optional[int]
    next_cursor: Optional[float]

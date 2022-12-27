from typing import TypeVar, Optional
from src.models.base import BaseDocument
from mongoengine.queryset import QuerySet
from src.schemas.model_pagination import (
    ModelPagination,
    PaginationCursor,
    QueryParamPagination
)
from src.schemas.filter import FilterSchema
from pymongo.client_session import ClientSession
from src.constants import ALLOWED_QUERY_OPERATORS
from src.interfaces.repository import IRepository
from src.errors.filter import InvalidFilterOperator, InvalidFilterColumn

ModelType = TypeVar('ModelType', bound=BaseDocument)


class MongoEngineRepository(IRepository[ModelType, QuerySet]):

    def __init__(
        self,
        model: ModelType,
        session: ClientSession
    ):
        self.model: ModelType = model
        self.session: ClientSession = session

    def apply_pagination(
        self,
        query: QuerySet,
        paginate: Optional[QueryParamPagination] = None
    ) -> ModelPagination:
        import datetime

        per_page: int = 10
        result: list[ModelType]
        cursor_timestamp: Optional[float] = None
        if paginate:
            per_page = paginate.per_page or 10
            cursor_timestamp = paginate.next_cursor

        if cursor_timestamp:
            cursor_timestamp = float(cursor_timestamp)
            cursor_date = datetime.datetime.fromtimestamp(
                cursor_timestamp
            )
            result = query.filter(
                created_at__le=cursor_date
            ).order_by('-created_at').limit(per_page).all()
        else:
            result = query.order_by('-created_at').limit(per_page).all()

        next_cursor: Optional[int] = None
        if result:
            next_cursor = result[-1].created_at.timestamp()

        return ModelPagination(
            records=result,
            cursor=PaginationCursor(
                prev=cursor_timestamp,
                next=next_cursor,
                per_page=per_page
            )
        )

    def _apply_filters(
        self,
        query: QuerySet,
        filters: list[FilterSchema]
    ) -> QuerySet:
        for raw_filter in filters:
            column = getattr(self.model, raw_filter.field_name, None)
            if column is None:
                raise InvalidFilterColumn(
                    f'Invalid filter column {raw_filter.field_name}'
                )
            if raw_filter.operation not in ALLOWED_QUERY_OPERATORS:
                raise InvalidFilterOperator(
                    f'Invalid filter operator: {raw_filter.operation}'
                )
            if raw_filter.operation == 'eq':
                crafted_filter = {raw_filter.field_name: raw_filter.value}
            else:
                crafted_filter = {
                    '{}__{}'.format(
                        raw_filter.field_name,
                        raw_filter.operation
                    ): raw_filter.value
                }
            query = query.filter(**crafted_filter)
        return query

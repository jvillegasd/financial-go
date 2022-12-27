from src.models.base import BaseDocument
from mongoengine.queryset import QuerySet
from src.schemas.filter import FilterSchema
from pymongo.client_session import ClientSession
from src.constants import ALLOWED_QUERY_OPERATORS
from src.interfaces.repository import IRepository
from src.errors.filter import InvalidFilterOperator, InvalidFilterColumn


class MongoEngineRepository(IRepository[BaseDocument]):

    def __init__(
        self,
        model: BaseDocument,
        session: ClientSession
    ):
        self.model = model
        self.session = session

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

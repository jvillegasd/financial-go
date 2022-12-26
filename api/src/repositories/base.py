from src.models.base import BaseDocument
from mongoengine.queryset import QuerySet
from src.schemas.filter import FilterSchema
from src.constants import ALLOWED_QUERY_OPERATORS
from src.errors.filter import InvalidFilterOperator, InvalidFilterColumn


class BaseRepository:

    def __init__(self, model: BaseDocument):
        self.model = model

    def _apply_filters(
        self,
        query: QuerySet,
        filters: list[FilterSchema]
    ) -> QuerySet:
        """Apply a list of simple filters to the provided
        query. Simple filters are intented to interact with
        fields of current model. Complex operations like Joins
        or filtering by relationship fields are not allowed.
        Args:
            -   query: QuerySet = Query to be filtered.
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current query.
        Returns:
            -   QuerySet = Provided query with filter applied.
        """

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

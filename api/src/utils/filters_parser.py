
import re
from src.schemas.filter import FilterSchema
from src.constants import QUERY_PARAMS_BRACKET_OPERATORS
from src.errors.filter import InvalidComplexQueryOperator


class QueryParameterParser(object):

    @classmethod
    def _get_query_operator(cls, field: str) -> tuple[str, str]:
        """Infer query operator from field. If brackets notation is detected,
        the right operator will be returned.
        The following table denotes allowed complex operations:
                -   '[lt]'  =   'Lower than'
                -   '[le]' =   'Lower or equal than'
                -   '[gt]'  =   'Greater than'
                -   '[ge]' =   'Greater or equal than'
                -   '[eq]'  =   'Equals to'

        Args:
            -   field: str = Field that can contain bracket notation.
        Returns:
            -   str = Query operator.
        """

        complex_op_match: re.Match = re.search('\[.*?\]', field)
        if complex_op_match:
            operator: str = complex_op_match.group(0)
            if operator in QUERY_PARAMS_BRACKET_OPERATORS:
                field = field.replace(operator, '')
                operator = operator.replace('[', '').replace(']', '')
                return field, operator
            else:
                raise InvalidComplexQueryOperator(
                    'Query operator cannot be processed'
                )

        return field, 'eq'


    @classmethod
    def transform_query_params(cls, query_params: dict) -> list[FilterSchema]:
        """Transform query params into a list of simple filters.
        Args:
            -   query_params: dict = Query params that represents filters
            to be applied to endpoint data.
        Returns:
            -   list[FilterSchema] = List filters from query params
            represented as FilterSchema filters for queries.
        """

        filters: list[FilterSchema] = []
        for param, value in query_params.items():
            field, op = cls._get_query_operator(param)
            filters.append(
                FilterSchema(
                    field_name=field,
                    operation=op,
                    value=value
                )
            )

        return filters

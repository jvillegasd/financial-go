class InvalidComplexQueryOperator(Exception):
    """Raises when an invalid complex query param operator was provided."""


class InvalidFilterOperator(Exception):
    """Raises when an operator is not found in Database operators."""


class InvalidFilterColumn(Exception):
    """Raises when a column does not belongs to model."""

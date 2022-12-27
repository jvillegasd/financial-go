from abc import ABC, abstractmethod
from src.schemas.model_pagination import (
    ModelPagination,
    QueryParamPagination
)
from src.schemas.filter import FilterSchema
from src.models import User, Transaction, Card
from typing import Optional, Any, Generic, TypeVar

T = TypeVar('T')


class IRepository(ABC, Generic[T]):

    @abstractmethod
    def find_one(
        self,
        filters: list[FilterSchema]
    ) -> Optional[T]:
        """Find one record from current model that
        match simple filters.
        Args:
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current model.
        Returns:
            -  Optional[T] = Record (domain object) that
            match provided filters.
        """
        raise NotImplementedError

    @abstractmethod
    def find_all(
        self,
        filters: list[FilterSchema]
    ) -> object:
        """Find all records from current model that
        match simple filters.
        Args:
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current model.
        Returns:
            -   object = Query of current models that match
            provided filters. Query is returned due to allows pagination
            application.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, record_id: Any) -> Optional[T]:
        """Find a record for loaded model by searching
        by id.
        Args:
            -   record_id: Any = Id to search in table.
        Returns:
            -   Optional[T] = Record (domain object) if found.
        """
        raise NotImplementedError

    @abstractmethod
    def apply_pagination(
        self,
        query: object,
        paginate: Optional[QueryParamPagination] = None
    ) -> ModelPagination:
        """Paginates Query using cursor technique. So,
        pagination will scales at the same time the records
        does.
        Args:
            -   query: object = Query to paginate.
            -   paginate: QueryParamPagination = Object that contains
            Datetime as timestamp as a cursor for pagination and how many
            records is going to be returned per page.
        Returns:
            -   ModelPagination = Pagination dict object that save cursors and
            records for current page.
        """
        raise NotImplementedError

    @abstractmethod
    def _apply_filters(
        self,
        query: object,
        filters: list[FilterSchema]
    ) -> object:
        """Apply a list of simple filters to the provided
        query. Simple filters are intented to interact with
        fields of current model. Complex operations like Joins
        or filtering by relationship fields are not allowed.
        Args:
            -   query: object = Query to be filtered.
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current query.
        Returns:
            -   object = Provided query with filter applied.
        """
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        record: T
    ) -> T:
        """Create a new record of defined domain model.
        Args:
            -   record: T = Domain model to be added into database.
        Returns:
            -   T = Created domain model.
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        record: T,
        fields_to_update: dict
    ) -> T:
        """Update an existing record of domain model.
        Args:
            -   record: T = Domain model to be updated.
            -   fields_to_update: dict = provided fields to be
            updated in record.

        Returns:
            -   T = Updated domain model.
        """
        raise NotImplementedError

    @abstractmethod
    def delete(self, record_id: Any):
        """Delete an existing record of domain model.
        Args:
            -   record_id: Any = Record id of domain model record
            to delete.
        """
        raise NotImplementedError


class IUserRepository(IRepository[User]):
    pass


class ITransactionRepository(IRepository[Transaction]):
    pass


class ICardRepository(IRepository[Card]):
    pass

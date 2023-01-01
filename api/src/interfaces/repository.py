from uuid import UUID
from abc import ABC, abstractmethod
from src.schemas.model_pagination import (
    ModelPagination,
    QueryParamPagination
)
from src.schemas.filter import FilterSchema
from src.models import User, Transaction, Card
from typing import Optional, Any, Generic, TypeVar

ModelType = TypeVar('ModelType')
QueryType = TypeVar('QueryType')


class IRepository(ABC, Generic[ModelType, QueryType]):
    @abstractmethod
    def find_one(
        self,
        filters: list[FilterSchema]
    ) -> Optional[ModelType]:
        """Find one record from current model that
        match simple filters.
        Args:
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current model.
        Returns:
            -  Optional[ModelType] = Record (domain object) that
            match provided filters.
        """
        raise NotImplementedError

    @abstractmethod
    def find_all(
        self,
        filters: list[FilterSchema]
    ) -> QueryType:
        """Find all records from current model that
        match simple filters.
        Args:
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current model.
        Returns:
            -   QueryType = Query of current models that match
            provided filters. Query is returned due to allows pagination
            application.
        """
        raise NotImplementedError

    @abstractmethod
    def find_by_id(self, record_id: Any) -> Optional[ModelType]:
        """Find a record for loaded model by searching
        by id.
        Args:
            -   record_id: Any = Id to search in table.
        Returns:
            -   Optional[QueryType] = Record (domain object) if found.
        """
        raise NotImplementedError

    @abstractmethod
    def apply_pagination(
        self,
        query: QueryType,
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
        query: QueryType,
        filters: list[FilterSchema]
    ) -> QueryType:
        """Apply a list of simple filters to the provided
        query. Simple filters are intented to interact with
        fields of current model. Complex operations like Joins
        or filtering by relationship fields are not allowed.
        Args:
            -   query: QueryType = Query to be filtered.
            -   filters: list[FilterSchema] = List of simple
            filters for apply to current query.
        Returns:
            -   QueryType = Provided query with filter applied.
        """
        raise NotImplementedError

    @abstractmethod
    def create(
        self,
        record: ModelType
    ) -> ModelType:
        """Create a new record of defined domain model.
        Args:
            -   record: ModelType = Domain model to be added into database.
        Returns:
            -   ModelType = Created domain model.
        """
        raise NotImplementedError

    @abstractmethod
    def update(
        self,
        record: ModelType,
        fields_to_update: dict
    ) -> ModelType:
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


class IUserRepository(IRepository[User, QueryType]):
    pass


class ITransactionRepository(IRepository[Transaction, QueryType]):
    pass


class ICardRepository(IRepository[Card, QueryType]):
    @abstractmethod
    def number_of_cards(self, owner_id: UUID) -> int:
        """Calculates the number of cards of provided
        owner.
        Args:
            -   owner_id: UUID = Owner id
        Returns:
            -   int = Number of cards of user
        """

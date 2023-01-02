from uuid import UUID
from src.models import Transaction
from src.interfaces.unit_of_work import IUnitOfWork
from src.interfaces.repository import ITransactionRepository
from src.schemas.filter import FilterSchema
from src.schemas.transaction import TransactionSchema
from src.errors.transaction import TransactionNotFound


class TransactionService:
    def create_transaction(
        self,
        card_id: UUID,
        transaction_info: TransactionSchema,
        uow: IUnitOfWork
    ) -> Transaction:
        """Creates a new transaction for specific user.
        Before a transaction is created, validation to Card
        and User is made.
        Args:
            -   card_uuid: str = Card uuid owner of the transaction.
            -   transaction_info: TransactionSchema = This dict contains
            information about the transation to be created.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - new_transaction: Transaction = New transaction
            Mongoengine object created by provided information.
        """
        transaction_repo: ITransactionRepository = uow.get_repo(
            name='transaction'
        )
        new_transaction = Transaction(
            **transaction_info,
            card_id=card_id
        )
        transaction_repo.create(new_transaction)
        return new_transaction

    def get_transaction_by_id(
        self,
        transaction_id: UUID,
        card_id: UUID,
        uow: IUnitOfWork
    ) -> Transaction:
        """Fetch a transaction form database using uuid.
        Args:
            -   transaction_id: UUID = Provided uuid used to check
            transaction existance.
            -   card_id: UUID = Card id owned of transaction.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Raises:
            - TransactionNotFound = Raised when a transaction is not found
            using provided uuid.
        """
        transaction_repo: ITransactionRepository = uow.get_repo(
            name='transaction'
        )
        filters: list[FilterSchema] = [
            FilterSchema(
                field_name='doc_id',
                operation='eq',
                value=transaction_id
            ),
            FilterSchema(
                field_name='card_id',
                operation='eq',
                value=card_id
            )
        ]
        transaction = transaction_repo.find_one(filters)
        if transaction is None:
            raise TransactionNotFound('This transaction was not found in card')
        return transaction

    def update_transaction(
        self,
        transaction_info: TransactionSchema,
        transaction_id: UUID,
        card_id: UUID,
        uow: IUnitOfWork
    ) -> Transaction:
        """Updates an existing transaction basic information.
        Args:
            -   transaction_info: TransactionSchema = This dict contains
            information about the transation to be created.
            -   transaction_id: str = Provided uuid used to check
            transaction existance.
            -   card_id: UUID = Card id owned of transaction.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - transaction: Transaction = Existing transaction Mongoengine
            object with updated information.
        """
        transaction = self.get_transaction_by_id(
            transaction_id=transaction_id,
            card_id=card_id,
            uow=uow
        )
        transaction_repo: ITransactionRepository = uow.get_repo(
            name='transaction'
        )
        updated_record = transaction_repo.update(
            record=transaction,
            fields_to_update=dict(transaction_info)
        )
        return updated_record

    def delete_transaction(
        self,
        transaction_id: UUID,
        card_id: UUID,
        uow: IUnitOfWork
    ):
        """Delete transaction from database.
        
        Args:
            - transaction_uuid: str = Provided uuid used to check
            transaction existance.
            -   card_id: UUID = Card id owned of transaction.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        """
        transaction = self.get_transaction_by_id(
            transaction_id=transaction_id,
            card_id=card_id,
            uow=uow
        )
        transaction_repo: ITransactionRepository = uow.get_repo(
            name='transaction'
        )
        transaction_repo.delete(transaction.doc_id)

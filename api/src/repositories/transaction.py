from src.models import Transaction
from mongoengine.queryset import QuerySet
from src.interfaces.repository import ITransactionRepository
from src.repositories.base.mongo import MongoRepository


class TransactionRepository(
    MongoRepository[Transaction],
    ITransactionRepository[QuerySet]
):
    pass

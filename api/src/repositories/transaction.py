from src.models import Transaction
from mongoengine.queryset import QuerySet
from src.interfaces.repository import ITransactionRepository
from src.repositories.base.mongo import MongoEngineRepository


class TransactionRepository(
    MongoEngineRepository[Transaction],
    ITransactionRepository[QuerySet]
):
    pass

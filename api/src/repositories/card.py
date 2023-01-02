from src.models import Card
from mongoengine.queryset import QuerySet
from src.interfaces.repository import ICardRepository
from src.repositories.base.mongo import MongoRepository


class CardRepository(
    MongoRepository[Card],
    ICardRepository[QuerySet]
):
    pass

from uuid import UUID
from src.models import Card
from mongoengine.queryset import QuerySet
from src.interfaces.repository import ICardRepository
from src.repositories.base.mongo import MongoRepository


class CardRepository(
    MongoRepository[Card],
    ICardRepository[QuerySet]
):
    def number_of_cards(self, owner_id: UUID) -> int:
        return self.model.objects.filter(owner_id=owner_id).count()

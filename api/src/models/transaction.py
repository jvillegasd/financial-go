from mongoengine.fields import (
    UUIDField,
    StringField,
    FloatField
)
from src.models.base.mongo import BaseDocument
from src.constants import TRANSACTION_TYPES, TRANSACTION_CATEGORIES


class Transaction(BaseDocument):
    card_id = UUIDField(binary=False)
    title = StringField(required=True)
    type = StringField(required=True, choices=TRANSACTION_TYPES)
    amount = FloatField(default=0.0)
    category = StringField(required=True, choices=TRANSACTION_CATEGORIES)

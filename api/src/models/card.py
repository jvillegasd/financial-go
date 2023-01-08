from mongoengine.fields import (
    UUIDField,
    StringField,
    FloatField
)
from src.models.base.mongo import BaseDocument


class Card(BaseDocument):
    owner_id = UUIDField(binary=False)
    title = StringField(required=True)
    initial_amount = FloatField(default=0.0)
    # TODO: Amount hybrid prod pre-calculated
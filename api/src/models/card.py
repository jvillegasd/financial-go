from mongoengine.fields import (
    UUIDField,
    StringField,
    FloatField
)
from models.base.mongo import BaseDocument


class Card(BaseDocument):
    owner_uuid = UUIDField(binary=False)
    title = StringField(required=True)
    amount = FloatField(default=0.0)

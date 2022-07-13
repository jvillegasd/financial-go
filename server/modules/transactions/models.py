import mongoengine
from modules.mixin import DocumentMixin
from modules.constants import TRANSACTION_TYPES, TRANSACTION_CATEGORIES


class Transaction(DocumentMixin):
    card_uuid = mongoengine.fields.UUIDField(binary=False)
    title = mongoengine.fields.StringField(required=True)
    type = mongoengine.fields.StringField(required=True, choices=TRANSACTION_TYPES)
    amount = mongoengine.fields.FloatField(default=0.0)
    category = mongoengine.fields.StringField(required=True, choices=TRANSACTION_CATEGORIES)

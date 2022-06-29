import mongoengine
from modules.mixin import DocumentMixin


class Card(DocumentMixin):
    title = mongoengine.fields.StringField(required=True)
    amount = mongoengine.fields.FloatField(default=0.0)
    owner_uuid = mongoengine.fields.UUIDField()

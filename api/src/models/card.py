from mongoengine.fields import (
    UUIDField,
    StringField,
    FloatField
)
from src.models.base.mongo import BaseDocument


class Card(BaseDocument):
    owner_id = UUIDField(binary=False)
    title = StringField(required=True)

    @property
    def account_balance(self):
        from src.models import Transaction

        balance = Transaction.objects.filter(
            card_id=self.doc_id
        ).sum('amount')
        return balance

from mongoengine.fields import (
    UUIDField,
    StringField,
    FloatField
)
from models import BaseDocument


class Card(BaseDocument):
    owner_uuid = UUIDField(binary=False)
    title = StringField(required=True)
    amount = FloatField(default=0.0)

    def add_transaction(self, new_transaction: Transaction):
        """
          Save a reference of Transaction to current user.
          Args:
            - new_transaction: Transaction = Transaction
            to be referenced to user.
        """

        new_transaction.owner_uuid = self.uuid
        new_transaction.save()

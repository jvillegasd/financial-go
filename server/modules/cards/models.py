import mongoengine
from modules.mixin import DocumentMixin
from modules.transactions.models import Transaction


class Card(DocumentMixin):
    owner_uuid = mongoengine.fields.UUIDField(binary=False)
    title = mongoengine.fields.StringField(required=True)
    amount = mongoengine.fields.FloatField(default=0.0)
    transactions = mongoengine.fields.ListField(
        mongoengine.fields.ReferenceField(
            Transaction,
            reverse_delete_rule=mongoengine.PULL
        ))

    def add_transaction(self, new_transaction: Transaction):
        """
          Save a reference of Transaction to current user.

          Args:
            - new_transaction: Transaction = Transaction
            to be referenced to user.
        """

        new_transaction.owner_uuid = self.uuid
        self.transactions.append(new_transaction)

        new_transaction.save()
        self.save()

import modules.cards.service as cards_service

from modules.transactions.models import Transaction
from modules.cards.exceptions import InvalidCardOwner
from modules.transactions.serializers import TransactionSchema
from modules.transactions.exceptions import TransactionNotFound


def create_transaction(
        card_uuid: str,
        owner_uuid: str,
        transaction_info: TransactionSchema) -> Transaction:
    """
      Creates a new transaction for specific user.
      Before a transaction is created, validation to Card
      and User is made.

      Args:
        - card_uuid: str = Card uuid owner of the transaction.
        - owner_uuid: str = User uuid owner of the card.
        - transaction_info: TransactionSchema = This dict
        contains information about the transation to be
        created.

      Return:
        - new_transaction: Transaction = New transaction
        Mongoengine object created by provided information.

      Raises:
        - InvalidCardOwner = Raised when a user is not owner of provided
        card.
    """

    card = cards_service.get_card_by_id(card_uuid, owner_uuid)
    if not card.owner_uuid == owner_uuid:
        raise InvalidCardOwner

    new_transaction = Transaction(**transaction_info)
    new_transaction.save()
    card.add_transaction(new_transaction)

    return new_transaction


def get_transaction_by_id(
        transaction_uuid: str,
        owner_uuid: str) -> Transaction:
    """
      Fetch a transaction form database using uuid.

      Args:
        - transaction_uuid: str = Provided uuid used to check
        transaction existance.
        - owner_uuid: str = User uuid owner of the transaction.
      
      Raises:
        - TransactionNotFound = Raised when a transaction is not found
        using provided uuid.
        - InvalidCardOwner = Raised when a user is not owner of provided
        card.
    """
    
    transaction = Transaction.objects.filter(uuid=transaction_uuid).first()
    if not transaction:
        raise TransactionNotFound
    
    card = cards_service.get_card_by_id(transaction.card_uuid, owner_uuid)
    if not card.owner_uuid == owner_uuid:
        raise InvalidCardOwner

    return transaction
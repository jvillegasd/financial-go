import modules.cards.service as cards_service

from typing import Union
from modules.users.exceptions import UserNotFound
from modules.transactions.models import Transaction
from modules.cards.exceptions import InvalidCardOwner
from modules.transactions.serializers import TransactionSchema


def create_transaction(
        card_uuid: str,
        user_uuid: str,
        transaction_info: TransactionSchema) -> Transaction:
    """
      Creates a new transaction for specific user.
      Before a transaction is created, validation to Card
      and User is made.

      Args:
        - card_uuid: str = Card uuid owner of the transaction.
        - user_uuid: str = User uuid owner of the card.
        - transaction_info: TransactionSchema = This dict
        contains information about the transation to be
        created.

      Return:
        - new_transaction: Transaction = New transaction
        Mongoengine object created by provided information.
      
      Raises:
        - UserNotFound = Raised when a user with provided user_uuid
        does not exists.
        - InvalidCardOwner = Raised when a user is not owner of provided
        card.
    """
    
    card = cards_service.get_card_by_id(card_uuid)
    if not card:
        raise UserNotFound
    
    if not card.owner_uuid == user_uuid:
        raise InvalidCardOwner
    
    new_transaction = Transaction(**transaction_info)
    new_transaction.save()
    card.add_transaction(new_transaction)
    
    return new_transaction

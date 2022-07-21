import uuid
import pytest
import modules.cards.exceptions as cards_exceptions

from modules.users.models import User
from modules.cards.models import Card
from modules.transactions import service
from modules.transactions.models import Transaction
from modules.transactions.serializers import TransactionSchema


def test_create_transaction(mock_user: User, mock_card: Card):
    """
      Test creating a transaction.
      
      Args:
        - mock_user: User = Mocked user fixture.
        - mock_card: Card = Mocked card fixture.
    """
    
    # Add mock_card to mock_user
    mock_user.add_card(mock_card)
    
    transaction_info = {
      'title': 'test',
      'type': 'Unique',
      'amount': 750.1,
      'category': 'Money'
    }
    params = TransactionSchema().load(transaction_info)
    new_transaction = service.create_transaction(str(mock_card.uuid),
                                                str(mock_user.uuid),
                                                params)

    assert isinstance(new_transaction, Transaction)
    assert new_transaction.title == params['title']
    assert new_transaction.type == params['type']
    assert new_transaction.amount == params['amount']
    assert new_transaction.category == params['category']
    
    card = Card.objects.filter(uuid=mock_card.uuid).first()
    transaction_filter = [
      transaction
      for transaction in card.transactions
      if transaction.id == new_transaction.uuid
    ]
    
    assert len(transaction_filter) == 1


def test_get_transaction_by_id(mock_transaction: Transaction,
                              mock_user: User,
                              mock_card: Card):
    """
      Test getting a transaction by id.
      
      Args:
        - mock_transaction: Transaction = Mocked transaction fixture.
        - mock_user: User = Mocked user fixture.
        - mock_card: Card = Mocked card fixture.
    """
    
    mock_user.add_card(mock_card)
    
    transaction = service.get_transaction_by_id(str(mock_transaction.uuid),
                                                str(mock_user.uuid))
    
    assert isinstance(transaction, Transaction)


def test_transaction_update(mock_transaction: Transaction,
                            mock_user: User,
                            mock_card: Card):
    """
      Test updating a transaction.
      
      Args:
        - mock_transaction: Transaction = Mocked transaction fixture.
        - mock_user: User = Mocked user fixture.
        - mock_card: Card = Mocked card fixture.
    """
    
    mock_user.add_card(mock_card)
    
    transaction_info = {
      'title': 'updated',
      'type': 'Unique',
      'amount': 670.1,
      'category': 'Money'
    }
    params = TransactionSchema().load(transaction_info)
    updated_transaction = service.update_transaction(params,
                                                    str(mock_transaction.uuid),
                                                    str(mock_user.uuid))

    assert updated_transaction.uuid == mock_transaction.uuid
    assert updated_transaction.title == params['title']
    assert updated_transaction.amount == params['amount']


def test_delete_transaction(mock_transaction: Transaction,
                            mock_user: User,
                            mock_card: Card):
    """
      Test deleting a transaction.
      
      Args:
        - mock_transaction: Transaction = Mocked transaction fixture.
        - mock_user: User = Mocked user fixture.
        - mock_card: Card = Mocked card fixture.
    """
    
    mock_user.add_card(mock_card)
    
    service.delete_transaction(str(mock_transaction.uuid), str(mock_user.uuid))
    transaction = Transaction.objects.filter(uuid=mock_transaction.uuid).first()
    
    assert transaction is None

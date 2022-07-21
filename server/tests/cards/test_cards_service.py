import uuid
import pytest
import modules.users.exceptions as users_exceptions
import modules.cards.exceptions as cards_exceptions

from modules.cards import service
from modules.users.models import User
from modules.cards.models import Card
from modules.cards.serializers import CardSchema
from modules.constants import MAX_NUMBER_OF_CARDS


def test_create_card(mock_user: User):
    """
      Test creating a new card.

      Args:
        - mock_user: User = Mocked user fixture.
    """

    card_info = {
        'title': 'testing card',
        'amount': 1050.0
    }
    params = CardSchema().load(card_info)
    new_card = service.create_card(params, str(mock_user.uuid))

    assert isinstance(new_card, Card)
    assert new_card.title == params['title']
    assert new_card.amount == params['amount']
    assert new_card.owner_uuid == mock_user.uuid

    user = User.objects.filter(uuid=mock_user.uuid).first()
    user_card_filter = [
        card
        for card in user.cards
        if card.id == new_card.uuid
    ]
    
    assert len(user.cards) > 0
    assert len(user_card_filter) == 1


def test_create_card_with_non_existing_user():
    """
      Test creating a new card using a random generated
      uuid in order to raises expected exception.

      Raises:
        - UserNotFound = Raised when a user is not found
        with provided uuid.
    """
    
    non_existing_user_uuid = uuid.uuid4()
    card_info = {
        'title': 'testing card',
        'amount': 1050.0
    }
    params = CardSchema().load(card_info)
    
    with pytest.raises(users_exceptions.UserNotFound):
        service.create_card(params, str(non_existing_user_uuid))


def test_update_card(mock_card: Card, mock_user: User):
    """
      Test updating an existing card.
      
      Args:
        - mock_card: Card = Mocked card fixture.
        - mock_user: User = Mocked user owner of card.
    """
    
    card_info = {
        'title': 'edited card',
        'amount': 1050.0
    }
    params = CardSchema().load(card_info)
    mock_user.add_card(mock_card)
    updated_card = service.update_card(params,
                                      str(mock_card.uuid),
                                      str(mock_card.owner_uuid))

    assert updated_card.uuid == mock_card.uuid
    assert updated_card.title == params['title']
    assert updated_card.amount == params['amount']


def test_update_non_existing_card(mock_user: User):
    """
      Test updating an unexisting card with a random
      generated uuid in order to raises expected exception.

      Raises:
        - CardNotFound = Raised when a card is not found
        with provided uuid.
    """

    non_existing_card_uuid = uuid.uuid4()
    card_info = {
        'title': 'edited card',
        'amount': 1050.0
    }
    params = CardSchema().load(card_info)
    
    with pytest.raises(cards_exceptions.CardNotFound):
        service.update_card(params,
                            str(non_existing_card_uuid),
                            str(mock_user.uuid))


def test_delete_card(mock_card: Card, mock_user: User):
    """
      Test deleting an existing card.
      
      Args:
        - mock_card: Card = Mocked card fixture.
        - mock_user: User = Mocked user owner of card.
    """
    
    mock_user.add_card(mock_card)
    service.delete_card(str(mock_card.uuid), str(mock_card.owner_uuid))
    card = Card.objects.filter(uuid=mock_card.uuid).first()
    
    assert card is None


def test_user_can_create_card(mock_user: User):
    """
      Test if mocked user can have another card.

      Args:
        - mock_user: User = Mocked user fixture.
    """

    can_add_card = service.user_can_create_card(str(mock_user.uuid))

    assert can_add_card


def test_user_cannot_create_card(mock_user: User):
    """
      Test if mocked user cannot have another card.
      An user can have only MAX_NUMER_OF_CARDS.

      Args:
        - mock_user: User = Mocked user fixture.
    """
    
    # Add MAX_NUMBER_OF_CARDS to mock_user
    for i in range(MAX_NUMBER_OF_CARDS):
        card_info = {
            'title': f'testing card {i}',
            'amount': 1050.0
        }
        new_card = Card(**card_info)
        mock_user.add_card(new_card)

    can_add_card = service.user_can_create_card(str(mock_user.uuid))

    assert not can_add_card


def test_get_card_by_id(mock_card: Card, mock_user: User):
    """
      Test getting a card by id.
      
      Args:
        - mock_card: Card = Mocked card fixture.
        - mock_user: User = Mocked user owner of card.
    """
    
    mock_user.add_card(mock_card)
    card = service.get_card_by_id(str(mock_card.uuid), str(mock_user.uuid))
    
    assert card.uuid == mock_card.uuid


def test_get_non_existing_card_by_id(mock_user: User):
    """
      Test getting a card with random generated uuid
      for raise expected exception.
      
      Args:
        - mock_user: User = Mocked user fixture.
      
      Raises:
        - CardNotFound = Raised when a card is not found
        with provided uuid.
    """
    
    non_existing_card_uuid = uuid.uuid4()
    
    with pytest.raises(cards_exceptions.CardNotFound):
        service.get_card_by_id(str(non_existing_card_uuid),
                              str(mock_user.uuid))


def test_get_card_by_id_another_owner(mock_card: Card):
    """
      Test getting a card with another owner for
      raise expected exception. Another owner uuid
      is random generated for testing purpose.
      
      Args:
        - mock_card: Card = Mocked card fixture.
      
      Raises:
        - InvalidCardOwner = Raises when a card owner differs on
        provided user uuid.
    """
    
    another_user_uuid = uuid.uuid4()
    
    with pytest.raises(cards_exceptions.InvalidCardOwner):
        service.get_card_by_id(str(mock_card.uuid),
                              str(another_user_uuid))

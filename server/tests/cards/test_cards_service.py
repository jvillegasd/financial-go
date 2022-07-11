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
    new_card = service.create_card(params)
    new_card.save()
    mock_user.add_card(new_card)

    assert isinstance(new_card, Card)
    assert new_card.title == params['title']
    assert new_card.amount == params['amount']
    assert new_card.owner_uuid == mock_user.uuid

    user_card_filter = [
        card
        for card in mock_user.cards
        if card.uuid == new_card.uuid
    ]
    
    assert len(mock_user.cards) > 0
    assert len(user_card_filter) == 1
    
    card = Card.objects.filter(uuid=new_card.uuid).first()
    
    assert card is not None


def test_add_card_to_user(mock_user: User, mock_card: Card):
    """
      Test adding a new card to mocked_user.
      
      Args:
        - mock_user: User = Mocked user fixture.
        - mock_card: Card = Mocked card fixture.
    """
    
    service.add_card_to_user(mock_card, str(mock_user.uuid))

    assert mock_card.owner_uuid == mock_user.uuid

    user = User.objects.filter(uuid=mock_user.uuid).first()
    user_card_filter = [
        card
        for card in user.cards
        if card.id == mock_card.uuid
    ]
    
    assert len(user.cards) > 0
    assert len(user_card_filter) == 1 


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
    updated_card = service.update_card(params, str(mock_card.uuid), str(mock_card.owner_uuid))

    assert updated_card.uuid == mock_card.uuid
    assert updated_card.title == params['title']
    assert updated_card.amount == params['amount']


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

    assert can_add_card == True


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
        params = CardSchema().load(card_info)
        new_card = service.create_card(params)
        new_card.save()
        mock_user.add_card(new_card)

    can_add_card = service.user_can_create_card(str(mock_user.uuid))

    assert can_add_card == False

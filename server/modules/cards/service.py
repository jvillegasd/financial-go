import uuid
import modules.users.service as users_service
from typing import Union
from modules.cards.models import Card
from modules.cards.serializers import CardSchema
from modules.constants import MAX_NUMBER_OF_CARDS


def user_can_create_card(owner_uuid: str) -> bool:
    """
      Check if an user can create a new card by fetching
      their current number of cards. A user can create
      only MAX_NUMBER_OF_CARDS.

      Args:
        - owner_uuid: str = uuid of card's owner.

      Return:
        - A boolean represeting if the user can create the card.
    """

    number_of_cards = Card.objects.filter(
        owner_uuid=uuid.UUID(owner_uuid)).count()
    return number_of_cards < MAX_NUMBER_OF_CARDS


def create_card(card_info: CardSchema) -> Card:
    """
      Creates a new card for specific user.

      Args:
        - card_info: CardSchema = This dict contains information of
        the card to be created.

      Return:
        - new_card: Card = New card Mongoengine object created by provided information.
    """

    new_card = Card(**card_info)
    new_card.save()
    return new_card


def add_card_to_user(card: Card, user_uuid: str):
    """
      Reference a card to a specific user.

      Args:
        - card: Card = Card Mongoengine object to be referenced to user.
        - user_uuid: str = User uuid owner of provided card.
    """

    user = users_service.get_user_by_id(user_uuid)
    if user:
        user.add_card(card)


def delete_card(card_uuid: str, owner_uuid: str):
    """
      Delete card from database.

      Args:
        - card_uuid: str = Card uuid to be deleted.
        - owner_uuid: str = User uuid owner of the provided card.
    """
    Card.objects.filter(
        uuid=uuid.UUID(card_uuid), owner_uuid=uuid.UUID(owner_uuid)).delete()


def update_card(card_info: CardSchema, card_uuid: str, owner_uuid: str) -> Union[Card, None]:
    """
      Updates an existing card basic information.

      Args:
        - card_info: CardSchema = This dict contains the new information
        of the provided card.
        - card_uuid: str = Card uuid to be updated.
        - owner_uuid: str = User uuid owner of the provided card.

      Return:
        - card: Card = Existing card Mongoengine object with updated information.
    """

    card = Card.objects.filter(
        uuid=uuid.UUID(card_uuid), owner_uuid=uuid.UUID(owner_uuid)).first()
    if card:
        for attr, value in card_info.items():
            setattr(card, attr, value)
        card.save()
    
    return card

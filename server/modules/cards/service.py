import uuid
import modules.users.service as users_service
from modules.cards.models import Card
from modules.constants import MAX_NUMBER_OF_CARDS
from modules.cards.serializers import CardSchema


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
    card.owner_uuid = user.uuid
    user.cards.append(card)

    card.save()
    user.save()

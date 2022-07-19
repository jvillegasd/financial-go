import uuid
import modules.users.service as users_service

from modules.cards.models import Card
from modules.cards.serializers import CardSchema
from modules.constants import MAX_NUMBER_OF_CARDS
from modules.users.exceptions import UserNotFound
from modules.cards.exceptions import CardNotFound


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


def create_card(card_info: CardSchema, user_uuid: str) -> Card:
    """
      Creates a new card for specific user.

      Args:
        - card_info: CardSchema = This dict contains information of
        the card to be created.
        - user_uuid: str = User uuid owner of the new card.

      Return:
        - new_card: Card = New card Mongoengine object created by
        provided information.

      Raises:
        - UserNotFound = Raised when a user with provided user_uuid
        does not exists.
    """

    user = users_service.get_user_by_id(user_uuid)
    if not user:
        raise UserNotFound

    new_card = Card(**card_info)
    new_card.save()
    user.add_card(new_card)

    return new_card


def get_card_by_id(card_uuid: str, owner_uuid: str) -> Card:
    """
      Fetch a card from database using uuid.

      Args:
        - card_uuid: str = Provided uuid used to check card existance.
        - owner_uuid: str = User uuid owner of the provided card.

      Return:
        - card: Card = Card instance fetched by uuid from database.

      Raises:
        - CardNotFound = Exception raises when a card is not found with
        provided owner_uuid.
    """

    card = Card.objects.filter(uuid=card_uuid, owner_uuid=owner_uuid).first()
    if not card:
        raise CardNotFound

    return card


def delete_card(card_uuid: str, owner_uuid: str):
    """
      Delete card from database.

      Args:
        - card_uuid: str = Card uuid to be deleted.
        - owner_uuid: str = User uuid owner of the provided card.
    """
    
    card = get_card_by_id(card_uuid, owner_uuid)
    Card.objects.filter(uuid=card.uuid).delete()


def update_card(card_info: CardSchema,
                card_uuid: str,
                owner_uuid: str) -> Card:
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

    card = get_card_by_id(card_uuid, owner_uuid)

    for attr, value in card_info.items():
        setattr(card, attr, value)
    card.save()

    return card

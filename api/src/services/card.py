from uuid import UUID
from src.models import Card
from src.schemas.card import CardSchema
from src.schemas.filter import FilterSchema
from src.constants import MAX_NUMBER_OF_CARDS
from src.interfaces.unit_of_work import IUnitOfWork
from src.interfaces.repository import ICardRepository
from src.errors.card import CardNotFound


class CardService:
    def user_can_create_card(
        self,
        owner_id: UUID,
        uow: IUnitOfWork
    ) -> bool:
        """
        Check if an user can create a new card by fetching
        their current number of cards. A user can create
        only MAX_NUMBER_OF_CARDS.
        Args:
            -   owner_uuid: str = uuid of card's owner.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            -   A boolean represeting if the user can create the card.
        """
        card_repo: ICardRepository = uow.get_repo(name='card')
        number_of_cards = card_repo.number_of_cards(owner_id)
        return number_of_cards < MAX_NUMBER_OF_CARDS

    def create_card(
        self,
        card_info: CardSchema,
        user_id: UUID,
        uow: IUnitOfWork
    ) -> Card:
        """
        Creates a new card for specific user.
        Args:
            - card_info: CardSchema = This dict contains information of
            the card to be created.
            -   user_id: UUID = User uuid owner of the new card.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - new_card: Card = New card Mongoengine object created by
            provided information.
        Raises:
            - UserNotFoundError = Raised when a user with provided user_uuid
            does not exists.
        """
        from src.services.user import UserService

        user_service = UserService()
        card_repository: ICardRepository = uow.get_repo(name='card')
        new_card = Card(**card_info)
        card_repository.create(new_card)
        user = user_service.get_user_by_id(user_id, uow)
        user.add_card(new_card)
        return new_card

    def get_card_by_id(
        self,
        card_id: UUID,
        owner_id: UUID,
        uow: IUnitOfWork
    ) -> Card:
        """
        Fetch a card from database using uuid.
        Args:
            - card_uuid: UUID = Provided uuid used to check card existance.
            - owner_uuid: UUID = User uuid owner of the provided card.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - card: Card = Card instance fetched by uuid from database.
        Raises:
            - CardNotFound = Exception raises when a card is not found with
            provided owner_uuid.
        """
        card_repository: ICardRepository = uow.get_repo(name='card')
        filters: list[FilterSchema] = [
            FilterSchema(
                field_name='doc_id',
                operation='eq',
                value=card_id
            ),
            FilterSchema(
                field_name='owner_id',
                operation='eq',
                value=owner_id
            )
        ]
        card_instance = card_repository.find_one(filters)
        if card_instance is None:
            raise CardNotFound('This card was not found')
        return card_instance

    def delete_card(
        self,
        card_id: UUID,
        owner_id: UUID,
        uow: IUnitOfWork
    ):
        """
        Delete card from database.
        Args:
            -   card_ud: UUID = Card uuid to be deleted.
            -   owner_id: UUID = User uuid owner of the provided card.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        """
        card = self.get_card_by_id(card_id, owner_id, uow)
        card_repository: ICardRepository = uow.get_repo('card')
        card_repository.delete(card.doc_id)

    def update_card(
        self,
        card_info: CardSchema,
        card_id: str,
        owner_id: str,
        uow: IUnitOfWork
    ) -> Card:
        """
        Updates an existing card basic information.
        Args:
            -   card_info: CardSchema = This dict contains the new information
            of the provided card.
            -   card_id: UUID = Card uuid to be updated.
            -   owner_id: UUID = User uuid owner of the provided card.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - card: Card = Existing card Mongoengine object
            with updated information.
        """
        card = self.get_card_by_id(card_id, owner_id, uow)
        card_repository: ICardRepository = uow.get_repo('card')
        updated_record = card_repository.update(
            record=card,
            fields_to_update=card_info
        )
        return updated_record

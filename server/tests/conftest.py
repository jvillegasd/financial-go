from pytest import fixture
from mongoengine import connect
from modules.users.models import User
from modules.cards.models import Card
from modules.transactions.models import Transaction


@fixture(scope='module', autouse=True)
def connect_db():
    """
      This fixture loads MongoDB connection before
      a module is going to be tested.
    """
    connect(
        'mongoenginetest',
        is_mock=True,
        uuidRepresentation='standard'
    )


@fixture
def mock_user(connect_db: fixture) -> User:
    """
      Mocks a user and save it in mocked database.

      Args:
        - connect_db: fixture = MongoDB connection fixture.

      Return:
        - mocked_user: User = Mocked user saved in mocked database.
    """

    mocked_user = User(
        first_name='John',
        last_name='Doe',
        email='johndoe@email.com',
        password='johndoe123'
    )
    mocked_user.save()
    return mocked_user


@fixture
def mock_card(connect_db: fixture) -> Card:
    """
      Mocks a card and save it in mocked database.

      Args:
        - connect_db: fixture = MongoDB connection fixture.

      Return:
        - mocked_card: Card = Mocked card saved in mocked database.
    """

    mocked_card = Card(
        title='Mocked card',
        amount=150.0
    )
    mocked_card.save()
    return mocked_card


@fixture
def mock_transaction(connect_db: fixture, mock_card: Card) -> Transaction:
    """
      Mocks a transaction and save it in mocked database.

      Args:
        - connect_db: fixture = MongoDB connection fixture.
        - mocked_card: Card = Mocked card fixture.
    """

    mocked_transaction = Transaction(
        card_uuid=mock_card.uuid,
        title='Mocked transaction',
        type='Unique',
        amount=750.1,
        category='Money'
    )
    mocked_transaction.save()
    return mocked_transaction

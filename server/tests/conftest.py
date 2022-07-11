import uuid
from pytest import fixture
from mongoengine import connect

from modules.users.models import User
from modules.cards.models import Card


@fixture(scope='module', autouse=True)
def connect_db():
    """
      This fixture loads MongoDB connection before
      a module is going to be tested.
    """
    connect(
        'mongoenginetest',
        is_mock=True,
        uuidRepresentation='pythonLegacy'
    )


@fixture(scope='module')
def mock_user(connect_db: fixture) -> User:
    """
      Mocks a user and save it in mocked database.

      Args:
        - connect_db: fixture = MongoDB connection fixture.

      Return:
        - mocked_user: User = Mocked user saved in mocked database.
    """

    mocked_user = User(
        uuid=uuid.uuid4(),
        first_name='John',
        last_name='Doe',
        email='johndoe@email.com',
        password='johndoe123'
    )
    mocked_user.save()
    return mocked_user


@fixture(scope='module')
def mock_card(connect_db: fixture, mock_user: User) -> Card:
    """
      Mocks a card and save it in mocked database.

      Args:
        - connect_db: fixture = MongoDB connection fixture.
        - mocked_user: User = Mocked user saved in mocked database
          who is owner of mocked_card.

      Return:
        - mocked_card: Card = Mocked card saved in mocked database.
    """

    mocked_card = Card(
        uuid=uuid.uuid4(),
        title='Mocked card',
        amount=150.0
    )
    mocked_card.save()
    mock_user.add_card(mocked_card)

    return mocked_card

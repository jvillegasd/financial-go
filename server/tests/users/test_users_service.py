import uuid
from modules.users import service
from modules.users.models import User
from modules.users.serializers import UserSchema


def test_get_existing_user_by_email(mock_user: User):
    """
      Test getting existing user instance by email.

      Args:
        - mock_user: User = Mocked user fixture.
    """

    user = service.get_user_by_email(mock_user.email)

    assert user is not None
    assert isinstance(user, User)
    assert user.first_name == mock_user.first_name
    assert user.last_name == mock_user.last_name


def test_get_non_existing_user_by_email():
    """
      Test getting non existing user instance by email.
      If user not exists, None have to be returned.
    """

    non_existing_email = 'some@email.com'
    non_existing_user = service.get_user_by_email(non_existing_email)

    assert non_existing_user is None


def test_get_existing_user_by_id(mock_user: User):
    """
      Test getting existing user instance by id.

      Args:
        - mock_user: User = Mocked user fixture.
    """

    user = service.get_user_by_id(str(mock_user.uuid))

    assert user is not None
    assert isinstance(user, User)
    assert user.first_name == mock_user.first_name
    assert user.last_name == mock_user.last_name


def test_get_non_existing_user_by_id():
    """
      Test getting non existing user instance by id.
      If user not exists, None have to be returned.
    """

    non_existing_id = str(uuid.uuid4())
    non_existing_user = service.get_user_by_id(non_existing_id)

    assert non_existing_user is None


def test_create_user():
    """Test creating a new user."""

    user_info = {
        'first_name': 'Testing',
        'last_name': 'this feature',
        'email': 'email@email.com',
        'password': 'testingthis123'
    }
    params = UserSchema().load(user_info)
    new_user = service.create_user(params)
    
    assert isinstance(new_user, User)
    assert new_user.first_name == params['first_name']
    assert new_user.last_name == params['last_name']
    assert new_user.email == params['email']
    assert new_user.check_password(params['password'])
    
    user = User.objects.filter(uuid=new_user.uuid).first()
    assert user is not None

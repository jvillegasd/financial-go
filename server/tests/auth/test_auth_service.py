import jwt
import pytest
from modules.auth import service
from modules.users.models import User


def test_create_auth_token(mock_user: User):
    """
      Test authorization token creation
      
      Args:
        - mock_user: User = Mocked user fixture.
    """
    
    auth_token = service.create_auth_token(mock_user)
    
    assert isinstance(auth_token, str)
    assert len(auth_token) > 0


def test_decode_auth_token(mock_user: User):
    """
      Test successful auth token decoding.
      
      Args:
        - mock_user: User = Mocked user fixture.
    """
    
    auth_token = service.create_auth_token(mock_user)
    auth_token = f'Bearer {auth_token}'
    user_info = service.decode_auth_token(auth_token)
    
    assert isinstance(user_info, dict)
    assert user_info['first_name'] == mock_user.first_name
    assert user_info['last_name'] == mock_user.last_name
    assert user_info['email'] == mock_user.email


def test_decode_malformed_auth_token(mock_user: User):
    """
      Test exception raise at malformed auth token decoding.
      
      Args:
        - mock_user: User = Mocked user fixture.
    """
    
    auth_token = service.create_auth_token(mock_user)
    malformed_auth_token = f'Bearer asdasdas {auth_token}'
    
    with pytest.raises(jwt.DecodeError):
        service.decode_auth_token(malformed_auth_token)

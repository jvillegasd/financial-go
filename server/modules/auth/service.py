import os
import jwt
import datetime
from modules.users.models import User


def create_auth_token(user: User) -> str:
    """
      Create a JWT authorization token of 30 minutes of duration.
      JWT saves the following information related to user:
        - uuid
        _ first_name
        - last_name
        - email

      Args:
        - user: User = User instance that requires JWT token.

      Return:
        - auth_token: str = JWT token with user information.
    """

    JWT_KEY = os.getenv('JWT_SECRET_KEY')
    
    expiration_date = datetime.datetime.now() + datetime.timedelta(minutes=30)
    auth_token = jwt.encode({
        'sub': str(user.uuid),
        'first_name': user.first_name,
        'last_name': user.last_name,
        'email': user.email,
        'exp': expiration_date,
        'iat': datetime.datetime.now(),
    }, JWT_KEY, algorithm='HS256')

    return auth_token

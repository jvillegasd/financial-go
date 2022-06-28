import os
import jwt
import datetime
from modules.users.models import User

def create_auth_token(db_user):
    JWT_KEY = os.getenv("SECRET_KEY")
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=1)
    auth_token = jwt.encode({
        'sub': db_user.username,
        'name': db_user.name,
        'doc_id': str(db_user.doc_id),
        'exp': expiration_date,
        'iat': datetime.datetime.now(),
    }, JWT_KEY, algorithm='HS256')

    return auth_token


def user_exists(email: str) -> bool:
    """
      Check if an user with provided email exists in database.
      
      Args:
        - email: str = Provided email used to check user existance.
      
      Return:
        - Boolean that represents if user exists or not.
    """
    return len(User.objects.filter(email=email)) > 0


def create_user(params: dict) -> User:
    """
      Creates a new user from dict and save it into database.
      
      Args:
        - params: dict = This dict contains new user info to be saved.
      
      Return:
        - new_user: User = New user Mongoengine object created by provided params.
    """
    
    new_user = User(**params)
    new_user.save()
    return new_user

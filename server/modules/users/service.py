from typing import Union
from modules.users.models import User
from modules.users.serializers import UserSchema


def get_user_by_email(email: str) -> Union[User, None]:
    """
      Fetch an user from database using email.
      
      Args:
        - email: str = Provided email used to check user existance.
      
      Return:
        - user: User = User instance fetched by email from database.
    """
    return User.objects.filter(email=email).first()


def create_user(params: UserSchema) -> User:
    """
      Creates a new user from dict and save it into database.
      
      Args:
        - params: UserSchema = This dict contains new user info to be saved.
      
      Return:
        - new_user: User = New user Mongoengine object created by provided params.
    """
    
    new_user = User(**params)
    new_user.save()
    return new_user

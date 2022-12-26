
from uuid import UUID
from typing import Optional
from src.models.user import User
from modules.users.serializers import UserSchema


class UserService:

    def get_user_by_email(self, email: str) -> Optional[User]:
        """Fetch an user from database using email.

        Args:
            - email: str = Provided email used to check user existance.

        Return:
            - user: User = User instance fetched by email from database.
        """
        return User.objects.filter(email=email).first()

    def get_user_by_id(self, user_uuid: UUID) -> Optional[User]:
        """Fetch an user from database using uuid.

        Args:
            - user_uuid: str = Provided uuid used to check user existance.

        Return:
            - user: User = User instance fetched by uuid from database.
        """
        return User.objects.filter(uuid=user_uuid).first()


    def create_user(params: UserSchema) -> User:
        """Creates a new user from dict and save it into database.

        Args:
            - params: UserSchema = This dict contains new user info to be saved.

        Return:
            - new_user: User = New user Mongoengine object created by provided params.
        """

        new_user = User(**params)
        new_user.encrypt_password()
        new_user.save()
        return new_user


from uuid import UUID
from typing import Optional
from src.models import User
from src.schemas.user import UserSchema
from src.schemas.filter import FilterSchema
from src.interfaces.unit_of_work import IUnitOfWork
from src.interfaces.repository import IUserRepository
from src.errors.user import UserNotFoundError, UserAlreadyExists


class UserService:
    def get_user_by_email(
        self,
        email: str,
        uow: IUnitOfWork
    ) -> Optional[User]:
        """Fetch an user from database using email.
        Args:
            -   email: str = Provided email used to check user existance.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - user: User = User instance fetched by email from database.
        """
        user_repo: IUserRepository = uow.get_repo(name='user')
        filters: list[FilterSchema] = [
            FilterSchema(
                field_name='email',
                operation='eq',
                value=email
            )
        ]
        user_instance = user_repo.find_one(filters)
        if user_instance is None:
            raise UserNotFoundError('There is not user using provided email')
        return user_instance

    def get_user_by_id(
        self,
        user_id: UUID,
        uow: IUnitOfWork
    ) -> Optional[User]:
        """Fetch an user from database using uuid.
        Args:
            -   user_id: UUID = Provided uuid used to check user existance.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - user: User = User instance fetched by uuid from database.
        """
        user_repo: IUserRepository = uow.get_repo(name='user')
        filters: list[FilterSchema] = [
            FilterSchema(
                field_name='doc_id',
                operation='eq',
                value=user_id
            )
        ]
        user_instance = user_repo.find_one(filters)
        if user_instance is None:
            raise UserNotFoundError('There is not user using provided email')
        return user_instance

    def create_user(
        self,
        params: UserSchema,
        uow: IUnitOfWork
    ) -> User:
        """Creates a new user from dict and save it into database.
        Args:
            -   params: UserSchema = This dict contains
            new user info to be saved.
            -   uow: IUnitOfWork = Provided Unit of Work for Database
            operations.
        Return:
            - new_user: User = New user Mongoengine object
            created by provided params.
        """
        try:
            self.get_user_by_email(
                email=params['email'],
                uow=uow
            )
            raise UserAlreadyExists('User already exists')
        except UserNotFoundError:
            pass
        new_user = User(**params)
        new_user.encrypt_password()
        user_repo: IUserRepository = uow.get_repo(name='user')
        user_repo.create(record=new_user)
        return new_user

from src.models import User
from mongoengine.queryset import QuerySet
from src.interfaces.repository import IUserRepository
from src.repositories.base.mongo import MongoRepository


class UserRepository(
    MongoRepository[User],
    IUserRepository[QuerySet]
):
    pass

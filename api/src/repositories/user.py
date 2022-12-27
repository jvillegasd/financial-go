from src.models import User
from mongoengine.queryset import QuerySet
from src.interfaces.repository import IUserRepository
from src.repositories.base.mongo import MongoEngineRepository


class UserRepository(
    MongoEngineRepository[User],
    IUserRepository[QuerySet]
):
    pass

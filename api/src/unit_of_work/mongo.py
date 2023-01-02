from src.interfaces.repository import IRepository
from src.interfaces.unit_of_work import IUnitOfWork
from src.repositories.user import UserRepository
from src.repositories.card import CardRepository
from src.repositories.transaction import TransactionRepository
from src.models.user import User
from src.models.card import Card
from src.models.transaction import Transaction
from src.errors.unit_of_work import RepositoryNotFoundError


class MongoUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.__repositories: dict[str, IRepository] = {
            'user': UserRepository(User),
            'card': CardRepository(Card),
            'transaction': TransactionRepository(Transaction)
        }

    def get_repo(self, name: str) -> IRepository:
        repository: IRepository = self.__repositories.get(name, None)
        if repository is None:
            raise RepositoryNotFoundError(
                'Repository is not stored in this unit of work'
            )
        return repository

    def commit(self):
        pass

    def rollback(self):
        pass

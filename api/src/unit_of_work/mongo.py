from src.models import User
from src.models import Card
from src.models import Transaction
from src.repositories import UserRepository
from src.repositories import CardRepository
from src.repositories import TransactionRepository
from src.interfaces.repository import IRepository
from src.interfaces.unit_of_work import IUnitOfWork
from src.errors.unit_of_work import RepositoryNotFoundError


class MongoUnitOfWork(IUnitOfWork):
    def __enter__(self):
        self.__repositories = {
            'user': UserRepository(User),
            'card': CardRepository(Card),
            'transaction': TransactionRepository(Transaction)
        }
        return self

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

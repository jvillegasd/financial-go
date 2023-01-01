from abc import ABC, abstractmethod
from src.interfaces.repository import IRepository


class IUnitOfWork(ABC):
    def __init__(self):
        self.__repositories: dict[str, IRepository] = {}

    def __enter__(self) -> 'IUnitOfWork':
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def get_repo(self, name: str) -> IRepository:
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError

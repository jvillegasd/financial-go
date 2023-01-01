from abc import ABC, abstractmethod
from src.interfaces.repository import IRepository


class IUnitOfWork(ABC):
    def __init__(self):
        """Init unit of work with stored repository. Those repository
        can be used in the whole UoW execution.
        Repositories are saved in a private dict in order to mantain them
        hidden from client.
        """
        self.__repositories: dict[str, IRepository] = {}

    def __enter__(self) -> 'IUnitOfWork':
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def get_repo(self, name: str) -> IRepository:
        """Return the repository stored in our private dict variable. If
        there is not a repository called by the provided name, an exception
        is raised.
        Args:
            -   name: str = Name of the requested repository.
        Returns:
            -   IRepository = Requested repository.
        """
        raise NotImplementedError

    @abstractmethod
    def commit(self):
        """Makes a commit of operations for the implemented database."""
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        """Makes a rollback for the implemented database."""
        raise NotImplementedError

import os
import json
from abc import ABC, abstractmethod
from src.constants import ROOT_PATH


class IDataImporter(ABC):
    def __init__(self):
        self.pwd: str = ROOT_PATH
        self.seeds: dict[str, dict] = self._load_seeds()
        self.import_order: list[str] = self._load_import_order()

    @abstractmethod
    def _load_seeds(self) -> dict[str, dict]:
        """This method loads seeds JSON files stored in their
        folder for in-memory consulting.
        Returns:
            -   dict[str, dict] = A dict with the seeds
            stored in the specified folder. Where their keys represents
            model's name and their value the seeds.
        """

        seeds: dict[str, dict] = {}
        seeds_dir = os.path.abspath(os.path.join(self.pwd, 'seeds'))
        seeds_files = os.listdir(seeds_dir)
        for file_name in seeds_files:
            file = os.path.abspath(os.path.join(seeds_dir, file_name))
            with open(file, 'r') as f:
                seed_dict = json.load(f)
                seeds[seed_dict['model_name']] = seed_dict
        return seeds

    @abstractmethod
    def _load_import_order(self) -> list[str]:
        """This method loads the import order list stored
        in JSON file and it's used for loads all models in the right
        order.
        Returns:
            -   list[str] = List of model names.
        """

        import_order: dict = {}
        order_dir = os.path.abspath(
            os.path.join(self.pwd, 'import_order.json')
        )
        with open(order_dir, 'r') as f:
            import_order = json.load(f)
        return import_order

    @abstractmethod
    def load_model(self, model_name: str) -> list:
        """Loads seeds to database for the provided
        model name.
        Args:
            -   model_name: str
        Returns:
            -   list = A list with the seeds of the model.
        """
        raise NotImplementedError

    @abstractmethod
    def load_all_models(self):
        """This method load all tables of models that
        have created seeds.
        """
        raise NotImplementedError

    @abstractmethod
    def clear_model(self, model_name: str):
        """This method clean records from database
        related to provided model name.
        Args:
            -   model_name: str
        """
        raise NotImplementedError

    @abstractmethod
    def clear_all_models(self):
        """This method clean all tables of loaded
        models.
        """
        raise NotImplementedError

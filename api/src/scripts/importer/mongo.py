from importlib import import_module
from src.interfaces.importer import IDataImporter
from src.interfaces.unit_of_work import IUnitOfWork
from src.unit_of_work.mongo import MongoUnitOfWork


class MongoDataImporter(IDataImporter):
    def __init__(self):
        super().__init__()
        self.uow: IUnitOfWork = MongoUnitOfWork()

    def load_model(self, model_name: str) -> list:
        data = self.seeds[model_name]
        with self.uow:
            module_name, class_name = data['model'].rsplit('.', 1)
            module = import_module(module_name)
            model = getattr(module, class_name)
            repo = self.uow.get_repo(name=model_name)
            for seed in data['records']:
                record = model(**seed)
                if model_name == 'user':
                    record.encrypt_password()
                repo.create(record)
        return data['records']

    def clear_model(self, model_name: str):
        with self.uow:
            repo = self.uow.get_repo(name=model_name)
            repo.delete_all()

from src.models.base import BaseDocument


class BaseRepository:

    def __init__(self, model: BaseDocument):
        self.model = model

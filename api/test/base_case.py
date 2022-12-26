import unittest
from src import create_app
from src.connection.database import DataAccessLayer


class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._import_api()
        cls.dal = DataAccessLayer()

    @classmethod
    def tearDownClass(cls):
        pass

    @classmethod
    def _import_api(cls):
        cls.app = create_app(config_name='test')
        cls.client = cls.app.test_client()
        cls.headers = {
            'Content-Type': 'application/json'
        }

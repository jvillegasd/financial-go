import os
import mongoengine
from pymongo import MongoClient


class DataAccessLayer:

    def __init__(self):
        database_host: str = (
            f'mongodb://{os.getenv("MONGO_HOST")}:'
            f'{os.getenv("MONGO_PORT")}'
        )
        self.client: MongoClient = mongoengine.connect(
            os.getenv('MONGO_INITDB_DATABASE'),
            username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
            password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
            host=database_host,
            port=int(os.getenv('MONGO_PORT')),
            authentication_source='admin',
            uuidRepresentation='pythonLegacy'
        )

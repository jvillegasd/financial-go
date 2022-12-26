import os
import mongoengine
from typing import Iterator
from pymongo import MongoClient
from contextlib import contextmanager
from pymongo.client_session import ClientSession


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

    @contextmanager
    def get_session(self) -> Iterator[ClientSession]:
        """This generator yields a new session and closes
        it when it finished.

        Returns:
            -   Iterator[ClientSession]
        """

        session: ClientSession = self.client.start_session()
        try:
            yield session
        except Exception as e:
            session.abort_transaction()
            raise e
        finally:
            session.end_session()

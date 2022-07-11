import os
from mongoengine import connect


def connect_to_db():
    """ Connect to MongoDB database using mongoengine ORM """
    connect(
        os.getenv('MONGO_INITDB_DATABASE'),
        username=os.getenv('MONGO_INITDB_ROOT_USERNAME'),
        password=os.getenv('MONGO_INITDB_ROOT_PASSWORD'),
        host=f'mongodb://{os.getenv("MONGO_HOST")}:{os.getenv("MONGO_PORT")}',
        port=int(os.getenv('MONGO_PORT')),
        authentication_source='admin',
        uuidRepresentation='pythonLegacy'
    )

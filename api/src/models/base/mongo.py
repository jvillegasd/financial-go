import uuid
import datetime
from mongoengine import Document
from mongoengine.fields import (
    UUIDField,
    DateTimeField
)


class BaseDocument(Document):
    """ Model mixin that contains common fields and functions. """
    meta = {'abstract': True}

    uuid = UUIDField(
        binary=False,
        default=uuid.uuid4,
        primary_key=True
    )
    created_at = DateTimeField(default=datetime.datetime.utcnow)
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, *args, **kwargs):
        """Overrides mongoengine save function to change
        date of update_at field.
        """
        self.updated_at = datetime.datetime.utcnow()
        super().save(*args, **kwargs)

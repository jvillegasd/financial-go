import uuid
import datetime
import mongoengine


class DocumentMixin(mongoengine.Document):
    """ Model mixin that contains common fields and functions. """
    
    uuid = mongoengine.fields.UUIDField(binary=False, default=uuid.uuid4, primary_key=True)
    created_at = mongoengine.fields.DateTimeField(default=datetime.datetime.utcnow)
    updated_at = mongoengine.fields.DateTimeField(default=datetime.datetime.utcnow)

    meta = {'abstract': True}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def save(self, *args, **kwargs):
        """ Overrides mongoengine save function to change date of update_at field. """
        self.updated_at = datetime.datetime.utcnow()
        super().save(*args, **kwargs)

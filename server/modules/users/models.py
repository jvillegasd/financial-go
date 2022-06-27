import uuid
import datetime
import mongoengine


class User(mongoengine.Document):
    uuid = mongoengine.fields.UUIDField(binary=True, default=uuid.uuid4, primary_key=True)
    first_name = mongoengine.fields.StringField(required=True)
    last_name = mongoengine.fields.StringField(required=True)
    email = mongoengine.fields.EmailField(required=True)
    password = mongoengine.fields.StringField(required=True)
    created_at = mongoengine.fields.DateTimeField(default=datetime.datetime.now)
    updated_at = mongoengine.fields.DateTimeField()

    def save(self, *args, **kwargs) -> 'User':
        self.updated_at = datetime.datetime.now()
        return super(User, self).save(*args, **kwargs)

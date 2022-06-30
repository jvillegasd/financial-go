import bcrypt
import mongoengine
from modules.mixin import DocumentMixin
from modules.users.utils import PasswordField
from modules.cards.models import Card


class User(DocumentMixin):
    first_name = mongoengine.fields.StringField(required=True)
    last_name = mongoengine.fields.StringField(required=True)
    email = mongoengine.fields.EmailField(required=True)
    password = PasswordField(required=True)
    cards = mongoengine.fields.ListField(
        mongoengine.fields.ReferenceField(Card, reverse_delete_rule=mongoengine.PULL))

    def check_password(self, value: str) -> bool:
        return bcrypt.checkpw(value.encode('utf-8'),
                              self.password.encode('utf-8'))

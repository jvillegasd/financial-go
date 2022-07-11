import bcrypt
import mongoengine
from modules.cards.models import Card
from modules.mixin import DocumentMixin


class User(DocumentMixin):
    first_name = mongoengine.fields.StringField(required=True)
    last_name = mongoengine.fields.StringField(required=True)
    email = mongoengine.fields.EmailField(required=True)
    password = mongoengine.fields.StringField(required=True)
    cards = mongoengine.fields.ListField(
        mongoengine.fields.ReferenceField(Card, reverse_delete_rule=mongoengine.PULL))

    def check_password(self, value: str) -> bool:
        return bcrypt.checkpw(value.encode('utf-8'),
                              self.password.encode('utf-8'))

    def add_card(self, new_card: Card):
        """
          Save a reference of Card to current user.

          Args:
            - new_card: Card = Card to be referenced to user.
        """

        new_card.owner_uuid = self.uuid
        self.cards.append(new_card)

        new_card.save()
        self.save()

    def encrypt_password(self):
        """
          Encrypt raw password by hashing it using a fixed Salt rounds.
        """

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf8'), salt)
        self.password = hashed_password.decode('utf8')
        self.save()

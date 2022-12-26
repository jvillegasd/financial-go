import bcrypt
from mongoengine import PULL
from models.card import Card
from mongoengine.fields import (
    StringField,
    EmailField,
    ListField,
    ReferenceField
)
from models.base import BaseDocument


class User(BaseDocument):
    first_name = StringField(required=True)
    last_name = StringField(required=True)
    email = EmailField(required=True)
    password = StringField(required=True)
    cards = ListField(
        ReferenceField(
            Card,
            reverse_delete_rule=PULL
        )
    )

    def check_password(self, value: str) -> bool:
        """Check if tentative password matchs with
          current user password.

          Args:
            - value: str = Raw password to check.

          Return:
            - Boolean = A boolean that represents if tentative
            password matches with hashed password.
        """
        return bcrypt.checkpw(value.encode('utf-8'),
                              self.password.encode('utf-8'))

    def add_card(self, new_card: Card):
        """Save a reference of Card to current user.
          Args:
            - new_card: Card = Card to be referenced to user.
        """

        new_card.owner_uuid = self.uuid
        self.cards.append(new_card)
        new_card.save()
        self.save()

    def encrypt_password(self):
        """Encrypt raw password by hashing it using a
        fixed Salt rounds.
        """

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(self.password.encode('utf8'), salt)
        self.password = hashed_password.decode('utf8')
        self.save()

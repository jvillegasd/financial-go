import bcrypt
import mongoengine
from modules.cards.models import Card
from modules.mixin import DocumentMixin
from modules.users.utils import PasswordField


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

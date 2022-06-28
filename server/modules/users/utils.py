import bcrypt
import mongoengine


class PasswordField(mongoengine.StringField):
    """ Custom Mongoengine password field implementation """

    def __init__(self, regex=None, **kwargs):
        self.salt = bcrypt.gensalt()
        super(PasswordField, self).__init__(**kwargs)

    def __set_password(self, password: str) -> str:
        """
          Encrypt raw password by hashing it using a fixed Salt rounds.
          
          Args:
            - password: str = Raw password to be hashed.
          
          Return:
            - hashed_password: str = Hashed password in string representation
        """
        
        hashed_password = bcrypt.hashpw(password.encode('utf8'), self.salt)
        return hashed_password.decode('utf8')

    def to_mongo(self, value: str) -> str:
        """
          Encrypt password before saved in MongoDB, this function is
          called by Mongoengine.

          Args:
            - value: str = Raw password to be hashed.
          
          Return:
            - Hashed password as string representation.
        """
        return self.__set_password(value)

    def to_python(self, value: str) -> str:
        """
          Return password value, this function is called by Mongoengine.
          
          Args:
            - value: str = Hashed password.
          
          Return:
            - Hashed password as string representation.
        """
        return value

    def to_dict(self, value: str) -> dict:
        """
          Return password value as dict representation.
          
          Args:
            - value: str = Hashed password.
          
          Return:
            - Hashed password as dict representation.
        """
        return {'password': value}

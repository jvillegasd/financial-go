import os
import jwt
import datetime
from src.models import User

JWT_KEY: str = os.getenv('JWT_SECRET_KEY')


class AuthService:
    def create_auth_token(self, user: User) -> str:
        """Create a JWT authorization token of 30 minutes of duration.
        JWT saves the following information related to user:
            - uuid
            _ first_name
            - last_name
            - email
        Args:
            - user: User = User instance that requires JWT token.
        Return:
            - auth_token: str = JWT token with user information.
        """

        expiration_date = (
            datetime.datetime.now()
            + datetime.timedelta(minutes=30)
        )
        auth_token = jwt.encode({
            'sub': str(user.doc_id),
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'exp': expiration_date,
            'iat': datetime.datetime.now(),
        }, JWT_KEY, algorithm='HS256')
        return auth_token

    def decode_auth_token(self, auth_token: str) -> dict:
        """Decode a JWT authorization token and extract user information
        saved on it.
        Args:
            - auth_token: str = JWT authorization token.
        Return:
            - user_info: dict = User information saved in JWT token.
        """

        decoded_token = jwt.decode(
            auth_token.replace('Bearer ', ''),
            JWT_KEY,
            algorithms='HS256'
        )
        user_info = {
            'doc_id': decoded_token['sub'],
            'first_name': decoded_token['first_name'],
            'last_name': decoded_token['last_name'],
            'email': decoded_token['email'],
        }
        return user_info

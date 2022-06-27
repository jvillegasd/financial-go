import os
import jwt
import datetime
import mongoengine

def create_auth_token(db_user):
    JWT_KEY = os.getenv("SECRET_KEY")
    expiration_date = datetime.datetime.now() + datetime.timedelta(days=1)
    auth_token = jwt.encode({
        'sub': db_user.username,
        'name': db_user.name,
        'doc_id': str(db_user.doc_id),
        'exp': expiration_date,
        'iat': datetime.datetime.now(),
    }, JWT_KEY, algorithm='HS256')

    return auth_token


def check_user_existance(username, email):
    from modules.users.models import User

    query = mongoengine.Q(username=username) | mongoengine.Q(email=email)
    db_users = User.objects.filter(query)
    return True if db_users else False

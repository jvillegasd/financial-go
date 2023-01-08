from src.models import User
from src.schemas.user import UserSchema
from src.schemas.auth import AuthSchema
from src.services.auth import AuthService
from src.services.user import UserService
from src.middlewares.schemas import validate_body
from flask import request, Blueprint, abort
from src.errors.user import UserNotFoundError, UserBadCredentials
from src.unit_of_work.mongo import MongoUnitOfWork
from src.interfaces.unit_of_work import IUnitOfWork

auth_api = Blueprint('Authorization', __name__)
auth_service = AuthService()
user_service = UserService()
uow: IUnitOfWork = MongoUnitOfWork()


@auth_api.post('/')
@validate_body(schema=UserSchema(only=('email', 'password',)))
def create_auth_token():
    body = request.get_json()
    try:
        with uow:
            user: User = user_service.get_user_by_email(
                body['email'],
                uow
            )
            if not user.check_password(body['password']):
                raise UserBadCredentials
            auth_token = auth_service.create_auth_token(user)
        return AuthSchema().dump({
            'token': f'Bearer {auth_token}',
            'user': user
        })
    except UserNotFoundError:
        abort(404, 'User not found')
    except UserBadCredentials:
        abort(400, 'Email or password is wrong')

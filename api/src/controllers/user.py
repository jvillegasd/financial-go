from src.schemas.user import UserSchema
from src.services.user import UserService
from src.services.auth import AuthService
from middlewares.auth import jwt_required
from middlewares.schemas import validate_body
from flask import request, Blueprint, abort
from src.unit_of_work.mongo import MongoUnitOfWork
from src.errors.user import UserAlreadyExists, UserNotFoundError

user_api = Blueprint('User', __name__)
auth_service = AuthService()
user_service = UserService()
uow = MongoUnitOfWork()


@user_api.post('/')
@validate_body(schema=UserSchema(
    exclude=('doc_id', 'created_at', 'updated_at')
))
def create():
    body = request.get_json()
    try:
        with uow:
            new_user = user_service.create_user(
                params=UserSchema(**body),
                uow=uow
            )
        return UserSchema().dump(new_user)
    except UserAlreadyExists:
        abort(400, 'User with same email exists.')
    except UserNotFoundError as e:
        abort(404, str(e))


@user_api.get('/')
@jwt_required
def read():
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            user = user_service.get_user_by_email(
                email=user_info['email'],
                uow=uow
            )
        return UserSchema(exclude=('password',)).dump(user)
    except UserNotFoundError as e:
        abort(404, str(e))

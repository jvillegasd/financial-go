import modules.users.service as service
import modules.auth.service as auth_service
import modules.users.serializers as serializers

from middlewares.auth import jwt_required
from middlewares.schemas import parameters
from flask import request, Blueprint, abort


user_blueprint = Blueprint('User module', __name__)


@user_blueprint.post('/')
@parameters(schema=serializers.UserSchema())
def create():
    body = request.get_json()

    if not service.get_user_by_email(body['email']):
        new_user = service.create_user(body)
        return serializers.UserSchema().dump(new_user)
    else:
        abort(400, 'User with same email exists.')


@user_blueprint.get('/')
@jwt_required
def read():
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    user = service.get_user_by_email(user_info['email'])

    return serializers.UserSchema(exclude=('password',)).dump(user)

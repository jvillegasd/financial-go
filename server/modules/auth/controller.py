import modules.users.serializers as user_serializers
import modules.users.service as user_service
import modules.auth.service as service
from flask import request, Blueprint, abort
from middlewares.schemas import parameters


auth_blueprint = Blueprint('Auth module', __name__)


@auth_blueprint.post('/')
@parameters(schema=user_serializers.UserSchema(only=('email', 'password',)))
def create_auth_token():
    body = request.get_json()

    user = user_service.get_user_by_email(body['email'])
    if user and user.check_password(body['password']):
        auth_token = service.create_auth_token(user)
        return {'token': f'Bearer {auth_token}'}
    else:
        abort(404, 'Invalid email or password.')

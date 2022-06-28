import modules.users.service as service
import modules.users.serializers as serializers
from flask import request, Blueprint, abort
from middlewares.schemas import parameters


user_blueprint = Blueprint('User module', __name__)


@user_blueprint.post('/')
@parameters(schema=serializers.UserSchema())
def create():
    body = request.get_json()

    if not service.get_user_by_email(body['email']):
        new_user = service.create_user(body)
        response = serializers.UserSchema().dump(new_user)
        return response
    else:
        abort(400, 'User with same email exists.')

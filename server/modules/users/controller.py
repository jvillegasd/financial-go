from flask import request, Blueprint, abort
import modules.users.service as service


user_blueprint = Blueprint('User module', __name__)

@user_blueprint.post('/')
def create():
    body = request.get_json()
    
    if not service.user_exists(body['email']):
        new_user = service.create_user(body)
        return {'message': 'done'}
    else:
        abort(400, 'User with same email exists.')

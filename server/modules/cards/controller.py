
import modules.cards.serializers as serializers
import modules.cards.service as service
import modules.auth.service as auth_service
from flask import request, Blueprint, abort
from middlewares.auth import jwt_required
from middlewares.schemas import parameters


cards_blueprint = Blueprint('Cards module', __name__)


@cards_blueprint.post('/')
@jwt_required
@parameters(schema=serializers.CardSchema(only=('title', 'amount',)))
def create():
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    if service.user_can_create_card(user_info.get('uuid')):
        new_card = service.create_card(body)
        service.add_card_to_user(new_card, user_info.get('uuid'))
        return serializers.CardSchema().dump(new_card)
    else:
        abort(400, 'Created cards limit exceeded.')

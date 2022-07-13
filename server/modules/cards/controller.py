import modules.cards.service as service
import modules.auth.service as auth_service
import modules.cards.serializers as serializers

from middlewares.auth import jwt_required
from middlewares.schemas import parameters
from flask import request, Blueprint, abort


cards_blueprint = Blueprint('Cards module', __name__)


@cards_blueprint.post('/')
@jwt_required
@parameters(schema=serializers.CardSchema(
    only=(
        'title',
        'amount',
    )
))
def create():
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    if service.user_can_create_card(user_info.get('uuid')):
        new_card = service.create_card(body, user_info.get('uuid'))
        return serializers.CardSchema().dump(new_card)
    else:
        abort(403, 'Created cards limit exceeded.')


@cards_blueprint.patch('/<card_uuid>')
@jwt_required
@parameters(schema=serializers.CardSchema(
    only=(
        'title',
        'amount',
    )
))
def update(card_uuid: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    card = service.update_card(body, card_uuid, user_info.get('uuid'))
    if card:
        return serializers.CardSchema().dump(card)
    else:
        abort(404, 'User does not have provided card.')


@cards_blueprint.delete('/<card_uuid>')
@jwt_required
def delete(card_uuid: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    service.delete_card(card_uuid, user_info.get('uuid'))
    return {'message': 'Card deleted successfully.'}

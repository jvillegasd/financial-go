import modules.auth.service as auth_service
import modules.transactions.service as service
import modules.transactions.serializers as serializers

from middlewares.auth import jwt_required
from middlewares.schemas import parameters
from flask import request, Blueprint, abort


transaction_blueprint = Blueprint('Transaction module', __name__)


@transaction_blueprint.post('/card/<card_uuid>')
@jwt_required
@parameters(schema=serializers.TransactionSchema(
    only=(
        'title',
        'type',
        'amount',
        'category',
    )
))
def create(card_uuid: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    new_transaction = service.create_transaction(card_uuid,
                                                user_info.get('uuid'),
                                                body)

    return serializers.TransactionSchema().dump(new_transaction)


@transaction_blueprint.get('/<transaction_uuid>')
@jwt_required
def read(transaction_uuid: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    transaction = service.get_transaction_by_id(transaction_uuid,
                                                user_info.get('uuid'))
    return serializers.TransactionSchema().dump(transaction)


@transaction_blueprint.patch('/<transaction_uuid>')
@jwt_required
@parameters(schema=serializers.TransactionSchema(
    only=(
        'title',
        'type',
        'amount',
        'category'
    )
))
def update(transaction_uuid: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)

    transaction = service.update_transaction(body,
                                            transaction_uuid,
                                            user_info.get('uuid'))
    return serializers.TransactionSchema().dump(transaction)


@transaction_blueprint.delete('/<transaction_uuid>')
@jwt_required
def delete(transaction_uuid: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    service.delete_transaction(transaction_uuid, user_info.get('uuid'))
    return {'message': 'Transaction deleted successfully.'}

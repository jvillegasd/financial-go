from src.schemas.card import CardSchema
from src.schemas.transaction import TransactionSchema
from src.services.card import CardService
from src.services.auth import AuthService
from src.services.transaction import TransactionService
from src.middlewares.auth import jwt_required
from src.middlewares.schemas import validate_body
from flask import request, Blueprint, abort
from src.unit_of_work.mongo import MongoUnitOfWork
from src.interfaces.unit_of_work import IUnitOfWork
from src.errors.transaction import TransactionNotFound
from src.errors.card import CardLimitExceeded, CardNotFound

card_api = Blueprint('Card', __name__)
card_service = CardService()
auth_service = AuthService()
transaction_service = TransactionService()
uow: IUnitOfWork = MongoUnitOfWork()


@card_api.post('/')
@jwt_required
@validate_body(schema=CardSchema(
    only=(
        'title',
        'amount',
    )
))
def create_card():
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            new_card = card_service.create_card(
                card_info=CardSchema.load(body),
                user_id=user_info.get('uuid'),
                uow=uow
            )
        return CardSchema().dump(new_card)
    except CardLimitExceeded as e:
        abort(403, str(e))


@card_api.patch('/<card_id>')
@jwt_required
@validate_body(schema=CardSchema(
    only=(
        'title',
        'amount',
    )
))
def update_card(card_id: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card = card_service.update_card(
                card_info=CardSchema.load(body),
                card_id=card_id,
                owner_id=user_info.get('uuid'),
                uow=uow
            )
        return CardSchema().dump(card)
    except CardNotFound as e:
        abort(404, str(e))


@card_api.delete('/<card_id>')
@jwt_required
def delete_card(card_id: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card_service.delete_card(
                card_id=card_id,
                owner_id=user_info.get('uuid'),
                uow=uow
            )
        return {'message': 'Card deleted successfully.'}
    except CardNotFound as e:
        abort(404, str(e))


@card_api.post('/<card_id>/transaction')
@jwt_required
@validate_body(schema=TransactionSchema(
    only=(
        'title',
        'type',
        'amount',
        'category',
    )
))
def create_transaction(card_id: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card = card_service.get_card_by_id(
                card_id=card_id,
                owner_id=user_info['uuid'],
                uow=uow
            )
            new_transaction = transaction_service.create_transaction(
                card_id=card.doc_id,
                transaction_info=TransactionSchema.load(body),
                uow=uow
            )
        return TransactionSchema().dump(new_transaction)
    except CardNotFound as e:
        abort(404, str(e))


@card_api.get('/<card_id>/transaction/<transaction_id>')
@jwt_required
def read_transaction(card_id: str, transaction_id: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card = card_service.get_card_by_id(
                card_id=card_id,
                owner_id=user_info['uuid'],
                uow=uow
            )
            transaction = transaction_service.get_transaction_by_id(
                card_id=card.doc_id,
                transaction_id=transaction_id,
                uow=uow
            )
        return TransactionSchema().dump(transaction)
    except CardNotFound as e:
        abort(404, str(e))
    except TransactionNotFound as e:
        abort(404, str(e))


@card_api.patch('/<card_id>/transaction/<transaction_id>')
@jwt_required
@validate_body(schema=TransactionSchema(
    only=(
        'title',
        'type',
        'amount',
        'category'
    )
))
def update_transaction(card_id: str, transaction_id: str):
    body = request.get_json()
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card = card_service.get_card_by_id(
                card_id=card_id,
                owner_id=user_info['uuid'],
                uow=uow
            )
            transaction = transaction_service.update_transaction(
                transaction_info=TransactionSchema.load(body),
                card_id=card.doc_id,
                transaction_id=transaction_id,
                uow=uow
            )
        return TransactionSchema().dump(transaction)
    except CardNotFound as e:
        abort(404, str(e))
    except TransactionNotFound as e:
        abort(404, str(e))


@card_api.delete('/<card_id>/transaction/<transaction_id>')
@jwt_required
def delete_transaction(card_id: str, transaction_id: str):
    auth_token = request.headers.get('Authorization')
    user_info = auth_service.decode_auth_token(auth_token)
    try:
        with uow:
            card = card_service.get_card_by_id(
                card_id=card_id,
                owner_id=user_info['uuid'],
                uow=uow
            )
            transaction_service.delete_transaction(
                card_id=card.doc_id,
                transaction_id=transaction_id,
                uow=uow
            )
        return {'message': 'Transaction deleted successfully.'}
    except CardNotFound as e:
        abort(404, str(e))
    except TransactionNotFound as e:
        abort(404, str(e))

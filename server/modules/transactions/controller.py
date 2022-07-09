import modules.transactions.serializers as serializers
import modules.transactions.service as service
import modules.auth.service as auth_service
from flask import request, Blueprint, abort
from middlewares.auth import jwt_required
from middlewares.schemas import parameters


transaction_blueprint = Blueprint('Transaction module', __name__)


@transaction_blueprint.post('/')
@jwt_required
def create():
    pass
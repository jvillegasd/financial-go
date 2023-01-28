from marshmallow import fields, validate
from src.schemas.base.library import MarshmallowSchema
from src.constants import TRANSACTION_TYPES, TRANSACTION_CATEGORIES


class TransactionSchema(MarshmallowSchema):
    card_id = fields.UUID()
    title = fields.String(required=True)
    type = fields.String(validate=validate.OneOf(TRANSACTION_TYPES))
    amount = fields.Float()
    category = fields.String(validate=validate.OneOf(TRANSACTION_CATEGORIES))

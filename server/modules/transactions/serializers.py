from marshmallow import Schema, fields, validate
from modules.constants import TRANSACTION_TYPES, TRANSACTION_CATEGORIES


class TransactionSchema(Schema):
    uuid = fields.UUID()
    card_uuid = fields.UUID()
    title = fields.String(required=True)
    type = fields.String(validate=validate.OneOf(TRANSACTION_TYPES))
    amount = fields.Float()
    category = fields.String(validate=validate.OneOf(TRANSACTION_CATEGORIES))
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

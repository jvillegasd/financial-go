from marshmallow import Schema, fields


class CardSchema(Schema):
    uuid = fields.UUID()
    owner_uuid = fields.UUID()
    title = fields.String(required=True)
    amount = fields.Float()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

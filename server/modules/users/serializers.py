from marshmallow import Schema, fields


class UserSchema(Schema):
    uuid = fields.UUID()
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    cards = fields.List(fields.Nested('CardSchema'))
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

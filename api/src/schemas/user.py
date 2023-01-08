from marshmallow import fields
from src.schemas.base.library import MarshmallowSchema


class UserSchema(MarshmallowSchema):
    first_name = fields.String(required=True)
    last_name = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
    cards = fields.List(fields.Nested('CardSchema'))

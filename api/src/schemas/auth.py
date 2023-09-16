from marshmallow import fields, Schema


class AuthSchema(Schema):
    token = fields.String()
    user = fields.Nested('UserSchema', exclude=('password',))

from marshmallow import Schema, fields


class MarshmallowSchema(Schema):
    doc_id = fields.UUID()
    created_at = fields.DateTime()
    updated_at = fields.DateTime()

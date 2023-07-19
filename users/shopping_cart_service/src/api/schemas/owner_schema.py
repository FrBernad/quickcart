from marshmallow import Schema, fields

class OwnerSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)
    url = fields.Str(required=True)

owner_schema = OwnerSchema()

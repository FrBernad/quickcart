from marshmallow import Schema, fields


class TagSchema(Schema):
    name = fields.String(required=True)


tag_schema = TagSchema()
tags_schema = TagSchema(many=True)

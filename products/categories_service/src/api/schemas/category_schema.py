from marshmallow import Schema, fields


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

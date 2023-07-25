from marshmallow import Schema, fields


class OwnerSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class TagSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)


class ProductsSchema(Schema):
    id = fields.Int(required=True)
    category = fields.Nested(CategorySchema, required=True)
    name = fields.Str(required=True)
    tags = fields.Nested(TagSchema, many=True, required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    score = fields.Float(required=True)
    owner = fields.Nested(OwnerSchema, required=True)


product_schema = ProductsSchema()
products_schema = ProductsSchema(many=True)

from marshmallow import Schema, fields

class ShoppingCartSchema(Schema):
    id = fields.Int(required=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)

shopping_cart_schema = ShoppingCartSchema()
shopping_carts_schema = ShoppingCartSchema(many=True)
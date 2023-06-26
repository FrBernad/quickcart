from marshmallow import Schema, fields

class ShoppingCartSchema(Schema):
    user_id = fields.Int(required=True)
    product_id = fields.Int(required=True)

shopping_cart_schema = ShoppingCartSchema()
shopping_carts_schema = ShoppingCartSchema(many=True)
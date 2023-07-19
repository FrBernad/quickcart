from marshmallow import Schema, fields

from src.api.schemas.owner_schema import OwnerSchema
class ShoppingCartProduct(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    category = fields.Str(required=True)
    name = fields.String(required=True)
    tags = fields.List(fields.Str(required=True), required=True)
    price = fields.Float(required=True)
    stock = fields.Int(required=True)
    owner = fields.Nested(OwnerSchema)


shopping_cart_product_schema = ShoppingCartProduct()
shopping_cart_products_schema = ShoppingCartProduct(many=True)

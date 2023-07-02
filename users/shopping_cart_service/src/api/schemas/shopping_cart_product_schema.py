from marshmallow import Schema, fields


class ShoppingCartProduct(Schema):
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)


shopping_cart_product_schema = ShoppingCartProduct()
shopping_cart_products_schema = ShoppingCartProduct(many=True)

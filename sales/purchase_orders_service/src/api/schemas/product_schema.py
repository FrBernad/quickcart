from marshmallow import Schema, fields


class ProductsSchema(Schema):
    product_id = fields.Int(required=True)
    product_price = fields.Double(required=True)
    product_quantity = fields.Int(required=True)

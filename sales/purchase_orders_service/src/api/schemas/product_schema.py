from marshmallow import Schema, fields


class ProductsSchema(Schema):
    product_id = fields.Int(required=True)
    product_price = fields.Float(required=True)
    product_quantity = fields.Int(required=True)
    product_name = fields.String(required=True)

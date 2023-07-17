from marshmallow import Schema, fields

from src.api.schemas.product_schema import ProductsSchema


class PurchaseOrderDetailsSchema(Schema):
    purchase_order_id = fields.Int(required=True)
    creation_date = fields.DateTime(required=True)
    comments = fields.String(required=False)
    user_id = fields.Int(required=True)
    total_price = fields.Double(required=True)
    # FIXME: payment_method = db.Column(EnumType(PaymentMethod), nullable=False)
    card_number = fields.String(required=False)
    expiration_year = fields.Int(required=True)
    expiration_month = fields.Int(required=True)
    cvv = fields.Int(required=True)
    # FIXME: card_type = db.Column(EnumType(CardType), nullable=False)
    products = fields.Nested(ProductsSchema, many=True)


purchase_order_schema = PurchaseOrderDetailsSchema()
purchase_orders_schema = PurchaseOrderDetailsSchema(many=True)

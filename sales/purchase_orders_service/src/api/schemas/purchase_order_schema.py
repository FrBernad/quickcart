from marshmallow import Schema, fields
from src.api.schemas.product_schema import ProductsSchema
from src.api.models.payment_method import PaymentMethod
from src.api.models.card_type import CardType
from marshmallow_enum import EnumField


class PurchaseOrderDetailsSchema(Schema):
    purchase_order_id = fields.Int(required=True)
    creation_date = fields.DateTime(required=True)
    comments = fields.String(required=False)
    user_id = fields.Int(required=True)
    total_price = fields.Float(required=True)
    payment_method = EnumField(PaymentMethod, required=True)
    card_number = fields.String(required=False)
    expiration_year = fields.Int(required=True)
    expiration_month = fields.Int(required=True)
    cvv = fields.Int(required=True)
    card_type = EnumField(CardType, required=True)
    products = fields.Nested(ProductsSchema, many=True)


purchase_order_schema = PurchaseOrderDetailsSchema()
purchase_orders_schema = PurchaseOrderDetailsSchema(many=True)

from marshmallow import Schema, fields

class ReviewSchema(Schema):
    id            = fields.Int(required=True)
    product_id    = fields.Int(required=True)
    user_id       = fields.Int(required=True)
    review_body   = fields.Str(required=True)
    score         = fields.Float(required=True)
    creation_date = fields.Str(required=True)


review_schema = ReviewSchema()
reviews_schema = ReviewSchema(many=True)
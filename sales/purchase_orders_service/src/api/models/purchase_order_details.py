class PurchaseOrderDetails:

    def __init__(self,
                 purchase_order_id,
                 comments,
                 user_id,
                 total_price,
                 payment_method,
                 card_number,
                 expiration_year,
                 expiration_month,
                 cvv,
                 card_type,
                 products):
        self.purchase_order_id = purchase_order_id
        self.comments = comments
        self.user_id = user_id
        self.total_price = total_price
        self.payment_method = payment_method
        self.card_number = card_number
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.cvv = cvv
        self.card_type = card_type
        self.products = products

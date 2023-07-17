class PaymentDetails:
    def __init__(self,
                 payment_method,
                 card_number,
                 expiration_year,
                 expiration_month,
                 cvv,
                 card_type):
        self.payment_method = payment_method
        self.card_number = card_number
        self.expiration_year = expiration_year
        self.expiration_month = expiration_month
        self.cvv = cvv
        self.card_type = card_type

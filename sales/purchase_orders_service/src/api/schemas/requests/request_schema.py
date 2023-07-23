create_purchase_order_schema = {
    "type": "object",
    "properties": {
        "comments": {"type": "string"},
        "user_id": {"type": "integer"},
        "products": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "product_id": {"type": "integer"},
                    "product_price": {
                        "type": "number",
                        "minimum": 0,
                    },
                    "product_quantity": {
                        "type": "integer",
                        "minimum": 0,
                    },
                },
                "required": ["product_id", "product_price", "product_quantity"]
            }
        },
        'total_price': {
            "type": "number",
            "minimum": 0,
        },
        "payment_details": {
            "type": "object",
            "properties": {
                "payment_method": {
                    "type": "string",
                    "enum": ["CREDIT_CARD", "DEBIT_CARD"],
                },
                "card_number": {
                    "type": "string",
                    "pattern": "^[0-9]{14,20}$",
                },
                "expiration_year": {
                    "type": "integer",
                    "minimum": 2022,
                },
                "expiration_month": {
                    "type": "integer",
                    "minimum": 1,
                    "maximum": 12,
                },
                "cvv": {
                    "type": "string",
                    "pattern": "^[0-9]{3,4}$",
                },
                "card_type": {
                    "type": "string",
                    "enum": ["VISA", "MASTERCARD"],
                },
            },
            "required": [
                "payment_method",
                "card_number",
                "expiration_year",
                "expiration_month",
                "cvv",
                "card_type",
            ],
        }
    },
    "required": ["user_id", "products", "total_price", "payment_details"]
}

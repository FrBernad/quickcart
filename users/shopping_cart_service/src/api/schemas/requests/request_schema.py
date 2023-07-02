update_shopping_cart_schema = {
    "type": "object",
    "properties": {
        "quantity": {
            "type": "integer",
            "minimum": 1,
        },
    },
    "required": ["quantity"],
}

checkout_shopping_cart_schema = {
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
            "type": "string",
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

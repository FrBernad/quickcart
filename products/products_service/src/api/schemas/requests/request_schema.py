create_product_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'price': {
            'type': 'number',
            'minimum': 0,
        },
        'category_id': {'type': 'string'},
        'tags': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        },
        'stock': {
            'type': 'integer',
            'minimum': 0,
        },
    },
    'required': ['name', 'price', 'category_id', 'tags', 'stock']
}

update_product_schema = {
    'type': 'object',
    'properties': {
        'name': {'type': 'string'},
        'price': {
            'type': 'number',
            'minimum': 0,
        },
        'category_id': {'type': 'string'},
        'tags': {
            'type': 'array',
            'items': {
                'type': 'string'
            }
        }
    }
}

update_product_score_schema = {
    'type': 'object',
    'properties': {
        'score': {
            'type': 'number',
            'minimum': 0.0,
            'maximum': 5.0,
        },
    },
    'required': ['score']
}

update_product_stock_schema = {
    'type': 'object',
    'properties': {
        'stock': {
            'type': 'integer',
            'minimum': 0,
        },
    },
    'required': ['stock']
}

create_review_schema = {
    'type': 'object',
    'properties': {
        'description': {'type': 'string'},
        'score': {
            'type': 'integer',
            "minimum": 1,
            "maximum": 5,
        },
    },
    'required': ['description', 'score']
}

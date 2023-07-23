create_user_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password', 'username']
}

update_user_schema = {
    'type': 'object',
    'properties': {
        'username': {'type': 'string'},
        'password': {'type': 'string'}
    },
}

login_user_schema = {
    'type': 'object',
    'properties': {
        'email': {'type': 'string'},
        'password': {'type': 'string'}
    },
    'required': ['email', 'password']
}
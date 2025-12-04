from functools import wraps
from flask import request


class AuthenticationManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.valid_tokens = {'abcd12345', 'abcd1234'}
        return cls._instance

    def is_valid_token(self, token):
        return token in self.valid_tokens

    def add_token(self, token):
        self.valid_tokens.add(token)


def require_auth(func):
    @wraps(func)
    def decorated_function(*args, **kwargs):
        auth_manager = AuthenticationManager()
        token = request.headers.get('Authorization')

        if not token:
            return {'message': 'Unauthorized - token not found'}, 401

        if not auth_manager.is_valid_token(token):
            return {'message': 'Unauthorized - invalid token'}, 401

        return func(*args, **kwargs)

    return decorated_function

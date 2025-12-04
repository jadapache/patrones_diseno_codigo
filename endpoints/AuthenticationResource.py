# endpoints/auth.py
from flask_restful import Resource, reqparse
from flask import request
from auth_decorator import AuthenticationManager

class AuthenticationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True)
        self.parser.add_argument('password', type=str, required=True)
        self.auth_manager = AuthenticationManager()
    
    def post(self):
        args = self.parser.parse_args()
        username = args['username']
        password = args['password']
        
        # Esto debería ser más seguro en producción
        if username == 'student' and password == 'desingp':
            token = 'abcd12345'
            self.auth_manager.add_token(token)
            return {'token': token}, 200
        else:
            return {'message': 'unauthorized'}, 401
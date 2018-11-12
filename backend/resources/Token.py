from flask_restful import Resource
from backend import app
from flask_httpauth import HTTPBasicAuth
from models.User import User
from functools import wraps
from flask import request

g = app


class TokenResource(Resource):
    auth = HTTPBasicAuth()

    @staticmethod
    @auth.verify_password
    def verify_password(username, password):
        user = User.query.filter_by(email=username).first()
        if not user or not user.verify_password(password):
            return False
        g.user = user
        return True

    @auth.login_required
    def post(self):
        token = g.user.generate_auth_token(app)
        return {'token': token.decode('ascii')}, 200

    @staticmethod
    def token_required(f):
        @wraps(f)
        def _token_required(*args, **kwargs):
            if 'username' not in request.authorization:
                return {'message': 'No oauth token provided'}, 401
            user = User.verify_auth_token(request.authorization['username'])
            if user is None:
                return {'message': 'Bad oauth token'}, 403
            g.user = user
            return f(*args, **kwargs)
        return _token_required

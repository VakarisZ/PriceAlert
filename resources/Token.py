from flask_restful import Resource
import app
from flask_httpauth import HTTPBasicAuth
from models.User import User

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
        token = self.user.generate_auth_token(app)
        return {'token': token.decode('ascii')}, 200

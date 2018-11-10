from flask import request
from flask_restful import Resource
from models.Model import db
from models.User import User, UserSchema

user_schema = UserSchema()


class UserResource(Resource):
    @staticmethod
    def post():
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        data, errors = user_schema.load(json_data)
        if json_data['email'] is None or json_data['password'] is None:
            return {'message': 'No input data provided'}, 400  # missing arguments
        if User.query.filter_by(email=data['email']).first() is not None:
            return {'message': 'No input data provided'}, 400 # existing user
        user = User(email=data['email'], password=json_data['password'])
        data, errors = user_schema.load(user_schema.dump(user).data)
        if errors:
            return {"status": "error", "data": errors}, 422
        db.session.commit()
        result = user_schema.dump(user).data
        return {'status': "success", 'data': result}, 201
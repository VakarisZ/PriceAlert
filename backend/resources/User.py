from flask import request
from flask_restful import Resource
from models.Model import db
from models.User import User, UserSchema

user_schema = UserSchema()


class UserResource(Resource):

    # Registration
    def post(self):
        json_data = request.get_json(force=True)
        data, errors = user_schema.load(json_data)
        if errors:
            return errors, 422
        if not json_data:
            return {'message': 'No input data provided'}, 400
        if json_data['email'] is None or json_data['password'] is None:
            return {'message': 'Not enough info provided'}, 400  # missing arguments
        if User.query.filter_by(email=json_data['email']).first() is not None:
            return {'message': 'User with this e-mail is already registered'}, 400 # existing user
        user = User(email=json_data['email'], password=json_data['password'])
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user).data
        return {'status': "success", 'data': result}, 201
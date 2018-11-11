from flask import Blueprint, request
from flask_restful import Api
from resources.Company import CompanyResource
from resources.Price import PriceResource
from resources.User import UserResource
from resources.Token import TokenResource
from resources.Category import CategoryResource
from functools import wraps

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Decorators


# Routes

api.add_resource(UserResource, '/user')
api.add_resource(TokenResource, '/token')
api.add_resource(CompanyResource, '/company')
api.add_resource(PriceResource, '/company/<string:symbol>/price')
api.add_resource(CategoryResource, '/Category')

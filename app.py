from flask import Blueprint
from flask_restful import Api
from resources.Company import CompanyResource
from resources.Price import PriceResource
from resources.User import UserResource
from resources.Token import TokenResource

api_bp = Blueprint('api', __name__)
api = Api(api_bp)

# Routes

api.add_resource(UserResource, '/user')
api.add_resource(TokenResource, '/token')
api.add_resource(CompanyResource, '/company')
api.add_resource(PriceResource, '/company/<string:symbol>/price')


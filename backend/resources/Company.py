from flask import request
from flask_restful import Resource
from models.Model import db
from models.Company import Company, CompanySchema
from resources.Token import TokenResource

companies_schema = CompanySchema(many=True)
company_schema = CompanySchema()


class CompanyResource(Resource):

    @TokenResource.token_required
    def get(self):
        companies = Company.query.all()
        companies = companies_schema.dump(companies).data
        return {'status': 'success', 'data': companies}, 200

    @TokenResource.token_required
    def post(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'Input data not provided/not in json'}, 400
        # Validate and deserialize input
        data, errors = company_schema.load(json_data)
        if errors:
            return errors, 422
        company = Company.query.filter_by(symbol=data['symbol']).first()
        if company:
            return {'message': 'Company already exists, try to update'}, 400
        company = Company(json_data)

        db.session.add(company)
        db.session.commit()

        result = company_schema.dump(company).data

        return {"status": 'success', 'data': result}, 201

    @TokenResource.token_required
    def put(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = company_schema.load(json_data)
        if errors:
            return errors, 422
        company = Company.query.filter_by(symbol=data['symbol']).first()
        if not company:
            return {'message': 'Company does not exist'}, 400
        company.name = data['name']
        if 'market' in data:
            market = data['market']
        else:
            market = None
        if 'employees' in data:
            employees = data['employees']
        else:
            employees = None
        if 'sector' in data:
            sector = data['sector']
        else:
            sector = None
        company.market = market
        company.employees = employees
        company.sector = sector
        db.session.commit()

        result = company_schema.dump(company).data

        return {"status": 'success', 'data': result}, 201

    @TokenResource.token_required
    def delete(self):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        data, errors = company_schema.load(json_data)
        if errors:
            return errors, 422
        company = Company.query.filter_by(symbol=data['symbol']).delete()
        db.session.commit()
        return CompanyResource.get()

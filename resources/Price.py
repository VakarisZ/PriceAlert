from flask import request
from flask_restful import Resource
from models.Company import Company
from models.Price import PriceSchema, Price
from models.Model import db
from resources.Token import TokenResource

prices_schema = PriceSchema(many=True)
price_schema = PriceSchema()


class PriceResource(Resource):

    @TokenResource.token_required
    def get(self, symbol):
        prices = Price.query.filter_by(symbol=symbol).all()
        prices = prices_schema.dump(prices).data
        return {"status": "success", "data": prices}, 200

    @TokenResource.token_required
    def post(self, symbol):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        json_data['symbol'] = symbol
        data, errors = price_schema.load(json_data)
        if errors:
            return {"status": "error", "data": errors}, 422
        company = Company.query.filter_by(symbol=data['symbol']).first()
        if not company:
            return {'status': 'error', 'message': 'Company '+data['symbol']+' does not exist'}, 400
        price = Price(
            symbol=data['symbol'],
            date=data['date'],
            high=data['high'],
            low=data['low'],
            open=data['open'],
            close=data['close'],
            volume=data['volume']
            )
        db.session.add(price)
        db.session.commit()

        result = price_schema.dump(price).data

        return {'status': "success", 'data': result}, 201

    @TokenResource.token_required
    def patch(self, symbol):
        json_data = request.get_json(force=True)
        if not json_data:
            return {'message': 'No input data provided'}, 400
        # Validate and deserialize input
        json_data['symbol'] = symbol
        data = json_data
        company = Company.query.filter_by(symbol=data['symbol']).first()
        if not company:
            return {'status': 'error', 'message': 'Company ' + data['symbol'] + ' does not exist'}, 400
        price = Price.query.filter_by(symbol=data['symbol'], date=data['date']).first()
        if 'high' in data:
            price.high = data['high']
        if 'low' in data:
            price.low = data['low']
        if 'open' in data:
            price.open = data['open']
        if 'close' in data:
            price.close = data['close']
        if 'volume' in data:
            price.volume = data['volume']

        data, errors = price_schema.load(price_schema.dump(price).data)
        if errors:
            return {"status": "error", "data": errors}, 422

        db.session.commit()
        result = price_schema.dump(price).data
        return {'status': "success", 'data': result}, 201
from marshmallow import fields
from models.Model import db, ma


class Company(db.Model):
    __tablename__ = 'companies'
    symbol = db.Column(db.String(15), unique=True, primary_key=True)
    name = db.Column(db.String(250))
    sector = db.Column(db.String(250))
    employees = db.Column(db.Integer)
    market = db.Column(db.String(250))

    def __init__(self, data):
        self.symbol = data['symbol']
        self.name = data['name']
        if 'sector' in data:
            self.sector = data['sector']
        if 'employees' in data:
            self.employees = data['employees']
        if 'market' in data:
            self.market = data['market']


class CompanySchema(ma.Schema):
    symbol = fields.String(required=True)
    name = fields.String(required=True)
    sector = fields.String()
    employees = fields.Integer()
    market = fields.String()
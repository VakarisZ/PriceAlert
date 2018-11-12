from marshmallow import fields
from models.Model import db, ma


class Price(db.Model):
    __tablename__ = 'prices'
    symbol = db.Column(db.String(15), db.ForeignKey('companies.symbol', ondelete='CASCADE'), primary_key=True)
    date = db.Column(db.DateTime, primary_key=True)
    high = db.Column(db.Float, nullable=False)
    low = db.Column(db.Float, nullable=False)
    open = db.Column(db.Float, nullable=False)
    close = db.Column(db.Float, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    company = db.relationship('Company', backref=db.backref('companies', lazy='dynamic'))

    def __init__(self, symbol, date, high, low, open, close, volume):
        self.symbol = symbol
        self.date = date
        self.high = high
        self.low = low
        self.open = open
        self.close = close
        self.volume = volume


class PriceSchema(ma.Schema):
    symbol = fields.String(required=True)
    date = fields.DateTime(required=True)
    high = fields.Float(required=True)
    low = fields.Float(required=True)
    open = fields.Float(required=True)
    close = fields.Float(required=True)
    volume = fields.Float(required=True)
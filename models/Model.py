from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

ma = Marshmallow()
db = SQLAlchemy()

from models.User import User
from models.Category import Category
from models.Price import Price
from models.Company import Company
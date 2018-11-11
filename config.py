import os

# You need to replace the next values with the appropriate values for your configuration
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_ECHO = False
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:paprastas@localhost/pricealert"
SECRET_KEY = "k3xC!uaN&hx$c-DX"
EXPIRATION = 600 # How long does it take for oauth token to expire
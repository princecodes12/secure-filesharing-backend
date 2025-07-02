import os
basedir = os.path.abspath(os.path.dirname(__file__))

class config:
    SECRET_KEY = "Prince"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir,'app.db')
    SQKALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "PrinceSeth"
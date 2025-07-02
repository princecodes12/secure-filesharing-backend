from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from config import config

db = SQLAlchemy()
bcrypt = Bcrypt()


def create_app():
    app = Flask(__name__)

    app.config.from_object(config)
    db.init_app(app)

    from .routes.ops_routes import ops_bp
    from .routes.client_routes import client_bp

    app.register_blueprint(ops_bp,url_prefix="/ops")
    app.register_blueprint(client_bp,url_prefix="/client")

    return app
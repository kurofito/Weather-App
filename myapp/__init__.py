from flask import Flask
from .site.routes import site
from .extensions import db
from flask_restful import Api
from .user_api.requests import Weather


def create_app():
    app = Flask(__name__)
    api = Api(app)

    app.config['SECRET_KEY'] = 'secret'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.sqlite3'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(site)
    api.add_resource(Weather, '/weather')
    return app

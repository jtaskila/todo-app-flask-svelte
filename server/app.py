from flask import Flask
from database import db, db_config
from database.models import UserModel
from schemas import ma
from resources import *

from flask_restful import Api
api = Api()

from flask_cors import CORS, cross_origin
cors = CORS()

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = db_config['SQLALCHEMY_DATABASE_URI']
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = db_config['SQLALCHEMY_TRACK_MODIFICATIONS']

    api.add_resource(DefaultResource, "/")
    api.add_resource(RegisterResource, "/register")
    api.add_resource(LoginResource, "/login")
    api.add_resource(TodosResource, "/todos")
    api.add_resource(TodoResource, "/todo/<int:id>")

    api.init_app(app)
    ma.init_app(app)
    cors.init_app(app)

    db.init_app(app)
    return app

def main():
    app = create_app()

    with app.app_context():
        db.create_all()

    app.run('127.0.0.1', 5000, debug = True)

if __name__ == '__main__':
    main()

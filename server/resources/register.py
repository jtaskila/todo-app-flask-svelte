from flask import request
from flask_restful import Resource

from database import db
from database.models import UserModel

from schemas import LoginSchema
from marshmallow import ValidationError

class RegisterResource(Resource):
    def post(self):
        # validating input data with marshmallow
        try:
            loginschema = LoginSchema()
            data = loginschema.load(request.json)
        except ValidationError as err:
            return {
                "message": "Invalid post request",
                "invalid": err.messages,
            }, 400

        # check if user already exists
        check_user = UserModel.query.filter_by(name = data['name']).first()
        if(check_user):
            return {"message": "User already exists"},409

        # if guard clauses passed, create the user
        user = UserModel(data['name'], data['password'])
        db.session.add(user)
        db.session.commit()

        return {"message": "User was created"}, 200

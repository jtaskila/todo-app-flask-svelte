from flask import request
from flask_restful import Resource


from database import db
from database.models import UserModel

from schemas import LoginSchema
from marshmallow import ValidationError

from auth import generate_apikey, delete_user_sessions, check_apikey, delete_apikey

class LoginResource(Resource):
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


        # check if the user exists
        check_user = UserModel.query.filter_by(name = data['name'], password = data['password']).first()

        if(check_user):
            return {
                "message": "You are now successfully logged in",
                "apikey": generate_apikey(check_user._id),
                "user_id": check_user._id
            }
        else:
            return {"message": "User not found"}, 404

    # with delete request to login, you can delete your users session
    # by specifying ?all=true, all keys are deleted
    def delete(self):
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        all = request.args.get("all")
        if(all == None or all != "true"):
            delete_apikey(apikey)
        else:
            delete_user_sessions(user_id)

        return {"message": "User logged out successfully"},200

from flask import request
from flask_restful import Resource

from auth import check_apikey

from database import db
from database.models import TodoModel

class TodoResource(Resource):
    def get(self, id):

        # check if apikey exists
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        # check the existense of the todo
        # also prevent other users from seeing others todos
        todo = TodoModel.query.filter_by(user_id = user_id, _id = id).first()
        if(todo == None):
            return {"message": "Todo not found"},404

        # return the entry
        return {
            "message": "A single todo entry",
            "data": [
                {
                    "id": todo._id,
                    "todo": todo.todo,
                    "status": todo.status
                }
            ]
        }

    def update(self, id):

        # check if apikey exists
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        return {"message": "Update did nothing for now"},200

    def delete(self, id):
        # check if apikey exists
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        # get the todo
        todo = TodoModel.query.filter_by(user_id = user_id, _id = id).first()
        if(todo == None):
            return {"message": "Todo not found"},404

        db.session.delete(todo)
        db.session.commit()
        return {"message": "Todo deleted succesfully"},200

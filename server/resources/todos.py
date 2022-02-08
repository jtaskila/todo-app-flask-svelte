from flask import request
from flask_restful import Resource

from auth import check_apikey

from database import db
from database.models import TodoModel

class TodosResource(Resource):
    def get(self):
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        # query users todos
        todos = TodoModel.query.filter_by(user_id = user_id).order_by(TodoModel._id.desc())
        data = list()

        if(todos):
            for todo in todos:
                data.append({
                    "id": todo._id,
                    "todo": todo.todo,
                    "status": todo.status
                })

            return {"message": "Here are your todos", "data": data},200

        return {"message": "No todos found"},404

    def post(self):
        # check if apikey exists
        apikey = request.headers.get("apikey")
        if(apikey == None):
            return {"message": "Permission denied"},403

        # check if the key is valid
        user_id = check_apikey(apikey)
        if(user_id == None):
            return {"message": "Permission denied"},403

        # validate post body
        data = request.json
        if("todo" not in data):
            return {"message": "Bad request"}, 403

        todo = TodoModel(user_id, data['todo'])
        db.session.add(todo)
        db.session.commit()

        return {"message": "Todo added succesfully"}, 200

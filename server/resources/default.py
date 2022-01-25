from flask_restful import Resource

class DefaultResource(Resource):

    def get(self):
        return {
            "message": "Todo App API V1.0"
        }

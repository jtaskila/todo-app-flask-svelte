from database import db

class TodoModel(db.Model):
    _id     = db.Column("id", db.Integer, primary_key = True)
    user_id = db.Column("user_id", db.Integer)
    todo    = db.Column("todo", db.String(200))
    status  = db.Column("status", db.String(50))

    def __init__(self, user_id, todo):
        self.user_id = user_id
        self.todo = todo
        self.status = "waiting"

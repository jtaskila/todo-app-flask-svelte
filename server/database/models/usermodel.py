from database import db

class UserModel(db.Model):
    _id         = db.Column("id", db.Integer, primary_key = True)
    name        = db.Column("name", db.String(100))
    password    = db.Column("password", db.String(100))

    def __init__(self, name, password):
        self.name = name
        self.password = password

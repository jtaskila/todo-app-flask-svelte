from database import db

class SessionModel(db.Model):
    _id     = db.Column("id", db.Integer, primary_key = True)
    user_id = db.Column("user_id", db.Integer)
    apikey  = db.Column("apikey", db.String(50))

    def __init__(self, user_id, apikey):
        self.user_id = user_id
        self.apikey = apikey

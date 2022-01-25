import secrets

from database import db
from database.models import UserModel, SessionModel

def generate_apikey(user_id):
    apikey = secrets.token_urlsafe(32)

    # generate the session
    session = SessionModel(user_id, apikey)
    db.session.add(session)
    db.session.commit()

    return apikey

def delete_apikey(key):
    delete_apikey = SessionModel.query.filter_by(apikey = key).first()
    db.session.delete(delete_apikey)
    db.session.commit()

def delete_user_sessions(id):
    delete_apikeys = SessionModel.query.filter_by(user_id = id)
    for key in delete_apikeys:
        db.session.delete(key)
    db.session.commit()

def check_apikey(key):
    check_apikey = SessionModel.query.filter_by(apikey = key).first()

    if(check_apikey):
        return check_apikey.user_id
    else:
        return None

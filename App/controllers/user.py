from App.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

def create_user(username, password, role, id=None):
    newuser = User(username=username, password=password, role=role, id=id)
    doc_ref = db.collection(u'Users').document(newuser.get_id()).set(newuser.toDict())
    return newuser

def create_user_dict(dict):
    return User.fromDict(dict)

def get_all_users():
    return db.collection(u'Users').stream()

def get_user(id):
    return db.collection(u'Users').document(id).get()

def get_user_by_username(username):
    return db.collection(u'Users').where(u'username', u'==', username).limit(1).get()

def delete_user(id):
    return db.collection(u'Users').document(id).delete()
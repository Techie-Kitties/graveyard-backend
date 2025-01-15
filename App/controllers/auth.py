import flask_login
from werkzeug.security import check_password_hash
from App.models import User
from App.controllers import get_user_by_username
from App.database import db

def authenticate(username, password):
    user_data = get_user_by_username(username)
    if user_data:
        users_array = []
        for user in user_data:
            user_dict = user.to_dict()
            user_dict['id'] = user.id
            users_array.append(user_dict)
        user = users_array[0]
        if check_password_hash(user["password"], password):
            return user
    return None

# Payload is a dictionary which is passed to the function by Flask JWT
def identity(payload):
    return db.collection(u'Users').document(payload['identity']).get()

def login_user(user, remember):
    return flask_login.login_user(user, remember=remember)

def logout_user():
    flask_login.logout_user()

def setup_jwt(app):
    return (app, authenticate, identity)
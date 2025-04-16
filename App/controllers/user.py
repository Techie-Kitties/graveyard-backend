from App.models import User
from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


def create_user(username, password, role=1,):
    if User.query.filter_by(username=username).first():
        print("already exists")
        return "Error: user already exists"
    new_user = User(username=username, password=password, role=role)
    db.session.add(new_user)
    db.session.commit()
    return new_user

def create_user_oauth(username, google_id, role=1):
    if User.query.filter_by(username=username).first():
        print("already exists")
        return "Error: user already exists"
    new_user = User(username=username, google_id=google_id, role=role)
    db.session.add(new_user)
    db.session.commit()
    return new_user


def get_all_users():
    return User.query.all()

def get_user(id):
    return User.query.get(id)

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def delete_user(id):
    user = User.query.get(id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return True
    return False

from .user import create_user
from App.models import customPackage
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass',1)
    customPackage.initialize_defaults()

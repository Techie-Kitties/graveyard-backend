from App.models import Graveyard, Grave
from App.database import db
from App.controllers.grave import get_grave_by_graveyard
from firebase_admin import firestore

def create_graveyard(name, location, max_plots, owner_id, single_price, companion_price, family_price, id=None):
    graveyard = Graveyard(name=name, location=location, max_plots=max_plots, owner_id=owner_id, single_price=single_price, companion_price=companion_price, family_price=family_price, id=id)
    doc_ref = db.collection(u'Graveyards').document(graveyard.get_id()).set(graveyard.toDict())
    return graveyard

def create_graveyard_dict(dict):
    return Graveyard.fromDict(dict)

def get_all_graveyards():
    return db.collection(u'Graveyards').stream()

def get_graveyard(id):
    return db.collection(u'Graveyards').document(id).get()

def get_graveyard_by_name(name):
    return db.collection(u'Graveyards').where(u'name', u'==', name).get()

def get_graveyard_by_owner_id(owner_id):
    return db.collection(u'Graveyards').where(u'owner_id', u'==', owner_id).get()

def get_graveyard_by_user_access(id):
    return db.collection(u'Graveyards').where(u'access', u'array_contains', id).get()

def delete_graveyard(id):
    return db.collection(u'Graveyards').document(id).delete()

def at_max_plots(id):
    at_max = False
    graveyard = db.collection(u'Graveyards').document(id).get()
    graveyard = graveyard.to_dict()

    graves = get_grave_by_graveyard(id)
    graves_array = []
    if graves:
        for grave in graves:
            grave_dict = grave.to_dict()
            graves_array.append(grave_dict)

    if graveyard['max_plots'] == len(graves_array):
        at_max = True
    return at_max

def add_access(graveyard_id, user_id):
    graveyard = db.collection(u'Graveyards').document(graveyard_id)
    graveyard.update({u'access': firestore.ArrayUnion([user_id])})

def update_price(graveyard_id, single_price, companion_price, family_price):
    graveyard = db.collection(u'Graveyards').document(graveyard_id)
    if single_price is not None:
        graveyard.update({u'single_price': single_price})
    if companion_price is not None:
        graveyard.update({u'companion_price': companion_price})
    if family_price is not None:
        graveyard.update({u'family_price': family_price})
    return graveyard
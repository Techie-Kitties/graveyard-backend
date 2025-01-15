from App.models import Deceased
from App.database import db
from datetime import datetime
from App.controllers.grave import get_grave_by_graveyard

def create_deceased(name, date_of_birth, date_of_death, cause_of_death, grave_id, id=None):
    deceased = Deceased(name=name, date_of_birth=datetime.fromisoformat(date_of_birth), date_of_death=datetime.fromisoformat(date_of_death), cause_of_death=cause_of_death, grave_id=grave_id, id=id)
    doc_ref = db.collection(u'Deceaseds').document(deceased.get_id()).set(deceased.toDict())
    return deceased

def get_all_deceaseds():
    return db.collection(u'Deceaseds').stream()

def get_deceased(id):
    return db.collection(u'Deceaseds').document(id).get()

def get_deceased_by_name(name):
    return db.collection(u'Deceaseds').where(u'name', u'==', name).get()

def get_deceased_by_grave(id):
    return db.collection(u'Deceaseds').where(u'grave_id', u'==', id).get()

def get_deceased_by_graveyard(id):
    deceased_array = []
    graves = get_grave_by_graveyard(id)
    for grave in graves:
        deceaseds = get_deceased_by_grave(grave.id)
        for deceased in deceaseds:
                deceased_dict = deceased.to_dict()
                deceased_dict['id'] = deceased.id
                deceased_array.append(deceased_dict)
    return deceased_array

def delete_deceased(id):
    return db.collection(u'Deceaseds').document(id).delete()
from App.models import Grave
from App.database import db
from datetime import datetime

def create_grave(plot_num, graveyard_id, grave_type, id=None):
    grave = Grave(plot_num=plot_num, graveyard_id=graveyard_id, grave_type=grave_type, id=id)
    doc_ref = db.collection(u'Graves').document(grave.get_id()).set(grave.toDict())
    return grave

def create_grave_dict(dict):
    return Grave.fromDict(dict)

def get_all_graves():
    return db.collection(u'Graves').stream()

def get_grave(id):
    return db.collection(u'Graves').document(id).get()

def get_grave_by_plot_num(plot_num):
    return db.collection(u'Graves').where(u'plot_num', u'==', plot_num).get()

def get_grave_by_graveyard(graveyard_id):
    return db.collection(u'Graves').where(u'graveyard_id', u'==', graveyard_id).get()

def get_grave_by_type(grave_type):
    return db.collection(u'Graves').where(u'grave_type', u'==', grave_type).get()

def update_grave(id, date):
    grave = db.collection(u'Graves').document(id)
    grave.update({u'last_buried': date})
    try:
        available_date = date.replace(year=date.year + 7)
    except ValueError:
        #accounting for the 29th of Feb
        available_date = date.replace(year=date.year + 7, day=28)
    grave.update({u'next_available': available_date})

def delete_grave(id):
    return db.collection(u'Graves').document(id).delete()

def grave_available(id):
    grave = get_grave(id)
    grave = grave.to_dict()
    available = grave['next_available']
    today = datetime.today()
    print(available)
    print(today)
    if available.year > today.year:
        return False
    if available.month > today.month:
        return False
    if available.day > today.day:
        return False
    return True

def graves_available():
    graves = db.collection(u'Graves').stream()
    graves_array = []
    for grave in graves:
        grave_dict = grave.to_dict()
        grave_dict['id'] = grave.id
        if grave_available(grave.id):
            graves_array.append(grave_dict)
    return graves_array

def graves_unavailable():
    graves = db.collection(u'Graves').stream()
    graves_array = []
    for grave in graves:
        grave_dict = grave.to_dict()
        grave_dict['id'] = grave.id
        if not grave_available(grave.id):
            graves_array.append(grave_dict)
    return graves_array
from App.models import Reservation
from App.database import db

#Can add check to ensure that reservation does not clash with other commitments (reservations and burials)
def create_reservation(customer_id, reservation_date, grave_id, id=None):
    reservation = Reservation(customer_id=customer_id, reservation_date=reservation_date, grave_id=grave_id, id=id)
    doc_ref = db.collection(u'Reservations').document(reservation.get_id()).set(reservation.toDict())
    return reservation

def get_all_reservations():
    return db.collection(u'Reservations').stream()

def get_reservation(id):
    return db.collection(u'Reservations').document(id).get()

def get_reservation_by_grave_id(grave_id):
    return db.collection(u'Reservations').where(u'grave_id', u'==', grave_id).get()

def get_reservation_by_customer_id(customer_id):
    return db.collection(u'Reservations').where(u'customer_id', u'==', customer_id).get()

def update_reservation(id, date):
    reservation = db.collection(u'Reservations').document(id)
    reservation.update({u'reservation_date': date})
    return reservation

def delete_reservation(id):
    return db.collection(u'Reservations').document(id).delete()
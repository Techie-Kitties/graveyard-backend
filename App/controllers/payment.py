from App.models import Payment
from App.database import db
from datetime import datetime, date

def create_payment(customer_id, user_id, amount, date_created, id=None):
    payment = Payment(customer_id=customer_id, user_id=user_id, amount=amount, date_created=date_created, id=id)
    doc_ref = db.collection(u'Payments').document(payment.get_id()).set(payment.toDict())
    return payment

def get_all_payments():
    return db.collection(u'Payments').stream()

def get_payment(id):
    return db.collection(u'Payments').document(id).get()

def get_payment_by_customer_id(customer_id):
    return db.collection(u'Payments').where(u'customer_id', u'==', customer_id).get()

def get_payment_by_user_id(user_id):
    return db.collection(u'Payments').where(u'user_id', u'==', user_id).get()

def get_payment_by_date_created(date_created):
    return db.collection(u'Payments').where(u'date_created', u'==', date_created).get()

def delete_payment(id):
    return db.collection(u'Payments').document(id).delete()
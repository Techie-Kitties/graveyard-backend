from App.models import Customer
from App.database import db

def create_customer(name, phone_number, email_address, id=None):
    customer = Customer(name=name, phone_number=phone_number, email_address=email_address, id=id)
    doc_ref = db.collection(u'Customers').document(customer.get_id()).set(customer.toDict())
    return customer

def get_all_customers():
    return db.collection(u'Customers').stream()

def get_customer(id):
    return db.collection(u'Customers').document(id).get()

def get_customer_by_name(name):
    return db.collection(u'Customers').where(u'name', u'==', name).get()

def delete_customer(id):
    return db.collection(u'Customers').document(id).delete()

def update_customer(id, phone_number, email_address):
    customer = db.collection(u'Customers').document(id)
    if phone_number is not None:
        customer.update({u'phone_number': phone_number})
    if email_address is not None:
        customer.update({u'email_address': email_address})
    return customer
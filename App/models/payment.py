from App.database import db
from datetime import date, datetime

class Payment():

    def __init__(self, customer_id, user_id, amount, date_created, id=None):
        self.set_customer_id(customer_id)
        self.set_user_id(user_id)
        self.set_amount(amount)
        self.set_date_created(date_created)
        self.set_id(id)

    #customer_id
    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        if not isinstance(customer_id, str):
            raise TypeError("customer_id must be a string")
        self._customer_id = customer_id

    #amount
    def get_amount(self):
        return self._amount

    def set_amount(self, amount):
        if not isinstance(amount, float):
            raise TypeError("amount must be a float")
        self._amount = amount
    
    #user_id
    def get_user_id(self):
        return self._user_id

    def set_user_id(self, user_id):
        if not isinstance(user_id, str):
            raise TypeError("user_id must be a string")
        self._user_id = user_id

    #date_created
    def get_date_created(self):
        return self._date_created

    def set_date_created(self, date_created):
        if not isinstance(date_created, datetime):
            raise TypeError("date_created must be a date")
        self._date_created = date_created

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'customer_id': self._customer_id,
            'amount': self._amount,
            'user_id': self._user_id,
            'date_created': self._date_created
        }
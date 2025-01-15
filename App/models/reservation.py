from App.database import db
from datetime import date, datetime

class Reservation():

    def __init__(self, customer_id, reservation_date, grave_id, id=None):
        self.set_customer_id(customer_id)
        self.set_reservation_date(reservation_date)
        self.set_grave_id(grave_id)
        self.set_id(id)

    #customer_id
    def get_customer_id(self):
        return self._customer_id

    def set_customer_id(self, customer_id):
        if not isinstance(customer_id, str):
            raise TypeError("customer_id must be a string")
        self._customer_id = customer_id

    #grave_id
    def get_grave_id(self):
        return self._grave_id

    def set_grave_id(self, grave_id):
        if not isinstance(grave_id, str):
            raise TypeError("grave_id must be a string")
        self._grave_id = grave_id
    
    #reservation_date
    def get_reservation_date(self):
        return self._reservation_date

    def set_reservation_date(self, reservation_date):
        if not isinstance(reservation_date, datetime):
            raise TypeError("reservation_date must be a date")
        self._reservation_date = reservation_date

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'customer_id': self._customer_id,
            'grave_id': self._grave_id,
            'reservation_date': self._reservation_date
        }
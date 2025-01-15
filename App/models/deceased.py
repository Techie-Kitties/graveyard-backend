from App.database import db
from datetime import datetime

class Deceased():

    def __init__(self, name, date_of_birth, date_of_death, cause_of_death, grave_id, id=None):
        self.set_name(name)
        self.set_date_of_birth(date_of_birth)
        self.set_date_of_death(date_of_death)
        self.set_cause_of_death(cause_of_death)
        self.set_grave_id(grave_id)
        self.set_id(id)

    #name
    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    #date_of_birth
    def get_date_of_birth(self):
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth):
        if not isinstance(date_of_birth, datetime):
            raise TypeError("date_of_birth must be a date")
        self._date_of_birth = date_of_birth
    
    #date_of_death
    def get_date_of_death(self):
        return self._date_of_death

    def set_date_of_death(self, date_of_death):
        if not isinstance(date_of_death, datetime):
            raise TypeError("date_of_death must be a date")
        self._date_of_death = date_of_death

    #cause_of_death
    def get_cause_of_death(self):
        return self._cause_of_death

    def set_cause_of_death(self, cause_of_death):
        if not isinstance(cause_of_death, str):
            raise TypeError("cause_of_death must be a string")
        self._cause_of_death = cause_of_death

    #grave_id
    def get_grave_id(self):
        return self._grave_id

    def set_grave_id(self, grave_id):
        if not isinstance(grave_id, str):
            raise TypeError("grave_id must be a string")
        self._grave_id = grave_id

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'name': self._name,
            'date_of_birth': self._date_of_birth,
            'date_of_death': self._date_of_death,
            'cause_of_death': self._cause_of_death,
            'grave_id': self._grave_id
        }
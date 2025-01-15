from App.database import db
from App.models import Grave

class Graveyard():

    def __init__(self, name, location, max_plots, owner_id, single_price, companion_price, family_price, id=None):
        self.set_name(name)
        self.set_location(location)
        self.set_max_plots(max_plots)
        self.set_owner_id(owner_id)
        self.set_single_price(single_price)
        self.set_companion_price(companion_price)
        self.set_family_price(family_price)
        self.set_id(id)
        self._access = []
        self.add_access(owner_id)

    #name
    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    #max_plots
    def get_max_plots(self):
        return self._max_plots

    def set_max_plots(self, max_plots):
        if not isinstance(max_plots, int):
            raise TypeError("max_plots must be an int")
        self._max_plots = max_plots
    
    #location
    def get_location(self):
        return self._location

    def set_location(self, location):
        if not isinstance(location, str):
            raise TypeError("location must be a string")
        self._location = location

    #owner_id
    def get_owner_id(self):
        return self._owner_id

    def set_owner_id(self, owner_id):
        if not isinstance(owner_id, str):
            raise TypeError("owner_id must be a string")
        self._owner_id = owner_id

    #single_price
    def get_single_price(self):
        return self._single_price

    def set_single_price(self, single_price):
        if not isinstance(single_price, float):
            raise TypeError("single_price must be a float")
        self._single_price = single_price

    #companion_price
    def get_companion_price(self):
        return self._companion_price

    def set_companion_price(self, companion_price):
        if not isinstance(companion_price, float):
            raise TypeError("companion_price must be a float")
        self._companion_price = companion_price

    #family_price
    def get_family_price(self):
        return self._family_price

    def set_family_price(self, family_price):
        if not isinstance(family_price, float):
            raise TypeError("family_price must be a float")
        self._family_price = family_price

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id

    #access
    def get_access(self):
        return self._access

    def add_access(self, id):
        if not isinstance(id, str):
            raise TypeError("id must be a string")
        self._access.append(id)

    #Operations
    def toDict(self):
        return{
            'name': self._name,
            'max_plots': self._max_plots,
            'location': self._location,
            'owner_id': self._owner_id,
            'single_price': self._single_price,
            'companion_price': self._companion_price,
            'family_price': self._family_price,
            'access': self._access
        }
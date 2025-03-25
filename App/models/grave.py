from App.database import db
from datetime import datetime, date
from App.database import db
class Grave():
    def __init__(self, plot_num, graveyard_id, grave_type, id=None):
        self.set_plot_num(plot_num)
        self.set_last_buried(datetime.today())
        self.set_next_available(datetime.today())
        self.set_graveyard_id(graveyard_id)
        self.set_grave_type(grave_type)
        self.set_id(id)

    #plot_num
    def get_plot_num(self):
        return self._plot_num

    def set_plot_num(self, plot_num):
        if not isinstance(plot_num, int):
            raise TypeError("plot_num must be a int")
        self._plot_num = plot_num

    #next_available
    def get_next_available(self):
        return self._next_available

    def set_next_available(self, next_available):
        if not isinstance(next_available, date):
            raise TypeError("next_available must be an date")
        self._next_available = next_available
    
    #last_buried
    def get_last_buried(self):
        return self._last_buried

    def set_last_buried(self, last_buried):
        if not isinstance(last_buried, date):
            raise TypeError("last_buried must be a date")
        self._last_buried = last_buried

    #graveyard_id
    def get_graveyard_id(self):
        return self._graveyard_id

    def set_graveyard_id(self, graveyard_id):
        if not isinstance(graveyard_id, str):
            raise TypeError("graveyard_id must be a string")
        self._graveyard_id = graveyard_id

    #grave_type
    def get_grave_type(self):
        return self._grave_type

    def set_grave_type(self, grave_type):
        if not isinstance(grave_type, str):
            raise TypeError("grave_type must be a string")
        if grave_type == "single" or grave_type == "companion" or grave_type == "family":
            self._grave_type = grave_type
        else:
            raise TypeError("grave_type must be single, companion or family")

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'plot_num': self._plot_num,
            'next_available': self._next_available,
            'last_buried': self._last_buried,
            'graveyard_id': self._graveyard_id,
            'grave_type': self._grave_type
        }
from App.database import db

class Customer():

    def __init__(self, name, phone_number, email_address, id=None):
        self.set_name(name)
        self.set_phone_number(phone_number)
        self.set_email_address(email_address)
        self.set_id(id)

    #name
    def get_name(self):
        return self._name

    def set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("name must be a string")
        self._name = name

    #email_address
    def get_email_address(self):
        return self._email_address

    def set_email_address(self, email_address):
        if not isinstance(email_address, str):
            raise TypeError("email_address must be a string")
        self._email_address = email_address
    
    #phone_number
    def get_phone_number(self):
        return self._phone_number

    def set_phone_number(self, phone_number):
        if not isinstance(phone_number, str):
            raise TypeError("phone_number must be a string")
        self._phone_number = phone_number

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'name': self._name,
            'email_address': self._email_address,
            'phone_number': self._phone_number
        }
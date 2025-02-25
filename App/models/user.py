from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

# Roles
# 0 - developer
# 1 - admin
# 2 - employee
# 3 - customer
class User():

    def __init__(self, username, password, role, id=None):
        self.set_username(username)
        self.set_role(role)
        self.set_password(password)
        self.set_id(id)

    #username
    def get_username(self):
        return self._username

    def set_username(self, username):
        if not isinstance(username, str):
            raise TypeError("username must be a string")
        self._username = username

    #password
    def get_password(self):
        return self._password

    def set_password(self, password):
        """Create hashed password."""
        if not isinstance(password, str):
            raise TypeError("password must be a string")
        self._password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return 

    #role
    def get_role(self):
        return self._role

    def set_role(self, role):
        if not isinstance(role, int):
            raise TypeError("role must be a int")
        if role < 0 or role > 2:
            raise TypeError("role must be 0, 1, or 2")
        self._role = role

    #id
    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = id
    
    #Operations
    def toDict(self):
        return{
            'username': self._username,
            'password': self._password,
            'role': self._role
        }

    @staticmethod
    def fromDict(dict):
        if not dict.username or not dict.password or not dict.role:
            return None

        if not dict.id:
            user = User(dict.username, dict.password, dict.role)
        else:
            user = User(dict.username, dict.password, dict.role, dict.id)
            
        if user:
            return user
        return None
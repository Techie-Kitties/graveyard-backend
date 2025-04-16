from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db


# Roles
# 0 - developer
# 1 - admin
# 2 - employee
# 3 - customer
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(120), nullable=True)
    role = db.Column(db.Integer, nullable=False)
    google_id = db.Column(db.String(64), unique=True)


    def __init__(self, username, password, role):
        self.username = username
        self.role = role
        self.set_password(password)
    def is_oauth_user(self):
        return self.google_id is not None and self.password is None


    def get_json(self):
        if self.google_id:
            return {
                'id': self.id,
                'username': self.username,
                'role': self.role,
                'google_id': self.google_id
            }
        else:
            return {
                'id': self.id,
                'username': self.username,
                'role': self.role,
            }


    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)


    def is_admin(self):
        return self.role == 1 or self.role == 0


    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

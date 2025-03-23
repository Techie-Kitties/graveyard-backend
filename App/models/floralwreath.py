from flask_sqlalchemy import SQLAlchemy

from App.database import db
class FloralWreathS(db.Model):
    __tablename__ = 'floral_wreath'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.String(50), nullable=True)  # The size of the floral wreath

    def get_json(self):
        return {
            'id': self.id,
            'size': self.size
        }

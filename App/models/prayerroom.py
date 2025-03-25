from flask_sqlalchemy import SQLAlchemy
from App.database import db

class PrayerRoom(db.Model):
    __tablename__ = 'prayer_room'
    id = db.Column(db.Integer, primary_key=True)
    availability = db.Column(db.Boolean, default=False)
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'availability': self.availability,
            'price': self.price
        }

from flask_sqlalchemy import SQLAlchemy

from App.database import db
class Safekeeping(db.Model):
    __tablename__ = 'safekeeping'
    id = db.Column(db.Integer, primary_key=True)
    days = db.Column(db.Integer, nullable=False)
    price_per_day = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'days': self.days,
            'price_per_day': self.price_per_day
        }

from flask_sqlalchemy import SQLAlchemy

from App.database import db
class LoweringDevice(db.Model):
    __tablename__ = 'lowering_device'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'price': self.price
        }


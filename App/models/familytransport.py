from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class FamilyTransport(db.Model):
    __tablename__ = 'family_transport'
    id = db.Column(db.Integer, primary_key=True)
    vehicle_type = db.Column(db.String(100), nullable=False)
    capacity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'vehicle_type': self.vehicle_type,
            'capacity': self.capacity,
            'price': self.price
        }

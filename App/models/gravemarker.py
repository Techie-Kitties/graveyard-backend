from flask_sqlalchemy import SQLAlchemy

from App.database import db
class GraveMarker(db.Model):
    __tablename__ = 'grave_marker'
    id = db.Column(db.Integer, primary_key=True)
    material = db.Column(db.String(100), nullable=False)
    style = db.Column(db.String(100), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'material': self.material,
            'style': self.style,
            'size': self.size,
            'price': self.price
        }


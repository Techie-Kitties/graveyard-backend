from flask_sqlalchemy import SQLAlchemy

from App.database import db
class BodyPreparation(db.Model):
    __tablename__ = 'body_preparation'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'price': self.price
        }


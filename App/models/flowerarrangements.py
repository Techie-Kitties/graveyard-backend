from flask_sqlalchemy import SQLAlchemy

from App.database import db
class FlowerArrangements(db.Model):
    __tablename__ = 'flower_arrangements'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether additional flower arrangements are included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

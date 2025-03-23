from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class FloralSprays(db.Model):
    __tablename__ = 'floral_sprays'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether custom floral sprays are included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

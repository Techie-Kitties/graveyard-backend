from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Casket(db.Model):
    __tablename__ = 'casket'
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200), nullable=False)  
    price = db.Column(db.Float, nullable=False)  

    def get_json(self):
        return {
            'id': self.id,
            'type': self.type,
            'price': self.price
        }

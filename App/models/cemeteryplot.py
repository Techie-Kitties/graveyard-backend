from flask_sqlalchemy import SQLAlchemy

from App.database import db
class CemeteryPlot(db.Model):
    __tablename__ = 'cemetery_plot'
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(200), nullable=False)  
    size = db.Column(db.String(50), nullable=False)  
    type = db.Column(db.String(100), nullable=False) 
    price = db.Column(db.Float, nullable=False)  

    def get_json(self):
        return {
            'id': self.id,
            'location': self.location,
            'size': self.size,
            'type': self.type,
            'price': self.price
        }

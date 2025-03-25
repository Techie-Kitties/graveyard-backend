from flask_sqlalchemy import SQLAlchemy
from App.database import db
class MemorialProgram(db.Model):
    __tablename__ = 'memorial_program'
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, nullable=False)  # Number of memorial programs
    price_per_program = db.Column(db.Float, nullable=False) 
    custom_program_included = db.Column(db.Boolean, default=False)  # True if user customized the count

    def get_json(self):
        return {
            'id': self.id,
            'count': self.count,  
            'price_per_program': self.price_per_program,
            'custom_program_included': self.custom_program_included  
        }

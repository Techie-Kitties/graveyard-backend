from flask_sqlalchemy import SQLAlchemy

from App.database import db
class ProfessionalOfficiant(db.Model):
    __tablename__ = 'professional_officiant'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether a professional officiant is included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

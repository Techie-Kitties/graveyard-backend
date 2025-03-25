from flask_sqlalchemy import SQLAlchemy

from App.database import db
class MultimediaSlideshow(db.Model):
    __tablename__ = 'multimedia_slideshow'
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    included = db.Column(db.Boolean, default=False,nullable = True)  # Whether a multimedia slideshow is included


    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class MultimediaSlideshow(db.Model):
    __tablename__ = 'multimedia_slideshow'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether a multimedia slideshow is included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

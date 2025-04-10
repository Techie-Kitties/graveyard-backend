from flask_sqlalchemy import SQLAlchemy
from App.database import db
class SocialMediaAnnouncement(db.Model):
    __tablename__ = 'social_media_announcement'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether a social media announcement is included
    price = db.Column(db.Float, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included  
        }

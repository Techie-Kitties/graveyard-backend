from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class SocialMediaAnnouncement(db.Model):
    __tablename__ = 'social_media_announcement'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether a social media announcement is included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included  
        }

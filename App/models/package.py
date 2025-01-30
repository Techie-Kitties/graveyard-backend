from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Package(db.Model):
    _tablename_ = 'packages'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    cemetery_plot = db.Column(db.String(200), nullable=True)
    grave_marker = db.Column(db.String(200), nullable=True)
    lowering_device = db.Column(db.Boolean, default=False)
    body_preparation = db.Column(db.String(200), nullable=True)
    funeral_transport = db.Column(db.String(200), nullable=True)
    family_transport = db.Column(db.Boolean, default=False)
    safekeeping_days = db.Column(db.Integer, nullable=True)
    prayer_room = db.Column(db.Boolean, default=False)
    memorial_program_count = db.Column(db.Integer, nullable=True)
    custom_programs = db.Column(db.Boolean, default=False)
    social_media_announcement = db.Column(db.Boolean, default=False)
    multimedia_slideshow = db.Column(db.Boolean, default=False)
    floral_wreath_size = db.Column(db.String(50), nullable=True)
    custom_floral_sprays = db.Column(db.Boolean, default=False)
    additional_flower_arrangements = db.Column(db.Boolean, default=False)
    professional_officiant = db.Column(db.Boolean, default=False)
    casket_type = db.Column(db.String(200), nullable=True)
    permanent_casket = db.Column(db.Boolean, default=False)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'cemetery_plot': self.cemetery_plot,
            'grave_marker': self.grave_marker,
            'lowering_device': self.lowering_device,
            'body_preparation': self.body_preparation,
            'funeral_transport': self.funeral_transport,
            'family_transport': self.family_transport,
            'safekeeping_days': self.safekeeping_days,
            'prayer_room': self.prayer_room,
            'memorial_program_count': self.memorial_program_count,
            'custom_programs': self.custom_programs,
            'social_media_announcement': self.social_media_announcement,
            'multimedia_slideshow': self.multimedia_slideshow,
            'floral_wreath_size': self.floral_wreath_size,
            'custom_floral_sprays': self.custom_floral_sprays,
            'additional_flower_arrangements': self.additional_flower_arrangements,
            'professional_officiant': self.professional_officiant,
            'casket_type': self.casket_type,
            'permanent_casket': self.permanent_casket
        }

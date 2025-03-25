from flask_sqlalchemy import SQLAlchemy
from App.database import db
from App.models.casket import Casket
from App.models.floralwreath import FloralWreaths
from App.models.flowerarrangements import FlowerArrangements
from App.models.bodypreparation import BodyPreparation
from App.models.funeraltransport import FuneralTransport
from App.models.familytransport import FamilyTransport
from App.models.professionalofficiant import ProfessionalOfficiant
from App.models.memorialprogram import MemorialProgram
from App.models.announcement import SocialMediaAnnouncement
from App.models.multimediaslideshow import MultimediaSlideshow
from App.models.prayerroom import PrayerRoom
from App.models.permanentcasket import PermanentCasket
from App.models.loweringdevice import LoweringDevice

class Package(db.Model):
    __tablename__ = 'package'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    cemetery_plot = db.Column(db.Boolean, default=False)
    grave_marker = db.Column(db.Boolean, default=False)
    body_preparation = db.Column(db.String(200), nullable=True)
    funeral_transport = db.Column(db.String(200), nullable=True)
    family_transport = db.Column(db.String(200), default=False)
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

    # lowering_device_id = db.Column(db.Integer, db.ForeignKey('lowering_device.id'), nullable=True)
    # body_preparation_id = db.Column(db.Integer, db.ForeignKey('body_preparation.id'), nullable=True)
    # funeral_transport_id = db.Column(db.Integer, db.ForeignKey('funeral_transport.id'), nullable=True)
    # family_transport_id = db.Column(db.Integer, db.ForeignKey('family_transport.id'), nullable=True)
    # floral_wreath_id = db.Column(db.Integer, db.ForeignKey('floral_wreath.id'), nullable=True)
    # flower_arrangements_id = db.Column(db.Integer, db.ForeignKey('flower_arrangements.id'), nullable=True)
    # professional_officiant_id = db.Column(db.Integer, db.ForeignKey('professional_officiant.id'), nullable=True)
    # memorial_program_id = db.Column(db.Integer, db.ForeignKey('memorial_program.id'), nullable=True)
    # social_media_announcement_id = db.Column(db.Integer, db.ForeignKey('social_media_announcement.id'), nullable=True)
    # multimedia_slideshow_id = db.Column(db.Integer, db.ForeignKey('multimedia_slideshow.id'), nullable=True)
    # prayer_room_id = db.Column(db.Integer, db.ForeignKey('prayer_room.id'), nullable=True)
    # permanent_casket_id = db.Column(db.Integer, db.ForeignKey('permanent_casket.id'), nullable=True)

    # lowering_device = db.relationship('LoweringDevice', backref='packages', lazy=True)
    # body_preparation = db.relationship('BodyPreparation', backref='packages', lazy=True)
    # funeral_transport = db.relationship('FuneralTransport', backref='packages', lazy=True)
    # family_transport = db.relationship('FamilyTransport', backref='packages', lazy=True)
    # floral_wreath = db.relationship('FloralWreaths', backref='packages', lazy=True)
    # flower_arrangements = db.relationship('FlowerArrangements', backref='packages', lazy=True)
    # professional_officiant = db.relationship('ProfessionalOfficiant', backref='packages', lazy=True)
    # memorial_program = db.relationship('MemorialProgram', backref='packages', lazy=True)
    # social_media_announcement = db.relationship('SocialMediaAnnouncement', backref='packages', lazy=True)
    # multimedia_slideshow = db.relationship('MultimediaSlideshow', backref='packages', lazy=True)
    # prayer_room = db.relationship('PrayerRoom', backref='packages', lazy=True)
    # permanent_casket = db.relationship('PermanentCasket', backref='packages', lazy=True)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'price': self.price,
            'cemetery_plot': self.cemetery_plot,
            'grave_marker': self.grave_marker,
            'body_preparation': self.body_preparation,
            'funeral_transport': self.funeral_transport,
            'family_transport': self.family_transport,
            'floral_wreath': self.floral_wreath_size,
            'memorial_program': self.memorial_program_count,
            'prayer_room': self.prayer_room,
            'professional_officiant': self.professional_officiant,
            'social_media_announcement': self.social_media_announcement,
            'multimedia_slideshow': self.multimedia_slideshow,
            'custom_programs': self.custom_programs,
            'custom_floral_sprays': self.custom_floral_sprays,
            'additional_flower_arrangements': self.additional_flower_arrangements,
            'casket_type': self.casket_type,
            'permanent_casket': self.permanent_casket,
            'safekeeping_days': self.safekeeping_days
        }

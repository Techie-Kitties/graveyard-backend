from App.database import db

class customPackage(db.Model):
    __tablename__ = 'customPackage'
    id = db.Column(db.Integer, primary_key=True, default=1)
    base_price = db.Column(db.Float, nullable=False)
    cemetery_plot_price = db.Column(db.Float, nullable=True)
    grave_marker_price = db.Column(db.Float, nullable=True)
    body_preparation_price = db.Column(db.Float, nullable=True)
    funeral_transport_price = db.Column(db.Float, nullable=True)
    family_transport_price = db.Column(db.Float, nullable=True)
    safekeeping_price_per_day = db.Column(db.Float, nullable=True)
    prayer_room_price = db.Column(db.Float, nullable=True)
    memorial_program_price_per_copy = db.Column(db.Float, nullable=True)
    custom_programs_price = db.Column(db.Float, nullable=True)
    social_media_announcement_price = db.Column(db.Float, nullable=True)
    multimedia_slideshow_price = db.Column(db.Float, nullable=True)
    floral_wreath_price = db.Column(db.Float, nullable=True)
    custom_floral_sprays_price = db.Column(db.Float, nullable=True)
    additional_flower_arrangements_price = db.Column(db.Float, nullable=True)
    professional_officiant_price = db.Column(db.Float, nullable=True)
    casket_price = db.Column(db.Float, nullable=True)
    permanent_casket_price = db.Column(db.Float, nullable=True)

    _instance = None

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            package = cls.query.first()
            if package is None:
                package = cls(base_price=0.0)
                db.session.add(package)
                db.session.commit()
            cls._instance = package
        return cls._instance

    def update(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                setattr(self, key, value)

        db.session.commit()
        return self

    def get_json(self):
        return {
            "id": self.id,
            "base_price": self.base_price,
            "cemetery_plot_price": self.cemetery_plot_price,
            "grave_marker_price": self.grave_marker_price,
            "body_preparation_price": self.body_preparation_price,
            "funeral_transport_price": self.funeral_transport_price,
            "family_transport_price": self.family_transport_price,
            "safekeeping_price_per_day": self.safekeeping_price_per_day,
            "prayer_room_price": self.prayer_room_price,
            "memorial_program_price_per_copy": self.memorial_program_price_per_copy,
            "custom_programs_price": self.custom_programs_price,
            "social_media_announcement_price": self.social_media_announcement_price,
            "multimedia_slideshow_price": self.multimedia_slideshow_price,
            "floral_wreath_price": self.floral_wreath_price,
            "custom_floral_sprays_price": self.custom_floral_sprays_price,
            "additional_flower_arrangements_price": self.additional_flower_arrangements_price,
            "professional_officiant_price": self.professional_officiant_price,
            "casket_price": self.casket_price,
            "permanent_casket_price": self.permanent_casket_price,
        }
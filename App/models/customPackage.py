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

    @classmethod
    def initialize_defaults(cls):
        #have to make sure there is no entry already
        if cls.query.first() is not None:
            return

        default_values = {
            "base_price": 1245.75,
            "cemetery_plot_price": 32.50,
            "grave_marker_price": 215.00,
            "body_preparation_price": 365.00,
            "funeral_transport_price": 425.00,
            "family_transport_price": 510.25,
            "safekeeping_price_per_day": 275.00,
            "prayer_room_price": 185.00,
            "memorial_program_price_per_copy": 22.00,
            "custom_programs_price": 120.00,
            "social_media_announcement_price": 45.00,
            "multimedia_slideshow_price": 130.00,
            "floral_wreath_price": 160.00,
            "custom_floral_sprays_price": 225.00,
            "additional_flower_arrangements_price": 95.00,
            "professional_officiant_price": 340.00,
            "casket_price": 1425.00,
            "permanent_casket_price": 3680.00,
        }

        default_package = cls(**default_values)
        db.session.add(default_package)
        db.session.commit()

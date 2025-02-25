from App.database import db
from flask_sqlalchemy import SQLAlchemy

class VirtualScene(db.Model):
    __tablename__ = "virtualscenes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    panorama_url = db.Column(db.String(200), nullable=True)  # Store the panorama image URL
    navigation_items = db.relationship(
        "NavigationItem",
        backref="virtualscene",
        lazy=True,
        cascade="all, delete-orphan"
    )
    meta_items = db.relationship(
        "MetaItem",
        backref="virtualscene",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __init__(self, name, panorama_url, navigation_items=None, meta_items=None):
        self.name = name
        self.panorama_url = panorama_url
        self.navigation_items = navigation_items if navigation_items else []
        self.meta_items = meta_items if meta_items else []

    def get_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "panorama_url": self.panorama_url,
            "navigation_items": [item.get_json() for item in self.navigation_items],
            "meta_items": [meta.get_json() for meta in self.meta_items]
        }
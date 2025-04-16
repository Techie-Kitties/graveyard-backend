from App.database import db


class VirtualScene(db.Model):
    __tablename__ = "virtualscenes"
    id = db.Column(db.Integer, primary_key=True)
    panorama_url = db.Column(db.String(200), nullable=True, unique=True)

    outgoing_navigation = db.relationship(
        "NavigationItem",
        foreign_keys="[NavigationItem.source_scene_id]",
        back_populates="source_scene_rel",
        cascade="all, delete-orphan"
    )

    incoming_navigation = db.relationship(
        "NavigationItem",
        foreign_keys="[NavigationItem.target_scene_id]",
        back_populates="target_scene_rel"
    )

    meta_items = db.relationship(
        "MetaItem",
        backref="virtualscene",
        cascade="all, delete-orphan"
    )

    def __init__(self, panorama_url=None):
        self.panorama_url = panorama_url

    def get_json(self):
        return {
            "id": self.id,
            "panorama_url": self.panorama_url,
            "arrows": [item.get_json() for item in self.outgoing_navigation],
            "highlights": [meta.get_json() for meta in self.meta_items]
        }
    @classmethod
    def get_by_id(cls, scene_id):
        return cls.query.get(scene_id)
    @classmethod
    def get_by_panorama_url(cls, panorama_url):
        return cls.query.filter_by(panorama_url=panorama_url).first()

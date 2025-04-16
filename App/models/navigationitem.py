
from App.database import db
class NavigationItem(db.Model):
    __tablename__ = "navigationitems"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.JSON, nullable=False)
    source_scene_id = db.Column(db.Integer, db.ForeignKey('virtualscenes.id'), nullable=False)
    target_scene_id = db.Column(db.Integer, db.ForeignKey('virtualscenes.id'), nullable=False)

    source_scene_rel = db.relationship(
        'VirtualScene',
        foreign_keys=[source_scene_id],
        back_populates='outgoing_navigation'
    )
    target_scene_rel = db.relationship(
        'VirtualScene',
        foreign_keys=[target_scene_id],
        back_populates='incoming_navigation'
    )

    def __init__(self, position, source_scene_id, target_scene_id):
        self.position = position
        self.source_scene_id = source_scene_id
        self.target_scene_id = target_scene_id

    def get_json(self):
        return {
            "id": self.id,
            "position": self.position,
            "source_scene_id": self.source_scene_id,
            "target_scene_id": self.target_scene_id,
            "panorama": self.target_scene_id  # For frontend compatibility
        }
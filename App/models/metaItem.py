from App.database import db
from flask_sqlalchemy import SQLAlchemy

class MetaItem(db.Model):
    __tablename__ = "metaitems"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.JSON, nullable=False)
    label = db.Column(db.String, nullable=True)
    color = db.Column(db.Integer, nullable=True)
    virtualscene_id = db.Column(db.Integer, db.ForeignKey('virtualscenes.id'), nullable=False)

    def __init__(self, position, virtualscene_id, label=None, color=None):
        self.position = position
        self.virtualscene_id = virtualscene_id
        self.label = label
        self.color = color

    def get_json(self):
        return {
            "id": self.id,
            "position": self.position,
            "virtualscene_id": self.virtualscene_id,
            "label": self.label,
            "color": self.color
        }

    def __repr__(self):
        return f"<MetaItem {self.id}, VirtualScene {self.virtualscene_id}>"
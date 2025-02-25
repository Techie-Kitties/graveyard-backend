from App.database import db
from flask_sqlalchemy import SQLAlchemy


class NavigationItem(db.Model):
    __tablename__ = "navigationitems"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.JSON, nullable=False)
    virtualscene_id = db.Column(db.Integer, db.ForeignKey('virtualscenes.id'), nullable=False)

    def __init__(self, position, virtualscene_id):
        self.position = position
        self.virtualscene_id = virtualscene_id

    def get_json(self):
        return {
            "id": self.id,
            "position": self.position,
            "virtualscene_id": self.virtualscene_id
        }
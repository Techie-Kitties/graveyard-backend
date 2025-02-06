from App.database import db
from flask_sqlalchemy import SQLAlchemy


class NavigationItem(db.Model):
    __tablename__ = "navigationitems"
    id = db.Column(db.Integer, primary_key=True)
    position = db.Column(db.JSON, nullable=False)

    def get_json(self):
        return {
            "id": self.id,
            "position": self.position
        }

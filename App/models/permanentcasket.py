from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class PermanentCasket(db.Model):
    __tablename__ = 'permanent_casket'
    id = db.Column(db.Integer, primary_key=True)
    included = db.Column(db.Boolean, default=False)  # Whether a permanent casket is included

    def get_json(self):
        return {
            'id': self.id,
            'included': self.included
        }

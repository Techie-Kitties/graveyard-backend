from App.models import VirtualScene,MetaItem
from App.database import db

def createScene(name, navigationItems, metaItems):
    scene = VirtualScene(name=name)
    db.session.add(scene)
    db.session.commit()
    return scene
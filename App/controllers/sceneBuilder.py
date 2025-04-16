from App.models import VirtualScene,MetaItem
from App.database import db

def createScene( navigationItems, metaItems,panorama_url):
    scene = VirtualScene(panorama_url=panorama_url,meta_items=metaItems,navigation_items=navigationItems)
    db.session.add(scene)
    db.session.commit()
    return scene
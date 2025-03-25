import json

from App.database import db
from App.models.package import *

# def init_components():

def init_packages():
    Package.query.delete()
    
    try:
        basic_package = Package(
            name="Basic Package",
            description="Essential funeral services with standard options",
            price=7000.00,
            cemetery_plot=True,
            grave_marker=True,
            body_preparation="Standard",
            funeral_transport="Standard Coach",
            family_transport=True,
            floral_wreath_size="Small",
            memorial_program_count=50,
            prayer_room=True,
            professional_officiant=True,
            social_media_announcement=True,
            multimedia_slideshow=True
        )
        
        standard_package = Package(
            name="Standard Package",
            description="Enhanced funeral services with upgraded options",
            price=12000.00,
            cemetery_plot=True,
            grave_marker=True,
            body_preparation="Premium",
            funeral_transport="Standard Coach",
            family_transport=True,
            floral_wreath_size="Medium",
            memorial_program_count=50,
            prayer_room=True,
            professional_officiant=True,
            social_media_announcement=True,
            multimedia_slideshow=True
        )
        
        premium_package = Package(
            name="Premium Package",
            description="Luxury funeral services with premium options",
            price=20000.00,
            cemetery_plot=True,
            grave_marker=True,
            body_preparation="Premium",
            funeral_transport="Luxury Coach",
            family_transport=True,
            floral_wreath_size="Large",
            memorial_program_count=100,
            prayer_room=True,
            professional_officiant=True,
            social_media_announcement=True,
            multimedia_slideshow=True
        )
        
        db.session.add(basic_package)
        db.session.add(standard_package)
        db.session.add(premium_package)
        db.session.commit()
            
    except Exception as e:
        db.session.rollback()
        raise e

def get_all_packages():
    packages = Package.query.all()
    return [package.get_json() for package in packages]

def create_package(json_data):
    try:
        data = json.loads(json_data)

        package = Package(
            name=data.get('name'),
            description=data.get('description', None),
            price=float(data.get('price', 0)),
            body_preparation=data.get('body_preparation', None),
            funeral_transport=data.get('funeral_transport', None),
            family_transport=data.get('family_transport', False),
            floral_wreath_size=data.get('floral_wreath', None),
            memorial_program_count=int(data.get('memorial_program', 0)),
            prayer_room=data.get('prayer_room', False),
            professional_officiant=data.get('professional_officiant', False),
            social_media_announcement=data.get('social_media_announcement', False),
            multimedia_slideshow=data.get('multimedia_slideshow', False),
            grave_marker=data.get('grave_marker', False),
            custom_programs=data.get('custom_programs', False),
            custom_floral_sprays=data.get('custom_floral_sprays', False),
            additional_flower_arrangements=data.get('additional_flower_arrangements', False),
            casket_type=data.get('casket_type', None),
            permanent_casket=data.get('permanent_casket', False),
            safekeeping_days=data.get('safekeeping_days', None)
        )

        db.session.add(package)
        db.session.commit()
        return package

    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format provided.")
    except Exception as e:
        raise ValueError(e)

def delete_package(package_id):
    try:
        package = Package.query.get(package_id)
        if package:
            db.session.delete(package)
            db.session.commit()
            return True
        return False
    except Exception as e:
        db.session.rollback()
        raise ValueError(e)

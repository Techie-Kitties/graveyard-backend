import json
import os

from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt, get_jwt_identity
from datetime import datetime, date
from werkzeug.utils import secure_filename
from App.database import db
from App.models import NavigationItem,MetaItem,VirtualScene,User
from App.controllers.sceneBuilder import createScene
tour_views = Blueprint('tour_views', __name__, template_folder='../templates')


@tour_views.route('/api/addImage', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def addScene():
    user_id =  get_jwt_identity()
    print(user_id)
    user = User.query.filter_by(id=user_id).first()
    if user.role != 1:
        print("User role is ",user.role )
        return "Error"

    # print("Got request")
    upload_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'static', 'images', 'panoramas')
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    if 'panorama' not in request.files:
        return jsonify({"error": "No image files provided"}), 400
    files = request.files.getlist('panorama')
    print(files)
    if not files:
        return jsonify({"error": "No files to upload"}), 400
    filenames = []
    for file in files:
        extension = os.path.splitext(file.filename)[1].lower()
        print(extension)
        if extension not in ['.jpg', '.jpeg', '.png', '.webp']:
            return jsonify({"error": f"Invalid file type for {file.filename}"}), 400

        filename = secure_filename(str(datetime.timestamp(datetime.now())) + extension)
        file_path = os.path.join(upload_folder, filename)
        file.save(file_path)
        filenames.append(filename)
    return jsonify({"message": "Virtual scene uploaded successfully", "filenames": filenames}), 200

@tour_views.route('/api/getImages', methods=['get'])
def list_files():
    image_folder = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
    try:
        files = os.listdir(image_folder)
        valid_extensions = {"jpg", "png", "webp", "jpeg"}
        image_files = [file for file in files if file.split(".")[-1].lower() in valid_extensions]
        image_urls = [url_for("static", filename=f"images/panoramas/{image}") for image in image_files]
        print(image_urls)
        return jsonify(image_urls)


    except Exception as e:
        return jsonify({"error": str(e)}), 500


@tour_views.route('/api/getAllScenes')
def get_all_scenes():
    scenes = VirtualScene.query.all()
    image_folder = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
    files = sorted([
        f for f in os.listdir(image_folder)
        if f.split(".")[-1].lower() in {"jpg", "png", "webp", "jpeg"}
    ])


    existing_filenames = {os.path.basename(scene.panorama_url) for scene in scenes}


    new_scenes = []
    for file in files:
        if file not in existing_filenames:
            new_scene = VirtualScene(panorama_url=f"static/images/panoramas/{file}")
            db.session.add(new_scene)
            new_scenes.append(new_scene)

    if new_scenes:
        db.session.commit()
        scenes.extend(new_scenes)

    result = []
    for index, scene in enumerate(scenes):
        scene_data = {
            "currentPanorama": scene.panorama_url,
            "arrows": [],
            "highlights": []
        }

        for arrow in scene.outgoing_navigation:
            target_url = arrow.target_scene_rel.panorama_url
            target_filename = os.path.basename(target_url)
            try:
                target_index = files.index(target_filename)
                scene_data["arrows"].append({
                    "position": arrow.position,
                    "panorama": target_index
                })
            except ValueError:
                continue


        for highlight in scene.meta_items:
            scene_data["highlights"].append({
                "position": highlight.position,
                "label": highlight.label,
                "color": highlight.color
            })

        result.append(scene_data)

    return jsonify({"scenes": result})

@tour_views.route('/api/saveScene', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def save_scene_items():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    # if user.role != 1:
    #     return
    try:
        data = request.get_json()
    except Exception as e:
        print("Failed to parse JSON:", str(e))
        return jsonify({"error": "Invalid JSON"}), 400

    print("Received data:", data)
    if not data:
        return jsonify({"error": "Missing JSON data"}), 400

    panorama_url = data.get("currentPanorama")
    arrows = data.get("arrows", [])
    print(arrows)
    highlights = data.get("highlights", [])

    if not panorama_url:
        return jsonify({"error": "Missing panorama URL"}), 400

    source_scene = VirtualScene.query.filter_by(panorama_url=panorama_url).first()

    if not source_scene:
        source_scene = VirtualScene(panorama_url=panorama_url)
        db.session.add(source_scene)
        db.session.commit()

    NavigationItem.query.filter_by(source_scene_id=source_scene.id).delete()


    image_folder = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
    files = sorted([
        f for f in os.listdir(image_folder)
        if f.split(".")[-1].lower() in {"jpg", "png", "webp", "jpeg"}
    ])

    for arrow in arrows:
        target_index = arrow.get("panorama")
        position = arrow.get("position")

        if (
            target_index is None or
            not (0 <= target_index < len(files)) or
            not position or len(position) != 3
        ):
            continue

        target_url = f"static/images/panoramas/{files[target_index]}"
        target_scene = VirtualScene.query.filter_by(panorama_url=target_url).first()

        if not target_scene:
            target_scene = VirtualScene(panorama_url=target_url)
            db.session.add(target_scene)

        nav_item = NavigationItem(
            position=json.dumps(position),
            source_scene_id=source_scene.id,
            target_scene_id=target_scene.id
        )
        db.session.add(nav_item)

    for highlight in highlights:
        position = highlight.get("position")
        if not position or len(position) != 3:
            continue

        meta_item = MetaItem(
            position=json.dumps(position),
            label=highlight.get("label", ""),
            color=highlight.get("color", 16776960),
            virtualscene_id=source_scene.id
        )
        db.session.add(meta_item)

    try:
        db.session.commit()
        # print("COMMIT")
        return jsonify(source_scene.get_json()), 200
    except Exception as e:
        db.session.rollback()
        print("Error saving scene:", str(e))
        return jsonify({"error": "Failed to save scene"}), 500

@tour_views.route('/api/removeImage/<filename>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
@jwt_required()
def remove_image(filename):

    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    if user.role != 1:
        return
    panorama_dir = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
    try:
        safe_filename = secure_filename(filename)
        if not safe_filename:
            return jsonify({"error": "Invalid filename"}), 400
        valid_extensions = {"jpg", "png", "webp", "jpeg"}
        file_ext = safe_filename.split('.')[-1].lower()
        if file_ext not in valid_extensions:
            return jsonify({"error": "Invalid file type"}), 400

        file_path = os.path.join(panorama_dir, safe_filename)
        panorama_url = f"static/images/panoramas/{safe_filename}"
        if not os.path.exists(file_path):
            return jsonify({"error": "File not found"}), 404
        scene = VirtualScene.query.filter_by(panorama_url=panorama_url).first()
        deleted_scene_id = scene.id if scene else None

        if scene:
            NavigationItem.query.filter(
                (NavigationItem.source_scene_id == scene.id) |
                (NavigationItem.target_scene_id == scene.id)
            ).delete()
            MetaItem.query.filter_by(virtualscene_id=scene.id).delete()
            db.session.delete(scene)
        db.session.commit()
        try:
            os.remove(file_path)
        except OSError as e:
            return jsonify({
                "error": f"File deletion failed: {str(e)}",
                "database_cleanup_complete": True,
                "deleted_scene_id": deleted_scene_id
            }), 500

        return jsonify({
            "message": "Image and associated data deleted successfully",
            "filename": safe_filename,
            "deleted_scene_id": deleted_scene_id
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({
            "error": str(e),
            "message": "Operation rolled back due to error"
        }), 500

@tour_views.route('/api/saveAllScenes', methods=['POST'])
@cross_origin(supports_credentials=True)
@jwt_required()
def save_all_scenes():
    user_id = get_jwt_identity()
    user = User.query.filter_by(id=user_id).first()
    if user.role != 1:
        return
    data = request.get_json()
    print(data)
    if not data or 'scenes' not in data:
        return jsonify({"error": "Missing scenes data"}), 400

    try:
        db.session.query(NavigationItem).delete()
        db.session.query(MetaItem).delete()
        db.session.query(VirtualScene).delete()
        db.session.commit()

        for scene_data in data['scenes']:
            panorama_index = scene_data.get("currentPanorama")
            arrows = scene_data.get("arrows", [])
            highlights = scene_data.get("highlights", [])


            image_folder = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
            files = sorted([
                f for f in os.listdir(image_folder)
                if f.split(".")[-1].lower() in {"jpg", "png", "webp", "jpeg"}
            ])

            if panorama_index is None or panorama_index >= len(files):
                continue

            panorama_url = f"static/images/panoramas/{files[panorama_index]}"

            scene = VirtualScene(panorama_url=panorama_url)
            db.session.add(scene)
            db.session.flush()


            for arrow in arrows:
                pos = arrow.get("position")
                nav_item = NavigationItem(position=pos, virtualscene_id=scene.id)
                scene.navigation_items.append(nav_item)

            for highlight in highlights:
                pos = highlight.get("position")
                label = highlight.get("label", "")
                color = highlight.get("color", 16776960)
                meta_item = MetaItem(position=pos, label=label, virtualscene_id=scene.id)
                meta_item.color = color
                scene.meta_items.append(meta_item)

        db.session.commit()
        return jsonify({"success": True, "message": "success"})

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
import os

from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date

from werkzeug.utils import secure_filename

tour_views = Blueprint('tour_views', __name__, template_folder='../templates')


@tour_views.route('/api/add', methods=['POST'])
def addScene():
    upload_folder = os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'static', 'images', 'panoramas')
    if 'panorama' not in request.files:
        return jsonify({"error": "No panorama file provided"}), 400
    file = request.files['panorama']
    extension = os.path.splitext(file.filename)[1]
    if extension not in ['.jpg', '.jpeg', '.png',"webp"]:
        return jsonify({"error": "Invalid file type"}), 400
    folder = upload_folder
    filename = secure_filename(str(datetime.timestamp(datetime.now())) + extension)
    # print(file.filename)
    # print(filename)
    file.save(os.path.join(folder, filename))
    navigation_items = request.json["navItems"]
    meta_items = request.json["metaItems"]

    return jsonify({"message": "Virtual scene uploaded successfully"}), 200

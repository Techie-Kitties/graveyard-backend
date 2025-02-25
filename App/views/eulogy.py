import os

from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for, redirect, session, \
    make_response
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt
from datetime import datetime, date

from App.controllers import (
    generate_eulogy,
    oauth_google,
    google_callback
)

graveyard_views = Blueprint('graveyard_views', __name__, template_folder='../templates')


@graveyard_views.route('/api/generateEulogy', methods=['POST'])
def create_eulogy():
    data = request.json
    name = data.get('name')
    birth_date = data.get('birth_date')
    death_date = data.get('death_date')
    relationships = data.get('relationships')
    occupation = data.get('occupation')
    personality_traits = data.get('personality_traits')
    hobbies = data.get('hobbies')
    accomplishments = data.get('accomplishments')
    anecdotes = data.get('anecdotes')
    tone = data.get('tone')
    return generate_eulogy(name, birth_date, death_date, relationships, occupation, personality_traits, hobbies,
                           accomplishments, anecdotes, tone)


@graveyard_views.route('/api/getImages', methods=['get'])
def list_files():
    image_folder = os.path.join(os.path.dirname(__file__), "..", "static/images/panoramas")
    try:
        files = os.listdir(image_folder)
        valid_extensions = {"jpg", "png", "webp", "jpeg"}
        image_files = [file for file in files if file.split(".")[-1].lower() in valid_extensions]
        image_urls = [url_for("static", filename=f"/images/panoramas/{image}") for image in image_files]
        return jsonify(image_urls)

    except Exception as e:
        return jsonify({"error": str(e)}), 500





@graveyard_views.route('/login_google', methods=['get'])
def login_google():
    return oauth_google()


# @graveyard_views.route('/api/fetchUser', methods=['GET'])
# @cross_origin(supports_credentials=True)
# def fetch_user():
#     print(f"Session Data FETCH: {session.get('google_data')}")
#     print("DATA:", session.keys())
#     data = session.get('google_data')
#     return jsonify(data)


@graveyard_views.route('/callback', methods=['GET'])
@cross_origin(supports_credentials=True)
def callback_google():
    response = google_callback()
    # status_code = response.status_code
    data = response.get_json()
    session['google_data'] = {
        "id": data.get("id"),
        "email": data.get("email"),
        "name": data.get("name"),
        "picture": data.get("picture")
    }

    redirect_response = redirect("http://localhost:3000/auth")
    google_data = session.get('google_data', {})
    for key, value in google_data.items():
        redirect_response.set_cookie(
            key=key,
            value=str(value),
            samesite='None',
            secure=True
        )

    return redirect_response

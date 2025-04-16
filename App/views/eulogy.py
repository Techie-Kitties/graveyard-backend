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
@cross_origin( supports_credentials=True)
@jwt_required()
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









# @graveyard_views.route('/api/fetchUser', methods=['GET'])
# @cross_origin(supports_credentials=True)
# def fetch_user():
#     print(f"Session Data FETCH: {session.get('google_data')}")
#     print("DATA:", session.keys())
#     data = session.get('google_data')
#     return jsonify(data)




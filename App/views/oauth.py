import os
from flask import Blueprint, render_template, jsonify, request, send_from_directory, url_for, redirect, session, \
    make_response
from flask_cors import cross_origin
from flask_jwt_extended import jwt_required, get_jwt, current_user, get_jwt_identity, verify_jwt_in_request, \
    unset_jwt_cookies
from datetime import datetime, date

from App.controllers import (
    generate_eulogy,
    oauth_google,
    google_callback,
    login_google_controller,
)

from App.models import User

oauth_views = Blueprint('oauth_views', __name__, template_folder='../templates')


@oauth_views.route('/login_google', methods=['get'])
def login_google():
    return oauth_google()


@oauth_views.route('/identity', methods=['GET'])
@cross_origin(supports_credentials=True)
@jwt_required()
def check_identity():
    try:
        current_user_id = get_jwt_identity()
        # print("Identity is:", current_user_id)
        user = None
        if isinstance(current_user_id, int) or str(current_user_id).isdigit():
            user = User.query.get(int(current_user_id))
        else:
            user = User.query.filter_by(username=current_user_id).first()

        if not user:
            return jsonify({"msg": "User not found"}), 404

        return jsonify({
            "id": user.id,
            "username": user.username,
            "role": user.role
        })

    except Exception as e:
        return jsonify({"msg": "Missing or invalid token", "error": str(e)}), 401
@oauth_views.route('/callback', methods=['GET'])
@cross_origin(supports_credentials=True)
def callback_google():
    user_info, status_code = google_callback()
    print(status_code)
    if status_code != 200:
        return user_info, status_code

    redirect_response = redirect("http://localhost:3000/auth")
    google_data = session.get('google_data', {})
    jwt_token = login_google_controller(google_data)
    print(jwt_token)

    for key, value in google_data.items():
        redirect_response.set_cookie(
            key=key,
            value=str(value),
            samesite='None',
            secure=True,
            httponly=False,
        )

    redirect_response.set_cookie(
        key='jwt_token',
        value=jwt_token,
        samesite='None',
        secure=True,
        httponly=False
    )

    return redirect_response


@oauth_views.route("/logout", methods=["POST"])
@cross_origin(supports_credentials=True)
@jwt_required()
def logout():
    response = jsonify({"msg": "Logout successful"})
    unset_jwt_cookies(response)
    return response

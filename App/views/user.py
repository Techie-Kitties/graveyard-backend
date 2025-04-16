from datetime import timedelta

from flask import Blueprint, render_template, jsonify, request, send_from_directory, redirect
from flask_cors import CORS, cross_origin
from flask_jwt_extended import jwt_required, create_access_token, get_jwt, set_access_cookies
from App.models import User

from App.controllers import (
    create_user, 
    get_all_users,
    get_user,
    get_user_by_username,
    delete_user,
    login
    # authenticate,
    # identity
)
from werkzeug.security import generate_password_hash

user_views = Blueprint('user_views', __name__, template_folder='../templates')

@user_views.route('/api/users', methods=['POST'])
def create_user_route():
    data = request.json
    if not 'username' in data or not 'password' in data or not 'role' in data:
        return jsonify({"message":"Missing parameters"}), 400

    if not 'id' in data:
        user = create_user(data['username'], data['password'], data['role'])
    else:
        user = get_user(data['id'])
        if user.exists:
            return jsonify({"message":"Id already in use"}), 400
        user = create_user(data['username'], data['password'], data['role'], data['id'])

    return jsonify({"message":"User Created"}), 201

@user_views.route('/api/users', methods=['GET'])
def get_users_route():
    id = request.args.get('id')
    username = request.args.get('username')

    if id:
        user = get_user(id)
        if user.exists:
            user_dict = user.to_dict()
            user_dict['id'] = user.id
            return user_dict, 200
        return jsonify({"message":"User Not Found"}), 404

    if username:
        users = get_user_by_username(username)
        if users:
            users_array = []
            for user in users:
                user_dict = user.to_dict()
                user_dict['id'] = user.id
                users_array.append(user_dict)
            return jsonify(users_array), 200
        return jsonify({"message":"User Not Found"}), 404

    users = get_all_users()
    users_array = []
    for user in users:
        user_dict = user.to_dict()
        user_dict['id'] = user.id
        users_array.append(user_dict)
    return jsonify(users_array), 200

@user_views.route('/api/users', methods=['DELETE'])
@jwt_required()
def delete_user_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    user = get_user(id)
    if user.exists:
        delete_user(id)
        return jsonify({"message":"User Deleted"}), 200
    return jsonify({"message":"User Not Found"}), 404


@user_views.route("/login", methods=["POST"])
@cross_origin(supports_credentials=True)
def login_route():
    data = request.json
    if not data or 'username' not in data or 'password' not in data:
        print("No")
        return jsonify({"message": "Missing username or password"}), 400

    username = data['username']
    password = data['password']
    print(username,password)
    access_token = login(username=username, password=password)

    if access_token is None:
        print("Nopp")
        return jsonify({"msg": "Invalid username or password"}), 401

    resp = jsonify({"msg": "Login successful"})

    set_access_cookies(resp, access_token)
    resp.set_cookie("username", username, max_age=3600,httponly=False, samesite='Strict')
    resp.location = "http://localhost:3000/auth"

    return resp, 200

@user_views.route("/register", methods=["POST"])
@cross_origin()
def register_user():
    data = request.get_json()

    if not data or 'username' not in data or 'password' not in data:
        return jsonify({"message": "Missing required fields"}), 400

    username = data['username']
    password = data['password']
    print(password)
    new_user = create_user(username=username, password=password)
    if isinstance(new_user, User):
        return jsonify({
            "message": "User registered successfully",
            "user": {
                "id": new_user.id,
                "username": new_user.username,
                "role": new_user.role
            }
        }), 201
    else:
        return jsonify({"message": "User is already registered"}), 409
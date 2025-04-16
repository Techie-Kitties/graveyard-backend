import json
import os
import requests

from flask import redirect, jsonify, request, session

key_path = os.path.join(os.path.dirname(__file__), "../key.json")
with open(key_path, "r") as file:
    config = json.load(file)


def oauth_google():
    client_id = "1021515142000-1vibql027boo1al57577451c0pui1v9e.apps.googleusercontent.com"
    redirect_uri = "http://localhost:8080/callback"
    scope = "https://www.googleapis.com/auth/userinfo.email https://www.googleapis.com/auth/userinfo.profile"
    auth_url = f"https://accounts.google.com/o/oauth2/auth?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}"
    return redirect(auth_url)


def google_callback():
    print("Google callback is running")

    code = request.args.get("code")
    if not code:
        return jsonify({"error": "Authorization code not found"}), 400

    token_url = "https://oauth2.googleapis.com/token"
    client_id = config.get("client_id")
    client_secret = config.get("client_secret")
    # print(client_id)
    # print(client_secret)
    redirect_uri = "http://localhost:8080/callback"

    data = {
        "code": code,
        "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": redirect_uri,
        "grant_type": "authorization_code",
    }

    try:
        token_response = requests.post(token_url, data=data, timeout=10)
        token_response.raise_for_status()
        token_json = token_response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to retrieve access token", "details": str(e)}), 400

    if "access_token" not in token_json:
        return jsonify({"error": "Failed to retrieve access token", "details": token_json}), 400

    access_token = token_json["access_token"]

    user_info_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    headers = {"Authorization": f"Bearer {access_token}"}

    try:
        user_info_response = requests.get(user_info_url, headers=headers, timeout=10)
        user_info_response.raise_for_status()
        user_info = user_info_response.json()
    except requests.exceptions.RequestException as e:
        return jsonify({"error": "Failed to retrieve user info", "details": str(e)}), 400

    session['google_data'] = {
        "id": user_info.get("id"),
        "email": user_info.get("email"),
        "name": user_info.get("name"),
        "picture": user_info.get("picture")
    }

    print(session['google_data'])
    return jsonify(user_info), 200

from flask import Blueprint, render_template, jsonify, request, send_from_directory
from flask_jwt_extended import jwt_required, get_jwt

from App.controllers import (
    create_graveyard, 
    get_all_graveyards,
    get_graveyard,
    get_graveyard_by_name,
    get_graveyard_by_owner_id,
    get_graveyard_by_user_access,
    delete_graveyard,
    add_access,
    update_price,
    get_user
)

graveyard_views = Blueprint('graveyard_views', __name__, template_folder='../templates')

@graveyard_views.route('/api/graveyards', methods=['POST'])
@jwt_required()
def create_graveyard_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'name' in data or not 'location' in data or not 'max_plots' in data or not 'owner_id' in data or not 'single_price' in data or not 'companion_price' in data or not 'family_price' in data:
        return jsonify({"message":"Missing parameters"}), 400

    if not 'id' in data:
        graveyard = create_graveyard(data['name'], data['location'], data['max_plots'], data['owner_id'], data['single_price'], data['companion_price'], data['family_price'])
    else:
        graveyard = get_graveyard(data['id'])
        if graveyard.exists:
            return jsonify({"message":"Id already in use"}), 400
        graveyard = create_graveyard(data['name'], data['location'], data['max_plots'], data['owner_id'], data['single_price'], data['companion_price'], data['family_price'], data['id'])

    return jsonify({"message":"graveyard Created"}), 201

@graveyard_views.route('/api/graveyards', methods=['GET'])
@jwt_required()
def get_graveyards_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    name = request.args.get('name')
    owner_id = request.args.get('owner_id')
    user_id = request.args.get('user_id')

    if id:
        graveyard = get_graveyard(id)
        if graveyard.exists:
            graveyard_dict = graveyard.to_dict()
            graveyard_dict['id'] = graveyard.id
            return graveyard_dict, 200
        return jsonify({"message":"graveyard Not Found"}), 404

    if name:
        graveyards = get_graveyard_by_name(name)
        if graveyards:
            graveyards_array = []
            for graveyard in graveyards:
                graveyard_dict = graveyard.to_dict()
                graveyard_dict['id'] = graveyard.id
                graveyards_array.append(graveyard_dict)
            return jsonify(graveyards_array), 200
        return jsonify({"message":"graveyard Not Found"}), 404

    if owner_id:
        graveyards = get_graveyard_by_owner_id(owner_id)
        if graveyards:
            graveyards_array = []
            for graveyard in graveyards:
                graveyard_dict = graveyard.to_dict()
                graveyard_dict['id'] = graveyard.id
                graveyards_array.append(graveyard_dict)
            return jsonify(graveyards_array), 200
        return jsonify({"message":"graveyard Not Found"}), 404

    if user_id:
        graveyards = get_graveyard_by_user_access(user_id)
        if graveyards:
            graveyards_array = []
            for graveyard in graveyards:
                graveyard_dict = graveyard.to_dict()
                graveyard_dict['id'] = graveyard.id
                graveyards_array.append(graveyard_dict)
            return jsonify(graveyards_array), 200
        return jsonify({"message":"graveyard Not Found"}), 404

    graveyards = get_all_graveyards()
    graveyards_array = []
    for graveyard in graveyards:
        graveyard_dict = graveyard.to_dict()
        graveyard_dict['id'] = graveyard.id
        graveyards_array.append(graveyard_dict)
    return jsonify(graveyards_array), 200

@graveyard_views.route('/api/graveyards', methods=['DELETE'])
@jwt_required()
def delete_graveyard_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    graveyard = get_graveyard(id)
    if graveyard.exists:
        delete_graveyard(id)
        return jsonify({"message":"Graveyard Deleted"}), 200
    return jsonify({"message":"Graveyard Not Found"}), 404

@graveyard_views.route('/api/graveyards', methods=['PUT'])
@jwt_required()
def add_graveyards_access_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'graveyard_id' in data or not 'user_id' in data:
        return jsonify({"message":"Missing parameters"}), 400

    graveyard = get_graveyard(data['graveyard_id'])
    if not graveyard.exists:
        return jsonify({"message":"Graveyard Not Found"}), 404
    user = get_user(data['user_id'])
    if not user.exists:
        return jsonify({"message":"User Not Found"}), 404

    add_access(data['graveyard_id'], data['user_id'])
    return jsonify({"message":"User access added"}), 200


@graveyard_views.route('/api/graveyards/price', methods=['PUT'])
@jwt_required()
def update_graveyards_price_route():
    jwt = get_jwt()
    if jwt['role'] > 1:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'graveyard_id' in data:
        return jsonify({"message":"Missing graveyard_id"}), 400

    graveyard = get_graveyard(data['graveyard_id'])
    if not graveyard.exists:
        return jsonify({"message":"Graveyard Not Found"}), 404

    if 'single_price' in data:
        single_price = data['single_price']
    else:
        single_price = None

    if 'companion_price' in data:
        companion_price = data['companion_price']
    else:
        companion_price = None

    if 'family_price' in data:
        family_price = data['family_price']
    else:
        family_price = None

    update_price(graveyard_id=data['graveyard_id'], single_price=single_price, companion_price=companion_price, family_price=family_price)
    return jsonify({"message":"Graveyard prices updated"}), 200
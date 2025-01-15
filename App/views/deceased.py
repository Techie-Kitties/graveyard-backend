from flask import Blueprint, render_template, jsonify, request, send_from_directory
from datetime import datetime
from flask_jwt_extended import jwt_required, get_jwt


from App.controllers import (
    create_deceased, 
    get_all_deceaseds,
    get_deceased,
    get_deceased_by_name,
    get_deceased_by_grave,
    get_deceased_by_graveyard,
    delete_deceased,
    get_grave,
    grave_available,
    update_grave
)

deceased_views = Blueprint('deceased_views', __name__, template_folder='../templates')

@deceased_views.route('/api/deceaseds', methods=['POST'])
@jwt_required()
def create_deceased_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    data = request.json
    if not 'name' in data or not 'date_of_birth' in data or not 'date_of_death' in data or not 'cause_of_death' in data or not 'grave_id' in data:
        return jsonify({"message":"Missing parameters"}), 400

    grave = get_grave(data['grave_id'])
    if not grave.exists:
        return jsonify({"message":"Grave does not exist"}), 404
    if not grave_available(data['grave_id']):
        return jsonify({"message":"Grave is not available"}), 400

    if not 'id' in data:
        deceased = create_deceased(data['name'], data['date_of_birth'], data['date_of_death'], data['cause_of_death'], data['grave_id'])
    else:
        deceased = get_deceased(data['id'])
        if deceased.exists:
            return jsonify({"message":"Id already in use"}), 400
        deceased = create_deceased(data['name'], data['date_of_birth'], data['date_of_death'], data['cause_of_death'], data['grave_id'], data['id'])

    update_grave(data['grave_id'], datetime.today())
    return jsonify({"message":"deceased Created"}), 201

@deceased_views.route('/api/deceaseds', methods=['GET'])
@jwt_required()
def get_deceaseds_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    name = request.args.get('name')
    grave_id = request.args.get('grave_id')
    graveyard_id = request.args.get('graveyard_id')

    if id:
        deceased = get_deceased(id)
        if deceased.exists:
            deceased_dict = deceased.to_dict()
            deceased_dict['id'] = deceased.id
            return deceased_dict, 200
        return jsonify({"message":"deceased Not Found"}), 404

    if name:
        deceaseds = get_deceased_by_name(name)
        if deceaseds:
            deceaseds_array = []
            for deceased in deceaseds:
                deceased_dict = deceased.to_dict()
                deceased_dict['id'] = deceased.id
                deceaseds_array.append(deceased_dict)
            return jsonify(deceaseds_array), 200
        return jsonify({"message":"deceased Not Found"}), 404

    if grave_id:
        deceaseds = get_deceased_by_grave(grave_id)
        if deceaseds:
            deceaseds_array = []
            for deceased in deceaseds:
                deceased_dict = deceased.to_dict()
                deceased_dict['id'] = deceased.id
                deceaseds_array.append(deceased_dict)
            return jsonify(deceaseds_array), 200
        return jsonify({"message":"grave Not Found"}), 404

    if graveyard_id:
        deceaseds = get_deceased_by_graveyard(graveyard_id)
        if deceaseds:
            return jsonify(deceaseds), 200
        return jsonify({"message":"graveyard Not Found"}), 404

    deceaseds = get_all_deceaseds()
    deceaseds_array = []
    for deceased in deceaseds:
        deceased_dict = deceased.to_dict()
        deceased_dict['id'] = deceased.id
        deceaseds_array.append(deceased_dict)
    return jsonify(deceaseds_array), 200

@deceased_views.route('/api/deceaseds', methods=['DELETE'])
@jwt_required()
def delete_deceased_route():
    jwt = get_jwt()
    if jwt['role'] > 2:
        return jsonify({"message":"Not Authorized"}), 403

    id = request.args.get('id')
    if not id:
        return jsonify({"message":"Missing id parameter"}), 400
    deceased = get_deceased(id)
    if deceased.exists:
        delete_deceased(id)
        return jsonify({"message":"deceased Deleted"}), 200
    return jsonify({"message":"deceased Not Found"}), 404